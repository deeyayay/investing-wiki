#!/usr/bin/env python3
"""Social pulse fetcher — the StockTwits + Reddit half of /watchlist-refresh.

Companion to watchlist_refresh_fetch.py, same contract: every mechanical step
happens here, outside the model, so the model spends tokens only on judgment.

The news fetcher answers "what got *published* about this ticker?". This one
answers "what are retail traders and investing communities actually *saying*,
and is that unusual?" — the second question is the expensive one to answer by
hand, so the script does the filtering:

  1. StockTwits symbol stream per US-listed ticker → message volume, bull/bear
     split, and the few highest-engagement messages.
  2. Reddit search across the investing subs → posts ranked by score + comments.
  3. Compares today's StockTwits volume and bull% against a rolling baseline
     held in state, so a quiet ticker costs zero tokens while a chatter spike
     or a sentiment flip gets flagged.
  4. Dedupes every message/post against a seen-cache so twice-daily runs stay
     cheap.

Only tickers with something *notable* survive into the output — the point is to
surface the unusual, not to relay the firehose. Stdlib only.

Usage:
  python3 scripts/social_pulse.py [--all] [--limit 50] [--hours 36]
      [--tickers CRDO,SNDK] [--no-stocktwits] [--no-reddit] [--dry-run]
  python3 scripts/social_pulse.py --probe NVDA     # connectivity + shape check
  python3 scripts/social_pulse.py --selftest       # parser tests, no network

Output:  Investing/Raw/Inbox/social-pulse-digest.json  (overwritten each run)
State:   Investing/Raw/Inbox/.social-pulse-state.json  (seen cache + baselines)

Note: neither source is a documented, versioned public API. StockTwits' keyless
symbol stream and Reddit's .json listings both work today but can be gated or
rate-limited without notice — run --probe when a run reports fetch errors.
"""

import argparse
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from watchlist_refresh_fetch import (  # noqa: E402  (sibling module, path set above)
    INBOX_DIR,
    REGISTRY,
    REPO_ROOT,
    WATCHLIST,
    clean_company_name,
    extract_thesis,
    parse_registry,
    parse_watchlist_tickers,
    resolve_folder,
    select_tickers,
)

DIGEST_PATH = os.path.join(INBOX_DIR, "social-pulse-digest.json")
STATE_PATH = os.path.join(INBOX_DIR, ".social-pulse-state.json")

# Reddit asks for a unique descriptive User-Agent and throttles generic ones.
REDDIT_USER_AGENT = "python:investing-wiki.social-pulse:1.0 (personal research)"
STOCKTWITS_USER_AGENT = "Mozilla/5.0 (investing-wiki social-pulse)"

SEEN_RETENTION_DAYS = 21
BASELINE_HISTORY_DAYS = 14

# Subreddits searched in one multi-sub request per ticker.
REDDIT_SUBS = [
    "stocks",
    "investing",
    "wallstreetbets",
    "StockMarket",
    "SecurityAnalysis",
    "ValueInvesting",
    "options",
]

# --- Notability thresholds ---------------------------------------------------
# Everything below these floors is dropped before it costs a token.
ST_MIN_MESSAGES = 5          # fewer than this and volume stats are noise
ST_SPIKE_MULTIPLE = 2.0      # today's volume vs rolling baseline
ST_SENTIMENT_SHIFT_PTS = 25  # bull% swing vs last run that counts as a flip
ST_MIN_LIKES = 3             # a StockTwits message worth quoting
ST_MAX_QUOTED = 3
ST_BODY_CHARS = 220

RD_MIN_SCORE = 25            # upvote floor for a post worth a token
RD_TRACTION_SCORE = 150      # a post this big is a signal on its own
RD_MAX_KEPT = 3
RD_TITLE_CHARS = 200

# Tickers that collide with ordinary English words — search the company name
# instead, or Reddit returns pure noise.
AMBIGUOUS_TICKERS = {
    "AI", "ALL", "AN", "ARE", "BE", "BY", "CAR", "CC", "DAY", "EAT", "FAST",
    "FOR", "GO", "HAS", "HE", "IT", "KEY", "LOW", "MP", "NOW", "ON", "OR",
    "OUT", "PLAY", "REAL", "RUN", "SEE", "SO", "TE", "TRUE", "TWO", "UP",
    "WE", "WELL", "WHO", "X",
}

