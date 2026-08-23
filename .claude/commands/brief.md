---
description: The daily pass. A local script fetches news, SEC filings and topic themes for every Watchlist ticker at zero model tokens; Claude only triages the digest against each One-Line Thesis. Material items → signals.md, thesis drift → analysis.md, one summary → Output/Digest. Also files any social signals staged in Tweets.md. Usage: /brief [--all] [--hours H] [--tickers CSV] [--no-topics] [--no-push]
allowed-tools: Bash(python3 scripts/watchlist_refresh_fetch.py:*), Bash(python3 scripts/check_registry.py:*), Bash(git add:*), Bash(git commit:*), Bash(git push:*), Read, Edit, Write
---

# Brief — the daily pass

One command, one digest. Every mechanical step happens in a script; the model's
only job is judgment: *does today's news confirm, contradict, or not touch each
ticker's thesis?*

**Hard rule — no searching.** Never call WebSearch or WebFetch here. Judge from
headlines and filing metadata alone. Anything needing real research goes to the
deep-pass queue (`/dig TICKER`) in the summary instead. A single search would
cost more tokens than the entire rest of this run.

## Phase 1 — Fetch (zero model tokens)

```
python3 scripts/watchlist_refresh_fetch.py $ARGUMENTS
```

Scope is **Watchlist.md** (`--all` widens to the full registry). The script
fetches Google News headlines, SEC filings via EDGAR, and the themes in
`Topics.yaml`, dedupes against a seen-cache, and writes one digest.

**Check the exit status.** Non-zero means a provider was dead or an empty
digest would have overwritten a good one — the script refuses to publish a
broken run rather than let it look like a quiet day. Report what it printed to
stderr and stop; do not paper over it by triaging a stale digest.

## Phase 2 — Read the digest

Read `Investing/Raw/Inbox/watchlist-refresh-digest.json`. It is the ONLY file
you read unconditionally. Keys: `tickers`, `topics`, `discovered`, `errors`,
`providers`, `not_in_registry`.

If `with_news` is 0 and `topics` is empty: report "Quiet day — N scanned" plus
any errors, and **stop**. Write nothing.

## Phase 3 — Triage tickers against their thesis

Each digest entry pairs a ticker's items with its One-Line Thesis and current
Drift status. Classify every item:

| Verdict | Test | Action |
|---|---|---|
| **NOISE** | Recap, price-move story, listicle, unrelated company | Skip silently |
| **MATERIAL** | A new fact about the company or its supply chain — contract, product, filing, guidance, M&A, regulation, analyst action with reasoning | signals.md |
| **THESIS** | MATERIAL **and** it confirms, accelerates, weakens or breaks a specific leg of the One-Line Thesis | signals.md **and** analysis.md |

Items with `"kind": "filing"` are primary sources and rank above any headline
about the same event — an 8-K's item numbers (1.01 material agreement, 2.03
debt, 5.02 officer departure) usually say more than the story covering it.

Ambiguous but potentially thesis-breaking → MATERIAL, and add the ticker to the
deep-pass queue. A ticker with `thesis: null` → log MATERIAL to signals.md if
the folder exists; otherwise list it under "not onboarded".

## Phase 4 — Triage topics

Topic entries carry `tickers` (registered names the theme bears on) and `gaps`
(names that matter but are not registered). For each topic with hits:

- A theme development that bears on a **registered** ticker's thesis → treat it
  as a THESIS item for that ticker and write it through Phase 5.
- A development with no registered name attached → it belongs in the summary
  only. Do not manufacture a ticker page for it.
- Note when a topic's hits keep landing on its `gaps` — that is the signal the
  theme needs onboarding, not that the theme is noisy.

## Phase 5 — Layered writes (append-only, touched tickers only)

**signals.md — News & Alpha Log.** Match the file's existing shape. Table:
`| YYYY-MM-DD | item ≤25 words | source | so-what, 1 sentence |`. Bullets: use
the bullet form. Then one Research Log line:
`- **YYYY-MM-DD** — 📰 BRIEF | [n] items triaged, [m] logged[, drift flagged]`
Never write to a quiet ticker's signals.md.

**analysis.md — THESIS verdicts only.** Read it only when writing to it.
- Conviction Log: `| date | event ≤15 words | ↑/↓/→ | why, 1–2 sentences |`
- Drift status: update the `**Drift status:**` and `**Last validated:**` lines
  only when the direction actually changes (On track / Drifting / Broken).
  **Headline evidence alone never sets Broken** — flag for `/dig` instead.

## Phase 6 — Social signals (only if Tweets.md has content)

Read `Investing/Raw/Inbox/Tweets.md`. If empty, skip this phase silently.

Split into individual claims. For each, record **what kind of claim it is** —
this is the part that separates a fact from a take:

| Class | Example | Weight |
|---|---|---|
| `fact` | "Company filed an 8-K for a $2B facility" | Verifiable — check it against the digest's filings before logging |
| `projection` | "Revenue will double by 2027" | A forecast, never a fact |
| `opinion` | "This is the best name in the sector" | Sentiment only |
| `technical` | "Broke out over the 50-day" | Price action, not fundamentals |

Append to the ticker's signals.md under Social Mentions:
`| YYYY-MM-DD | @handle | class | claim ≤20 words | UNVERIFIED |`

Mark every `fact` claim `UNVERIFIED` unless the same run's filings confirm it,
in which case `CONFIRMED` with the filing URL. **Never** upgrade a claim on the
strength of a headline repeating it. Full verification and author scorecards
are a later build; until then the honest state is unverified, and recording it
as such is the point.

Then move the processed content to `Investing/Raw/Sentiment/` per its date and
clear Tweets.md.

## Phase 7 — Summary

Write `Investing/Output/Digest/YYYY-MM-DD-brief.md` (append `## Run 2 — HH:MM`
if it exists):

```
# Brief — YYYY-MM-DD
Scanned N | with news M | material K | drift flags J | topics T | errors E

| Ticker | Verdict | Item | Action |
|--------|---------|------|--------|

**Themes:** one line per topic with hits
**Discovered:** TICK — seen in "headline" (run /track TICK)
**Deep-pass queue:** /dig TICK — reason
**Not onboarded:** TICK1, TICK2 (run /track)
```

`discovered` entries are leads from a name match, not decisions — list them,
never auto-register them.

Print the same summary in chat.

## Phase 8 — Publish (skip with --no-push)

Commit everything touched (digest, signals.md / analysis.md edits, the summary,
any archived sentiment) as `Brief YYYY-MM-DD` and push.

## Token discipline

The digest is pre-deduped and pre-filtered — trust it. Never re-read Monitor
Registry.yaml, Watchlist.md, Topics.yaml or facts.md here. Read analysis.md
only for a THESIS write. No searches, no agents, no subagents. A typical run is
the digest (~3–6k tokens in) plus a handful of small edits.
