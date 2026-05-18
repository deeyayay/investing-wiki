---
description: Runs stock-research across all wiki ticker pages concurrently. Skips tickers whose core sections are already populated unless --refresh is passed. Usage: /stock-research-all [--refresh] [--sector SECTOR]
allowed-tools: Glob, Read, Agent
---

# Stock Research — Batch Run

Runs fundamental research across every wiki ticker page concurrently by spawning one sub-agent per ticker. Each agent writes directly to its vault file and returns a compact status. The main context never loads research content — only final summaries.

**Vault path:** `Investing/Wiki/Sectors/`

**Flags (`$ARGUMENTS`):**
- *(none)* — skip tickers whose One-Line Thesis, Investment Thesis, and Management table are already populated
- `--refresh` — run all tickers regardless of current content
- `--sector SECTOR` — limit to one sector folder (e.g. `--sector "Photonics & Optical"`)

---

## Phase 1 — Inventory

1. Use Glob to find all `*.md` files under `Investing/Wiki/Sectors/` excluding `_Sector Framework.md` and `_Ticker Template.md`.
2. Read each file. For each ticker, check whether these three sections have real content (not just `—` placeholders or `...`):
   - `## One-Line Thesis`
   - `## Investment Thesis` (specifically the body paragraphs — not just the `**Key moat:**` and `**Key risks:**` placeholder lines)
   - `## Management & Leadership` (CEO and CFO rows filled, track record and ownership fields populated)
3. Build two lists:
   - **Needs research**: any section above is a stub
   - **Already populated**: all three sections have real content
4. If `--refresh` was passed, move all tickers to the Needs research list.
5. If `--sector` was passed, filter both lists to that folder only.
6. Print the work list before proceeding:

```
Needs research (N tickers): TICKER1, TICKER2, ...
Already populated (M tickers): TICKER3, TICKER4, ...
Skipping populated tickers. Pass --refresh to overwrite.
```

If the Needs research list is empty, report "All tickers populated" and stop.

---

## Phase 2 — Concurrent research (batches of 5)

Split the Needs research list into batches of 5 tickers. Run each batch as a set of fully parallel Agent calls before moving to the next batch. This prevents API rate limit issues while maximising throughput.

For each ticker in a batch, spawn one Agent with the following prompt (substitute the actual ticker symbol, company name, sector, and full file path):

---

**Sub-agent prompt template:**

> You are a financial research assistant. Your job is to populate the fundamental sections of a wiki investment page for **[TICKER] — [Company Name]** ([Sector]).
>
> **Wiki file path:** `[FULL_FILE_PATH]`
>
> **Mode:** [populate stubs only / --refresh: overwrite all]
>
> ---
>
> **Step 1 — Read the current wiki page.**
> Note which sections have placeholder content (`—`, `...`) vs. real content. In populate mode, only write sections that are still stubs. In refresh mode, overwrite all three core sections.
>
> **Step 2 — Run all research in parallel:**
>
> Search A (business & thesis):
> - `[TICKER] [Company Name] business model competitive moat investment thesis 2025 2026`
> - `[TICKER] [Company Name] CEO CFO executive team background tenure track record`
>
> Search B (insider ownership):
> - Fetch: `https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=[TICKER]&type=DEF+14A&dateb=&owner=include&count=1`
> - If the company is foreign-listed or EDGAR returns no results, note it and rely on Search A only.
>
> **Step 3 — Edit the wiki file. Populate only these sections:**
>
> **One-Line Thesis:** One sentence, max 25 words, present tense. Lead with the core differentiation. No filler phrases like "a company that."
>
> **Investment Thesis:** 2–4 paragraphs covering: what it does and why it matters now, bull case and primary growth driver, key moat (specific), key risks (honest). End with `**Key moat:**` and `**Key risks:**` lines matching the existing page style.
>
> **Management & Leadership:** Fill the CEO and CFO table rows (add other roles only if critical to the thesis). Fill `**Execution track record:**` (1–2 sentences) and `**Insider ownership / alignment:**` (% from DEF 14A or best available source; note if unavailable).
>
> **Rules:**
> - Do not modify any other sections.
> - Do not truncate or delete any existing Research Log entries.
> - Keep writing style consistent with existing pages: direct, no hype, no passive voice.
> - If DEF 14A is unavailable write `— (not an SEC filer)` or `— (DEF 14A unavailable)` rather than leaving `—`.
>
> **Step 4 — Append to Research Log:**
> `- **[TODAY'S DATE]** — stock-research run. Fundamental sections populated from web research and SEC DEF 14A.`
>
> **Step 5 — Return a single compact JSON result (no other output):**
> ```json
> {
>   "ticker": "TICKER",
>   "status": "updated" | "skipped" | "error",
>   "sections_written": ["One-Line Thesis", "Investment Thesis", "Management & Leadership"],
>   "edgar_result": "DEF 14A found" | "foreign filer" | "not found" | "403 error",
>   "note": "one sentence on anything notable or flagged"
> }
> ```

---

## Phase 3 — Summary

After all batches complete, print a results table:

```
| Ticker | Status | Sections Written | EDGAR | Note |
|--------|--------|-----------------|-------|------|
| COHR   | updated | Thesis, Mgmt   | DEF 14A found | — |
| SIVE   | updated | All             | foreign filer | Criminal investigation flagged |
| NVDA   | skipped | —               | —     | Already populated |
```

Report total: updated / skipped / errors.
