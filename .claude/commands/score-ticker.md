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

### Step 2A — Generate the AI Adoption Profile

Using content already loaded from facts.md and analysis.md, evaluate the 5 layers using these sources:

| Layer | Source fields | Question | Rating values |
|-------|--------------|----------|---------------|
| Data Moat Depth | `moat.type`, `moat.notes`, Investment Thesis (key moat) | Proprietary irreplaceable data/network effects a funded startup can't close in 3yr? | strong / moderate / weak / none |
| Cost Structure Leverage | `earnings` gross margin %, Investment Thesis, sector framework | Labor-heavy COGS = margin expansion candidate; asset-light/human-judgment = most vulnerable | high / medium / low / negative |
| Distribution vs. Capability | `moat.type`, Investment Thesis (key moat), Conviction Log | Primary lock-in via product IP or customer relationship/GTM? | product / distribution / both / neither |
| Regulatory Insulation | Investment Thesis (key risks), sector framework, `moat.notes` | How many years does regulatory approval insulate the incumbent? Existing approvals = moat? | strong (3+yr) / moderate (1–3yr) / weak (<1yr) / none + integer years |
| Offense vs. Defense | Catalyst Timeline, Investment Thesis (bull case), Cross-Ticker Signals | Attacking new AI-enabled markets (deployer) or defending existing margins (target)? | deployer / target / both / neutral |

**Assign 2×2 quadrant:**
- Deployer + strong/moderate data moat → `re-rating winner`
- Deployer + weak/none data moat → `commodity improver`
- Target + strong/moderate data moat → `transition play`
- Target + weak/none data moat → `value trap`
- `both`/`neutral` posture: use data moat as tiebreaker; note ambiguity in rationale

**Write `## AI Adoption Profile`** to analysis.md using the template format (5-layer table + quadrant rationale + scoring implication line). If the section does not exist, insert it before `## Ecosystem Links`. If it exists, replace it entirely (replace-on-update).

**Note:** The `ai_profile:` YAML write is batched with the Step 8 `metrics:` edit — do not write it separately here.

If fewer than 3 sections are populated, set `ai_quadrant: "—"` and note "Insufficient data — AI profile pending" in the section. Score Macro Environment and Future Potential on existing evidence only.

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
| Macro Environment | Sector Framework (why this sector exists, cycle positioning) + `ai_profile.ai_quadrant` — see AI adoption guidance in Scoring Rubric.md |
| Future Potential | Investment Thesis (bull case) in analysis.md; Catalyst Timeline + `ai_profile.ai_quadrant` — see AI adoption guidance in Scoring Rubric.md |

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
```

### Step 8 — Update facts.md metrics and AI profile

In a **single Edit call**, update both blocks in facts.md YAML frontmatter:

```yaml
ai_profile:
  data_moat: "[value from Step 2A]"
  data_moat_notes: "[≤15 words]"
  cost_leverage: "[value]"
  cost_leverage_notes: "[≤15 words]"
  moat_source: "[value]"
  moat_source_notes: "[≤15 words]"
  regulatory_moat: "[value]"
  regulatory_moat_years: [integer or null]
  ai_posture: "[value]"
  ai_posture_notes: "[≤15 words]"
  ai_quadrant: "[quadrant]"
  ai_quadrant_rationale: "[≤20 words]"
  last_assessed: "YYYY-MM-DD"

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
- **YYYY-MM-DD** — Scored — Composite X.X/10 [Label] | P:[X] PP:[X] L:[X] FH:[X] ME:[X] FP:[X] | AI: [quadrant]
```

## Behavior Notes

- **analysis.md Scoring Summary is the only replace-not-append section.** Everything else is append-only.
- **facts.md metrics block is updated in-place.** Edit the YAML block between `---` markers.
- **signals.md Research Log entry IS append-only** — every scoring run adds a new dated line.
- **If fewer than 3 sections are populated** (Investment Thesis, Management, Earnings), note in signals.md Research Log that the score is low-confidence and should be refreshed after `/add-ticker [TICKER] --refresh-research`.
- **Never fabricate evidence.** If a criterion cannot be scored from existing wiki content, score it 2 (conservative default) and note "Insufficient data" in the Evidence column.
