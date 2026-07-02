---
description: Token-efficient daily watchlist refresh. A local script fetches news headlines for up to 50 registry tickers (zero model tokens), dedupes against a seen-cache, and pairs each ticker's headlines with its One-Line Thesis + Drift status. Claude only triages the resulting digest for thesis drift. Material items → signals.md; drift/conviction changes → analysis.md; compact daily summary → Output/Digest. Designed for a Claude Pro budget, 1–2 runs/day. Scans Watchlist.md tickers by default; --all widens to the full registry. Usage: /watchlist-refresh [--all] [--limit N] [--hours H] [--tickers CSV]
allowed-tools: Bash(python3 scripts/watchlist_refresh_fetch.py:*), Read, Edit, Write
---

# Watchlist Refresh — Daily Thesis-Drift Pass

Cheap daily loop over the ticker universe. All fetching happens in a script;
the model's only job is judgment: *does today's news confirm, contradict, or
not touch each ticker's thesis?*

**Hard rule — no searching.** Never call WebSearch/WebFetch in this skill.
Judge from headlines alone. Anything that needs real research goes to the
deep-pass queue (`/ticker-monitor --deep TICKER`) in the summary instead.

## Phase 1 — Fetch (zero model tokens)

```
python3 scripts/watchlist_refresh_fetch.py $ARGUMENTS
```

Default universe: **only tickers named in Watchlist.md** (resolved against
Monitor Registry.yaml). `--all` widens to the full registry (Watchlist first,
then scored, then least-recently-covered rotation). 36 h lookback, ≤5 unseen
headlines/ticker, ≤50 tickers/run. Watchlist names missing from the registry
are reported in the digest as `not_in_registry` — surface them in the summary
with a `/add-ticker` pointer.

## Phase 2 — Read the digest

Read `Investing/Raw/Inbox/watchlist-refresh-digest.json` — the ONLY file you
read unconditionally. Each entry: ticker, thesis, drift, folder, headlines.

If `with_news` is 0: report "Quiet day — N tickers scanned, no new headlines"
(plus any fetch errors) and **stop**. Write nothing.

## Phase 3 — Triage each ticker's headlines against its thesis

Classify every headline:

| Verdict | Test | Action |
|---------|------|--------|
| **NOISE** | Recap, price-move story, listicle, unrelated company | Skip silently |
| **MATERIAL** | New fact about the company or its supply chain (contract, product, filing, guidance, M&A, regulation, analyst action with reasoning) | Append to signals.md |
| **THESIS** | MATERIAL **and** it confirms, accelerates, weakens, or breaks a specific leg of the One-Line Thesis / current Drift status | signals.md **and** analysis.md |

Ambiguous but potentially thesis-breaking → treat as MATERIAL, add ticker to
the deep-pass queue. Ticker has `thesis: null` → log MATERIAL items to
signals.md if the folder exists; otherwise list under "not onboarded" in the
summary.

## Phase 4 — Layered writes (append-only, touched tickers only)

**signals.md — News & Alpha Log.** Match the file's existing format: if it's a
table, append `| YYYY-MM-DD | headline ≤25 words | source | so-what, 1 sentence |`;
if bullets, use the bullet form. Then append one Research Log line:
`- **YYYY-MM-DD** — 📰 WATCHLIST-REFRESH | [n] headlines triaged, [m] logged[, drift flagged]`
Do NOT write to signals.md of quiet tickers.

**analysis.md — THESIS verdicts only.** Read the file only when writing to it.
- Conviction Log: `| date | event ≤15 words | ↑/↓/→ | why, 1–2 sentences |`
- Drift status block: update `**Drift status:**` line + `**Last validated:**`
  date only if the direction actually changes (On track / Drifting / Broken).
  Headline-level evidence alone never sets **Broken** — flag for deep pass.

## Phase 5 — Daily summary

Write `Investing/Output/Digest/YYYY-MM-DD-watchlist-refresh.md` (append a
`## Run 2 — HH:MM` section if the file already exists):

```
# Watchlist Refresh — YYYY-MM-DD
Scanned N | with news M | material K | drift flags J | errors E

| Ticker | Verdict | Item | Action taken |
|--------|---------|------|--------------|

**Deep-pass queue:** /ticker-monitor --deep XXXX — reason
**Not onboarded:** TICK1, TICK2 (run /add-ticker)
```

Print the same summary in chat. Done.

## Token discipline

- The digest is pre-deduped and pre-filtered — trust it; never re-read
  Monitor Registry.yaml, Watchlist.md, or facts.md in this skill.
- Read analysis.md only for tickers getting a THESIS write.
- No searches, no agents, no EDGAR. Typical run ≈ digest (~2–5k tokens in)
  + a handful of small edits — comfortably 1–2×/day on a Pro plan.

## Scheduling

Cron (headless, from the repo root — adjust path):

```cron
# weekdays 7:30 & 16:30 — twice-daily refresh
30 7,16 * * 1-5  cd /path/to/investing-wiki && claude -p "/watchlist-refresh" >> .watchlist-refresh.log 2>&1
```

Inside a live session: `/loop 12h /watchlist-refresh`.
The fetch script is allowlisted in `.claude/settings.json`, and all other
writes are plain file edits, so headless runs need no extra permission flags
beyond your usual edit permissions (add `--permission-mode acceptEdits` if
unattended).
