---
description: Build a supplier × end-customer dependency matrix for a sector. Reads wiki pages and Cross-Ticker Signals to map revenue concentration, then writes _Customer Matrix.md with a JSON block the dashboard uses to render a heat map. Usage: /build-customer-matrix "Sector Name"
allowed-tools: WebSearch, Read, Write, Edit, Bash
---

# Build Customer Matrix — Supplier × End-Customer Dependency

Maps which companies in a sector sell to which end-customers, and how concentrated those relationships are. Output is `_Customer Matrix.md` — a human-readable table plus a machine-readable JSON block the dashboard renders as a heat map.

**Output:** `Investing/Wiki/Sectors/[Sector]/_Customer Matrix.md`
**Input:** `$ARGUMENTS` — `"Sector Name"` (required)

Token-efficient: reads wiki pages first, searches only for tickers with no customer data logged.

---

## Step 1 — Parse and load

Extract `SECTOR` from `$ARGUMENTS`.

Read these files in parallel:
- `Investing/Wiki/Reference/Monitor Registry.md` → get all tickers registered in this sector + their wiki page paths
- `Investing/Wiki/Sectors/[SECTOR]/_Supply Chain Map.md` → get each ticker's layer/tier (if map exists; skip gracefully if not)

If `_Customer Matrix.md` already exists at `Investing/Wiki/Sectors/[SECTOR]/_Customer Matrix.md`, print:
```
⚠️  Customer Matrix already exists for [SECTOR].
    The file will be overwritten with refreshed data. Continuing...
```

If fewer than 3 tickers are registered in this sector, print:
```
⚠️  Only [N] tickers registered in [SECTOR]. Matrix will be sparse.
    Consider running /add-ticker for more nodes before building the matrix.
    Continuing anyway...
```

---

## Step 2 — Extract customer data from wiki pages (parallel reads)

Read all ticker wiki pages for this sector in parallel.

For each ticker, extract:
- **Cross-Ticker Signals table** — all rows where `Direction = emits` and the signal type suggests a customer relationship (demand signal, design win, revenue dependency, capex read-through). Capture: `other_ticker`, `signal`, `implication`.
- **News & Alpha Log** — scan for customer names, revenue concentration mentions, "top customer", "largest customer", "design win at", "supply agreement with". Capture any named customers and context.
- **Earnings & Financials table** — note if any customer concentration % is mentioned in the Notes column.
- **Investment Thesis** — scan for named customers and dependency language.

Build per-ticker: `customer_signals[TICKER] = [{ customer_name, source, detail, concentration_hint }]`

A `concentration_hint` is any % or relative language found: "50% of revenue", "largest customer", "top 3 customers", "meaningful exposure", etc.

---

## Step 3 — Identify end-customer universe

From all customer signals collected in Step 2, compile a deduplicated list of end-customers. Normalize names:
- "Google", "Alphabet", "Google Cloud" → `Google (GOOGL)`
- "Amazon", "AWS", "Amazon Web Services" → `Amazon (AMZN)`
- "Microsoft", "Azure" → `Microsoft (MSFT)`
- "Meta", "Facebook" → `Meta (META)`
- "Apple" → `Apple (AAPL)`
- OEM/automotive/industrial customers: keep as-is

For well-known sectors, supplement from knowledge:
- **Semiconductors**: always include Google (GOOGL), Amazon (AMZN), Microsoft (MSFT), Meta (META), Apple (AAPL), TSMC (as intermediary), as column candidates — they appear in virtually every semicon supplier's customer base
- **Photonics & Optical**: always include hyperscalers + major telcos (AT&T, Verizon, Lumen)
- **AI Infrastructure**: hyperscalers + cloud providers
- **Clean Energy**: utilities, grid operators, auto OEMs

Limit to the 8 most relevant end-customers as columns. More than 8 makes the matrix unreadable.

---

## Step 4 — Fill gaps with targeted searches

For any ticker where Step 2 returned zero customer signals, run one search:
`[TICKER] major customers revenue concentration 10-Q 2025 2026`

Extract any named customers and % figures from results. Mark these as `source: "web"` (vs. `source: "wiki"` for data from ticker pages).

Maximum searches: one per ticker with no wiki data, capped at 5 total searches regardless of sector size.

---

## Step 5 — Score each cell

For each (supplier ticker, end-customer) pair, assign a relationship score:

| Evidence | Score | Display |
|---|---|---|
| Named in 10-Q as top customer + % disclosed ≥50% | 5 | `★★★★★` or `>50%` |
| Named in 10-Q as top customer, % not disclosed or 25–49% | 4 | `★★★★` or `~25–49%` |
| Named in earnings call / analyst report, meaningful exposure | 3 | `★★★` |
| Mentioned in news/thesis, indirect or partial exposure | 2 | `★★` |
| Inferred from supply chain position (no direct evidence) | 1 | `★` |
| No evidence | 0 | blank |