# Order matters: "Nasdaq Stockholm" and "Euronext Paris (EPA:XFAB) / OTC US: XFABF"
# both contain a US marker, so foreign venues are ruled out first.
FOREIGN_EXCHANGE_RE = re.compile(
    r"stockholm|amsterdam|paris|milan|frankfurt|xetra|euronext|london|"
    r"tokyo|taiwan|tse|tpex|twse|tsx|toronto|hong kong|hkex|korea|shenzhen|shanghai",
    re.IGNORECASE,
)
US_EXCHANGE_RE = re.compile(r"nasdaq|nyse|amex|otc markets", re.IGNORECASE)


# --- small helpers -----------------------------------------------------------

def _dig(obj, *keys, default=None):
    """Walk nested dicts without trusting any level to exist. Both feeds change
    shape between endpoints and neither is contract-stable."""
    for key in keys:
        if not isinstance(obj, dict):
            return default
        obj = obj.get(key)
        if obj is None:
            return default
    return obj


def _as_int(value, default=0):
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _truncate(text, limit):
    text = " ".join(str(text or "").split())
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def item_key(*parts):
    raw = "|".join(str(p) for p in parts)
    return hashlib.sha1(raw.encode("utf-8", "replace")).hexdigest()[:16]


def is_us_listed(entry):
    """StockTwits only covers US listings under their US symbol. Foreign names
    (285A.T, BESI, SIVE) still get a Reddit pass under their company name.

    A foreign primary listing disqualifies the ticker even when the registry
    also notes a US OTC line, because that line trades under a different symbol
    (XFAB → XFABF) and StockTwits would 404 on the one we hold."""
    exchange = entry.get("exchange") or ""
    if exchange:
        if FOREIGN_EXCHANGE_RE.search(exchange):
            return False
        return bool(US_EXCHANGE_RE.search(exchange))
    # No exchange recorded: fall back to symbol shape. Foreign symbols in this
    # registry carry a suffix (285A.T, 6451.TW, PRY.MI), so plain 1-5 letters
    # is the best available guess.
    return bool(re.fullmatch(r"[A-Z]{1,5}", entry.get("ticker", "")))


def parse_iso8601(value):
    """StockTwits stamps are ISO8601 with a literal Z."""
    if not value:
        return None
    text = str(value).strip().replace("Z", "+00:00")
    try:
        dt = datetime.fromisoformat(text)
    except ValueError:
        return None
    return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)


# --- network ----------------------------------------------------------------

class FetchError(Exception):
    """Carries a human-readable diagnosis, not just a status code."""


