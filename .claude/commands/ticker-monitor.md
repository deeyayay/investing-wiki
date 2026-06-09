---
description: Recurring update pass across all wiki ticker pages. Searches for new SEC filings, earnings, analyst coverage, and upcoming catalysts. Layered writes — earnings/filings go to facts.md (Layer 1), conviction/analyst/catalyst go to analysis.md (Layer 2), news and research log go to signals.md (Layer 3). Append-only. Run weekly or on-demand. Usage: /ticker-monitor [--force] [--dry-run] [--sector SECTOR] [--deep TICKER] [--news-only]
allowed-tools: WebSearch, WebFetch, Read, Edit, Agent
---

# Ticker Monitor — Recurring Update Pass

Scans the Registry and appends new data to the correct layer of each ticker's file structure. Never reads signals.md. Never rewrites existing content.

**Registry:** `Investing/Wiki/Reference/Monitor Registry.yaml`
**Layer 1 (facts):** `[path]/facts.md` — YAML frontmatter; earnings + filings written here
**Layer 2 (analysis):** `[path]/analysis.md` — conviction, analyst, catalyst, cross-ticker signals, thesis drift
**Layer 3 (signals):** `[path]/signals.md` — news log + research log (append-only)

**Input flags (`$ARGUMENTS`):**
- *(none)* — standard pass; skip tickers with `last_updated` < 3 days ago in facts.md
- `--force` — run all tickers regardless of recency
- `--dry-run` — print planned writes; make no file changes
- `--sector "Sector Name"` — limit to one sector
- `--deep TICKER` — single-ticker pass with 4 searches instead of 2
- `--news-only` — lightweight daily mode: 1 search/ticker, writes to signals.md only (no EDGAR, no conviction, no analyst); replaces the deprecated /daily-news skill

---

## Phase 0 — Migration check (before inventory)

Before building the work list, scan for old-format files:
`Glob: Investing/Wiki/Sectors/**/*.md` excluding `_Sector Framework.md`, `_Supply Chain Map.md`, `_Customer Matrix.md`, `Sector Sentiment.md`, `_analysis-template.md`, `_signals-template.md`, `_facts-template.md`

For any `.md` file found directly in a sector folder (not inside a ticker subfolder), that is an old-format file. Print a migration notice:
```
⚠️  Legacy single-file tickers found. Run /ticker-monitor --deep [TICKER] on each to migrate.
    Legacy files: [list of paths]
```

When `--deep TICKER` is run on a legacy ticker, perform the migration at the start of Phase 3:
1. Read the existing `[TICKER].md` in full
2. Create `[TICKER]/` subfolder
3. Write `facts.md` — extract YAML from: management table rows, earnings table rows, SEC filings table rows; populate moat fields from Investment Thesis key moat line; set last_updated to today
4. Write `analysis.md` — move One-Line Thesis, Scoring Summary, Investment Thesis (including Thesis Drift block), Conviction Log, Cross-Ticker Signals, Catalyst Timeline, Analyst Coverage, Ecosystem Links
5. Write `signals.md` — move News & Alpha Log, Social Mentions table, Research Log
6. Delete the old `[TICKER].md`
7. Update Monitor Registry.yaml path for this ticker (remove `.md` extension)
8. Log the migration in signals.md Research Log

---

## Phase 1 — Inventory (read-only)

1. Read `Investing/Wiki/Reference/Monitor Registry.yaml`. Build the full ticker list from the `tickers:` key.
2. Apply scope filters:
   - If `--sector`: keep only tickers where `sector` matches
   - If `--deep TICKER`: keep only that one ticker
3. For each ticker in scope, read **only** `[path]/facts.md`. Extract the `last_updated` field from the YAML frontmatter.
4. Build **work list**: tickers sorted oldest `last_updated` first.
   - Unless `--force` or `--news-only`: drop tickers where `last_updated` is < 3 days ago.
5. Print the work list as a table before proceeding:

```
| Ticker | Sector | Last Updated | Action |
```

