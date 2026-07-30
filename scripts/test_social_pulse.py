#!/usr/bin/env python3
"""Offline end-to-end test of the watchlist_refresh_fetch --social merge path.

Neither StockTwits nor Reddit is a contract-stable API, and CI has no network,
so the merge logic is pinned here against fixtures instead. Covers:
  - a ticker with news + social      -> one merged entry
  - a ticker with social only        -> pulled in when genuinely flagged
  - a ticker that is merely chatty   -> excluded (no flag, no Reddit thread)
  - a ticker with neither            -> lands in `quiet`
  - a source failure                 -> tagged error, excluded from `quiet`
  - a second run                     -> dedupes, serves next unseen quotes

Run:  python3 scripts/test_social_pulse.py     (exit 0 = pass)
Pair with: python3 scripts/social_pulse.py --selftest   (parser-level tests)

State and output go to a temp dir, so the repo's Inbox is never touched.
"""
import json
import os
import sys
import tempfile
from datetime import datetime, timezone
from email.utils import format_datetime

REPO = "/home/user/investing-wiki"
sys.path.insert(0, os.path.join(REPO, "scripts"))

import social_pulse
import watchlist_refresh_fetch as wrf

TMP = tempfile.mkdtemp(prefix="social-merge-")

# Redirect every write target away from the repo.
wrf.STATE_PATH = os.path.join(TMP, "news-state.json")
wrf.INBOX_DIR = TMP
social_pulse.STATE_PATH = os.path.join(TMP, "social-state.json")
social_pulse.INBOX_DIR = TMP
DIGEST = os.path.join(TMP, "digest.json")

NOW = datetime.now(timezone.utc)


def rss(titles):
    items = "".join(
        f"<item><title>{t} - Reuters</title><source>Reuters</source>"
        f"<pubDate>{format_datetime(NOW)}</pubDate></item>"
        for t in titles
    )
    return f"<rss><channel>{items}</channel></rss>"


# NEWS: ALAB has headlines, CRDO has none, SNDK has none, NVDA errors.
NEWS = {
    "Astera Labs": rss(["Astera Labs lands hyperscaler design win"]),
    "Credo Technology Group": rss([]),
    "SanDisk": rss([]),
}

# SOCIAL: CRDO spikes on chatter (no news), ALAB has a reddit post, SNDK quiet.
ST_MESSAGES = {
    "CRDO": [
        {"id": i, "body": f"CRDO ripping on the AEC ramp {i}", "created_at": NOW.isoformat(),
         "user": {"username": f"u{i}", "followers": 500},
         "entities": {"sentiment": {"basic": "Bullish"}}, "likes": {"total": 9}}
        for i in range(12)
    ],
    "ALAB": [],
    # SNDK: liked messages but no baseline history and no Reddit, so it is
    # "chatty, not unusual" — the merge must NOT pull it in without news.
    "SNDK": [
        {"id": 900 + i, "body": f"SNDK NAND pricing chatter {i}", "created_at": NOW.isoformat(),
         "user": {"username": f"s{i}", "followers": 100},
         "entities": {"sentiment": {"basic": "Bullish"}}, "likes": {"total": 6}}
        for i in range(4)
    ],
}
RD_POSTS = {
    "ALAB": [{"data": {"id": "z1", "title": "Deep dive on Astera Labs retimers",
                       "subreddit": "stocks", "score": 260, "num_comments": 45,
                       "created_utc": NOW.timestamp(),
                       "permalink": "/r/stocks/comments/z1/dd/"}}],
    "CRDO": [],
    "SNDK": [],
}


def fake_fetch_rss(url, timeout=15):
    for name, body in NEWS.items():
        if name.replace(" ", "+") in url or name.replace(" ", "%20") in url:
            return body
    raise RuntimeError("simulated news fetch failure")


