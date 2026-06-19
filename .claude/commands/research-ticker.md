---
description: Full-KB investment research view for a ticker. Reads all three layers (facts, analysis, signals) + Raw/Sentiment files + Sentiment Index + Sector Framework. Use for any investment question — buy/sell/hold, thesis review, risk assessment. Usage: /research-ticker TICKER [--question "specific question"]
allowed-tools: Read, Glob, Grep
---

# /research-ticker

Synthesize the full knowledge base for a ticker into a structured investment view. This is the only skill that reads **all three layers plus sentiment** — it exists so that ad-hoc investment questions get the same data coverage as a formal scoring run.

## Usage

```
/research-ticker TICKER [--question "specific question"]
```

- `TICKER` — required. The ticker symbol (e.g. `AAOI`, `NVDA`).
- `--question` — optional. The specific question driving the research (e.g. `"is this a buy at $162?"`, `"what changed since the last score?"`). Shapes the synthesis focus without changing what gets read.

---

## What This Skill Reads (and Why Each Source Matters)

| Source | Why |
|--------|-----|
| `facts.md` (Layer 1) | Structured data: earnings history, management, moat, score metrics |
| `analysis.md` (Layer 2) | Thesis, conviction log, risk flags, analyst coverage, catalysts |
| `signals.md` (Layer 3) | Recent news log, social mention stubs, research audit trail |
| `Raw/Sentiment/*[TICKER]*` | **The actual tweet/article text** — where market intelligence lives; signals.md only has links |
| `Sentiment Index.md` | Aggregated sentiment score and recency for this ticker |
| `_Sector Framework.md` | Cycle phase, archetype valuation matrix, bull/base/bear cases |

**signals.md and Raw/Sentiment are the layers most often skipped in ad-hoc answers. This skill makes them mandatory.**

---

## Workflow

### Step 1 — Locate the ticker

Read `Investing/Wiki/Reference/Monitor Registry.yaml`. Find the entry for TICKER. Extract:
- `path` → used for all three layer reads
- `sector` → used to find Sector Framework
- `score`, `next_earnings`

If not found, print:
```
⚠️  [TICKER] not in Monitor Registry.yaml. Run /add-ticker [TICKER] first.
```
Then stop.

### Step 2 — Read all three layers (parallel reads)

Run all three reads simultaneously:

**Layer 1:** `[path]/facts.md`
Extract: management (ownership, tenure, alignment notes), earnings array (revenue trend, EPS, beats, guidance), moat (type, pricing_power, competition_intensity), tech_exposure, demand_chain, metrics (score, last_scored), next_earnings.

**Layer 2:** `[path]/analysis.md`
Extract: One-Line Thesis, Investment Thesis (bull case, key moat, key risks, drift status), Scoring Summary table (all 6 criteria + composite), Risk Flags table, Conviction Log (all entries, especially recent ↑/↓), Cross-Ticker Signals, Catalyst Timeline (passed vs pending), Analyst Coverage (all PT and rating entries).

**Layer 3:** `[path]/signals.md`
Extract: News & Alpha Log (all entries), Social Mentions table (stub links only — actual content comes from Step 3), Research Log (last 3 entries).

### Step 3 — Load sentiment files

```
Glob: Investing/Raw/Sentiment/*[TICKER]*
```

Read **every file returned**. For each file extract:
- `date`, `author`, `source` from YAML frontmatter
- The full body text

If no files found, note "No sentiment files in KB for [TICKER]."

Also read `Investing/Wiki/Reference/Sentiment Index.md`. Find the row for this ticker. Extract: sentiment score, status (monitored/stub), signal count, last signal date.

### Step 4 — Read Sector Framework

Read `Investing/Wiki/Sectors/[sector]/_Sector Framework.md`.
Extract: current cycle phase, archetype for this ticker (from the Industry Structure table), valuation reference matrix row for that archetype (Fair Value Range, Peak Enthusiasm, Trough Fear), Sector Bull/Base/Bear cases.

### Step 5 — Synthesize

Produce a structured investment view with these sections. If `--question` was provided, open with a direct answer to it, then support with the sections below.

#### KB Snapshot
One-paragraph summary of what the KB currently knows: score, last scored date, thesis one-liner, next earnings, thesis drift status. Flag any staleness (score >90 days old = low-confidence; no earnings in facts.md = sparse data).

#### Conviction Trajectory
Summarize the Conviction Log — net direction (more ↑ or ↓ since inception?), most recent entry, and whether the thesis drift block says "On track / Drifting / Broken."

#### Sentiment Signals
For each Raw/Sentiment file found, extract the key claims about this ticker as bullet points with direct quotes. Note author handle if present. Note the aggregate Sentiment Index score.

**Do not paraphrase away specificity.** If a tweet says "$600M dilution" or "$400M/month H2 target," quote it exactly — these are the signals most likely to differ from the structured KB data.

#### Sector Context
One paragraph: where we are in the cycle per the Sector Framework, this ticker's archetype, what the archetype's fair value range is, and where the current price sits relative to it.

#### Bull / Bear
**Bull case** (3–5 bullets, sourced from Investment Thesis + positive Conviction Log entries + bullish sentiment signals)
**Bear / Risk** (3–5 bullets, sourced from Risk Flags + negative Conviction Log entries + bearish sentiment signals + Sector Framework bear case)

#### Catalyst Gates
List all pending `- [ ]` items from Catalyst Timeline with estimated dates. Bold the next gate.

#### Valuation
From Analyst Coverage + Sector Framework archetype matrix:
`[Cheap / Reasonable / Fair / Expensive] at $[price] | [Metric]: [X]x | Analyst range: $[low] ([firm, rating]) – $[high] ([firm, rating])`

If current price unknown, note "Price not in KB — check live data."

#### KB Gaps
List any data absent from the KB that would materially change the view (e.g., gross margin not in wiki, balance sheet absent, no sentiment files ingested). Flag what would close each gap (`/ticker-monitor --deep`, `/ingest-sentiment`, etc.).

---

## Output Rules

- **Quote sentiment files directly** — don't flatten specific claims into generic summaries.
- **Cite the source layer** for every claim: `(facts.md)`, `(analysis.md)`, `(signals.md)`, `(Raw/Sentiment/[filename])`, `(Sector Framework)`.
- **Never fabricate.** If a data point is absent from the KB, say so. Do not substitute web knowledge for KB knowledge — this skill synthesizes the KB, not the internet.
- **Recency matters.** Always note the `last_scored` date and `last_updated` date from facts.md. A 90-day-old score on a fast-moving stock is low-confidence.
- **This skill does not write to any file.** It is read-only. To update the KB, use `/ticker-monitor --deep TICKER` or `/score-ticker TICKER`.