If the work list is empty, report "All tickers up to date" and stop.

---

## Phase 2 — Batch searches (token-efficient)

### --news-only mode (skip to per-ticker searches)
In `--news-only` mode, skip global searches entirely. Go directly to per-ticker searches with 1 search per ticker. Do not spawn agents — run searches sequentially or in small parallel batches.

For each ticker:
Search: `[TICKER] news earnings analyst announcement last 7 days 2026`
Return: up to 3 headline-level items (date, headline, category, why it matters). No EDGAR fetch.
Write results to `signals.md` News & Alpha Log and Research Log only. Skip all other phases.

### Standard / --deep mode

**G1 — Earnings calendar (once for all tickers):**
`earnings date calendar [all work-list tickers comma-separated] next 60 days 2026`

**G2 — Analyst activity sweep (once for all tickers):**
`[all work-list tickers comma-separated] analyst upgrade downgrade price target 2026`

**Per-ticker searches (parallel Agent calls):**

For each ticker in the work list, spawn a Haiku agent:

> You are a financial research assistant. For **[TICKER]** ([company name], [sector]):
>
> Run [2 / 4 if --deep] searches and return structured JSON only.
>
> **Search 1 — Recent news (last 30 days):**
> `[TICKER] [company name] news earnings SEC filing 8-K 10-Q 2026`
>
> **Search 2 — EDGAR recent filings:**
> Fetch: `https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=[CIK]&type=&dateb=&owner=include&count=5`
> (Skip if CIK is null — foreign-listed ticker)
>
> [--deep only] **Search 3:** `[TICKER] analyst price target earnings guidance Q2 Q3 2026`
> [--deep only] **Search 4:** `[TICKER] competitor supply chain customer concentration moat risk 2026`
>
> Return JSON only:
> ```json
> {
>   "ticker": "...",
>   "new_earnings": {
>     "quarter": "Q1 FY2027",
>     "date": "YYYY-MM-DD",
>     "revenue_b": 81.6,
>     "eps_nongaap": 1.87,
>     "beat": true,
>     "guidance_next_b": 91.0,
>     "notes": "max 20 words"
>   },
>   "new_filings": [{"type": "10-Q", "period": "Q1_FY2027", "date": "YYYY-MM-DD", "url": ""}],
>   "material_news": [
>     {
>       "date": "YYYY-MM-DD",
>       "headline": "max 25 words",
>       "category": "EARNINGS|FILING|PARTNERSHIP|PRODUCT|REGULATORY|ANALYST|MACRO",
>       "why_it_matters": "one sentence — the mechanism, not just the event",
>       "conviction_delta": "up|down|neutral",
>       "conviction_why": "1–2 sentences",
>       "cross_ticker_signals": [
>         {"direction": "emits|receives", "other_ticker": "NVDA", "signal": "≤10 words", "implication": "1 sentence"}
>       ]
>     }
>   ],
>   "nothing_new": true
> }
> ```
> If no material news or filings in 30 days, set `nothing_new: true`.

Collect all agent results before Phase 3.

---

## Phase 3 — Layered writes

For each ticker, process its agent result. Skip if `nothing_new: true`. If `--dry-run`, print planned writes instead.

### facts.md — Layer 1 writes (earnings + filings only)

**Earnings:** If `new_earnings` is present and the quarter is not already in the YAML `earnings:` array, prepend a new item to the array. Edit the YAML block between `---` markers. Preserve existing earnings entries.

**Filings:** For each entry in `new_filings` not already in the YAML `filings:` array, append a new item. Edit the YAML block.

**last_updated:** Update the `last_updated` field to today's date.

**next_earnings:** If G1 or the per-ticker agent returned a future earnings date for this ticker, update the `next_earnings` field to that date (`"YYYY-MM-DD"`). If the existing value is already a future date and no newer date was found, leave it unchanged. If the date has now passed (≤ today), clear it to `null`. Also update the `next_earnings` field in Monitor Registry.yaml for the same ticker.