def fake_http_get_json(url, user_agent, timeout=20):
    if "stocktwits.com" in url:
        sym = url.rsplit("/", 1)[-1].replace(".json", "")
        if sym not in ST_MESSAGES:
            raise social_pulse.FetchError("HTTP 404 — symbol not covered by this source")
        return {"messages": ST_MESSAGES[sym]}
    if "reddit.com" in url:
        for sym, posts in RD_POSTS.items():
            if f'%22{sym}%22' in url or sym.lower() in url.lower():
                return {"data": {"children": posts}}
        return {"data": {"children": []}}
    raise AssertionError(f"unexpected url {url}")


wrf.fetch_rss = fake_fetch_rss
social_pulse.http_get_json = fake_http_get_json
wrf.time.sleep = lambda *_: None
social_pulse.time.sleep = lambda *_: None

# Pre-seed a StockTwits baseline for CRDO so the spike can be detected.
with open(social_pulse.STATE_PATH, "w") as f:
    json.dump({"seen": {}, "st_bull_pct": {},
               "st_history": {"CRDO": [["d1", 3], ["d2", 4], ["d3", 3]]}}, f)

rc = wrf.main(["--tickers", "ALAB,CRDO,SNDK,XFAB", "--social", "--output", DIGEST])
assert rc == 0, f"exit code {rc}"

with open(DIGEST) as f:
    digest = json.load(f)

print(json.dumps(digest, indent=1)[:2200])
print("\n--- assertions ---")

failures = []


def check(label, got, want):
    if got != want:
        failures.append(f"{label}: got {got!r}, want {want!r}")
    else:
        print(f"  ok  {label}")


by = {t["ticker"]: t for t in digest["tickers"]}

check("social pass recorded", digest.get("social_scanned"), True)
check("ALAB present (news + social)", "ALAB" in by, True)
check("ALAB has headline", len(by["ALAB"]["headlines"]), 1)
check("ALAB has reddit block", "reddit" in by["ALAB"]["social"], True)
check("ALAB reddit traction flagged", by["ALAB"]["social"]["flags"], ["reddit traction"])

check("CRDO pulled in on social alone", "CRDO" in by, True)
check("CRDO has no headlines", by["CRDO"]["headlines"], [])
check("CRDO chatter spike flagged",
      any("chatter spike" in f for f in by["CRDO"]["social"]["flags"]), True)
check("CRDO bull_pct computed", by["CRDO"]["social"]["stocktwits"]["bull_pct"], 100.0)
check("CRDO quotes capped at 3", len(by["CRDO"]["social"]["stocktwits"]["top"]), 3)

check("SNDK chatty-but-not-unusual excluded", "SNDK" not in by, True)
check("SNDK in quiet list", "SNDK" in digest["quiet"], True)

check("XFAB errored (no news fixture)", any(e["ticker"] == "XFAB" for e in digest["errors"]), True)
check("XFAB excluded from quiet", "XFAB" not in digest["quiet"], True)
check("news errors tagged with source",
      all("source" in e for e in digest["errors"]), True)
check("XFAB skipped stocktwits (foreign)",
      any(e["ticker"] == "XFAB" and e["source"] == "stocktwits" for e in digest["errors"]), False)

check("thesis metadata carried", "thesis" in by["CRDO"], True)
check("with_news counts news only", digest["with_news"], 1)
check("with_social counts social", digest["with_social"], 2)

# Second run must dedupe everything away.
rc2 = wrf.main(["--tickers", "ALAB,CRDO,SNDK,XFAB", "--social", "--output", DIGEST])
with open(DIGEST) as f:
    digest2 = json.load(f)
by2 = {t["ticker"]: t for t in digest2["tickers"]}
check("rerun dedupes headlines", digest2["with_news"], 0)
check("rerun drops ALAB reddit post",
      "reddit" not in by2.get("ALAB", {}).get("social", {}), True)
check("rerun keeps CRDO on the still-live spike flag", "CRDO" in by2, True)
check("rerun serves the next unseen quotes, not repeats",
      [q["user"] for q in by2["CRDO"]["social"]["stocktwits"]["top"]], ["u3", "u4", "u5"])
check("rerun still excludes chatty-only SNDK", "SNDK" not in by2, True)

print()
if failures:
    print(f"FAILED ({len(failures)})")
    for f_ in failures:
        print(f"  x {f_}")
    sys.exit(1)
print("MERGE TEST PASSED")
