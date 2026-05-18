---
description: Add a new ticker to the wiki. Creates the wiki page from template, registers it in Monitor Registry, and runs stock-research to populate fundamental sections. Usage: /add-ticker TICKER [--sector "Sector Name"]
allowed-tools: WebSearch, WebFetch, Read, Write, Edit, Glob, Bash
---

# Add Ticker — Onboarding a New Name

One-command workflow to add a new ticker to the wiki. Creates the page, registers it, and populates it with fundamental research in a single pass.

**Vault path:** `Investing/Wiki/`
**Template path:** `Investing/Wiki/Reference/_Ticker Template.md`
**Monitor Registry:** `Investing/Wiki/Reference/Monitor Registry.md`

**Input:** `$ARGUMENTS` — the ticker symbol (required), plus optional `--sector "Sector Name"`

---

## Step 1 — Parse arguments

Extract from `$ARGUMENTS`:
- `TICKER` — the ticker symbol (uppercase), e.g. `SOFI`
- `--sector "..."` — optional sector name (must match an existing Sectors subfolder exactly, or be a new one)

If `--sector` is not provided, print the list of existing sectors and ask the user to confirm which one before continuing:
```
Existing sectors:
  1. AI Infrastructure
  2. Clean Energy
  3. Cybersecurity
  4. Fintech & E-Commerce
  5. Photonics & Optical
  6. Semiconductors
  7. Space & Comms
  8. [New sector — I'll create the folder]

Which sector does [TICKER] belong in?
```

---

## Step 2 — Check for duplicates

Use Glob to check if `[TICKER].md` already exists anywhere under `Investing/Wiki/Sectors/`.

If found, print:
```
⚠️  [TICKER] already exists at [path]
    Use /stock-research [TICKER] --refresh to update existing content.
    Aborting.
```
Then stop.

---

## Step 3 — Resolve company info from SEC EDGAR

Fetch the EDGAR company search page for this ticker:
`https://www.sec.gov/cgi-bin/browse-edgar?company=&CIK=[TICKER]&type=&dateb=&owner=include&count=5&search_text=&action=getcompany`

Extract:
- **Legal company name** (as registered with SEC)
- **CIK number** (10-digit, e.g. `0001818201`)
- **Exchange** (NASDAQ or NYSE — shown in the filing entity line)

If the EDGAR fetch fails or returns no result (foreign-listed company), set:
- Company name: search the web for `[TICKER] stock company name`
- CIK: `none`
- Exchange: note the actual exchange (e.g. `Nasdaq Stockholm`, `TSX Venture`)

---

## Step 4 — Create the wiki page

Read the template: `Investing/Wiki/Reference/_Ticker Template.md`

Make the following replacements throughout the content:
- `TICKER` → actual ticker symbol (e.g. `SOFI`)
- `Company Name` → legal company name from Step 3 (e.g. `SoFi Technologies`)
- `{{date}}` → today's date in `Month DD, YYYY` format (e.g. `May 16, 2026`)

Determine the output path:
- Sector folder: `Investing/Wiki/Sectors/[SECTOR]/`
- If this folder does not exist, create it (Bash: `mkdir`)
- Output file: `Investing/Wiki/Sectors/[SECTOR]/[TICKER].md`

Write the file.

---

## Step 5 — Add to Monitor Registry

Read the Monitor Registry. Find the table under the correct sector heading (e.g., `## Fintech & E-Commerce`).

Append a new row to that table:
```
| [TICKER] | [Company Name] | [CIK] | [Exchange] | Investing/Wiki/Sectors/[SECTOR]/[TICKER].md |
```

If the sector heading doesn't exist in the registry, add it:
```markdown
## [SECTOR]

| Ticker | Company | CIK | Exchange | Path |
|--------|---------|-----|----------|------|
| [TICKER] | [Company Name] | [CIK] | [Exchange] | Investing/Wiki/Sectors/[SECTOR]/[TICKER].md |
```

Also update the `*Last updated:` line at the top of the registry to today's date.

Write the updated Monitor Registry back.

---

## Step 6 — Run stock research (inline)

Now populate the fundamental sections of the newly created wiki page.

Run three lookups in parallel:

**Search A — Business & thesis:**
`[TICKER] business model competitive moat investment thesis 2025 2026`
`[TICKER] CEO CFO executive team background tenure track record`

**Search B — SEC DEF 14A for insider ownership:**
`https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=[TICKER]&type=DEF+14A&dateb=&owner=include&count=1&search_text=`

If CIK is `none`, skip Search B and note `— (not an SEC filer)`.

Using the research results, populate these sections in the new wiki page:

### One-Line Thesis
One sentence. Max 25 words. Present tense. Lead with core differentiation — not "a company that." No filler phrases.

### Investment Thesis

First, fill in the **Thesis Drift block** at the top of the section:
```
> **Thesis established:** [TODAY'S DATE]
> **Last validated:** [TODAY'S DATE]
> **Drift status:** On track — initial thesis established; monitor for first earnings validation
```

Then write 2–4 paragraphs covering:
1. What the company does and why it matters now
2. The bull case and primary growth driver
3. Key moat (specific and concrete)
4. Key risks (specific and honest)

Then the `**Key moat:**` and `**Key risks:**` summary lines.

### Management & Leadership
Fill in the CEO and CFO table rows (and any other C-suite notably relevant to the thesis). Notes column: max 15 words per row.

Fill in:
- **Execution track record:** 1–2 sentences on capital allocation history, guidance accuracy, prior company outcomes
- **Insider ownership / alignment:** Ownership % from DEF 14A, recent Form 4 activity if notable; if unavailable write `— (DEF 14A pending)` or `— (not an SEC filer)`

---

## Step 7 — Append to Research Log

Add one entry at the bottom of the Research Log section in the new wiki page:
`- **[TODAY'S DATE]** — add-ticker run. Note created from template; fundamental sections populated from web research and SEC DEF 14A.`

---

## Step 8 — Print summary

Print the completion summary:
```
✅ [TICKER] — [Company Name] added to Wiki

   📄 Page:      Investing/Wiki/Sectors/[SECTOR]/[TICKER].md
   🏛️  CIK:       [CIK] ([Exchange])
   📋 Registry:  Monitor Registry updated — [SECTOR] section
   ✍️  Populated: One-Line Thesis · Investment Thesis · Management & Leadership

   Next steps:
   • Run /ticker-monitor --deep [TICKER] to pull recent SEC filings and news
   • Check the Catalyst Timeline — add upcoming earnings date if known
   • Add Cross-Ticker Signals if this name has clear read-throughs to existing names
```

---

## Rules

- **Never overwrite an existing wiki page.** If the file exists, abort (Step 2).
- **Preserve all template sections.** Do not remove or reorder any sections from the template, even if content is not yet available.
- **Leave placeholder tables intact.** The Conviction Log, Cross-Ticker Signals, Earnings & Financials, and SEC Filings tables should remain as empty tables (the `| — |` row pattern) if no real data is available yet. Do not delete them.
- **Keep writing style consistent** with existing pages: direct, no hype, no passive voice.
- **Fail gracefully.** If EDGAR is unavailable, continue with `none` for CIK and note the source. If web search returns thin results, write what's available and note the gap in the Research Log entry.
