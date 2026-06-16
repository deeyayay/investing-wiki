# Scoring Rubric — Unrivaled Investing Framework

_Created: 2026-05-18 | Based on Unrivaled Investing 7-criterion framework_

---

## Overview

Each ticker is scored on 6 criteria (1–5 each, total /30) that roll up to a composite /10. Valuation is assessed separately as a point-in-time snapshot — it is not included in the composite because it changes daily and a great company shouldn't be penalized for being accurately priced.

**Composite formula:** `(sum of 6 criteria / 30) × 10`, rounded to nearest 0.5

**Pre-revenue cap:** Companies with no revenue history (OKLO, ASTS, LWLG, POET, etc.) are structurally capped at **7.0/10** composite due to N/A or modified Financial Health scoring.

---

## Score Buckets

| Composite | Label | Action |
|-----------|-------|--------|
| 8.0–10.0 | **Unrivaled** | Maximize position; Core Holdings candidate |
| 6.0–7.9 | **Strong** | Solid hold; size appropriately |
| 4.0–5.9 | **Average** | Monitor closely; thesis validation required before adding |
| <4.0 | **Reassess** | Reduce or exit; document what would need to change |

---

## Criteria Definitions

### 1. Product — The "Love Factor" (/5)

Does the product inspire genuine loyalty or lock-in? Is there a near-irreplaceable position in the market?

| Score | Criteria |
|-------|----------|
| **5** | Category-defining; no adequate substitute; switching is prohibitively costly (CUDA ecosystem, SOFI 75% 30-day cross-sell adoption) |
| **4** | Strong differentiation; alternatives exist but switching costs are high; clear customer preference |
| **3** | Competitive product in a crowded market; above average but not dominant |
| **2** | Undifferentiated or commoditized; limited evidence of customer preference or loyalty |
| **1** | Weak product position; easily replaced; no observable "love factor" |

_Sources in wiki: Investment Thesis (moat section), One-Line Thesis, News & Alpha Log_

---

### 2. Pricing Power (/5)

Can the company raise prices without losing customers? Are margins protected against inflation?

| Score | Criteria |
|-------|----------|
| **5** | Demonstrably raised prices in the last 2 years without volume loss; gross margins expanding |
| **4** | Pricing stable above inflation; margins holding or slightly improving; limited competitive pressure |
| **3** | Some pricing power in key sub-segments; mixed margin story |
| **2** | Price-taking behavior; margins under pressure; limited ability to pass cost increases |
| **1** | No pricing power; commodity-level dynamics; margin compression trend |

_Sources in wiki: Earnings & Financials (gross margin trend), Investment Thesis, Sector Framework valuation matrix_

---

### 3. Leadership & Alignment (/5)

Does management have a long-term vision and show the ability to delay gratification? Is executive incentive aligned with shareholders?

| Score | Criteria |
|-------|----------|
| **5** | Founder-led or founder-equivalent; >5% insider ownership; ≥3 consecutive guidance beats; zero or minimal insider selling |
| **4** | Strong track record; meaningful insider ownership (2–5%); consistent execution; 2 of 3 above criteria met |
| **3** | Competent management; moderate insider ownership; 1 guidance miss tolerable; tenure ≥3 years |
| **2** | Recent CEO change or limited track record; low insider ownership; guidance history mixed |
| **1** | Misalignment signals: insider selling pattern, poor guidance credibility, high executive turnover |

_Sources in wiki: Management & Leadership section, Conviction Log (guidance beats/misses), News & Alpha Log_

---

### 4. Financial Health (/5)

Does the company have a fortress balance sheet? Can it weather downturns and self-fund growth? This criterion also considers **demand chain health** — whether the capex flowing to this ticker originates from FCF (durable) or from debt/external raises (fragile). A company can have a clean balance sheet but be fully exposed to customers who cannot self-fund.

**Revenue-generating companies:**

| Score | Criteria |
|-------|----------|
| **5** | Net cash position; FCF positive and growing; debt/EBITDA <0.5x; self-funded R&D and capex; primary customers are FCF-funded (hyperscalers or enterprises with strong cash generation) |
| **4** | Net cash or low leverage (<1x EBITDA); positive operating cash flow; improving FCF trajectory; customer funding mix is predominantly FCF-backed with limited debt-funded neocloud exposure (<25% revenue) |
| **3** | Manageable debt (1–2x EBITDA); breakeven or slight FCF positive; no near-term maturity risk; meaningful revenue exposure to debt-funded neoclouds or pre-IPO ecosystem players (25–50%) |
| **2** | Elevated leverage (2–4x EBITDA); FCF negative; requires capital markets access; OR majority revenue from debt-funded or circular-valuation customers (>50%), or a primary customer is pre-IPO with unclear runway |
| **1** | High leverage (>4x EBITDA) or cash burn without clear path to sustainability; OR primary customer is heavily levered, pre-IPO, or part of a circular-valuation structure with limited buffer |