Do not touch any other facts.md fields.

### analysis.md — Layer 2 writes

**Conviction Log:** For EARNINGS, PARTNERSHIP, or REGULATORY items that materially affect thesis, append a row:
`| [date] | [event ≤15 words] | [↑/↓/→] | [1–2 sentences why] |`

Conviction delta rules:
- ↑ Strengthened: earnings beat + guidance raise, strategic contract win, sole-source confirmation, insider buy at scale
- ↓ Weakened: earnings miss + guidance cut, new credible competitor, customer concentration loss, key exec departure
- → Neutral: in-line results, routine filing, macro cross-current with no direct thesis impact

**Cross-Ticker Signals:** For events with clear read-through implications, append rows to **both** affected tickers' analysis.md files:
- Source: `| [date] | Emits | [OTHER] | [signal ≤10 words] | [implication 1 sentence] |`
- Impacted: `| [date] | Receives | [SOURCE] | [signal ≤10 words] | [implication 1 sentence] |`

**Analyst Coverage:** For any analyst activity from global G2, append:
`- **[date]** — [Firm] [action] [TICKER] to [rating], PT $[X] ([reason ≤10 words])`

**Catalyst Timeline:** Mark passed `- [ ]` items as `- [x]`. Add upcoming earnings from G1 if not already listed.

**Thesis Drift Block:** Only update if the event materially changes the thesis direction:
```
> **Drift status:** [On track / Drifting / Broken] — [updated one-line reason]
> **Last validated:** [TODAY'S DATE]
```

### signals.md — Layer 3 writes

**News & Alpha Log:** For EARNINGS, FILING, PARTNERSHIP, PRODUCT, REGULATORY items (not routine MACRO or ANALYST), append:
```
- **[date]** — [headline ≤25 words]
  **Why it matters:** [1 sentence — the mechanism, not just the event]
```

**Research Log:** Append one summary line (even if `nothing_new: true`):
`- **[TODAY'S DATE]** — 📊 MONITOR | [1-sentence summary or "No material updates found"]`

---

## Phase 4 — Earnings Calendar rebuild

After all per-ticker writes are complete:

1. Read `Investing/Wiki/Reference/Monitor Registry.yaml`
2. Collect every ticker entry where `next_earnings` is not null and `next_earnings >= today`
3. Sort ascending by date
4. Write (overwrite) `Investing/Wiki/Reference/Earnings Calendar.json`:

```json
[
  {
    "ticker": "XXXX",
    "company": "Company Name",
    "sector": "Sector Name",
    "next_earnings": "YYYY-MM-DD",
    "confidence": "confirmed"
  }
]
```

`confidence` should be `"confirmed"` if the date came from an official IR announcement or SEC filing, `"estimated"` otherwise.

Skip this phase in `--news-only` mode.

---

## Phase 5 — Summary

Print a summary table:

```
| Ticker | facts.md | analysis.md | signals.md | Status |
|--------|----------|-------------|------------|--------|
```

Where Status: `Updated` / `No new data` / `Skipped (recent)` / `Migrated` / `Error`

---

## Rules

- **Layered writes only.** Earnings/filings → facts.md YAML. Conviction/analyst/catalyst/thesis drift → analysis.md. News/research log → signals.md.
- **Never read signals.md.** It is write-only during a monitor pass. Only the --news-only mode and ingest-sentiment append to it.
- **Append only.** Never modify or delete existing YAML array entries or table rows.
- **No duplicates.** Check the existing array (facts.md) or table rows (analysis.md) before appending.
- **Material news only.** Skip routine price moves, earnings whispers, articles recapping old news.
- **Compact.** News ≤25 words. Analyst entries ≤15 words. Research Log one sentence.
- **Fail gracefully.** If a search or EDGAR fetch fails, log the error in signals.md Research Log and continue.
- **Foreign-listed tickers:** EDGAR fetch will fail (CIK is null) — skip EDGAR step, rely on Search 1 only.
