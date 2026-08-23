# Rebuild Plan — session handoff

*Written 2026-08-23. Carries the audit + plan from a prior session into the new cloud container.*

**Goal in the owner's words:** stay on top of sector news and social sentiment across the
AI/robotics ecosystem; track news against chosen topics and tickers; leave the door open for
discovering new tickers; be able to tell fact from fiction. Explicitly *not* a sophisticated
investing apparatus.

**Owner uses X/Twitter as the primary news source.** What works there: real-time alpha as news
breaks, good downstream-impact analysis on major announcements (e.g. NVDA), some useful technical
analysis. What doesn't: no way to separate fact from fiction.

---

## Audit findings (all verified against the repo on 2026-08-23)

### 1. 73 of 77 registry paths are broken — highest priority

Sector folders were renamed to layer-prefixed names (`Application` → `L01 Application`,
`Interconnect` → `L07 Interconnect`, etc.) and `Investing/Wiki/Reference/Monitor Registry.yaml`
was never updated to match. Every skill resolves ticker folders through that registry, so
`/ticker-monitor`, `/score-ticker`, and `/stock-research-all` all read from a dead index.

Only `scripts/watchlist_refresh_fetch.py` still works, because it happens to have a scan-disk
fallback for stale registry paths.

Reproduce:

```bash
grep -E '^\s+path:' "Investing/Wiki/Reference/Monitor Registry.yaml" \
  | sed 's/.*path: *"\?//; s/"$//' \
  | while read -r p; do [ -e "$p" ] || echo "MISSING: $p"; done | wc -l
```

Current sector folder names on disk are inconsistent — some layer-prefixed, some not:
`Edge & Physical AI`, `L01 Application`, `L02 AI Model`, `L04 Cloud Infrastructure`,
`L05 Compute Hardware`, `L06 Memory`, `L07 Interconnect`, `L08 Advanced Packaging`,
`L09 Semiconductor Foundry`, `L10 Semiconductor Equipment`, `L11 Semiconductor Materials`,
`L12 Critical Minerals`, `Power`, `Security`, `Space & Comms`.

### 2. The automation backbone never ran

`scripts/watchlist_refresh_fetch.py` is the zero-token, no-typing half of `/watchlist-refresh`.
In the old container every outbound host was blocked by egress policy — `news.google.com` returned
403 at the CONNECT tunnel, and `sec.gov`, `data.sec.gov`, Yahoo Finance, GlobeNewswire, PRNewswire,
Businesswire, Reuters and Seeking Alpha all refused to tunnel. So the filings-dependent skills were
dead too, not just the news fetcher.

The committed seed digest admits it in its own `note` field: *"RSS egress blocked; subsequent runs
come from scripts/watchlist_refresh_fetch.py."* They never did.

**The new cloud container is provisioned to fix this. Verify before building on top of it** — see
"First steps" below.

Nothing is scheduled either: no GitHub Actions, and `gemini-scribe/Scheduled-Tasks/scheduled-tasks-state.json`
is `{}`. "Daily pass" has only ever meant the owner opening a session and typing.

Evidence of decay: last digest `2026-05-20`, last dashboard `2026-06-20`, last commit `2026-07-02`.

### 3. The system is built for KB construction, not for the stated goal

13 skills, ~2,500 lines of prompt. Eight of them exist to *build* structure — `map-sector`,
`build-customer-matrix`, `scout-tickers`, `screen-stocks`, `detect-shifts`, `ingest-ecosystem`,
`score-ticker`, `stock-research-all` — against an owner who wants news and sentiment.

The sprawl shows in a stalled migration: 80 legacy single-file tickers alongside 35 three-layer
folders, and 15 of 46 `signals.md` files are still empty templates.

### 4. `Watchlist.md` is empty, and it scopes the daily pass

`Investing/Wiki/Reference/Watchlist.md` has empty Core Holdings / Rockets / Compounders tables and
7 tickers under a malformed "Watching" table. The daily pass defaults to Watchlist scope, so it
covered 7 of 77 names.

### 5. Fact-vs-fiction is unaddressed

`/ingest-sentiment` transcribes tweet claims verbatim into signal notes. There is no verification
step anywhere, so the vault mirrors X's core weakness instead of filtering it. This is the owner's
single biggest complaint and the largest unbuilt opportunity.