For the JSON heat map, use the numeric score (0–5). For the markdown table, use the display string.

Also flag each cell's source: `wiki` (from Cross-Ticker Signals / thesis / news) or `web` (from search).

---

## Step 6 — Write `_Customer Matrix.md`

Write the file at `Investing/Wiki/Sectors/[SECTOR]/_Customer Matrix.md`:

```markdown
# [SECTOR] — Customer Matrix
*Built: [TODAY'S DATE] | Refresh: after each /ticker-monitor pass or earnings event*
*Rows = suppliers registered in this sector. Columns = major end-customers.*
*Score: ★★★★★ >50% revenue | ★★★★ ~25–49% | ★★★ meaningful | ★★ partial/indirect | ★ inferred | blank = no evidence*

---

## Dependency Table

| Supplier | Layer | [Customer 1] | [Customer 2] | [Customer 3] | ... | Concentration Notes |
|----------|-------|-------------|-------------|-------------|-----|---------------------|
[one row per registered ticker, sorted by layer then ticker]

---

## Critical Paths

[2–4 sentences identifying the most concentrated dependencies — e.g., "ASML → TSMC is the single most critical bilateral relationship in the chain: TSMC is ASML's largest customer by revenue and ASML is TSMC's sole EUV supplier. Disruption to either direction halts leading-edge chip production globally."]

---

## Coverage Gaps

| Ticker | Issue |
|--------|-------|
[Any ticker where no customer data was found in wiki or web search]

---

## Data Sources

| Ticker | Primary Source | Last Updated |
|--------|---------------|-------------|
[wiki or web, with date]

---

## Heat Map Metadata
<!-- Machine-readable block — parsed by /daily-dashboard to render the visual heat map. Do not edit manually. -->

```json
{
  "sector": "[SECTOR]",
  "built": "[TODAY'S DATE]",
  "customers": ["Customer 1", "Customer 2", ...],
  "rows": [
    {
      "ticker": "NVDA",
      "company": "NVIDIA Corporation",
      "layer": "Design (Fabless — Compute)",
      "cells": {
        "Customer 1": { "score": 4, "display": "★★★★", "source": "wiki", "note": "Hyperscaler GPU demand — H100/H200 allocation" },
        "Customer 2": { "score": 3, "display": "★★★", "source": "wiki", "note": "Azure AI infrastructure build-out" },
        ...
      }
    },
    ...
  ]
}
` `` (close json block)

---

## Research Log
- **[TODAY'S DATE]** — build-customer-matrix run. [N] suppliers × [N] customers. [N] cells scored from wiki data, [N] from web search, [N] inferred, [N] blank. [N] coverage gaps.
```

---

## Step 7 — Update `_Supply Chain Map.md` framework status

If `_Supply Chain Map.md` exists for this sector, find the Framework Status checklist and check off the customer matrix step:

```
- [ ] Customer matrix built (`/build-customer-matrix "[SECTOR]"`)
```
→
```
- [x] Customer matrix built (`/build-customer-matrix "[SECTOR]"`) — [TODAY'S DATE]
```

---

## Step 8 — Print summary

```
✅ Customer Matrix — [SECTOR]

   📄 Investing/Wiki/Sectors/[SECTOR]/_Customer Matrix.md
   📊 [N] suppliers × [N] customers = [N] cells
   🔴 High concentration (★★★★+): [N] cells
   🟡 Meaningful exposure (★★★):   [N] cells
   ⬜ No evidence:                  [N] cells
   ⚠️  Coverage gaps:               [N] tickers (no customer data found)

   Most concentrated relationships:
   • [TICKER] → [Customer]: [display score] — [note]
   • [TICKER] → [Customer]: [display score] — [note]
   • [TICKER] → [Customer]: [display score] — [note]

   Next: /daily-dashboard to render the heat map visualization
         /ticker-monitor --sector "[SECTOR]" to keep Cross-Ticker Signals fresh
```

---

## Rules

- **Wiki-first.** Never search for a ticker that already has customer data in Cross-Ticker Signals or thesis. Search is the fallback, not the default.
- **Cap searches at 5.** If the sector has more than 5 tickers with no wiki data, fill them as coverage gaps rather than running unlimited searches.
- **No invented relationships.** Score 0 (blank) is correct when there's no evidence. Do not infer a relationship just because it's plausible from supply chain position — that's what score 1 (★, inferred) is for, and use it sparingly with a clear note.
- **Overwrite is safe.** Unlike ticker pages, the matrix is a derived artifact — it's always regenerated from source data. Overwriting is expected behavior.
- **JSON block must be valid JSON.** Close all braces. The dashboard parser will fail on malformed JSON.
- **8-column maximum.** If more than 8 distinct end-customers appear, keep the 8 with the highest total score across all suppliers. Note excluded customers in a comment above the JSON block.
