---
description: Token-efficient daily watchlist refresh. A local script fetches news headlines for up to 50 registry tickers (zero model tokens), dedupes against a seen-cache, and pairs each ticker's headlines with its One-Line Thesis + Drift status. With --social it also folds in StockTwits + Reddit chatter, flagging volume spikes and sentiment flips. Claude only triages the resulting digest for thesis drift. Material items → signals.md; social → Social Mentions; drift/conviction changes → analysis.md; compact daily summary → Output/Digest. Designed for a Claude Pro budget, 1–2 runs/day. Scans Watchlist.md tickers by default; --all widens to the full registry. Usage: /watchlist-refresh [--all] [--social] [--limit N] [--hours H] [--tickers CSV]
allowed-tools: Bash(python3 scripts/watchlist_refresh_fetch.py:*), Bash(python3 scripts/social_pulse.py:*), Bash(git add:*), Bash(git commit:*), Bash(git push:*), Read, Edit, Write
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

**`--social`** adds a StockTwits + Reddit pass into the same digest
(`scripts/social_pulse.py`). It roughly doubles wall-clock time (one extra
request per source per ticker, 1 s spacing) but adds little to the token bill,
because the script only emits what is *unusual*:

- **StockTwits** (US listings only — foreign lines like BESI/SIVE/XFAB are
  skipped) → message volume vs a 14-day rolling baseline, bull/bear split, and
  ≤3 highest-engagement messages.
- **Reddit** → `r/stocks+investing+wallstreetbets+StockMarket+SecurityAnalysis+ValueInvesting+options`,
  ≤3 posts clearing 25 upvotes.
- **Flags** — `chatter spike Nx baseline`, `sentiment more bullish/bearish:
  A% → B%`, `reddit traction`.

A ticker that is merely chatty (liked messages, no flag, no Reddit thread) is
dropped unless it also has news — otherwise every liquid name would appear
every run. Baselines need ~3 prior runs before spikes can be detected, so the
first few `--social` runs will flag little; that is expected, not a fault.

If the run reports fetch errors on `stocktwits` or `reddit`, diagnose with
`python3 scripts/social_pulse.py --probe NVDA` and report the outcome — do not
retry the batch. Neither source is a stable public API; both can gate keyless
access without notice.

## Phase 2 — Read the digest

Read `Investing/Raw/Inbox/watchlist-refresh-digest.json` — the ONLY file you
read unconditionally. Each entry: ticker, thesis, drift, folder, headlines, and
on `--social` runs an optional `social` block (`flags`, `stocktwits`, `reddit`).
An entry can have an empty `headlines` list and still be present — that is a
ticker pulled in on social signal alone.

Stop and write nothing when there is nothing to triage: `with_news` is 0 **and**
(`social_scanned` is absent or `with_social` is 0). Report "Quiet day — N
tickers scanned, no new headlines[, no unusual chatter]" plus any fetch errors.

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

### Social blocks (`--social` runs)

A ticker's `social` block is **sentiment, not fact**. Retail chatter is a
prompt to look, never evidence that something happened:

| Content | Action |
|---------|--------|
| Flags + quotes with no substantive claim | Social Mentions in signals.md only |
| A quote or Reddit post asserting a *checkable fact* (contract, guidance, filing, departure) | Treat as the headline case above — but it is MATERIAL only once corroborated; otherwise log to Social Mentions and add to the deep-pass queue |
| `chatter spike` / `sentiment` flip with no news that day | Social Mentions + deep-pass queue |

**A social flag alone never moves Conviction Log or Drift status.** Volume and
bull% measure attention, not fundamentals — writing them into analysis.md
would let retail noise contaminate the thesis record. Escalation path for an
unexplained spike is `/ticker-monitor --deep TICKER`, not a drift edit.

## Phase 4 — Layered writes (append-only, touched tickers only)

**signals.md — News & Alpha Log.** Match the file's existing format: if it's a
table, append `| YYYY-MM-DD | headline ≤25 words | source | so-what, 1 sentence |`;
if bullets, use the bullet form. Then append one Research Log line:
`- **YYYY-MM-DD** — 📰 WATCHLIST-REFRESH | [n] headlines triaged, [m] logged[, drift flagged]`
Do NOT write to signals.md of quiet tickers.

**signals.md — Social Mentions** (`--social` runs only). Same section
`/ingest-sentiment` writes, so keep its format. One line per flagged ticker,
not per message — the digest already collapsed the firehose:
`- **YYYY-MM-DD** — 💬 StockTwits [n] msgs, [bull%]% bull ([Nx] baseline) · Reddit: [post title] (r/sub, ↑[score]) — [what the crowd thinks, 1 sentence]`
Attribute quotes to the handle the digest gives. Create the section if absent.

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
Scanned N | with news M | social S | material K | drift flags J | errors E

| Ticker | Verdict | Item | Action taken |
|--------|---------|------|--------------|

**Social flags:** CRDO chatter spike 2.4× · SNDK sentiment 40% → 75% bull
**Deep-pass queue:** /ticker-monitor --deep XXXX — reason
**Not onboarded:** TICK1, TICK2 (run /add-ticker)
```

Omit the `social` count and `Social flags` line entirely on non-`--social` runs.

Print the same summary in chat.

## Phase 6 — Publish (skip with --no-push)

The dashboard's Watchlist tab fetches
`Investing/Raw/Inbox/watchlist-refresh-digest.json` from `master` via
raw.githubusercontent at page load — new headlines appear on the deployed
dashboard only after a push. Commit everything the run touched (digest,
state file, signals.md / analysis.md edits, Output/Digest summary) with
message `Watchlist refresh YYYY-MM-DD` and `git push`. No gh-pages deploy
needed — the dashboard HTML doesn't change, only the data it fetches.

## Token discipline

- The digest is pre-deduped and pre-filtered — trust it; never re-read
  Monitor Registry.yaml, Watchlist.md, or facts.md in this skill.
- Read analysis.md only for tickers getting a THESIS write.
- No searches, no agents, no EDGAR. Typical run ≈ digest (~2–5k tokens in)
  + a handful of small edits — comfortably 1–2×/day on a Pro plan.
- `--social` adds roughly 1–2k tokens on a busy day: quotes are capped at 3 per
  ticker and 220 chars each, and unflagged chatty tickers never reach you.
  Never re-fetch a social source yourself to "check" a flag.

## Scheduling

Cron (headless, from the repo root — adjust path):

```cron
# weekdays 7:30 & 16:30 — twice-daily refresh, social on the morning pass
30 7  * * 1-5  cd /path/to/investing-wiki && claude -p "/watchlist-refresh --social" >> .watchlist-refresh.log 2>&1
30 16 * * 1-5  cd /path/to/investing-wiki && claude -p "/watchlist-refresh" >> .watchlist-refresh.log 2>&1
```

Inside a live session: `/loop 12h /watchlist-refresh`.
The fetch script is allowlisted in `.claude/settings.json`, and all other
writes are plain file edits, so headless runs need no extra permission flags
beyond your usual edit permissions (add `--permission-mode acceptEdits` if
unattended).
