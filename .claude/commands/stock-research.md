---
description: One-time fundamental research for a ticker. Populates Investment Thesis, Management & Leadership, and One-Line Thesis in the wiki page. Usage: /stock-research TICKER [--refresh]
allowed-tools: WebSearch, WebFetch, Read, Edit, Glob
---

# Stock Research — Fundamental Deep Dive

One-time skill that builds or refreshes the core fundamental sections of a wiki ticker page. Writes directly to the vault — no Obsidian MCP required.

**Vault path:** `Investing/Wiki/Sectors/`

**Input:** `$ARGUMENTS` — the ticker symbol, e.g. `COHR`. Optionally `COHR --refresh` to overwrite existing content.

---

## Step 1 — Locate the wiki page

Use Glob to find `$ARGUMENTS.md` under `Investing/Wiki/Sectors/`. Read its current contents. Note which sections already have real content vs. placeholder `—` values.

Unless `--refresh` was passed, skip any section that already has non-placeholder content. Only populate sections where the key fields are still `—`.

---

## Step 2 — Research (run all three in parallel)

**Search A — Business & thesis:**
Search: `[TICKER] business model competitive moat investment thesis 2025 2026`
Search: `[TICKER] CEO CFO executive team background tenure track record`

**Search B — Insider ownership via SEC EDGAR:**
Fetch the EDGAR filing index to find the most recent DEF 14A (proxy statement):
`https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=[TICKER]&type=DEF+14A&dateb=&owner=include&count=1&search_text=`

From the DEF 14A, extract: CEO/CFO names, beneficial ownership percentages, and any notable compensation or incentive alignment signals.

If EDGAR lookup fails (foreign-listed company or not an SEC filer), note it and rely on Search A only.

---

## Step 3 — Populate sections

Edit the wiki page. For each section below, only write if the section has placeholder content (or `--refresh` was passed).

### One-Line Thesis
One sentence. Max 25 words. Present tense. Lead with the core differentiation — not "a company that." No filler phrases.

### Investment Thesis
2–4 paragraphs covering:
1. What the company does and why it matters now
2. The bull case and primary growth driver
3. Key moat (specific and concrete)
4. Key risks (specific and honest)

Format as the existing pages use: paragraphs, then `**Key moat:**` and `**Key risks:**` lines.

### Management & Leadership
Fill in the table rows for CEO and CFO. Add other C-suite rows only if they are notably relevant to the thesis (e.g. a CTO at a deep-tech company). Notes column: max 15 words per row.

Fill in:
- **Execution track record:** 1–2 sentences on capital allocation history, guidance accuracy, prior company outcomes.
- **Insider ownership / alignment:** Ownership % from DEF 14A, any recent Form 4 purchases or sales worth noting.

---

## Step 4 — Append to Research Log

Add one entry at the bottom of the Research Log:
`- **[TODAY'S DATE]** — stock-research run. Fundamental sections populated from web research and SEC DEF 14A.`

---

## Rules

- Never truncate or overwrite existing Research Log entries.
- If DEF 14A data is unavailable, write `— (not an SEC filer)` or `— (DEF 14A pending)` rather than leaving `—`.
- Keep the writing style consistent with the existing pages: direct, no hype, no passive voice.
- Do not add sections beyond the template. Do not reformat or reorder existing sections.
