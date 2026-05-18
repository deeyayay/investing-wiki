---
description: Recurring update pass across all wiki ticker pages. Searches for new SEC filings, earnings, analyst coverage, and upcoming catalysts. Append-only — never rewrites existing content. Run weekly or on-demand. Usage: /ticker-monitor [--force] [--dry-run] [--sector SECTOR] [--deep TICKER]
allowed-tools: WebSearch, WebFetch, Read, Edit, Glob, Agent
---

# Ticker Monitor — Recurring Update Pass

Scans all wiki ticker pages and appends new data to: Earnings & Financials, SEC Filings, News & Alpha Log, Analyst Coverage, Catalyst Timeline, and Research Log.

**Vault path:** `Investing/Wiki/Sectors/`

**Input flags (`$ARGUMENTS`):**
- *(none)* — standard pass, skip tickers with a Research Log entry < 3 days old
- `--force` — run all tickers regardless of recency
- `--dry-run` — print what would be written, make no file changes
- `--sector "Photonics & Optical"` — limit to one sector folder
- `--deep TICKER` — single-ticker pass with 4 searches instead of 2

---

## Phase 1 — Inventory (read-only, no searches yet)

1. Use Glob to find all `*.md` files under `Investing/Wiki/Sectors/` excluding `_Sector Framework.md`.
2. Read each file. For each, extract:
   - Ticker symbol (from filename)
   - Sector (from folder path)
   - Date of the most recent Research Log entry
   - Any `- [ ]` Catalyst Timeline items (upcoming events)
   - Whether Earnings & Financials table has any real data rows
3. Build a **work list**: tickers sorted oldest-Research-Log-entry first.
   - Unless `--force`: drop any ticker whose most recent Research Log entry is < 3 days old.
   - Unless `--sector`: include all sectors.
4. Print the work list as a table before proceeding:

```
| Ticker | Sector | Last Updated | Catalyst items | Action |
```

If the work list is empty, report "All tickers up to date" and stop.

---

## Phase 2 — Batch searches (token-efficient)

### Global searches (run once for all tickers, not per-ticker)

**G1 — Earnings calendar:**
Search: `earnings date calendar [list all work-list tickers comma-separated] next 60 days 2026`
Extract upcoming earnings dates for each ticker. Note any earnings that occurred in the last 14 days.

**G2 — Analyst activity sweep:**
Search: `[all work-list tickers comma-separated] analyst upgrade downgrade price target raised lowered 2026`
Extract any rating changes or PT moves per ticker.

### Per-ticker searches (2 per ticker, run as parallel Agent calls)

For each ticker in the work list, spawn a Haiku agent with this prompt:

> You are a financial research assistant. For the ticker **[TICKER]** ([company name], [sector]):
>
> Run these two searches and return a structured JSON result:
>
> **Search 1 — Recent news & filings (last 30 days):**
> `[TICKER] SEC filing 8-K 10-Q earnings results news 2026`
>
> **Search 2 — SEC EDGAR recent filings:**
> Fetch: `https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=[TICKER]&type=&dateb=&owner=include&count=5`
> Extract the 5 most recent filings (type, date, description).
>
> Return JSON only:
> ```json
> {
>   "ticker": "...",
>   "new_filings": [{"type": "8-K", "date": "YYYY-MM-DD", "description": "..."}],
>   "earnings_result": {"quarter": "Q1 2026", "revenue": "$XM", "beat_miss": "Beat", "eps": "$X.XX", "guidance": "...", "notes": "..."},
>   "material_news": [
>     {
>       "date": "YYYY-MM-DD",
>       "headline": "...",
>       "category": "EARNINGS|FILING|PARTNERSHIP|PRODUCT|REGULATORY|ANALYST|MACRO",
>       "why_it_matters": "One sentence explaining the mechanism — why this moves the thesis",
>       "conviction_delta": "up|down|neutral",
>       "conviction_why": "1-2 sentences explaining why conviction changed or held",
>       "cross_ticker_signals": [
>         {"direction": "emits|receives", "other_ticker": "NVDA", "signal": "≤10 words", "implication": "1 sentence"}
>       ]
>     }
>   ],
>   "nothing_new": true/false
> }
> ```
> If no material news or new filings in the last 30 days, set `nothing_new: true` and return minimal JSON.
> For `cross_ticker_signals`, only include entries where the mechanism is direct and clear — not speculative.

