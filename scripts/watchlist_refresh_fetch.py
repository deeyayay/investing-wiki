#!/usr/bin/env python3
"""Watchlist refresh fetcher — the zero-token half of /watchlist-refresh.

Does every mechanical step outside the model:
  1. Builds the ticker universe: tickers named in Watchlist.md, resolved
     against Monitor Registry.yaml (--all widens to the full registry).
  2. Resolves each ticker's folder on disk (registry paths can go stale).
  3. Extracts the One-Line Thesis + Drift status from analysis.md.
  4. Fetches items per ticker from every enabled provider (last --hours,
     default 36). Providers are independent, so one blocked host degrades the
     run instead of killing it.
  5. Dedupes against a seen-item cache so twice-daily runs stay cheap.
  6. Writes ONE compact digest JSON for Claude to triage.

Only tickers with new, unseen items appear in the digest. Stdlib only, and no
model tokens are spent here — that is the whole point of this script.

Providers (--providers, default "googlenews,edgar"):
  googlenews  Google News RSS headlines.       kind="news"
  edgar       SEC EDGAR browse-edgar atom      kind="filing"
              feed of the ticker's filings.
              Needs cik: in the registry;
              foreign listings without one
              are skipped silently.

The two reach different hosts on purpose. Google News is the only reachable
headline source, so EDGAR is what keeps the pipeline producing something if it
goes dark. WebSearch is deliberately NOT a provider: it is a model tool, so its
results land in context and cost roughly two orders of magnitude more per run
than this script.

Usage:
  python3 scripts/watchlist_refresh_fetch.py [--all] [--limit 50] [--hours 36]
      [--max-per-ticker 5] [--tickers CRDO,SNDK] [--providers googlenews,edgar]
      [--dry-run]

Exit status:
  0  ran (even on a legitimately quiet day)
  1  every fetch failed, or an empty digest would have overwritten a good one

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
TOPICS = os.path.join(REPO_ROOT, "Investing", "Wiki", "Reference", "Topics.yaml")
SECTORS_DIR = os.path.join(REPO_ROOT, "Investing", "Wiki", "Sectors")
INBOX_DIR = os.path.join(REPO_ROOT, "Investing", "Raw", "Inbox")
DIGEST_PATH = os.path.join(INBOX_DIR, "watchlist-refresh-digest.json")
STATE_PATH = os.path.join(INBOX_DIR, ".watchlist-refresh-state.json")
# SEC's full company->ticker map, cached locally. 800KB, refreshed weekly.
SEC_TICKERS_PATH = os.path.join(INBOX_DIR, ".sec-company-tickers.json")
SEC_TICKERS_URL = "https://www.sec.gov/files/company_tickers.json"
SEC_TICKERS_MAX_AGE_DAYS = 7
# Filings look back at least this far regardless of --hours (see provider_edgar).
EDGAR_MIN_WINDOW_HOURS = 96

USER_AGENT = "Mozilla/5.0 (investing-wiki watchlist-refresh)"
# SEC fair-access REQUIRES a contact email in the User-Agent — it answers 403 to
# any UA without one, including a browser string. The default below satisfies the
# format check but is a placeholder, not a real mailbox; set SEC_USER_AGENT to
# "your-name your@email" so SEC can reach you before they rate-limit you.
SEC_UA_PLACEHOLDER = "investing-wiki set-SEC_USER_AGENT@example.com"
SEC_USER_AGENT = os.environ.get("SEC_USER_AGENT", SEC_UA_PLACEHOLDER)
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
                if key in ("company", "sector", "path", "score", "cik"):
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


def fetch_url(url, timeout=15, user_agent=USER_AGENT):
    req = urllib.request.Request(url, headers={"User-Agent": user_agent})
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


def unquote(value):
    """Strip ONE matching pair of outer quotes. Stripping both quote characters
    would eat the inner quotes of a query like '"HBM" OR "HBM4"'."""
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def parse_topics(path):
    """Parse Topics.yaml. Regex-based to match parse_registry — stdlib only, and
    the file is a fixed list-of-mappings shape."""
    if not os.path.exists(path):
        return []
    topics, current = [], None
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            m = re.match(r"^  - id:\s*(\S+)", line)
            if m:
                current = {"id": m.group(1), "tickers": [], "gaps": []}
                topics.append(current)
                continue
            if current is None:
                continue
            m = re.match(r'^    (label|query):\s*(.*)$', line)
            if m:
                current[m.group(1)] = unquote(m.group(2).strip())
                continue
            m = re.match(r"^    (tickers|gaps):\s*\[(.*)\]", line)
            if m:
                current[m.group(1)] = [
                    t.strip().strip('"\'') for t in m.group(2).split(",") if t.strip()]
    return [t for t in topics if t.get("query")]


# Financial headlines sometimes tag a company with its exchange. Reliable when
# present, but rare in RSS titles — which is why the name index below exists.
EXCHANGE_TICKER_RE = re.compile(
    r"\b(?:NASDAQ|NYSE|NYSEARCA|AMEX|OTC|TSX|LSE|ETR|EPA)\s*[:\-]\s*([A-Z]{1,5}(?:\.[A-Z]{1,2})?)\b")

# Company names too generic to match on. Every one of these is a real SEC
# registrant whose name is also an ordinary English word, so an unguarded match
# turns any headline using the word into a false candidate.
NAME_STOPLIST = {
    "apple", "block", "sea", "arm", "now", "open", "match", "gap", "target",
    "shell", "total", "unity", "corning", "marathon", "carvana", "root", "core",
    "compass", "olo", "rocket", "paycom", "science", "energy", "power", "vision",
    "global", "national", "american", "general", "united", "first", "new",
}

# Wire services and data vendors appear in bylines on a large share of
# headlines, so matching their names produces a steady stream of junk
# candidates ("ACCESS Newswire" -> ACCS) that has nothing to do with the story.
NAME_STOPWORD_RE = re.compile(
    r"newswire|news wire|business wire|globe ?newswire|pr ?newswire|"
    r"tradingview|benzinga|zacks|marketbeat|simply wall|motley fool|"
    r"seeking ?alpha|barron|reuters|bloomberg|associated press",
    re.IGNORECASE)


def load_sec_company_names():
    """{normalized company name: ticker} for every SEC registrant.

    Turns a company NAME in a headline into a ticker, which is what the
    discovery funnel actually needs — RSS titles say "Cloverleaf Infrastructure",
    not "(NASDAQ: XXXX)". Cached for a week; a fetch failure is non-fatal, the
    funnel just falls back to exchange tags.
    """
    raw = None
    try:
        age_days = (time.time() - os.path.getmtime(SEC_TICKERS_PATH)) / 86400
        if age_days < SEC_TICKERS_MAX_AGE_DAYS:
            with open(SEC_TICKERS_PATH, encoding="utf-8") as f:
                raw = json.load(f)
    except (OSError, ValueError):
        pass
    if raw is None:
        try:
            raw = json.loads(fetch_url(SEC_TICKERS_URL, timeout=30,
                                       user_agent=SEC_USER_AGENT))
            os.makedirs(os.path.dirname(SEC_TICKERS_PATH), exist_ok=True)
            with open(SEC_TICKERS_PATH, "w", encoding="utf-8") as f:
                json.dump(raw, f)
        except Exception:
            return {}
    index = {}
    for row in raw.values():
        name = COMPANY_SUFFIX_RE.sub("", (row.get("title") or "").strip()).lower()
        name = re.sub(r"[^a-z0-9 ]+", " ", name)
        name = re.sub(r"\s+", " ", name).strip()
        # One short word is almost always an English word too; require either
        # multiple words or a distinctly long single one.
        if not name or name in NAME_STOPLIST or NAME_STOPWORD_RE.search(name):
            continue
        if len(name.split()) < 2 and len(name) < 7:
            continue
        index.setdefault(name, row.get("ticker"))
    return index


def discover_tickers(items, known, name_index=None):
    """Untracked companies named in topic headlines — the discovery funnel.

    Two passes, both zero-token: an exchange tag when the headline carries one,
    otherwise a company-name match against SEC's registrant list. Bare
    capitalised words are never matched — "AI", "CEO" and "US" would swamp the
    result with noise that costs tokens to triage downstream.
    """
    found = {}

    def add(sym, title):
        if not sym or sym.upper() in known:
            return
        found.setdefault(sym.upper(), []).append(title[:100])

    for item in items:
        title = item.get("t", "")
        for sym in EXCHANGE_TICKER_RE.findall(title):
            add(sym, title)
        if name_index:
            haystack = re.sub(r"[^a-z0-9 ]+", " ", title.lower())
            haystack = " %s " % re.sub(r"\s+", " ", haystack).strip()
            for name, sym in name_index.items():
                if " %s " % name in haystack:
                    add(sym, title)
    return [{"ticker": k, "seen_in": v[:3]} for k, v in sorted(found.items())]


def topic_query_url(query, hours):
    return (
        "https://news.google.com/rss/search?q="
        + urllib.request.quote("%s when:%dh" % (query, max(1, round(hours))))
        + "&hl=en-US&gl=US&ceid=US:en"
    )


def provider_googlenews(entry, hours):
    """Google News RSS headlines for one ticker. kind='news'."""
    items = parse_rss_items(fetch_url(news_query_url(entry["company"], entry["ticker"], hours)),
                            hours)
    for item in items:
        item["kind"] = "news"
    return items


def edgar_atom_url(cik, count=10):
    return (
        "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK="
        + urllib.request.quote(str(cik))
        + "&type=&dateb=&owner=include&count=%d&output=atom" % count
    )


def parse_edgar_atom(xml_text, max_age_hours):
    """Return filings newer than the window from a browse-edgar atom feed.

    Titles are built from the form type plus, for an 8-K, its item numbers —
    'items 1.01, 2.03' is the part that says whether a filing is worth reading.
    """
    items = []
    cutoff = (datetime.now(timezone.utc) - timedelta(hours=max_age_hours)).date()
    for chunk in re.findall(r"<entry>(.*?)</entry>", xml_text, re.S):
        def field(name):
            m = re.search(r"<%s>(.*?)</%s>" % (name, name), chunk, re.S)
            return html.unescape(m.group(1)).strip() if m else ""

        date_str = field("filing-date")
        if not date_str:
            continue
        try:
            if datetime.strptime(date_str, "%Y-%m-%d").date() < cutoff:
                continue
        except ValueError:
            continue
        form = field("filing-type") or field("form-name")
        if not form:
            continue
        title = form
        desc = field("form-name")
        if desc and desc.lower() != form.lower():
            title += " — " + desc
        item_desc = field("items-desc")
        if item_desc:
            title += " (%s)" % re.sub(r"\s+", " ", item_desc)
        items.append({
            "t": title,
            "src": "SEC EDGAR",
            "d": date_str,
            "kind": "filing",
            "url": field("filing-href"),
        })
    return items


def provider_edgar(entry, hours):
    """SEC filings for one ticker. kind='filing'.

    Returns nothing for a company with no cik — foreign listings are not SEC
    filers, and that is a normal state, not a fetch error.
    """
    cik = entry.get("cik")
    if not cik:
        return []
    # EDGAR indexes by filing DATE, not timestamp, so the window is whole days.
    # At the default 36h that can leave barely one calendar day, which silently
    # drops filings the brief exists to surface — a 10-Q filed Wednesday is gone
    # by Friday's run. Give filings a wider floor than headlines; the seen-cache
    # stops the extra days from showing up twice.
    return parse_edgar_atom(
        fetch_url(edgar_atom_url(cik), user_agent=SEC_USER_AGENT),
        max(hours, EDGAR_MIN_WINDOW_HOURS))


PROVIDERS = {
    "googlenews": provider_googlenews,
    "edgar": provider_edgar,
}
DEFAULT_PROVIDERS = "googlenews,edgar"


def existing_digest_has_content(path):
    """True if a digest already on disk holds headlines worth not destroying."""
    try:
        with open(path, encoding="utf-8") as f:
            return bool(json.load(f).get("tickers"))
    except (OSError, ValueError):
        return False


# ---- impact scoring -------------------------------------------------------
# Ranks each item so the dashboard can sort the loud, formulaic stuff below the
# things that actually move a thesis. Zero model tokens: this is event-TYPE
# classification from the headline, a proxy for impact, not a judgement about
# any particular thesis. /brief's triage is the real verdict; this is the floor
# that exists on every item of every run.
#
# Scores are deliberately spread so ties break sensibly, and every item carries
# the tag that produced its score so a wrong call is visible rather than opaque.
IMPACT_RULES = [
    ("regulatory", 85, r"\b(ftc|doj|sec (probe|investigat)|antitrust|lawsuit|sued|settlement|"
                       r"injunction|export control|sanction|tariff|ban(ned|s)?\b|subpoena|"
                       r"recall|consent decree|fined)\b"),
    # "to buy" and a bare "acquires" matched clickbait ("A $31 Billion Reason to
    # Buy") and 13F filings ("Acquires Shares of 5,871") respectively, so both
    # are now anchored to an actual transaction.
    ("deal",       80, r"\b(contract|design win|supply agreement|partnership|partners with|"
                       r"merger|takeover|joint venture|awarded|agrees to (buy|acquire)|"
                       r"acquires? (?!shares|stake|a stake|holdings)\w+|"
                       r"wins? (a |the )?(deal|order|contract)|signs? (a |the )?(deal|contract|agreement)|"
                       r"lands? (a |the )?(deal|contract))\b"),
    # A bare "outlook" matched clickbait framing ("Weekend Outlook", "Analyst
    # Outlook"), so it now has to be the company's own outlook being changed.
    ("guidance",   78, r"\b(guidance|pre-?announc\w+|profit warning|"
                       r"(raises?|cuts?|lifts?|lowers?|reaffirms?|withdraws?) (its |the |full[- ]year |fy ?\d*|q\d )*"
                       r"(guidance|outlook|forecast)|"
                       r"(full[- ]year|fy|q\d) (guidance|outlook|forecast)|warns? (on|of|that))\b"),
    # "dividend" alone matched yield commentary, so it needs an actual action.
    ("capital",    72, r"\b(buyback|repurchase|secondary offering|equity offering|"
                       r"convertible|dilut\w+|capital raise|debt offering|spin-?off|\bipo\b|"
                       r"(declares?|raises?|hikes?|cuts?|suspends?|initiates?) (a |its |the )?"
                       r"(quarterly )?dividend|dividend (increase|hike|cut|suspension))\b"),
    ("management", 70, r"\b(ceo|cfo|coo|chairman|president)\b.{0,40}\b(steps? down|resign\w*|"
                       r"depart\w*|appoint\w*|names?|hires?|succeed\w*|ousted|fired)\b"),
    # earnings is tested before product: "earnings on deck: can the ramp continue"
    # is an earnings item, and "unveiled"/"milestone" were pulling in price
    # recaps ("Moved Up 3.37% ... Key Drivers Unveiled"), so both are gone.
    ("earnings",   55, r"\b(earnings|quarterly results|q[1-4] (results|report)|reports? (q[1-4]|results)|"
                       r"beats?\b|misses?\b|revenue (rose|fell|up|down))\b"),
    ("product",    52, r"\b(launch\w*|ships?\b|shipping|tape-?out|qualif\w+|ramp\w*|"
                       r"capacity|new fab|foundry deal|volume production)\b"),
    ("analyst",    45, r"\b(upgrade[sd]?|downgrade[sd]?|initiated? (with )?(a )?(buy|sell|hold|"
                       r"outperform|neutral)|price target|reiterat\w+|maintains?\b|"
                       r"raises? target|cuts? target)\b"),
]
# Formulaic filler. These fire AFTER the signal rules above, so a real event
# mentioning a price move still ranks on the event.
IMPACT_NOISE_RULES = [
    ("ownership", 8,  r"\b(increases?|decreases?|boosts?|trims?|lowers?|raises?|purchases?|sells?|"
                      r"acquires?|makes? (a )?new investment|buys?) (its )?(stake|position|holdings|"
                      r"shares? of|\d[\d,\.]* shares)|\b13f\b|\bstake in\b"),
    ("options",   10, r"\b(options?|contracts?) (spot-?on|volume|activity)|\b\d[\d,\.]*k? contracts "
                      r"were traded\b|unusual options"),
    # The percentage is often separated from the verb ("Moved Down BY 3.06%"),
    # so the connector is optional rather than absent.
    ("pricemove", 15, r"\b(moved (up|down)|trading|rises?|falls?|slips?|jumps?|drops?|gains?|"
                      r"climbs?|dips?|soars?|sinks?|surges?|plunges?|up|down)"
                      r"(\s+(by|over|nearly|about|more than))?\s+[\d.]+\s*%"
                      r"|\b(premarket|pre-?market) (price|move|action)"
                      r"|facts behind the movement|% (higher|lower)|key drivers"),
    ("roundup",   20, r"\b(top \d+|best|worst) .{0,24}stocks?\b|stocks? (to watch|to buy)|"
                      r"morning squawk|market (wrap|roundup|open|close)|stocks? open (lower|higher)|"
                      r"msci|s&p 500 (entry|inclusion)|index inclusion|nikkei|kospi"),
]
IMPACT_COMPILED = [(t, sc, re.compile(p, re.I)) for t, sc, p in IMPACT_RULES]
IMPACT_NOISE_COMPILED = [(t, sc, re.compile(p, re.I)) for t, sc, p in IMPACT_NOISE_RULES]
# 8-K item numbers that carry real weight; a Form 4 or 13F is routine.
# Not every filing is a signal. Form 4s, 144s and N-PX proxy-voting reports are
# routine paperwork that arrives constantly; ranking them as "a filing" put
# "N-PX — Annual Report of proxy voting record" above real news and let three of
# them eat a ticker's whole per-ticker allowance.
FILING_WEIGHT = [
    (r"\b(1\.01|2\.01|5\.02|8\.01)\b", 100),   # material agreement, acquisition, officer change
    (r"\b(2\.02|7\.01|9\.01)\b", 92),           # results, Reg FD
    (r"^\s*10-K\b|\b10-K —", 95),
    (r"^\s*10-Q\b|\b10-Q —", 90),
    (r"^\s*8-K\b|\b8-K —", 88),
    (r"^\s*(425|S-1|S-3|424B)\b", 86),             # M&A / offering paperwork
    (r"^\s*DEF ?14A\b|proxy statement", 62),
    (r"^\s*SC 13[DG]\b|schedule 13[dg]", 42),      # activist/large-holder, occasionally matters
    (r"^\s*4/?A?\b|statement of changes in beneficial", 22),   # Form 4 insider routine
    (r"^\s*144\b|proposed sale of securities", 18),
    (r"^\s*N-PX\b|proxy voting record", 12),       # fund proxy voting — pure noise
]
FILING_COMPILED = [(re.compile(p, re.I), sc) for p, sc in FILING_WEIGHT]


def score_impact(item):
    """Return (score, tag). Higher = more likely to matter."""
    title = item.get("t", "") or ""
    if item.get("kind") == "filing":
        for rx, sc in FILING_COMPILED:
            if rx.search(title):
                return sc, "filing"
        return 58, "filing"
    # 13F/ownership phrasing is unambiguous and routinely collides with the deal
    # vocabulary, so it wins outright rather than falling through the signal rules.
    own_tag, own_sc, own_rx = IMPACT_NOISE_COMPILED[0]
    if own_rx.search(title):
        return own_sc, own_tag
    for tag, sc, rx in IMPACT_COMPILED:
        if rx.search(title):
            return sc, tag
    for tag, sc, rx in IMPACT_NOISE_COMPILED:
        if rx.search(title):
            return sc, tag
    return 30, "unclassified"


def impact_tier(score):
    return "high" if score >= 70 else ("medium" if score >= 40 else "low")


def item_key(item):
    """Stable dedupe key. Filings key on their URL — every 8-K shares the title
    '8-K — Current report', so keying on text alone would hide all but the first."""
    basis = item.get("url") or item.get("t", "")
    normalized = re.sub(r"[^a-z0-9]+", "", basis.lower())
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
    ap.add_argument("--topics", dest="topics", action="store_true", default=True,
                    help="also scan Topics.yaml themes (default on)")
    ap.add_argument("--no-topics", dest="topics", action="store_false",
                    help="ticker pass only")
    ap.add_argument("--providers", default=DEFAULT_PROVIDERS,
                    help="comma-separated providers (default %(default)s; available: "
                         + ",".join(sorted(PROVIDERS)) + ")")
    ap.add_argument("--dry-run", action="store_true", help="resolve + select only; no network, no writes")
    ap.add_argument("--output", default=DIGEST_PATH, help="digest path (default %(default)s)")
    args = ap.parse_args(argv)

    chosen = [p.strip() for p in args.providers.split(",") if p.strip()]
    unknown = [p for p in chosen if p not in PROVIDERS]
    if unknown or not chosen:
        ap.error("unknown provider(s): %s (available: %s)"
                 % (", ".join(unknown) or "none given", ", ".join(sorted(PROVIDERS))))

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
    digest_tickers, errors = [], []
    # attempts/failures per provider — a provider that fails everywhere is the
    # signal that a host went dark, which is exactly what hid for seven weeks.
    stats = {name: {"attempts": 0, "failures": 0, "items": 0} for name in chosen}
    for e in selected:
        items, ticker_failed = [], 0
        for name in chosen:
            stats[name]["attempts"] += 1
            try:
                got = PROVIDERS[name](e, args.hours)
            except Exception as exc:  # one provider failing must not lose the others
                stats[name]["failures"] += 1
                ticker_failed += 1
                errors.append({"ticker": e["ticker"], "provider": name,
                               "error": str(exc)[:120]})
                continue
            stats[name]["items"] += len(got)
            items.extend(got)
            time.sleep(0.5)
        if ticker_failed == len(chosen):
            continue  # nothing came back at all; already recorded in errors
        # Rank by impact, not by kind. A material 8-K still beats any headline,
        # but a Form 4 no longer displaces real news just for being a filing.
        for it in items:
            it["impact"], it["impact_tag"] = score_impact(it)
        items.sort(key=lambda i: (-i["impact"], i.get("d") or ""))
        fresh = []
        for item in items:
            if item.get("kind") == "news" and NOISE_RE.search(item["t"]):
                continue
            key = item_key(item)
            if key in state["seen"]:
                continue
            state["seen"][key] = today
            item["impact_tier"] = impact_tier(item["impact"])
            fresh.append(item)
            if len(fresh) >= args.max_per_ticker:
                break
        # Best items first within a ticker, so a truncated list keeps the signal.
        state["last_included"][e["ticker"]] = today
        if fresh:
            folder_rel = os.path.relpath(e["folder"], REPO_ROOT) if e["folder"] else None
            digest_tickers.append({
                "ticker": e["ticker"],
                "company": e["company"],
                "sector": e.get("sector"),
                "thesis": e["thesis"],
                "drift": e["drift"],
                "folder": folder_rel,
                "headlines": fresh,
            })

    # ---- topic pass ---------------------------------------------------------
    # Themes, not tickers: coverage of a subject before there is a name for it,
    # plus the discovery funnel for untracked companies named in the results.
    topic_results, discovered = [], []
    topic_stats = {"attempts": 0, "failures": 0, "items": 0}
    if args.topics:
        known = {e["ticker"].upper() for e in entries}
        name_index = load_sec_company_names()
        for topic in parse_topics(TOPICS):
            topic_stats["attempts"] += 1
            try:
                items = parse_rss_items(
                    fetch_url(topic_query_url(topic["query"], args.hours)), args.hours)
            except Exception as exc:
                topic_stats["failures"] += 1
                errors.append({"ticker": "topic:" + topic["id"], "provider": "googlenews",
                               "error": str(exc)[:120]})
                continue
            topic_stats["items"] += len(items)
            fresh = []
            for item in items:
                if NOISE_RE.search(item["t"]):
                    continue
                key = item_key(item)
                if key in state["seen"]:
                    continue
                state["seen"][key] = today
                fresh.append(item)
                if len(fresh) >= args.max_per_ticker:
                    break
            discovered.extend(discover_tickers(fresh, known, name_index))
            if fresh:
                topic_results.append({
                    "id": topic["id"],
                    "label": topic.get("label", topic["id"]),
                    "tickers": topic.get("tickers", []),
                    "gaps": topic.get("gaps", []),
                    "headlines": fresh,
                })
            time.sleep(0.5)
        # collapse duplicates discovered across several topics
        merged = {}
        for d in discovered:
            merged.setdefault(d["ticker"], set()).update(d["seen_in"])
        discovered = [{"ticker": k, "seen_in": sorted(v)[:3]}
                      for k, v in sorted(merged.items())]

    digest = {
        "generated": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "window_hours": args.hours,
        "scanned": len(selected),
        "with_news": len(digest_tickers),
        "quiet": sorted(e["ticker"] for e in selected
                        if e["ticker"] not in {d["ticker"] for d in digest_tickers}
                        and e["ticker"] not in {x["ticker"] for x in errors}),
        "errors": errors,
        "providers": stats,
        "topic_stats": topic_stats,
        "not_in_registry": not_in_registry,
        # Drift for EVERY scanned ticker, not just the ones with news. The
        # dashboard flags thesis drift per card, and a flag that only appears
        # when a ticker happens to have a headline is worse than no flag.
        "drift_index": {e["ticker"]: e["drift"] for e in selected if e.get("drift")},
        "tickers": digest_tickers,
        "topics": topic_results,
        "discovered": discovered,
    }

    # A broken run produces a well-formed digest with zero headlines, which is
    # indistinguishable from a quiet day once written. That is how a seven-week
    # outage stayed invisible. Refuse to publish one over a digest that has
    # content, and treat a provider that returned nothing as suspect.
    #
    # Two ways a provider dies, and the silent one is the dangerous one:
    #   failing   — raises, lands in errors, obvious
    #   silent    — answers 200 with zero items, e.g. a feed format change that
    #               no longer matches the parser. Invisible without this check.
    total_attempts = sum(v["attempts"] for v in stats.values())
    total_failures = sum(v["failures"] for v in stats.values())
    total_items = sum(v["items"] for v in stats.values())
    all_failed = total_attempts > 0 and total_failures == total_attempts
    no_raw_items = total_attempts > 0 and total_items == 0
    # Topic hits deliberately do NOT count here. A digest whose ticker pass
    # wholly failed is a broken run even if the themes came back fine, and
    # writing it would quietly drop every ticker the previous one held.
    would_clobber = not digest_tickers and existing_digest_has_content(args.output)

    failing = [n for n, v in stats.items() if v["attempts"] and v["failures"] == v["attempts"]]
    silent = [n for n, v in stats.items()
              if v["attempts"] and not v["failures"] and v["items"] == 0]
    dead = failing + silent

    if all_failed or (would_clobber and (errors or no_raw_items)):
        reason = ("every fetch failed" if all_failed
                  else "no new items and %d fetch errors" % len(errors) if errors
                  else "no provider returned a single item")
        print("REFUSING to write digest: %s — leaving %s untouched."
              % (reason, os.path.relpath(args.output, REPO_ROOT)), file=sys.stderr)
        for name in failing:
            print("  provider %s failed on all %d attempts"
                  % (name, stats[name]["attempts"]), file=sys.stderr)
        for name in silent:
            print("  provider %s answered on all %d attempts but returned nothing "
                  "— check whether its feed format changed"
                  % (name, stats[name]["attempts"]), file=sys.stderr)
        for err in errors[:5]:
            print("  %s/%s: %s" % (err["ticker"], err["provider"], err["error"]), file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(digest, f, indent=1, ensure_ascii=False)
    save_state(state)

    summary = ", ".join("%s %d" % (n, v["items"]) for n, v in stats.items())
    if args.topics:
        summary += ", topics %d" % topic_stats["items"]
    print(f"Scanned {len(selected)} tickers → {len(digest_tickers)} with new items, "
          f"{len(topic_results)} topics with hits, {len(errors)} fetch errors. "
          f"Items by provider: {summary}. "
          f"Digest: {os.path.relpath(args.output, REPO_ROOT)}")
    if discovered:
        print("Discovered %d untracked ticker(s): %s"
              % (len(discovered), ", ".join(d["ticker"] for d in discovered)))
    for name in failing:
        print("WARNING: provider %s failed on all %d attempts — it may be blocked."
              % (name, stats[name]["attempts"]), file=sys.stderr)
    for name in silent:
        print("WARNING: provider %s returned zero items on all %d attempts — it may "
              "have changed format." % (name, stats[name]["attempts"]), file=sys.stderr)
    return 1 if dead else 0


if __name__ == "__main__":
    sys.exit(main())
