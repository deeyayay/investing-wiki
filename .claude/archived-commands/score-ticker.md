---
description: Score a ticker on the Unrivaled Investing 6-criterion rubric. Reads facts.md (Layer 1) and analysis.md (Layer 2) only. Writes Scoring Summary to analysis.md and updates Monitor Registry.yaml score field. Usage: /score-ticker TICKER [--refresh]
allowed-tools: Read, Edit, Glob
---

# /score-ticker

Score a ticker using the Unrivaled Investing 6-criterion rubric. Writes a Scoring Summary section into the ticker's analysis.md and updates Monitor Registry.yaml.

## Usage

```
/score-ticker TICKER [--refresh]
```

- `TICKER` — required. The ticker symbol to score (e.g. `SOFI`, `ASTS`).
- `--refresh` — re-score even if a Scoring Summary already exists and the last-scored date is recent.

## Workflow

### Step 1 — Load reference context

Read these files before scoring:
1. `Investing/Wiki/Reference/Scoring Rubric.md` — criteria definitions, scoring thresholds, pre-revenue rules
2. `Investing/Wiki/Reference/Monitor Registry.yaml` — locate the ticker's folder path
3. The sector's `_Sector Framework.md` at `Investing/Wiki/Sectors/[sector]/_Sector Framework.md` — macro context and valuation matrix

If the ticker is not found in `Monitor Registry.yaml`, print:
```
⚠️  [TICKER] not in Monitor Registry.yaml. Run /add-ticker [TICKER] first.
```
Then stop.

### Step 2 — Read Layer 1 and Layer 2

Read **only** these two files (do not read signals.md):

**`[path]/facts.md`** — extract from YAML frontmatter:
- `management` array → Leadership & Alignment criterion
- `earnings` array → Financial Health, Pricing Power (margin trend)
- `moat` object → Product (Love Factor), Pricing Power
- `metrics` object → current score (if exists), valuation fields
- `cik` → pre-revenue detection (cross-ref with earnings array)

**`[path]/analysis.md`** — extract from markdown sections:
- `## One-Line Thesis` → Product (Love Factor)
- `## Investment Thesis` → Product, Pricing Power, Future Potential (bull case)
- `## Conviction Log` table → Leadership & Alignment (guidance beat/miss history)
- `## Analyst Coverage` → Valuation snapshot (current price, PT)
- `## Catalyst Timeline` → Future Potential

### Step 3 — Determine pre-revenue status

Check whether `earnings:` array in facts.md has any entries with `revenue_b > 0`. If the array is empty or all entries have null revenue, treat this as a pre-revenue company:
- Cap Financial Health criterion at 3/5
- Score Financial Health based on cash runway evidence from Investment Thesis
- Apply composite cap of 7.0/10
- Set Valuation to `— (pre-revenue; no P/E applicable)`

### Step 4 — Score each of the 6 criteria

For each criterion (1–5), select the score that best matches the evidence. Cite the specific field or section that supports the score. When evidence is absent, score conservatively (default 2).

| Criterion | Primary source |
|-----------|---------------|
| Product (Love Factor) | `moat.type` + `moat.notes` in facts.md; One-Line Thesis in analysis.md |
| Pricing Power | `moat.pricing_power` in facts.md; gross margin trend in earnings array; Investment Thesis |
| Leadership & Alignment | `management` array (ownership %, notes) in facts.md; Conviction Log in analysis.md |
| Financial Health | `earnings` array (revenue trend, EPS) in facts.md; Investment Thesis (balance sheet) |
| Macro Environment | Sector Framework (why this sector exists, cycle positioning) |
| Future Potential | Investment Thesis (bull case) in analysis.md; Catalyst Timeline |

### Step 4.5 — Evaluate Risk Flags

Assess 5 structural risk flags. These are **not part of the composite** — they are output alongside the Scoring Summary as a separate block. Read `demand_chain:` from facts.md and customer concentration evidence from Investment Thesis / Cross-Ticker Signals in analysis.md.

Assign each flag: **CLEAR** / **WATCH** / **FLAG**. If evidence is absent, default to WATCH and note "Insufficient data."

