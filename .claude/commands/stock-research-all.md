---
description: Batch research refresh across all wiki tickers. Populates/refreshes facts.md (management, moat, metrics) and analysis.md (thesis, management notes) concurrently. Skips tickers whose core sections are already populated unless --refresh is passed. Usage: /stock-research-all [--refresh] [--sector SECTOR]
allowed-tools: Read, Write, Edit, Glob, Agent
---

# Stock Research — Batch Refresh

Runs fundamental research across every wiki ticker concurrently by spawning one sub-agent per ticker. Each agent writes directly to facts.md and analysis.md and returns compact JSON. The main context never loads research content.

**Registry:** `Investing/Wiki/Reference/Monitor Registry.yaml`

**Flags (`$ARGUMENTS`):**
- *(none)* — skip tickers whose One-Line Thesis and Investment Thesis are already populated in analysis.md
- `--refresh` — run all tickers regardless of current content
- `--sector SECTOR` — limit to one sector (e.g. `--sector "Photonics & Optical"`)

---

## Phase 1 — Inventory

1. Read `Investing/Wiki/Reference/Monitor Registry.yaml`. Get all tickers (filtered by `--sector` if set).
2. For each ticker, read `[path]/analysis.md`. Check whether `## One-Line Thesis` and `## Investment Thesis` have real content (not just template placeholders like `{{...}}` or `...`).
3. Also read `[path]/facts.md` (YAML frontmatter). Check if `management` array has real names (not `"—"`).
4. Build two lists:
   - **Needs research**: One-Line Thesis, Investment Thesis, or management stubs
   - **Already populated**: all three have real content
5. If `--refresh` was passed, move all tickers to Needs research.
6. Print the work list before proceeding.

If the Needs research list is empty, report "All tickers populated" and stop.

---

## Phase 2 — Concurrent research (batches of 5)

Split the Needs research list into batches of 5. Run each batch as fully parallel Agent calls before moving to the next batch.

For each ticker in a batch, spawn one Agent with this prompt:

---

**Sub-agent prompt template:**

> You are a financial research assistant. Populate the fundamental sections of the wiki for **[TICKER] — [Company Name]** ([Sector]).
>
> **Files to write:**
> - facts.md: `[FULL_FACTS_PATH]`
> - analysis.md: `[FULL_ANALYSIS_PATH]`
>
> **Mode:** [populate stubs only / --refresh: overwrite all]
>
> ---
>
> **Step 1 — Read current state.**
> Read facts.md YAML frontmatter and analysis.md. Note which sections have placeholder content vs. real content. In populate mode, only write stubs. In refresh mode, overwrite.
>
> **Step 2 — Run research in parallel:**
>
> Search A (business & thesis):
> - `[TICKER] [Company Name] business model competitive moat investment thesis 2025 2026`
> - `[TICKER] [Company Name] CEO CFO executive team background tenure track record`
>
> Search B (insider ownership):
> - Fetch: `https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=[CIK]&type=DEF+14A&dateb=&owner=include&count=1`
> - If CIK is null (foreign-listed), skip and note `— (not an SEC filer)`.
>
> **Step 3 — Update facts.md YAML.**
>
> Edit the YAML frontmatter block in facts.md. Update only these fields (do not touch earnings or filings):
> ```yaml
> management:
>   - role: CEO
>     name: "[Name from research]"
>     ownership_pct: [% from DEF 14A or null]
>     notes: "[max 12 words: tenure + key signal]"
>   - role: CFO
>     name: "[Name]"
>     ownership_pct: [% or null]
>     notes: "[max 12 words]"
> moat:
>   type: "[Platform/Ecosystem | Sole-source | IP/Patent | Cost | Network | Other]"
>   pricing_power: "[high | medium | low]"
>   competition_intensity: "[low | medium | high]"
>   made_in_usa: [true | false | null]
>   notes: "[max 15 words on the moat's defensibility]"
> last_updated: "[TODAY'S DATE]"
> ```
>
> **Step 4 — Update analysis.md.**
>
> Edit (or write) only these sections in analysis.md:
>
> **One-Line Thesis:** One sentence, max 25 words, present tense, lead with core differentiation. No filler like "a company that."
>
> **Investment Thesis:** Fill the Thesis Drift block with today's date and "initial thesis established". Then write 2–4 paragraphs covering: what it does and why now, bull case, key moat (specific), key risks (honest). End with `**Key moat:**` and `**Key risks:**` lines.
>
> Do not modify Scoring Summary, Conviction Log, Cross-Ticker Signals, Catalyst Timeline, Analyst Coverage, or Ecosystem Links.
>
> **Step 5 — Append to signals.md Research Log:**
> `- **[TODAY'S DATE]** — stock-research-all run. facts.md management/moat + analysis.md thesis populated.`
>
> **Step 6 — Return compact JSON (no other output):**
> ```json
> {
>   "ticker": "TICKER",
>   "status": "updated" | "skipped" | "error",
>   "facts_updated": ["management", "moat"],
>   "analysis_updated": ["One-Line Thesis", "Investment Thesis"],
>   "edgar_result": "DEF 14A found" | "foreign filer" | "not found",
>   "note": "one sentence on anything notable or flagged"
> }
> ```

---

## Phase 3 — Summary

After all batches complete, print a results table:

```
| Ticker | Status | facts.md | analysis.md | EDGAR | Note |
|--------|--------|----------|-------------|-------|------|
| COHR   | updated | mgmt+moat | thesis | DEF 14A found | — |
| SIVE   | updated | mgmt+moat | thesis | foreign filer | — |
| NVDA   | skipped | — | — | — | Already populated |
```

Report total: updated / skipped / errors.
