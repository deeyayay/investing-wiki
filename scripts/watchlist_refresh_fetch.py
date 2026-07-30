#!/usr/bin/env python3
"""Watchlist refresh fetcher — the zero-token half of /watchlist-refresh.

Does every mechanical step outside the model:
  1. Builds the ticker universe: tickers named in Watchlist.md, resolved
     against Monitor Registry.yaml (--all widens to the full registry).
  2. Resolves each ticker's folder on disk (registry paths can go stale).
  3. Extracts the One-Line Thesis + Drift status from analysis.md.
  4. Fetches Google News RSS headlines per ticker (last --hours, default 36).
  5. Dedupes against a seen-headline cache so twice-daily runs stay cheap.
  6. With --social, folds in StockTwits + Reddit chatter (see social_pulse.py).
  7. Writes ONE compact digest JSON for Claude to triage.

Only tickers with new, unseen headlines appear in the digest — plus, under
--social, tickers whose chatter is genuinely unusual even when the news was
quiet. Stdlib only.

Usage:
  python3 scripts/watchlist_refresh_fetch.py [--all] [--limit 50] [--hours 36]
      [--max-per-ticker 5] [--tickers CRDO,SNDK] [--social] [--dry-run]

Output:  Investing/Raw/Inbox/watchlist-refresh-digest.json  (overwritten each run)
State:   Investing/Raw/Inbox/.watchlist-refresh-state.json  (seen cache + rotation)
"""

import argparse
import hashlib
import html
import json
import os
import re
import sys
import time
import urllib.request
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTRY = os.path.join(REPO_ROOT, "Investing", "Wiki", "Reference", "Monitor Registry.yaml")
WATCHLIST = os.path.join(REPO_ROOT, "Investing", "Wiki", "Reference", "Watchlist.md")
SECTORS_DIR = os.path.join(REPO_ROOT, "Investing", "Wiki", "Sectors")
INBOX_DIR = os.path.join(REPO_ROOT, "Investing", "Raw", "Inbox")
DIGEST_PATH = os.path.join(INBOX_DIR, "watchlist-refresh-digest.json")
STATE_PATH = os.path.join(INBOX_DIR, ".watchlist-refresh-state.json")

USER_AGENT = "Mozilla/5.0 (investing-wiki watchlist-refresh)"
SEEN_RETENTION_DAYS = 21

# Headline patterns that are never thesis-relevant — dropped before they cost tokens.
NOISE_PATTERNS = [
    r"\bmotley fool\b",
    r"\bzacks\b",
    r"simply wall st",
    r"if you( ha|')d invested",
    r"\b\d+ (top |best |growth |ai )*stocks? to (buy|watch|own)\b",
    r"here'?s (why|how|what)",
    r"\bstock (jumps|pops|slides|dips|rises|falls|drops|surges|plunges)\b.*\btoday\b",
    r"what you need to know",
    r"\bprediction:",
]
NOISE_RE = re.compile("|".join(NOISE_PATTERNS), re.IGNORECASE)

COMPANY_SUFFIX_RE = re.compile(
    r",?\s+(inc|corp|corporation|co|company|ltd|limited|plc|holdings?"
    r"|n\.v|s\.a|s\.p\.a|se|ag|k\.k)\.?$",
    re.IGNORECASE,
)


def parse_registry(path):
    """Parse the tickers: block of Monitor Registry.yaml. Regex-based on purpose —
    the file is machine-written with a fixed 2/4-space indent shape."""
    tickers = []
    current = None
    in_tickers = False
    key_re = re.compile(r'^  (?:"([^"]+)"|([A-Za-z0-9.\-]+)):\s*(?:#.*)?$')
    field_re = re.compile(r'^    ([a-z_]+):\s*(.*?)\s*(?:#.*)?$')
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if line.startswith("tickers:"):
                in_tickers = True
                continue
            if line.startswith("candidates:"):
                break
            if not in_tickers:
                continue
            m = key_re.match(line)
            if m:
                current = {"ticker": m.group(1) or m.group(2)}
                tickers.append(current)
                continue
            if current is None:
                continue
            m = field_re.match(line)
            if m:
                key, val = m.group(1), m.group(2).strip().strip('"')
                if key in ("company", "sector", "path", "score", "exchange"):
                    current[key] = None if val in ("null", "") else val
    return [t for t in tickers if t.get("company")]