---

## Plan

### 1. Repair the registry — do this first

Mechanical, needs no network, unblocks every other skill. Rewrite `path:` values to match the
folders on disk, then settle on **one** sector naming convention so it can't rot again. Add a
cheap integrity check (the loop above) so drift surfaces immediately next time.

### 2. Harden the fetcher

Assuming egress now works, the RSS path runs at zero token cost and this shrinks a lot. Two fixes
still matter, because this exact failure hid for seven weeks:

- **Exit non-zero when every fetch errors.** It currently writes a well-formed digest containing
  zero headlines and exits `0`.
- **Never overwrite a good digest with an empty one.**
- Add `Investing/Raw/Inbox/.watchlist-refresh-state.json` to `.gitignore` — it's a machine-local
  seen-cache that currently shows up as untracked debris on every run.
- Optional now rather than required: a pluggable provider backend with `WebSearch` as fallback, so
  one blocked domain can't silently kill the pipeline again.

### 3. Topics, not just tickers

The system is 100% ticker-keyed today. Add a small `Topics.yaml` — *humanoid robotics, physical AI,
HBM supply, radar vs. lidar, NVDA downstream effects*. This buys two things: coverage of themes
before owning a name in them, and a **discovery funnel** — topic hits naming untracked tickers
become candidates automatically, as a byproduct rather than a separate `/scout-tickers` ritual.

Rebuild `Watchlist.md` at the same time; it's the scope input for everything.

### 4. Collapse 13 skills to 3

| Keep | Does |
|---|---|
| `/brief` | The automated daily: news + social across tickers *and* topics, triaged, one digest out |
| `/dig TICKER` | On-demand deep dive when the brief flags something |
| `/track TICKER` | Lightweight add-to-watchlist, no three-layer ceremony |

Move the other 10 to `.claude/commands/_archive/` — not deleted, just unloaded and unmaintained.

### 5. Schedule it, and pin the environment

A weekday-morning Routine is the difference between a tool that gets used and a repo that generates
guilt. **The Routine must be pinned to the environment that has egress** — if it fires into a
default or inherited environment it will silently produce empty digests exactly as before. Record
the sanctioned environment in `CLAUDE.md`.

Deliver the digest to **Slack or Notion** (both are connected). A 355KB `index.html` in a git repo
does not get read every morning; a Slack DM does. Keep the HTML dashboard as an occasional
deep-dive view.

### 6. Build the fact/fiction filter — the real unlock

For each substantive claim ingested from social:

- **Classify it** — verifiable fact / projection / opinion / technical analysis. Store them
  differently. A price target is not a fact.
- **Verify the verifiable ones** against a primary source (SEC filing, company PR, transcript) and
  stamp `CONFIRMED` / `UNCONFIRMED` / `CONTRADICTED` with a source link. Unverified claims stay
  visibly unverified.
- **Keep an author scorecard** — an append-only ledger per `@handle`: claims made, how many later
  confirmed. After a few months this shows empirically which accounts are worth reading. Nearly
  free to maintain, and it also blunts the "unbalanced" problem: when the brief surfaces a bull
  claim it can note whether a counterpoint exists.

### 7. Prune the KB

Don't finish the three-layer migration — reverse it for most names. Reserve three layers for the
handful actually held; everything else gets one lightweight file. 80 + 35 half-migrated is worse
than either end state.

---

## First steps in the new container

Confirm egress actually works before building on it:

```bash
python3 scripts/watchlist_refresh_fetch.py --tickers NVDA,CRDO --hours 168
# expect: "2 tickers → N with new headlines, 0 fetch errors"
# if 403 Forbidden → egress didn't take effect; sort that first

curl -sS -o /dev/null -w '%{http_code}\n' https://data.sec.gov/submissions/CIK0001045810.json
# expect 200 — the filings skills need this
```

Then start on step 1. The registry repair needs no network and unblocks the rest.

## Open decisions

- **Digest delivery** — Slack DM, Notion page, or both?
- **Provider fallback** — worth building the `WebSearch` backend now, or rely on RSS while egress holds?

Everything else has a sensible default.
