---
description: Add a new ticker to the wiki. Creates the three-layer file structure (facts.md + analysis.md + signals.md), registers it in Monitor Registry.yaml, and populates fundamental sections in a single pass. Usage: /add-ticker TICKER [--sector "Sector Name"] [--refresh-research]
allowed-tools: WebSearch, WebFetch, Read, Write, Edit, Glob, Bash
---

# Add Ticker — Onboarding a New Name

One-command workflow to add a new ticker to the wiki. Creates the three-layer folder structure, registers it in Monitor Registry.yaml, and populates facts.md + analysis.md with fundamental research.

**Vault path:** `Investing/Wiki/Sectors/`
**Templates:** `Investing/Wiki/Reference/_facts-template.md`, `_analysis-template.md`, `_signals-template.md`
**Monitor Registry:** `Investing/Wiki/Reference/Monitor Registry.yaml`

**Input:** `$ARGUMENTS`
- `TICKER` — required. The ticker symbol (uppercase), e.g. `SOFI`
- `--sector "..."` — optional sector name (must match an existing Sectors subfolder, or be a new one)
- `--refresh-research` — re-run the research pass on an existing ticker (updates facts.md + analysis.md thesis/management; never deletes existing data)

---

## Step 1 — Parse arguments

Extract from `$ARGUMENTS`:
- `TICKER` — ticker symbol (uppercase)
- `--sector "..."` — optional sector name
- `--refresh-research` — flag

If `--sector` is not provided, print the list of existing sectors and ask the user to confirm:
```
Existing sectors (layer-aligned folders):
  L01  1. Application
  L02  2. AI Model
  L03  3. Software Infrastructure
  L04  4. Cloud Infrastructure
  L05  5. Compute Hardware
  L06  6. Memory
  L07  7. Interconnect
  L08  8. Advanced Packaging
  L09  9. Semiconductor Foundry
  L10  10. Semiconductor Equipment
  L11  11. Semiconductor Materials
  L12  12. Critical Minerals
  Rail 13. Power Infrastructure
  Rail 14. Security
  Rail 15. Edge & Physical AI
  Cross 16. Electronic Components
       17. [New sector — I'll create the folder]

Which sector does [TICKER] belong in?
```

---

## Step 2 — Check for existing ticker

Use Glob to check if `Investing/Wiki/Sectors/*/[TICKER]/facts.md` already exists.

**If found and `--refresh-research` is NOT set:**
```
⚠️  [TICKER] already exists at [path]/facts.md
    Use /add-ticker [TICKER] --refresh-research to re-run fundamental research.
    Aborting.
```
Then stop.

**If found and `--refresh-research` IS set:** skip to Step 4 (research pass only; skip file creation and registry steps).

Also check for old-format files: `Investing/Wiki/Sectors/*/[TICKER].md`.
If an old-format file exists, print:
```
ℹ️  Found legacy file: [path]
    This is the old single-file format. Run /ticker-monitor --deep [TICKER] to migrate it to the three-layer structure.
    Aborting add-ticker to avoid conflicts.
```
Then stop.

---

## Step 3 — Resolve company info from SEC EDGAR

Fetch the EDGAR company search page for this ticker:
`https://www.sec.gov/cgi-bin/browse-edgar?company=&CIK=[TICKER]&type=&dateb=&owner=include&count=5&search_text=&action=getcompany`

Extract:
- **Legal company name** (as registered with SEC)
- **CIK number** (10-digit, e.g. `0001818201`)
- **Exchange** (NASDAQ or NYSE)

If EDGAR returns no result (foreign-listed company):
- Company name: search the web for `[TICKER] stock company name exchange`
- CIK: `null`
- Exchange: note the actual exchange (e.g. `Nasdaq Stockholm`, `TSX Venture`)

---

## Step 4 — Research pass (web + EDGAR)

Run three lookups in parallel:

**Search A — Business & thesis:**
`[TICKER] business model competitive moat investment thesis 2025 2026`
`[TICKER] CEO CFO executive team background tenure track record`

**Search B — SEC DEF 14A for insider ownership:**
`https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=[CIK]&type=DEF+14A&dateb=&owner=include&count=1`

If CIK is null, skip Search B and note `— (not an SEC filer)`.

**Search C — Key metrics:**
`[TICKER] [Company Name] revenue earnings gross margin P/B P/E forward guidance 2026`

From the research results, extract:
- One-line thesis (max 25 words, present tense, lead with core differentiation)
- Business description and bull case (2–4 paragraphs)
- Key moat and key risks
- CEO name, CFO name, tenure, insider ownership % from DEF 14A
- Execution track record (1–2 sentences)
- Latest revenue, gross margin, forward P/E or P/B if available
- Moat type, pricing power assessment, competitive intensity

---

## Step 5 — Create file structure (skip if --refresh-research)

Determine the output folder:
- `Investing/Wiki/Sectors/[SECTOR]/[TICKER]/`
- If the sector folder does not exist: `mkdir -p "Investing/Wiki/Sectors/[SECTOR]/[TICKER]"`
- If the ticker folder does not exist: `mkdir "Investing/Wiki/Sectors/[SECTOR]/[TICKER]"`