def parse_watchlist_tickers(path):
    """Tickers named anywhere in Watchlist.md tables — they get selection priority."""
    if not os.path.exists(path):
        return set()
    found = set()
    with open(path, encoding="utf-8") as f:
        for line in f:
            if not line.startswith("|"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if cells and re.fullmatch(r"(?=.*[A-Z0-9])[A-Z0-9.\-]{1,10}", cells[0] or ""):
                if cells[0] not in ("TICKER",):
                    found.add(cells[0])
    return found


def resolve_folder(ticker, registry_path):
    """Find the ticker's three-layer folder on disk. Registry paths drift out of
    date as sectors get reorganized, so trust the filesystem first."""
    if registry_path:
        candidate = os.path.join(REPO_ROOT, registry_path)
        if os.path.isfile(os.path.join(candidate, "analysis.md")) or os.path.isfile(
            os.path.join(candidate, "signals.md")
        ):
            return candidate
    for root, dirs, _files in os.walk(SECTORS_DIR):
        if ticker in dirs:
            return os.path.join(root, ticker)
    return None


def extract_thesis(folder):
    """Pull One-Line Thesis + Drift status out of analysis.md without the model."""
    thesis, drift = None, None
    if folder:
        analysis = os.path.join(folder, "analysis.md")
        if os.path.isfile(analysis):
            with open(analysis, encoding="utf-8") as f:
                text = f.read()
            m = re.search(r"^## One-Line Thesis\s*\n+(.+?)(?=\n---|\n##)", text, re.M | re.S)
            if m:
                thesis = " ".join(m.group(1).split())
            m = re.search(r"\*\*Drift status:\*\*\s*(.+)", text)
            if m:
                drift = m.group(1).strip()
    return thesis, drift


def clean_company_name(company):
    name = re.sub(r"\s*\(.*?\)", "", company)   # drop "(fka ...)" parentheticals
    name = name.split(",")[0].strip()
    prev = None
    while prev != name:
        prev = name
        name = COMPANY_SUFFIX_RE.sub("", name).strip()
    return name or company


def fetch_rss(url, timeout=15):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", "replace")


def parse_rss_items(xml_text, max_age_hours):
    """Return [{'t': title, 'src': source, 'd': YYYY-MM-DD}] from a Google News RSS body."""
    items = []
    cutoff = datetime.now(timezone.utc) - timedelta(hours=max_age_hours)
    for chunk in re.findall(r"<item>(.*?)</item>", xml_text, re.S):
        tm = re.search(r"<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>", chunk, re.S)
        if not tm:
            continue
        title = html.unescape(tm.group(1)).strip()
        sm = re.search(r"<source[^>]*>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</source>", chunk, re.S)
        source = html.unescape(sm.group(1)).strip() if sm else ""
        if source and title.endswith(" - " + source):
            title = title[: -len(" - " + source)]
        date_str = ""
        dm = re.search(r"<pubDate>(.*?)</pubDate>", chunk)
        if dm:
            try:
                dt = parsedate_to_datetime(dm.group(1).strip())
                if dt < cutoff:
                    continue
                date_str = dt.strftime("%Y-%m-%d")
            except (ValueError, TypeError):
                pass
        items.append({"t": title, "src": source, "d": date_str})
    return items


def news_query_url(company, ticker, hours):
    name = clean_company_name(company)
    query = f'"{name}"'
    if len(name.split()) == 1:
        query += " stock"
    query += f" when:{max(1, round(hours))}h"
    return (
        "https://news.google.com/rss/search?q="
        + urllib.request.quote(query)
        + "&hl=en-US&gl=US&ceid=US:en"
    )


def headline_key(title):
    normalized = re.sub(r"[^a-z0-9]+", "", title.lower())
    return hashlib.sha1(normalized.encode()).hexdigest()[:16]


def load_state():
    if os.path.exists(STATE_PATH):
        try:
            with open(STATE_PATH, encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            pass
    return {"seen": {}, "last_included": {}}


def save_state(state):
    cutoff = (datetime.now(timezone.utc) - timedelta(days=SEEN_RETENTION_DAYS)).strftime("%Y-%m-%d")
    state["seen"] = {k: v for k, v in state["seen"].items() if v >= cutoff}
    os.makedirs(INBOX_DIR, exist_ok=True)
    with open(STATE_PATH, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=1, sort_keys=True)


def select_tickers(entries, watchlist, state, limit, include_all):
    """Default universe: tickers named in Watchlist.md. With --all, the whole
    registry, prioritized Watchlist.md > scored > rest. Either way, ties break
    on a least-recently-covered rotation so a >limit universe cycles fully."""
    if not include_all:
        entries = [e for e in entries if e["ticker"] in watchlist]

    def sort_key(e):
        tier = 0 if e["ticker"] in watchlist else (1 if e.get("score") else 2)
        last = state["last_included"].get(e["ticker"], "")
        return (tier, last, e["ticker"])

    return sorted(entries, key=sort_key)[:limit]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--limit", type=int, default=50, help="max tickers per run (default 50)")
    ap.add_argument("--hours", type=float, default=36, help="headline lookback window (default 36)")
    ap.add_argument("--max-per-ticker", type=int, default=5, help="max headlines kept per ticker")
    ap.add_argument("--tickers", help="comma-separated override list (skips selection logic)")
    ap.add_argument("--all", action="store_true",
                    help="scan the full registry instead of just Watchlist.md tickers")
    ap.add_argument("--social", action="store_true",
                    help="also fetch StockTwits + Reddit chatter into the same digest")
    ap.add_argument("--no-stocktwits", action="store_true", help="with --social: skip StockTwits")
    ap.add_argument("--no-reddit", action="store_true", help="with --social: skip Reddit")
    ap.add_argument("--social-pause", type=float, default=1.0,
                    help="with --social: seconds between tickers (default 1.0)")
    ap.add_argument("--dry-run", action="store_true", help="resolve + select only; no network, no writes")
    ap.add_argument("--output", default=DIGEST_PATH, help="digest path (default %(default)s)")
    args = ap.parse_args(argv)

    if not args.social and (args.no_stocktwits or args.no_reddit):
        ap.error("--no-stocktwits/--no-reddit only apply to --social runs")
    if args.social and args.no_stocktwits and args.no_reddit:
        ap.error("--social with both sources disabled leaves nothing to fetch")

    entries = parse_registry(REGISTRY)
    watchlist = parse_watchlist_tickers(WATCHLIST)
    state = load_state()

    if args.tickers:
        wanted = {t.strip().upper() for t in args.tickers.split(",")}
        selected = [e for e in entries if e["ticker"].upper() in wanted]
    else:
        selected = select_tickers(entries, watchlist, state, args.limit, args.all)

    not_in_registry = sorted(watchlist - {e["ticker"] for e in entries})

    for e in selected:
        e["folder"] = resolve_folder(e["ticker"], e.get("path"))
        e["thesis"], e["drift"] = extract_thesis(e["folder"])

    if args.dry_run:
        print(f"{'Ticker':<8} {'Thesis':<7} {'Last incl.':<12} Company")
        for e in selected:
            last = state["last_included"].get(e["ticker"], "never")[:10]
            print(f"{e['ticker']:<8} {'yes' if e['thesis'] else 'NO':<7} {last:<12} {e['company']}")
        print(f"\n{len(selected)} of {len(entries)} registry tickers selected "
              f"({len(watchlist)} on Watchlist.md; scope: {'full registry' if args.all else 'watchlist only'}).")
        if not_in_registry:
            print(f"On Watchlist.md but NOT in registry (skipped): {', '.join(not_in_registry)}")
        return 0

    now = datetime.now(timezone.utc)
    today = now.strftime("%Y-%m-%d")
    news_by_ticker, errors = {}, []
    for e in selected:
        url = news_query_url(e["company"], e["ticker"], args.hours)
        try:
            items = parse_rss_items(fetch_rss(url), args.hours)
        except Exception as exc:  # network errors must never kill the batch
            errors.append({"ticker": e["ticker"], "source": "news", "error": str(exc)[:120]})
            continue
        fresh = []
        for item in items:
            if NOISE_RE.search(item["t"]):
                continue
            key = headline_key(item["t"])
            if key in state["seen"]:
                continue
            state["seen"][key] = today
            fresh.append(item)
            if len(fresh) >= args.max_per_ticker:
                break
        state["last_included"][e["ticker"]] = today
        if fresh:
            news_by_ticker[e["ticker"]] = fresh
        time.sleep(0.5)

    # Social pass is opt-in and additive: it can decorate a ticker that already
    # has headlines, or pull in one that was quiet on news but is spiking on
    # chatter — that combination is the whole point of running it.
    social_by_ticker = {}
    if args.social:
        import social_pulse  # lazy: keeps the news-only path import-free

        social_state = social_pulse.load_state()
        social_by_ticker, social_errors = social_pulse.collect(
            selected, args.hours, social_state, today,
            use_stocktwits=not args.no_stocktwits,
            use_reddit=not args.no_reddit,
            pause=args.social_pause,
        )
        errors.extend(social_errors)
        social_pulse.save_state(social_state)

    digest_tickers = []
    for e in selected:
        ticker = e["ticker"]
        fresh = news_by_ticker.get(ticker)
        social = social_by_ticker.get(ticker)
        if not fresh and not social:
            continue
        # Quoted messages enrich a ticker that already has news, but they must
        # not resurrect a news-quiet one on their own: any liquid ticker always
        # has *someone* posting, and the seen-cache would just walk further
        # down the message pool every run. Only a flag or a real Reddit thread
        # earns a quiet ticker a slot.
        if not fresh and not (social.get("flags") or social.get("reddit")):
            continue
        entry = {
            "ticker": ticker,
            "company": e["company"],
            "sector": e.get("sector"),
            "thesis": e["thesis"],
            "drift": e["drift"],
            "folder": os.path.relpath(e["folder"], REPO_ROOT) if e["folder"] else None,
            "headlines": fresh or [],
        }
        if social:
            entry["social"] = {k: v for k, v in social.items()
                               if k in ("flags", "stocktwits", "reddit")}
        digest_tickers.append(entry)

    covered = {d["ticker"] for d in digest_tickers} | {x["ticker"] for x in errors}
    digest = {
        "generated": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "window_hours": args.hours,
        "scanned": len(selected),
        "with_news": len(news_by_ticker),
        "quiet": sorted(e["ticker"] for e in selected if e["ticker"] not in covered),
        "errors": errors,
        "not_in_registry": not_in_registry,
        "tickers": digest_tickers,
    }
    if args.social:
        # Counted off the digest, not off the raw collect result — blocks the
        # merge dropped as "chatty, not unusual" are not signal.
        kept_social = [d["ticker"] for d in digest_tickers if "social" in d]
        digest["social_scanned"] = True
        digest["with_social"] = len(kept_social)
        digest["social_flagged"] = sorted(
            t for t in kept_social if social_by_ticker[t].get("flags")
        )
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(digest, f, indent=1, ensure_ascii=False)
    save_state(state)

    summary = (f"Scanned {len(selected)} tickers → {len(news_by_ticker)} with new headlines")
    if args.social:
        summary += (f", {digest['with_social']} with social signal "
                    f"({len(digest['social_flagged'])} flagged)")
    summary += (f", {len(errors)} fetch errors. "
                f"Digest: {os.path.relpath(args.output, REPO_ROOT)}")
    print(summary)
    return 0


if __name__ == "__main__":
    sys.exit(main())
