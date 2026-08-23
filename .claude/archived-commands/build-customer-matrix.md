---
description: Build a supplier × end-customer dependency matrix for a sector. Reads facts.md (Layer 1) for company identity and analysis.md (Layer 2) for cross-ticker signals and thesis. Writes _Customer Matrix.md with a JSON block the dashboard uses to render a heat map. Usage: /build-customer-matrix "Sector Name"
allowed-tools: WebSearch, Read, Write, Edit, Bash
---

# Build Customer Matrix — Supplier × End-Customer Dependency

Maps which companies in a sector sell to which end-customers, and how concentrated those relationships are. Output is `_Customer Matrix.md` — a human-readable table plus a machine-readable JSON block.

**Output:** `Investing/Wiki/Sectors/[Sector]/_Customer Matrix.md`
**Input:** `$ARGUMENTS` — `"Sector Name"` (required)

Token-efficient: reads facts.md + analysis.md first, searches only for tickers with no customer data in either.

---

## Step 1 — Parse and load

Extract `SECTOR` from `$ARGUMENTS`.

Read these files in parallel:
- `Investing/Wiki/Reference/Monitor Registry.yaml` → get all tickers registered in this sector + their folder paths
- `Investing/Wiki/Sectors/[SECTOR]/_Supply Chain Map.md` → get each ticker's layer/tier (skip gracefully if not present)

If `_Customer Matrix.md` already exists, print:
```
⚠️  Customer Matrix already exists for [SECTOR].
    The file will be overwritten with refreshed data. Continuing...
```

If fewer than 3 tickers are registered in this sector, print:
```
⚠️  Only [N] tickers registered in [SECTOR]. Matrix will be sparse.
    Consider /add-ticker for more nodes first. Continuing anyway...
```

---

## Step 2 — Extract customer data from ticker files (parallel reads)

For each ticker in this sector, read `[path]/facts.md` and `[path]/analysis.md` in parallel.

**From facts.md (YAML):**
- `moat.notes` — check for customer concentration language
- `earnings[].notes` — scan for customer % mentions
- `management` + `moat` — customer dependency signals

**From analysis.md (markdown):**
- **Cross-Ticker Signals table** — all rows where `Direction = Emits` and the signal suggests a customer relationship (demand signal, design win, revenue dependency, capex read-through). Capture: `other_ticker`, `signal`, `implication`
- **Investment Thesis** — scan for named customers and dependency language
- **Analyst Coverage** — scan for customer concentration % if disclosed

Build per-ticker: `customer_signals[TICKER] = [{ customer_name, source, detail, concentration_hint }]`

A `concentration_hint` is any % or relative language: "50% of revenue", "largest customer", "top 3 customers", "meaningful exposure".

Do NOT read signals.md (news log is too noisy for customer matrix; structured data from facts.md and analysis.md is sufficient).

---

## Step 3 — Identify end-customer universe

From all customer signals in Step 2, compile a deduplicated list of end-customers. Normalize names:
- "Google", "Alphabet", "Google Cloud" → `Google (GOOGL)`
- "Amazon", "AWS" → `Amazon (AMZN)`
- "Microsoft", "Azure" → `Microsoft (MSFT)`
- "Meta", "Facebook" → `Meta (META)`
- "Apple" → `Apple (AAPL)`

For well-known sectors, supplement from knowledge:
- **Semiconductors / Photonics:** include hyperscalers (GOOGL, AMZN, MSFT, META) + TSMC (intermediary) + Apple (AAPL)
- **AI Infrastructure:** hyperscalers + cloud providers
- **Clean Energy:** utilities, grid operators, auto OEMs

Limit to 8 most relevant end-customers as columns.

---

## Step 4 — Fill gaps with targeted searches

For any ticker where Steps 2–3 returned zero customer signals, run one search:
`[TICKER] major customers revenue concentration 10-Q 2025 2026`

Extract named customers and % figures. Mark as `source: "web"`.

Maximum 5 total searches regardless of sector size.

---

## Step 5 — Score each cell

| Evidence | Score | Display |
|---|---|---|
| Named in 10-Q as top customer + % ≥50% | 5 | `>50%` |
| Named in 10-Q as top customer, % 25–49% | 4 | `~25–49%` |
| Named in earnings call / analyst report, meaningful | 3 | `★★★` |
| Mentioned in thesis/signals, indirect exposure | 2 | `★★` |
| Inferred from supply chain position (no direct evidence) | 1 | `★` |
| No evidence | 0 | blank |

Flag each cell's source: `wiki` (from facts.md / analysis.md) or `web` (from search).

---

## Step 6 — Write `_Customer Matrix.md`

Write the file at `Investing/Wiki/Sectors/[SECTOR]/_Customer Matrix.md`:

```markdown
# [SECTOR] — Customer Matrix
*Built: [TODAY'S DATE] | Refresh: after each /ticker-monitor pass or earnings event*
*Rows = suppliers in this sector. Columns = major end-customers.*
*Score: >50% revenue | ~25–49% | ★★★ meaningful | ★★ partial/indirect | ★ inferred | blank = no evidence*

---

## Dependency Table

| Supplier | Layer | [Customer 1] | [Customer 2] | ... | Concentration Notes |
|----------|-------|-------------|-------------|-----|---------------------|
[one row per ticker, sorted by layer then ticker]

---

## Critical Paths

[2–4 sentences identifying the most concentrated dependencies]

---

## Coverage Gaps

| Ticker | Issue |
|--------|-------|
[Any ticker where no customer data was found]

---

## Data Sources

| Ticker | Primary Source | Last Updated |
|--------|---------------|-------------|
[wiki or web, with date]

---

## Heat Map Metadata
<!-- Machine-readable block — parsed by /daily-dashboard. Do not edit manually. -->

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
        "Customer 1": { "score": 4, "display": "~25–49%", "source": "wiki", "note": "..." },
        ...
      }
    }
  ]
}
```

---

## Research Log
- **[TODAY'S DATE]** — build-customer-matrix run. [N] suppliers × [N] customers. [N] cells from wiki, [N] from web, [N] blank.
```

---

## Step 7 — Update `_Supply Chain Map.md` framework status

If `_Supply Chain Map.md` exists for this sector, check off the customer matrix step:
`- [ ] Customer matrix built` → `- [x] Customer matrix built — [TODAY'S DATE]`

---

## Step 8 — Print summary

```
✅ Customer Matrix — [SECTOR]

   📄 Investing/Wiki/Sectors/[SECTOR]/_Customer Matrix.md
   📊 [N] suppliers × [N] customers = [N] cells
   🔴 High concentration (★★★★+): [N] cells
   🟡 Meaningful (★★★): [N] cells
   ⬜ No evidence: [N] cells
   ⚠️  Coverage gaps: [N] tickers

   Next: /daily-dashboard to render the heat map
         /ticker-monitor --sector "[SECTOR]" to keep signals fresh
```

---

## Rules

- **Wiki-first (facts.md + analysis.md).** Never search for a ticker that already has customer data in either file. Search is the fallback.
- **Cap searches at 5.** If more than 5 tickers have no wiki data, fill them as coverage gaps.
- **No invented relationships.** Score 0 (blank) is correct when there's no evidence. Use score 1 (★, inferred) sparingly with a clear note.
- **Never read signals.md.** The news log is too noisy for customer dependency analysis.
- **JSON block must be valid JSON.** The dashboard parser will fail on malformed JSON.
- **8-column maximum.** Keep the 8 end-customers with the highest total score across all suppliers.