### Write facts.md (Layer 1)

Read `Investing/Wiki/Reference/_facts-template.md` as the schema reference.

Write `Investing/Wiki/Sectors/[SECTOR]/[TICKER]/facts.md` with YAML frontmatter populated from research:

```markdown
---
ticker: [TICKER]
company: "[Legal Company Name]"
cik: "[CIK or null]"
exchange: [Exchange]
sector: "[SECTOR]"

management:
  - role: CEO
    name: "[Name]"
    ownership_pct: [% from DEF 14A, or null]
    notes: "[max 12 words: tenure + key signal]"
  - role: CFO
    name: "[Name]"
    ownership_pct: [% or null]
    notes: "[max 12 words]"

earnings: []

filings: []

moat:
  type: "[Platform/Ecosystem | Sole-source | IP/Patent | Cost | Network | Other]"
  pricing_power: "[high | medium | low]"
  competition_intensity: "[low | medium | high]"
  made_in_usa: [true | false | null]
  notes: "[max 15 words on the moat's defensibility]"

metrics:
  score: null
  score_label: "—"
  last_scored: null
  valuation_fpe: [forward P/E or null]
  analyst_pt: null
  analyst_upside_pct: null

last_updated: "[TODAY'S DATE]"
---
```

### Write analysis.md (Layer 2)

Read `Investing/Wiki/Reference/_analysis-template.md` as the schema reference.

Write `Investing/Wiki/Sectors/[SECTOR]/[TICKER]/analysis.md` with the following sections populated:

**One-Line Thesis:** one sentence, max 25 words, present tense, lead with core differentiation.

**Investment Thesis:** fill the Thesis Drift block with today's date, then write 2–4 paragraphs covering:
1. What the company does and why it matters now
2. Bull case and primary growth driver
3. Key moat (specific and concrete)
4. Key risks (specific and honest)

Then the `**Key moat:**` and `**Key risks:**` summary lines.

All other sections (Scoring Summary, Conviction Log, Cross-Ticker Signals, Catalyst Timeline, Analyst Coverage) remain as stubs from the template.

### Write signals.md (Layer 3)

Read `Investing/Wiki/Reference/_signals-template.md`.

Write `Investing/Wiki/Sectors/[SECTOR]/[TICKER]/signals.md` — replace `TICKER` with the actual ticker symbol. Body is empty (stubs only).

Append the initial Research Log entry:
`- **[TODAY'S DATE]** — add-ticker run. facts.md + analysis.md populated from web research and SEC EDGAR.`

---

## Step 6 — Register in Monitor Registry.yaml (skip if --refresh-research)

Read `Investing/Wiki/Reference/Monitor Registry.yaml`.

Append the new ticker under the `tickers:` key in the appropriate sector grouping:

```yaml
  [TICKER]:
    company: "[Legal Company Name]"
    cik: "[CIK or null]"
    exchange: [Exchange]
    sector: "[SECTOR]"
    path: "Investing/Wiki/Sectors/[SECTOR]/[TICKER]"
    score: null
```

If the ticker already exists as a `candidate` entry, remove it from the `candidates:` list.

Also update `last_updated` to today's date.

---

## Step 7 — Print summary

For new ticker:
```
✅ [TICKER] — [Company Name] added

   📁 Folder:    Investing/Wiki/Sectors/[SECTOR]/[TICKER]/
   📊 facts.md:  CIK [CIK] ([Exchange]) · moat: [type] · [pricing_power] pricing power
   📝 analysis.md: One-Line Thesis + Investment Thesis + Management populated
   📡 signals.md: empty (ready for news + sentiment)
   📋 Registry:  Monitor Registry.yaml updated

   Next steps:
   • /ticker-monitor --deep [TICKER]   ← pull recent SEC filings + news
   • /score-ticker [TICKER]            ← score on 6-criterion rubric
   • Check Catalyst Timeline in analysis.md — add upcoming earnings date if known
```

For `--refresh-research`:
```
✅ [TICKER] — research refreshed

   📊 facts.md:  management + moat + metrics updated
   📝 analysis.md: One-Line Thesis + Investment Thesis updated
   📋 Registry:  score preserved (re-run /score-ticker to update)
```

---

## Rules

- **Never overwrite an existing three-layer folder.** If `facts.md` already exists and `--refresh-research` is not set, abort (Step 2).
- **`--refresh-research` updates, never deletes.** It rewrites One-Line Thesis, Investment Thesis, and management rows in facts.md. It never touches Conviction Log, Cross-Ticker Signals, Scoring Summary, or Research Log.
- **YAML must be valid.** All string values with special characters must be quoted. Null values use `null`, not `—`.
- **Fail gracefully.** If EDGAR is unavailable, continue with `null` for CIK and note the source. If web search returns thin results, write what's available and note the gap in signals.md Research Log.
- **No old-format creation.** Never create a single `[TICKER].md` file. Always use the three-file folder structure.