def http_get_json(url, user_agent, timeout=20):
    req = urllib.request.Request(url, headers={
        "User-Agent": user_agent,
        "Accept": "application/json",
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as exc:
        if exc.code in (401, 403):
            raise FetchError(f"HTTP {exc.code} — keyless access refused or blocked upstream") from exc
        if exc.code == 429:
            raise FetchError("HTTP 429 — rate limited; lower --limit or space out runs") from exc
        if exc.code == 404:
            raise FetchError("HTTP 404 — symbol not covered by this source") from exc
        raise FetchError(f"HTTP {exc.code}") from exc
    except urllib.error.URLError as exc:
        raise FetchError(f"network unreachable ({exc.reason})") from exc
    except TimeoutError as exc:
        raise FetchError("timed out") from exc
    try:
        return json.loads(body)
    except json.JSONDecodeError as exc:
        # A login wall or edge-cache challenge returns HTML with a 200.
        snippet = _truncate(body[:120], 120)
        raise FetchError(f"non-JSON response (got: {snippet!r})") from exc


# --- StockTwits -------------------------------------------------------------

def stocktwits_url(ticker):
    return f"https://api.stocktwits.com/api/2/streams/symbol/{urllib.parse.quote(ticker)}.json"


def parse_stocktwits(payload, hours, now=None):
    """Return (messages, dropped_old). Each message:
    {'id', 'body', 'user', 'followers', 'sentiment', 'likes', 'dt'}"""
    now = now or datetime.now(timezone.utc)
    cutoff = now - timedelta(hours=hours)
    messages, dropped = [], 0
    for raw in _dig(payload, "messages", default=[]) or []:
        if not isinstance(raw, dict):
            continue
        dt = parse_iso8601(raw.get("created_at"))
        if dt is not None and dt < cutoff:
            dropped += 1
            continue
        sentiment = _dig(raw, "entities", "sentiment", "basic")
        messages.append({
            "id": raw.get("id"),
            "body": _truncate(raw.get("body"), ST_BODY_CHARS),
            "user": _dig(raw, "user", "username", default="") or "",
            "followers": _as_int(_dig(raw, "user", "followers")),
            "sentiment": sentiment if sentiment in ("Bullish", "Bearish") else None,
            "likes": _as_int(_dig(raw, "likes", "total")),
            "dt": dt.strftime("%Y-%m-%d") if dt else "",
        })
    return messages, dropped


def summarize_stocktwits(messages):
    """Bull/bear split over the messages that actually carried a tag. StockTwits
    tagging is opt-in, so `tagged` is reported alongside the percentage —
    a 100% bull read off two tagged messages is not a signal."""
    bulls = sum(1 for m in messages if m["sentiment"] == "Bullish")
    bears = sum(1 for m in messages if m["sentiment"] == "Bearish")
    tagged = bulls + bears
    return {
        "messages": len(messages),
        "bulls": bulls,
        "bears": bears,
        "tagged": tagged,
        "bull_pct": round(100.0 * bulls / tagged, 1) if tagged else None,
    }


def top_stocktwits(messages, seen, today):
    """Highest-engagement unseen messages, worth quoting to the model."""
    fresh = []
    for m in sorted(messages, key=lambda x: (-x["likes"], -x["followers"])):
        if m["likes"] < ST_MIN_LIKES:
            continue
        key = item_key("st", m["id"])
        if key in seen:
            continue
        seen[key] = today
        fresh.append({
            "body": m["body"],
            "user": m["user"],
            "sentiment": m["sentiment"],
            "likes": m["likes"],
            "d": m["dt"],
        })
        if len(fresh) >= ST_MAX_QUOTED:
            break
    return fresh


# --- Reddit -----------------------------------------------------------------

def reddit_query(ticker, company):
    """Ticker search is precise for distinctive symbols and useless for the ones
    that are also words. Mirrors the news fetcher's company-name fallback."""
    name = clean_company_name(company or "")
    ticker_usable = bool(re.fullmatch(r"[A-Za-z]{3,5}", ticker)) and ticker.upper() not in AMBIGUOUS_TICKERS
    if ticker_usable and name:
        return f'"{ticker}" OR "{name}"'
    if ticker_usable:
        return f'"{ticker}"'
    return f'"{name}"' if name else f'"{ticker}"'


def reddit_url(ticker, company, hours):
    subs = "+".join(REDDIT_SUBS)
    window = "day" if hours <= 24 else ("week" if hours <= 168 else "month")
    params = urllib.parse.urlencode({
        "q": reddit_query(ticker, company),
        "restrict_sr": "1",
        "sort": "new",
        "t": window,
        "limit": "25",
    })
    return f"https://www.reddit.com/r/{subs}/search.json?{params}"


def parse_reddit(payload, hours, now=None):
    """Return posts from a Reddit listing:
    {'id', 'title', 'sub', 'score', 'comments', 'url', 'dt'}"""
    now = now or datetime.now(timezone.utc)
    cutoff = (now - timedelta(hours=hours)).timestamp()
    posts = []
    for child in _dig(payload, "data", "children", default=[]) or []:
        data = child.get("data") if isinstance(child, dict) else None
        if not isinstance(data, dict):
            continue
        created = data.get("created_utc")
        try:
            created = float(created)
        except (TypeError, ValueError):
            created = None
        if created is not None and created < cutoff:
            continue
        permalink = data.get("permalink") or ""
        posts.append({
            "id": data.get("id"),
            "title": _truncate(data.get("title"), RD_TITLE_CHARS),
            "sub": data.get("subreddit") or "",
            "score": _as_int(data.get("score")),
            "comments": _as_int(data.get("num_comments")),
            "url": f"https://reddit.com{permalink}" if permalink else "",
            "dt": datetime.fromtimestamp(created, timezone.utc).strftime("%Y-%m-%d") if created else "",
        })
    return posts


def top_reddit(posts, seen, today):
    """Unseen posts clearing the upvote floor, biggest first."""
    kept = []
    for p in sorted(posts, key=lambda x: (-(x["score"] + 2 * x["comments"]), x["title"])):
        if p["score"] < RD_MIN_SCORE:
            continue
        key = item_key("rd", p["id"])
        if key in seen:
            continue
        seen[key] = today
        kept.append({
            "title": p["title"],
            "sub": p["sub"],
            "score": p["score"],
            "comments": p["comments"],
            "url": p["url"],
            "d": p["dt"],
        })
        if len(kept) >= RD_MAX_KEPT:
            break
    return kept


# --- baselines / state ------------------------------------------------------

def load_state():
    if os.path.exists(STATE_PATH):
        try:
            with open(STATE_PATH, encoding="utf-8") as f:
                state = json.load(f)
        except (json.JSONDecodeError, OSError):
            state = {}
    else:
        state = {}
    state.setdefault("seen", {})
    state.setdefault("st_history", {})    # ticker -> [[date, message_count], ...]
    state.setdefault("st_bull_pct", {})   # ticker -> last observed bull%
    return state


def save_state(state):
    cutoff = (datetime.now(timezone.utc) - timedelta(days=SEEN_RETENTION_DAYS)).strftime("%Y-%m-%d")
    state["seen"] = {k: v for k, v in state["seen"].items() if v >= cutoff}
    for ticker, history in list(state["st_history"].items()):
        state["st_history"][ticker] = history[-BASELINE_HISTORY_DAYS:]
    os.makedirs(INBOX_DIR, exist_ok=True)
    with open(STATE_PATH, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=1, sort_keys=True)


def volume_multiple(history, count):
    """Today's message count against the mean of prior observations. None until
    there is enough history to mean anything — a first run flags nothing."""
    prior = [c for _d, c in history if c > 0]
    if len(prior) < 3:
        return None
    baseline = sum(prior) / len(prior)
    if baseline <= 0:
        return None
    return round(count / baseline, 2)


def evaluate_flags(ticker, st_summary, reddit_kept, state):
    """Decide what, if anything, makes this ticker worth the model's attention."""
    flags = []
    count = st_summary["messages"] if st_summary else 0
    multiple = None

    if st_summary:
        history = state["st_history"].setdefault(ticker, [])
        multiple = volume_multiple(history, count)
        if multiple is not None and multiple >= ST_SPIKE_MULTIPLE and count >= ST_MIN_MESSAGES:
            flags.append(f"chatter spike {multiple}× baseline")

        bull_pct = st_summary["bull_pct"]
        prior_pct = state["st_bull_pct"].get(ticker)
        if (
            bull_pct is not None
            and prior_pct is not None
            and st_summary["tagged"] >= ST_MIN_MESSAGES
            and abs(bull_pct - prior_pct) >= ST_SENTIMENT_SHIFT_PTS
        ):
            direction = "more bullish" if bull_pct > prior_pct else "more bearish"
            flags.append(f"sentiment {direction}: {prior_pct}% → {bull_pct}% bull")

    if any(p["score"] >= RD_TRACTION_SCORE for p in reddit_kept):
        flags.append("reddit traction")

    return flags, multiple


def record_observation(ticker, st_summary, today, state):
    """Append today's volume + bull% so tomorrow has a baseline to compare to.
    Written for every scanned ticker, including quiet ones — a baseline built
    only from noisy days would never flag anything."""
    if not st_summary:
        return
    history = state["st_history"].setdefault(ticker, [])
    if history and history[-1][0] == today:
        history[-1][1] = st_summary["messages"]
    else:
        history.append([today, st_summary["messages"]])
    if st_summary["bull_pct"] is not None and st_summary["tagged"] >= ST_MIN_MESSAGES:
        state["st_bull_pct"][ticker] = st_summary["bull_pct"]


# --- per-ticker collection --------------------------------------------------

def collect_ticker(entry, hours, state, today, use_stocktwits=True, use_reddit=True):
    """Fetch both sources for one ticker. Returns (block_or_None, errors).
    A block is emitted only when something notable survived filtering."""
    ticker = entry["ticker"]
    errors = []
    st_summary, st_quotes, reddit_kept = None, [], []

    if use_stocktwits and is_us_listed(entry):
        try:
            payload = http_get_json(stocktwits_url(ticker), STOCKTWITS_USER_AGENT)
            messages, _ = parse_stocktwits(payload, hours)
            st_summary = summarize_stocktwits(messages)
            st_quotes = top_stocktwits(messages, state["seen"], today)
        except FetchError as exc:
            errors.append({"ticker": ticker, "source": "stocktwits", "error": str(exc)})

    if use_reddit:
        try:
            payload = http_get_json(reddit_url(ticker, entry.get("company"), hours), REDDIT_USER_AGENT)
            posts = parse_reddit(payload, hours)
            reddit_kept = top_reddit(posts, state["seen"], today)
        except FetchError as exc:
            errors.append({"ticker": ticker, "source": "reddit", "error": str(exc)})

    flags, multiple = evaluate_flags(ticker, st_summary, reddit_kept, state)
    record_observation(ticker, st_summary, today, state)

    if not (flags or st_quotes or reddit_kept):
        return None, errors

    block = {"ticker": ticker, "flags": flags}
    if st_summary and st_summary["messages"]:
        block["stocktwits"] = {
            "messages": st_summary["messages"],
            "bull_pct": st_summary["bull_pct"],
            "tagged": st_summary["tagged"],
            "vs_baseline": multiple,
        }
        if st_quotes:
            block["stocktwits"]["top"] = st_quotes
    if reddit_kept:
        block["reddit"] = reddit_kept
    return block, errors


def collect(entries, hours, state, today, use_stocktwits=True, use_reddit=True, pause=1.0):
    """Run collect_ticker across entries. Returns {ticker: block} plus errors."""
    blocks, errors = {}, []
    for i, entry in enumerate(entries):
        block, errs = collect_ticker(entry, hours, state, today, use_stocktwits, use_reddit)
        errors.extend(errs)
        if block:
            blocks[entry["ticker"]] = block
        if pause and i < len(entries) - 1:
            time.sleep(pause)
    return blocks, errors


# --- probe / selftest -------------------------------------------------------

def run_probe(ticker, hours):
    """One ticker, both sources, verbose. The thing to run when a batch reports
    fetch errors — distinguishes 'source gated' from 'network blocked' from
    'response shape changed'.

    Resolves the ticker against the registry when it is registered, so the probe
    exercises the same URLs a real run would build."""
    ticker = ticker.upper()
    entry = next((e for e in parse_registry(REGISTRY) if e["ticker"].upper() == ticker), None)
    if entry:
        print(f"Probing {entry['ticker']} — {entry['company']} "
              f"[{entry.get('exchange') or 'exchange unrecorded'}] (window {hours}h)\n")
    else:
        entry = {"ticker": ticker, "company": None}
        print(f"Probing {ticker} (not in registry; company-name query unavailable) "
              f"(window {hours}h)\n")

    failures = []

    if is_us_listed(entry):
        url = stocktwits_url(entry["ticker"])
        print(f"[stocktwits] GET {url}")
        try:
            payload = http_get_json(url, STOCKTWITS_USER_AGENT)
            messages, dropped = parse_stocktwits(payload, hours)
            summary = summarize_stocktwits(messages)
            print(f"  ok — {len(messages)} in window ({dropped} older), "
                  f"{summary['tagged']} tagged, bull% {summary['bull_pct']}")
            if not messages and _dig(payload, "messages") is None:
                print("  WARNING: no 'messages' key — response shape may have changed")
            for m in messages[:2]:
                print(f"    · @{m['user']} [{m['sentiment']}] ♥{m['likes']}: {_truncate(m['body'], 90)}")
        except FetchError as exc:
            print(f"  FAIL — {exc}")
            failures.append(str(exc))
    else:
        print("[stocktwits] skipped — foreign primary listing, no US symbol to query")

    url = reddit_url(entry["ticker"], entry.get("company"), hours)
    print(f"\n[reddit] GET {url}")
    try:
        payload = http_get_json(url, REDDIT_USER_AGENT)
        posts = parse_reddit(payload, hours)
        print(f"  ok — {len(posts)} posts in window")
        if not posts and _dig(payload, "data", "children") is None:
            print("  WARNING: no 'data.children' key — response shape may have changed")
        for p in posts[:3]:
            print(f"    · r/{p['sub']} ↑{p['score']} 💬{p['comments']}: {_truncate(p['title'], 90)}")
    except FetchError as exc:
        print(f"  FAIL — {exc}")
        failures.append(str(exc))

    if failures and all("network unreachable" in f for f in failures):
        print("\nEvery attempt failed at the network layer — egress is blocked here, "
              "which says nothing about the sources. Retry from a machine with "
              "direct internet access.")
    elif failures:
        print("\nReached the network but the source refused or changed shape — see "
              "the FAIL lines above. A 401/403 means keyless access is gated; a "
              "shape WARNING means the parser needs updating.")
    return 1 if failures else 0


ST_FIXTURE = {
    "messages": [
        {"id": 1, "body": "$NVDA breaking out, next leg up", "created_at": "2026-07-30T12:00:00Z",
         "user": {"username": "alpha", "followers": 900},
         "entities": {"sentiment": {"basic": "Bullish"}}, "likes": {"total": 12}},
        {"id": 2, "body": "overextended here, trimming", "created_at": "2026-07-30T11:00:00Z",
         "user": {"username": "beta", "followers": 40},
         "entities": {"sentiment": {"basic": "Bearish"}}, "likes": {"total": 4}},
        {"id": 3, "body": "no tag, low engagement", "created_at": "2026-07-30T10:00:00Z",
         "user": {"username": "gamma", "followers": 1},
         "entities": {"sentiment": None}, "likes": {"total": 0}},
        {"id": 4, "body": "stale message", "created_at": "2026-06-01T10:00:00Z",
         "user": {"username": "delta", "followers": 5},
         "entities": {"sentiment": {"basic": "Bullish"}}, "likes": {"total": 99}},
        {"id": 5, "body": "malformed, no user or likes", "created_at": "2026-07-30T09:00:00Z"},
    ]
}

RD_FIXTURE = {
    "data": {"children": [
        {"data": {"id": "a1", "title": "DD: why NVDA still has room", "subreddit": "stocks",
                  "score": 320, "num_comments": 88, "created_utc": 1785585600.0,
                  "permalink": "/r/stocks/comments/a1/dd/"}},
        {"data": {"id": "a2", "title": "low effort post", "subreddit": "wallstreetbets",
                  "score": 3, "num_comments": 1, "created_utc": 1785585600.0,
                  "permalink": "/r/wallstreetbets/comments/a2/x/"}},
        {"data": {"id": "a3", "title": "old but popular", "subreddit": "investing",
                  "score": 500, "num_comments": 40, "created_utc": 1748000000.0,
                  "permalink": "/r/investing/comments/a3/y/"}},
        {"kind": "t3"},
    ]}
}


def run_selftest():
    """Parser + notability tests against fixtures. No network, no writes."""
    now = datetime(2026, 7, 30, 18, 0, tzinfo=timezone.utc)
    today = "2026-07-30"
    failures = []

    def check(label, got, want):
        if got != want:
            failures.append(f"{label}: got {got!r}, want {want!r}")

    messages, dropped = parse_stocktwits(ST_FIXTURE, 36, now=now)
    check("st in-window count", len(messages), 4)
    check("st dropped stale", dropped, 1)
    check("st malformed tolerated", messages[3]["user"], "")
    check("st malformed likes", messages[3]["likes"], 0)

    summary = summarize_stocktwits(messages)
    check("st bulls", summary["bulls"], 1)
    check("st bears", summary["bears"], 1)
    check("st tagged", summary["tagged"], 2)
    check("st bull_pct", summary["bull_pct"], 50.0)
    check("st bull_pct untagged", summarize_stocktwits([])["bull_pct"], None)

    seen = {}
    quotes = top_stocktwits(messages, seen, today)
    check("st quotes kept", [q["user"] for q in quotes], ["alpha", "beta"])
    check("st quotes cached", len(seen), 2)
    check("st quotes deduped on rerun", top_stocktwits(messages, seen, today), [])

    posts = parse_reddit(RD_FIXTURE, 36, now=now)
    check("rd in-window count", len(posts), 2)
    seen_rd = {}
    kept = top_reddit(posts, seen_rd, today)
    check("rd kept above floor", [p["title"] for p in kept], ["DD: why NVDA still has room"])
    check("rd url built", kept[0]["url"], "https://reddit.com/r/stocks/comments/a1/dd/")
    check("rd deduped on rerun", top_reddit(posts, seen_rd, today), [])

    check("baseline needs history", volume_multiple([], 10), None)
    check("baseline too thin", volume_multiple([["d1", 5], ["d2", 5]], 10), None)
    check("baseline multiple", volume_multiple([["d1", 5], ["d2", 5], ["d3", 5]], 10), 2.0)
    check("baseline zero-safe", volume_multiple([["d1", 0], ["d2", 0], ["d3", 0]], 10), None)

    state = {"seen": {}, "st_history": {"T": [["d1", 5], ["d2", 5], ["d3", 5]]}, "st_bull_pct": {"T": 20.0}}
    flags, multiple = evaluate_flags("T", {"messages": 12, "bulls": 9, "bears": 1, "tagged": 10,
                                           "bull_pct": 90.0}, [], state)
    check("spike multiple", multiple, 2.4)
    check("flags raised", len(flags), 2)
    check("spike flagged", any("chatter spike" in f for f in flags), True)
    check("flip flagged", any("more bullish" in f for f in flags), True)

    quiet_state = {"seen": {}, "st_history": {}, "st_bull_pct": {}}
    quiet_flags, _ = evaluate_flags("Q", {"messages": 2, "bulls": 0, "bears": 0, "tagged": 0,
                                          "bull_pct": None}, [], quiet_state)
    check("quiet ticker unflagged", quiet_flags, [])

    check("query distinctive ticker", reddit_query("CRDO", "Credo Technology Group Holding Ltd"),
          '"CRDO" OR "Credo Technology Group"')
    check("query ambiguous ticker", reddit_query("MP", "MP Materials Corp."), '"MP Materials"')
    check("query foreign ticker", reddit_query("6451.TW", "Advantest Corporation"), '"Advantest"')
    # Exchange strings below are verbatim from Monitor Registry.yaml — the
    # awkward ones are why foreign venues are tested before US markers.
    check("us listed by exchange", is_us_listed({"ticker": "NVDA", "exchange": "NASDAQ"}), True)
    check("nyse listed", is_us_listed({"ticker": "LMND", "exchange": "NYSE"}), True)
    check("otc us listed", is_us_listed({"ticker": "OTCX", "exchange": "OTC Markets (US)"}), True)
    check("foreign not us listed", is_us_listed({"ticker": "6451.TW", "exchange": "TWSE (Taiwan)"}), False)
    check("nasdaq stockholm is foreign", is_us_listed({"ticker": "SIVE", "exchange": "Nasdaq Stockholm"}), False)
    check("euronext amsterdam is foreign", is_us_listed({"ticker": "BESI", "exchange": "Euronext Amsterdam"}), False)
    check("foreign primary beats us otc line",
          is_us_listed({"ticker": "XFAB", "exchange": "Euronext Paris (EPA:XFAB) / OTC US: XFABF"}), False)
    check("dual nyse euronext is foreign",
          is_us_listed({"ticker": "PRY.MI", "exchange": "NYSE / Euronext Paris"}), False)
    check("tokyo prime is foreign",
          is_us_listed({"ticker": "285A.T", "exchange": "TSE (Tokyo) — Prime Market"}), False)
    check("us listed fallback", is_us_listed({"ticker": "SNDK"}), True)
    check("suffixed symbol fallback", is_us_listed({"ticker": "285A.T"}), False)

    check("reddit window day", "t=day" in reddit_url("NVDA", "Nvidia", 12), True)
    check("reddit window week", "t=week" in reddit_url("NVDA", "Nvidia", 36), True)

    if failures:
        print(f"SELFTEST FAILED ({len(failures)})")
        for f in failures:
            print(f"  ✗ {f}")
        return 1
    print("SELFTEST PASSED — parsers, dedupe, baselines, flags, query heuristics")
    return 0


# --- main -------------------------------------------------------------------

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--limit", type=int, default=50, help="max tickers per run (default 50)")
    ap.add_argument("--hours", type=float, default=36, help="lookback window (default 36)")
    ap.add_argument("--tickers", help="comma-separated override list (skips selection logic)")
    ap.add_argument("--all", action="store_true",
                    help="scan the full registry instead of just Watchlist.md tickers")
    ap.add_argument("--no-stocktwits", action="store_true", help="skip the StockTwits pass")
    ap.add_argument("--no-reddit", action="store_true", help="skip the Reddit pass")
    ap.add_argument("--pause", type=float, default=1.0, help="seconds between tickers (default 1.0)")
    ap.add_argument("--dry-run", action="store_true", help="resolve + select only; no network, no writes")
    ap.add_argument("--probe", metavar="TICKER", help="verbose single-ticker connectivity + shape check")
    ap.add_argument("--selftest", action="store_true", help="run parser tests offline and exit")
    ap.add_argument("--output", default=DIGEST_PATH, help="digest path (default %(default)s)")
    args = ap.parse_args(argv)

    if args.selftest:
        return run_selftest()
    if args.probe:
        return run_probe(args.probe, args.hours)
    if args.no_stocktwits and args.no_reddit:
        ap.error("--no-stocktwits and --no-reddit together leave nothing to fetch")

    entries = parse_registry(REGISTRY)
    watchlist = parse_watchlist_tickers(WATCHLIST)
    state = load_state()

    if args.tickers:
        wanted = {t.strip().upper() for t in args.tickers.split(",")}
        selected = [e for e in entries if e["ticker"].upper() in wanted]
    else:
        selected = select_tickers(entries, watchlist, {"last_included": {}}, args.limit, args.all)

    if args.dry_run:
        print(f"{'Ticker':<10} {'StockTwits':<11} {'Baseline days':<14} Reddit query")
        for e in selected:
            days = len(state["st_history"].get(e["ticker"], []))
            st = "yes" if is_us_listed(e) else "skip (non-US)"
            print(f"{e['ticker']:<10} {st:<11} {days:<14} {reddit_query(e['ticker'], e.get('company'))}")
        print(f"\n{len(selected)} tickers selected "
              f"(scope: {'full registry' if args.all else 'watchlist only'}).")
        return 0

    now = datetime.now(timezone.utc)
    today = now.strftime("%Y-%m-%d")
    blocks, errors = collect(
        selected, args.hours, state, today,
        use_stocktwits=not args.no_stocktwits,
        use_reddit=not args.no_reddit,
        pause=args.pause,
    )

    for e in selected:
        if e["ticker"] in blocks:
            e["folder"] = resolve_folder(e["ticker"], e.get("path"))
            e["thesis"], e["drift"] = extract_thesis(e["folder"])
            blocks[e["ticker"]].update({
                "company": e["company"],
                "sector": e.get("sector"),
                "thesis": e["thesis"],
                "drift": e["drift"],
                "folder": os.path.relpath(e["folder"], REPO_ROOT) if e["folder"] else None,
            })

    digest = {
        "generated": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "window_hours": args.hours,
        "scanned": len(selected),
        "with_signal": len(blocks),
        "flagged": sorted(t for t, b in blocks.items() if b["flags"]),
        "errors": errors,
        "tickers": [blocks[t] for t in sorted(blocks)],
    }
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(digest, f, indent=1, ensure_ascii=False)
    save_state(state)

    print(f"Scanned {len(selected)} tickers → {len(blocks)} with social signal, "
          f"{len(digest['flagged'])} flagged, {len(errors)} fetch errors. "
          f"Digest: {os.path.relpath(args.output, REPO_ROOT)}")
    if errors:
        sources = sorted({e["source"] for e in errors})
        print(f"  fetch errors on: {', '.join(sources)} — run --probe TICKER to diagnose")
    return 0


if __name__ == "__main__":
    sys.exit(main())
