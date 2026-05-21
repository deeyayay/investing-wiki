# Ingest Ecosystem — Supply Chain Map from Image or Text

Reads an infographic, diagram, or pasted description of a sector's supply chain / ecosystem, extracts tickers and their relationships, and writes a structured ecosystem map file. Once ingested, the next `/daily-dashboard` run automatically renders a full tier diagram for all tickers in that ecosystem.

**Input:**
- `/ingest-ecosystem` — reads from clipboard/pasted text in the conversation (describe the ecosystem or paste a structured list)
- `/ingest-ecosystem --image PATH` — reads an image file (PNG, JPG, PDF page) using vision; PATH is relative to repo root
- `/ingest-ecosystem --sector "Sector Name"` — tag the map to a specific sector (optional; auto-detected if omitted)
- `/ingest-ecosystem --anchor TICKER` — specify the central company in the ecosystem (e.g., `--anchor NVDA`)

**Output:** `Investing/Wiki/Reference/Ecosystem Maps/[Name] Ecosystem Map.md`

---

## Phase 1 — Read input

**If `--image PATH`:**
Read the image file at the given path using your vision capability. Extract all companies, tickers, and the relationships shown (arrows, lines, labels, groupings, color coding, tier labels, etc.). Be thorough — scan every part of the diagram including legends, footnotes, and callout boxes.

**If no `--image`:**
Use the text, description, or data pasted in the conversation. If the user pasted raw text, structured tables, or described relationships verbally, treat that as the source.

---

## Phase 2 — Extract structure

From the source material, identify:

1. **Anchor company** (the central entity the ecosystem revolves around) — e.g., GE Vernova, NVDA, TSMC
2. **Tier or category labels** — the infographic may use "Upstream / Downstream", numbered tiers, functional categories ("Foundry", "Packaging", "Memory"), or custom groupings
3. **Company/ticker entries** — for each company: name, ticker symbol (if shown or known), tier/category, and the relationship to the anchor (supplier, customer, partner, competitor, enabler, portfolio company, etc.)
4. **Relationship direction** — does the arrow flow FROM this company TO the anchor (upstream / supplier) or FROM the anchor TO this company (downstream / customer/enabler)?
5. **Any notes** — deal sizes, market share stats, specific products, date context shown in the diagram

**Ticker resolution:**
- If a ticker is shown explicitly in the diagram, use it as-is
- If only a company name is shown, attempt to resolve to a ticker from the Monitor Registry (`Investing/Wiki/Reference/Monitor Registry.md`) — read the registry to cross-reference
- If not in the registry, check if the company is widely known (e.g., "Siemens" → SI or SIE.DE). Use your knowledge for common names; mark uncertain resolutions with a `?` in the Notes column
- If unresolvable, leave the Ticker column blank and use the company name only

---

## Phase 3 — Map to tier structure

Organize the extracted companies into a tier structure following the NVDA Ecosystem Map format. Use these canonical tier labels when they apply:

| Tier | Standard label |
|------|---------------|
| 1 | Direct Supply Chain |
| 2 | Infrastructure & Deployment |
| 3 | Networking & Interconnect |
| 4 | Power & Energy |
| 5 | Software & Platforms / Customers |

If the source uses different groupings (e.g., "Foundry / Packaging / Memory" categories), preserve those as-is and note them as functional categories rather than tiers.

For each tier or category, format a table:

```markdown
| Ticker | Company | Relationship | Notes |
|--------|---------|-------------|-------|
| TSM    | TSMC    | Sole foundry partner | 5nm, 3nm process nodes |
```

Relationship column should be a short phrase: "Primary supplier", "Key customer", "Design partner", "Competitor", "Minority investor", etc.

---

## Phase 4 — Check Monitor Registry for new tickers

Read `Investing/Wiki/Reference/Monitor Registry.md`.

For each ticker identified in the ecosystem that is NOT already in the Monitor Registry:
- Note it as a candidate for `/add-ticker` in a "New Tickers" section at the bottom of the ecosystem map
- Do NOT auto-add to the registry; just surface the candidates

---

## Phase 5 — Write the ecosystem map file

Determine the output filename:
- If `--anchor TICKER` is provided: `[TICKER] Ecosystem Map.md`
- If `--sector "Name"` is provided: `[Sector Name] Ecosystem Map.md`
- Otherwise: derive from the anchor company name: `[CompanyName] Ecosystem Map.md`

Write to: `Investing/Wiki/Reference/Ecosystem Maps/[filename]`

If a file already exists at that path, append a new dated section to it rather than overwriting (treat it as an update). Note the update date.

**File format:**

```markdown
# [Anchor Company / Sector] Ecosystem Map

*Source: [brief description — e.g., "Infographic: Energy Sector Supply Chain, May 2026" or "Manual entry"]*
*Last updated: [today's date]*
*Anchor: [[TICKER]] — [Company Name]*

---

## Tier 1 — [Label]

| Ticker | Company | Relationship | Notes |
|--------|---------|-------------|-------|
| ...    | ...     | ...         | ...   |

## Tier 2 — [Label]

| Ticker | Company | Relationship | Notes |
|--------|---------|-------------|-------|
| ...    | ...     | ...         | ...   |

[... repeat for each tier or category ...]

---

## New Tickers (not yet in Monitor Registry)

These companies appeared in the ecosystem but are not tracked in the Monitor Registry.
Run `/add-ticker TICKER` to onboard them fully.

| Ticker | Company | Why relevant |
|--------|---------|-------------|
| ...    | ...     | ...         |

---

## Notes

[Any additional context from the source material — date, caveats, data quality notes]
```

---

## Phase 6 — Print summary

```
✅ Ecosystem map ingested — [Anchor/Sector]

   📁 Written to: Investing/Wiki/Reference/Ecosystem Maps/[filename]
   🔗 Tickers mapped: N across M tiers/categories
   ⚠️  New candidates (not in registry): [TICKER list]

   Tier breakdown:
   • Tier 1 — [Label]: N tickers
   • Tier 2 — [Label]: N tickers
   ...

   Run /daily-dashboard to see the ecosystem diagram in the KB visualization.
   Run /add-ticker TICKER to onboard new candidates.
```

---

## Rules

- **Never overwrite existing ecosystem map content** — append new sections with dates if the file exists
- **Mark uncertain ticker resolutions** with `?` in the Notes column rather than guessing silently
- **Preserve source attribution** — always note where the data came from (image filename, date, description)
- **No hallucination** — if a relationship is ambiguous in the source, note the ambiguity rather than inventing a direction
- **Sector cross-links** — if companies span multiple sectors (e.g., a semiconductor in the Clean Energy ecosystem), note their primary sector in parentheses: `TSM (Semiconductors)`