**Pre-revenue modifier (cap this criterion at 3/5):**

| Score | Criteria |
|-------|----------|
| **3** | >18 months cash runway; burn rate stable or declining; milestone progress on track |
| **2** | 12–18 months runway; next raise required within 1 year at likely dilutive terms |
| **1** | <12 months runway; raise imminent at unclear pricing; survival risk elevated |

_Sources in wiki: Earnings & Financials (balance sheet notes), Research Log, SEC Filings, `demand_chain:` block in facts.md, Cross-Ticker Signals in analysis.md_

---

### Risk Flags (separate from composite)

Risk Flags are evaluated by `/score-ticker` and appended below the Scoring Summary table. They are **not included in the composite** — the same model as the Valuation snapshot. Their purpose is to surface structural fragilities that a per-criterion score can miss because it evaluates the ticker in isolation.

**Five flags, each assigned CLEAR / WATCH / FLAG:**

| Flag | CLEAR | WATCH | FLAG |
|------|-------|-------|------|
| **Capex sustainability** | FCF covers capex; debt/EBITDA <1x | Debt-funded capex with manageable coverage (1–2x EBITDA) | Capex funded by debt with weak FCF coverage or near-term maturity risk |
| **Demand chain health** | Primary customers are FCF-funded hyperscalers or diversified enterprise | Mix of FCF and debt-funded neocloud customers | Primary customer is pre-IPO, heavily levered, or part of a circular-valuation ecosystem (e.g. neocloud dependent on OpenAI funding) |
| **Customer concentration** | Top 3 customers <40% revenue; no single customer >20% | Top 3 = 40–60% or single customer 20–40% | Single customer >40% or single ecosystem >60% |
| **Circular revenue exposure** | No circular backlog structures; demand signal traceable to real end-user cash | Minor backlog from circular chains (<20%); low systemic risk | Substantial backlog from circular chains; demand signal may be self-referential (e.g. neocloud → AI lab → GPU vendor → neocloud) |
| **Rate sensitivity** | Minimal variable-rate or floating debt; Fed tightening immaterial | Moderate variable-rate exposure; manageable under +100bps scenario | Heavy variable-rate debt; Fed tightening materially impairs FCF coverage or customer solvency |

**Assignment rules:**
- Read `demand_chain:` block in facts.md and customer concentration from Investment Thesis / Cross-Ticker Signals in analysis.md
- If evidence is absent for a flag, assign WATCH and note "Insufficient data"
- CLEAR on all 5 = structurally sound demand chain; FLAG on Demand Chain Health or Circular Revenue = treat as thesis risk requiring monitoring cadence

**Output format** (appended below Scoring Summary table in analysis.md):

```markdown
## Risk Flags
_Evaluated: YYYY-MM-DD_

| Flag | Status | Notes |
|------|--------|-------|
| Capex sustainability | CLEAR / WATCH / FLAG | [one-line evidence] |
| Demand chain health | CLEAR / WATCH / FLAG | [primary customers + funding type] |
| Customer concentration | CLEAR / WATCH / FLAG | [top customer %] |
| Circular revenue exposure | CLEAR / WATCH / FLAG | [none / describe] |
| Rate sensitivity | CLEAR / WATCH / FLAG | [debt terms / variable rate exposure] |
```

---

### 5. Macro Environment (/5)

What trends in the world will impact this business? Are the tailwinds secular and durable?

| Score | Criteria |
|-------|----------|
| **5** | Multiple converging secular tailwinds; 5+ year demand visibility; no meaningful structural headwinds |
| **4** | Clear secular tailwind; 1 manageable headwind; industry growing 10–20%+/year |
| **3** | Moderate tailwind; balanced headwinds; industry growing 5–10%/year |
| **2** | Sector in transition; headwinds are near-term material; tailwinds are 3+ years out |
| **1** | Secular decline, regulatory overhang, or structural disruption with no clear resolution |