| Flag | CLEAR | WATCH | FLAG |
|------|-------|-------|------|
| **Capex sustainability** | FCF covers capex; debt/EBITDA <1x | Debt-funded capex, manageable coverage (1–2x) | Capex debt-funded with weak FCF coverage or near-term maturity risk |
| **Demand chain health** | Primary customers FCF-funded (hyperscalers, strong enterprise) | Mix of FCF and debt-funded neocloud customers | Primary customer pre-IPO, heavily levered, or circular-valuation ecosystem |
| **Customer concentration** | Top 3 <40%; no single customer >20% | Top 3 = 40–60% or single customer 20–40% | Single customer >40% or single ecosystem >60% |
| **Circular revenue exposure** | No circular backlog; demand traceable to real end-user cash | Minor circular-chain backlog (<20%) | Substantial circular-chain backlog; demand signal may be self-referential |
| **Rate sensitivity** | Minimal variable-rate debt; Fed tightening immaterial | Moderate variable exposure; manageable under +100bps | Heavy variable-rate debt; tightening materially impairs FCF or customer solvency |

### Step 5 — Calculate composite

`composite = round((sum of 6 scores / 30) × 10, nearest 0.5)`

Apply pre-revenue cap: `composite = min(composite, 7.0)`

Assign label: 8.0–10.0 = Unrivaled | 6.0–7.9 = Strong | 4.0–5.9 = Average | <4.0 = Reassess

### Step 6 — Assess valuation snapshot

Using Analyst Coverage in analysis.md and the sector framework's valuation reference matrix:
- Find the current price and analyst consensus price target
- Determine if current valuation is Cheap / Reasonable / Fair / Expensive relative to archetype range
- Note the relevant metric (P/E, EV/Revenue, EV/EBITDA) and analyst upside

Format: `Valuation: [label] at $[price] | [Metric]: [X]x | Analyst upside: [X]%`

### Step 7 — Write Scoring Summary to analysis.md

Locate `## Scoring Summary` in analysis.md. Replace it entirely (this is the one section that is not append-only):

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

## Risk Flags
_Evaluated: YYYY-MM-DD_

| Flag | Status | Notes |
|------|--------|-------|
| Capex sustainability | CLEAR / WATCH / FLAG | [one-line evidence] |
| Demand chain health | CLEAR / WATCH / FLAG | [primary customers + funding type] |
| Customer concentration | CLEAR / WATCH / FLAG | [top customer % or "Insufficient data"] |
| Circular revenue exposure | CLEAR / WATCH / FLAG | [none / describe / "Insufficient data"] |
| Rate sensitivity | CLEAR / WATCH / FLAG | [debt terms / variable rate exposure] |
```

### Step 8 — Update facts.md metrics

Edit the `metrics:` block in facts.md YAML frontmatter:
```yaml
metrics:
  score: X.X
  score_label: "[Label]"
  last_scored: "YYYY-MM-DD"
  valuation_fpe: [X or null]
  analyst_pt: [X or null]
  analyst_upside_pct: [X or null]
```

### Step 9 — Update Monitor Registry.yaml

Read `Investing/Wiki/Reference/Monitor Registry.yaml`. Find the entry for this ticker under `tickers:`. Update the `score` field to `X.X`.

### Step 10 — Update Watchlist

Read `Investing/Wiki/Reference/Watchlist.md`. Search all tables for this ticker. If found, update the Score column in that row.

### Step 11 — Append to signals.md Research Log

Append one line to the Research Log section of signals.md:

```
- **YYYY-MM-DD** — Scored — Composite X.X/10 [Label] | P:[X] PP:[X] L:[X] FH:[X] ME:[X] FP:[X]
```

## Behavior Notes

- **analysis.md Scoring Summary is the only replace-not-append section.** Everything else is append-only.
- **facts.md metrics block is updated in-place.** Edit the YAML block between `---` markers.
- **signals.md Research Log entry IS append-only** — every scoring run adds a new dated line.
- **If fewer than 3 sections are populated** (Investment Thesis, Management, Earnings), note in signals.md Research Log that the score is low-confidence and should be refreshed after `/add-ticker [TICKER] --refresh-research`.
- **Never fabricate evidence.** If a criterion cannot be scored from existing wiki content, score it 2 (conservative default) and note "Insufficient data" in the Evidence column.
