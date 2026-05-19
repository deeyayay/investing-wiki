# /score-ticker

Score a ticker using the Unrivaled Investing 6-criterion rubric. Writes a Scoring Summary section into the ticker's wiki page and updates Monitor Registry and Watchlist.

## Usage

```
/score-ticker TICKER [--refresh]
```

- `TICKER` — required. The ticker symbol to score (e.g. `SOFI`, `ASTS`).
- `--refresh` — re-score even if a Scoring Summary already exists and the last-scored date is recent.

## Workflow

### Step 1 — Load reference context
Read these three files before scoring:
1. `Investing/Wiki/Reference/Scoring Rubric.md` — criteria definitions, scoring thresholds, pre-revenue rules
2. `Investing/Wiki/Reference/Monitor Registry.md` — locate the ticker's wiki page path
3. The sector's `_Sector Framework.md` — macro context and valuation matrix for this archetype

### Step 2 — Read the ticker page
Read the full ticker wiki page at the path from Monitor Registry. Identify which sections are populated:
- Investment Thesis → used for Product, Pricing Power, Future Potential
- Management & Leadership → used for Leadership & Alignment
- Earnings & Financials → used for Financial Health, Pricing Power (margin trend)
- Conviction Log → used for Leadership & Alignment (guidance beat/miss history)
- Analyst Coverage → used for Valuation snapshot
- Sector Framework (already loaded) → used for Macro Environment

### Step 3 — Determine pre-revenue status
Check whether the Earnings & Financials table has any revenue rows with actual dollar amounts. If the table is empty or all rows show `—`, treat this as a pre-revenue company:
- Cap Financial Health criterion at 3/5
- Score Financial Health based on cash runway evidence from Research Log or Investment Thesis
- Apply composite cap of 7.0/10
- Set Valuation to `— (pre-revenue; no P/E applicable)`

### Step 4 — Score each of the 6 criteria
For each criterion (1–5), select the score that best matches the evidence in the wiki page. Cite the specific section or quote that supports the score. When evidence is absent for a criterion, score conservatively (default to 2).

| Criterion | Primary wiki source |
|-----------|-------------------|
| Product (Love Factor) | Investment Thesis → Key moat; One-Line Thesis |
| Pricing Power | Earnings & Financials (gross margin trend); Investment Thesis |
| Leadership & Alignment | Management & Leadership; Conviction Log |
| Financial Health | Earnings & Financials (balance sheet); Research Log |
| Macro Environment | Sector Framework (Why this sector exists, Cycle positioning) |
| Future Potential | Investment Thesis (bull case); Catalyst Timeline |

### Step 5 — Calculate composite
`composite = round((sum / 30) × 10, nearest 0.5)`

Apply pre-revenue cap if triggered: `composite = min(composite, 7.0)`

Assign label: 8.0–10.0 = Unrivaled | 6.0–7.9 = Strong | 4.0–5.9 = Average | <4.0 = Reassess

### Step 6 — Assess valuation snapshot
Using the Analyst Coverage section and the sector framework's valuation reference matrix:
- Find the current price (from most recent Research Log entry or Analyst Coverage)
- Find the archetype's Fair Value Range in the sector framework
- Determine if current valuation is Cheap / Reasonable / Fair / Expensive relative to that range
- Note the relevant metric (P/E, EV/Revenue, EV/EBITDA) and analyst consensus upside if available

Format: `Valuation: [label] at $[price] | [Metric]: [X]x | Analyst upside: [X]%`

### Step 7 — Write Scoring Summary to ticker page
Locate the `## One-Line Thesis` section header in the ticker page. Insert the Scoring Summary block immediately after the One-Line Thesis content and before the `## Investment Thesis` header.

If a Scoring Summary section already exists, replace it entirely (this is the one section that is not append-only).

```markdown
## Scoring Summary
_Last scored: YYYY-MM-DD | [[Scoring Rubric]]_

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Product (Love Factor) | X/5 | [one-line evidence cite] |
| Pricing Power | X/5 | [one-line evidence cite] |
| Leadership & Alignment | X/5 | [one-line evidence cite] |
| Financial Health | X/5 | [one-line evidence cite] |
| Macro Environment | X/5 | [one-line evidence cite] |
| Future Potential | X/5 | [one-line evidence cite] |
| **Composite** | **X.X/10** | **[Label]** |

**Valuation:** [label] at $[price] | [Metric]: [X]x | Analyst upside: [X]%
**Growth Potential:** — (pending real-time data integration)
```

### Step 8 — Update Monitor Registry
Read `Investing/Wiki/Reference/Monitor Registry.md`. Find the row for this ticker. Update the Score column to `X.X` (the composite). If the Score column doesn't exist yet in a given sector table, append it.

### Step 9 — Update Watchlist
Read `Investing/Wiki/Reference/Watchlist.md`. Search all tables for this ticker. If found, update the Score column in that row. If the Score column doesn't exist in a table where this ticker appears, append it.

### Step 10 — Append Research Log
Append one line to the Research Log section of the ticker page:

```
- **YYYY-MM-DD** — Scored — Composite X.X/10 [Label] | P:[X] PP:[X] L:[X] FH:[X] ME:[X] FP:[X]
```

## Behavior Notes

- This is the **only** section of a ticker page that is not append-only. The Scoring Summary replaces itself on re-score.
- The Research Log entry IS append-only — every scoring run adds a new dated line.
- If the ticker is not in Monitor Registry, output a warning and stop. Run `/add-ticker TICKER` first.
- If the wiki page has fewer than 3 populated sections (Investment Thesis, Management, Earnings), note in the Research Log that the score is low-confidence and should be refreshed after `/stock-research TICKER`.
- Never fabricate evidence. If a criterion cannot be scored from existing wiki content, score it 2 (conservative default) and note "Insufficient data" in the Evidence column.