**Technology preference alignment:** A ticker with *primary* exposure to a high-conviction preferred technology in [[Technology Preferences]] qualifies as a structural tailwind supporting a score of 4–5. Primary exposure to a disfavored or transitioning technology should score 2–3 on this criterion even if broader sector-level tailwinds exist. See the Technology Alignment section in `analysis.md` for the explicit per-ticker mapping.

_Sources in wiki: Sector Framework (Why this sector exists, Cycle positioning, Bull/Base/Bear cases), [[Technology Preferences]] (technology race outcomes and ticker exposure maps)_

---

### 6. Future Potential (/5)

How many ways can the company make money? Does it have multiple adjacent pathways to expand revenue?

| Score | Criteria |
|-------|----------|
| **5** | Multiple adjacent revenue pathways already showing traction; company positioned at 3+ layers of the value chain |
| **4** | 2–3 identified adjacencies; at least 1 showing measurable early revenue or signed LOIs |
| **3** | 1–2 adjacent opportunities; early exploration; TAM expansion thesis not yet validated |
| **2** | Core business is the primary and near-only path; limited adjacency identified |
| **1** | Single product, single market, no expansion pathway; TAM may be declining |

_Sources in wiki: Investment Thesis (bull case, moat), Catalyst Timeline, Cross-Ticker Signals_

---

### Valuation Snapshot (separate — not in composite)

Uses the sector framework's archetype valuation matrix and current analyst coverage.

**Format:** `Valuation: [Expensive / Fair / Reasonable / Cheap] at $[price] | [Metric]: [X]x | Analyst upside: [X]%`

| Label | Meaning |
|-------|---------|
| **Cheap** | Trading below the sector framework's trough fear range (asymmetric upside) |
| **Reasonable** | Within the fair value range for its archetype |
| **Fair** | At the upper end of the fair value range |
| **Expensive** | Above the "Peak Enthusiasm" threshold |

For pre-revenue names: `Valuation: — (pre-revenue; no P/E applicable)`

---

## Worked Examples

### SOFI — Expected composite ~9.0/10

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Product (Love Factor) | 5/5 | 75% 30-day cross-sell adoption; 9-product suite; sticky member flywheel with no adequate digital banking substitute |
| Pricing Power | 4/5 | NIM expanding post-bank-charter; deposit cost competitive; product pricing control via bank rails |
| Leadership & Alignment | 5/5 | CEO Noto: 11.9M shares, 39 buys/0 sells over 5 years; 9 consecutive GAAP-profitable quarters |
| Financial Health | 4/5 | Net cash positive; 9th consecutive GAAP profitable quarter; FCF improving; no leverage concerns |
| Macro Environment | 4/5 | Digital banking shift is structural; rate sensitivity is 1 manageable headwind |
| Future Potential | 5/5 | Galileo B2B, stablecoin, investing, credit card, insurance — multiple adjacencies in progress |
| **Composite** | **27/30 = 9.0/10** | **Unrivaled** |

Valuation: Fair at ~$14 | P/E ~18x | Analyst consensus upside ~35%

---

### ASTS — Expected composite ~7.0/10 (pre-revenue cap)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Product (Love Factor) | 4/5 | First-mover direct-to-cell; technically novel; not yet in-market at scale |
| Pricing Power | 2/5 | No in-market pricing data; MNO wholesale model logical but unproven |
| Leadership & Alignment | 4/5 | Abel Avellan: 71.6% voting control, prior $550M exit, zero cash compensation |
| Financial Health | 2/5 *(pre-rev)* | 12–18 month runway; constellation requires additional equity raises |
| Macro Environment | 5/5 | Mobile connectivity gap is a global structural problem; MNO contracts are incentive-aligned |
| Future Potential | 4/5 | MNO wholesale, direct enterprise, IoT, defense adjacencies identified |
| **Composite** | **21/30 = 7.0/10 → capped 7.0** | **Strong** (pre-revenue cap applied) |

Valuation: — (pre-revenue; no P/E applicable)

---

## Score Update Triggers

Re-score a ticker after any of these events:
- Quarterly earnings release
- New entry in Conviction Log (↑ or ↓ shift)
- CEO/CFO change
- Major product announcement or competitive development
- Thesis drift status changes from "On track" to "Drifting"
- Annual re-score for all tickers (year-end pass)

The Research Log entry format for a scoring run:
`Scored — Composite X.X/10 [Label] | P:[X] PP:[X] L:[X] FH:[X] ME:[X] FP:[X]`