Collect all agent results before proceeding to Phase 3.

---

## Phase 3 — Write appends

For each ticker in the work list, process its agent result. Skip if `nothing_new: true`. If `--dry-run`, print the planned appends instead of writing.

### Earnings & Financials
If `earnings_result` is present and the quarter is not already in the table, prepend a new row:
`| [quarter] | [revenue] | [beat_miss] | [eps] | [guidance] | [notes] |`

### SEC Filings
For each entry in `new_filings` not already in the table, add a row:
`| [type] | [date] | [[TICKER_TYPE_DATE]] |`

### News & Alpha Log
For each item in `material_news` where `category` is not `MACRO` or `ANALYST` (those go elsewhere), append:
```
- **[date]** — [headline, max 25 words]
  **Why it matters:** [1 sentence explaining the mechanism — why this event moves the thesis, not just what happened]
```

Skip items that are routine price action, index inclusion noise, or already noted in the log.

### Analyst Coverage
For any analyst activity found in global search G2 for this ticker, append:
`- **[date]** — [Firm] [action] [ticker] to [rating], PT $[X] ([reason ≤ 10 words])`

### Conviction Log
For each item in `material_news` that is material enough to affect conviction (EARNINGS, PARTNERSHIP, REGULATORY events — not routine ANALYST or MACRO), append one row to the Conviction Log table:
`| [date] | [event, max 15 words] | [↑ / ↓ / →] | [1-2 sentences: why this event strengthens, weakens, or holds the thesis] |`

**Conviction delta rules:**
- ↑ Strengthened: earnings beat + guidance raise, strategic contract win, sole-source confirmation, insider buy at scale
- ↓ Weakened: earnings miss + guidance cut, new competitor entrant with a credible product, customer concentration loss, key exec departure
- → Neutral: in-line results, routine filing, macro cross-current with no direct thesis impact

### Thesis Drift Block
If the event materially changes the thesis direction (e.g., a third consecutive gross margin expansion, a new strategic anchor customer, or a thesis-breaking data point), update the `Drift status` line in the Investment Thesis block:
`> **Drift status:** [On track / Drifting / Broken] — [updated one-line reason]`
`> **Last validated:** [TODAY'S DATE]`

Only update Drift status if the change is meaningful. Do not update it just because the monitor ran.

### Cross-Ticker Signals
For any event that has clear read-through implications for other monitored tickers, append a row to the Cross-Ticker Signals table of **both** the source ticker and the impacted ticker(s):

Source ticker row (Emits):
`| [date] | Emits | [OTHER_TICKER] | [signal in ≤ 10 words] | [implication for other ticker in 1 sentence] |`

Impacted ticker row (Receives):
`| [date] | Receives | [SOURCE_TICKER] | [signal in ≤ 10 words] | [implication for this ticker in 1 sentence] |`

Only log cross-ticker signals when the mechanism is clear and direct (e.g., NVDA capex raise → photonics demand, COHR capacity guidance → supply environment for LITE). Skip speculative read-throughs.

### Catalyst Timeline
- Check each `- [ ]` item. If the event date has passed (compare to today's date), change to `- [x]`.
- If G1 found an upcoming earnings date not already listed, add:
  `- [ ] Earnings — [Quarter] expected [date]`

### Research Log
Append one summary line per ticker (even if `nothing_new: true`, to track the monitor run):
`- **[TODAY'S DATE]** — 📊 MONITOR | [1-sentence summary, or "No material updates found"]`

---

## Phase 4 — Summary

After all writes complete, print a summary table:

```
| Ticker | Earnings | Filings | News | Analyst | Catalyst | Status |
```

Where Status is one of: `Updated`, `No new data`, `Skipped (recent)`, `Error`.

---

## Rules

- **Append only.** Never modify or delete existing table rows or log entries.
- **No duplicates.** Before appending any row or entry, check whether it already exists (by date and ticker).
- **Material news only.** Do not append routine price moves, earnings whispers, or articles that merely recap old news.
- **Compact.** News & Alpha Log entries max 25 words. Analyst entries max 15 words. Keep Research Log summary to one sentence.
- **Fail gracefully.** If a search or fetch fails for a ticker, log the error in Research Log and continue to the next ticker. Do not halt the entire pass.
- **Foreign-listed tickers** (SIVE, POET): EDGAR fetch will fail — skip EDGAR step, rely on Search 1 only and note the source.
