# Daily Dashboard — AI Buildout Stack Viewer

Deploys the dashboard to GitHub Pages via `gh-pages`. The HTML lives in `Investing/Output/Dashboard/index.html`. It loads two companion JSON files at runtime:
- **`data.json`** — the per-sector tier/company backbone (`sectors`, `edges`, `tech_races`) + the canonical 12-layer STACK (`stack.layers`, `stack.rails`). Updated by `--refresh-data`.
- **`scores.json`** — per-ticker scoring API (`fundamental`, `advisory` namespaces). Updated by `--refresh-scores`.

**Dashboard URL:** `https://deeyayay.github.io/investing-wiki/`
*GitHub Pages watches `gh-pages` — every push auto-deploys within ~1 minute.*

**Flags:**
- *(none)* — deploy existing `index.html` + `data.json` + `scores.json` to gh-pages as-is
- `--refresh-data` — re-read structural source files, write `data.json`, then deploy (~15K tokens)
- `--refresh-scores` — re-read Monitor Registry + scored analysis.md files, write `scores.json`, then deploy (~8–12K tokens)
- `--no-push` — write changes locally only, skip deployment

---

## Default path (no flags)

Run the deploy steps in Phase 3. No file reads needed.

---

## `--refresh-data` path

### Phase 1 — Read source files (parallel, up to 12 reads)

Run all reads in parallel.

**AI Buildout Stack** (`Investing/Wiki/Reference/AI Buildout Stack.md`) — **canonical taxonomy**:
- Parse the fenced ```json block. This is the `stack` key in `data.json` (layers + rails + connectors).
- Each sub-box's `slug` + `tier` must match a sector/tier in `data.json`'s `sectors` array so the drill-down resolves. If a referenced tier is missing, fix the slug/tier in `AI Buildout Stack.md` — do not invent tiers.
- `chips[]` are ticker symbols; they need not all be onboarded (candidates render and degrade gracefully to a "run /add-ticker" notice).

**Technology Preferences** (`Investing/Wiki/Reference/Technology Preferences.md`):
- Find all `## Sector Group: [Name]` headings → track `current_group`
- Within each group, find all `### Race N — ` entries → one race object per entry
- From each race block, extract:
  - `name` — text after the dash in the `### Race N — [Name]: ...` heading
  - `preference` — text after `**Preference:**`
  - `conviction` — text after `**Conviction:**` (High / Medium / Low / Watch)
  - `last_validated` — text after `**Last validated:**`
  - `status` — text after `**Status:**` (Active / Resolved)
  - `tickers[]` — rows from the `#### Ticker Exposure Map` markdown table: `{ ticker, technology, exposure, weighting }`
  - `application_driver` — paragraph(s) below `#### Application-Layer Driver` (plain text, not table headers)
  - `consensus_gap` — rows from the table below `#### Consensus vs. Reality Gap` as `[[belief, reality], ...]`
  - `bull_case` — bullet items below `#### Bull Case` as `["...", ...]`
  - `bear_risk` — bullet items below `#### Bear / Risk` as `["...", ...]`
- Add `tech_races: [...]` to the data.json object alongside `sectors` and `edges`

**Dimension Map** (`Investing/Wiki/Reference/Dimension Map.md`):
- Extract: `name`, `dimension` (D1–D5), `folder` slug, `status`
- Skip sectors where `status === "planned"`
- Folder slug overrides: Compute Infrastructure → `AI Infrastructure`, Energy & Power → `Clean Energy`, Materials & Mining → `Metals & Mining`, Space & Communications → `Space & Comms`, Fintech & Commerce AI → `Fintech & E-Commerce`

**Supply chain maps** — for each active sector read `Investing/Wiki/Sectors/[folder]/_Supply Chain Map.md`:
- From the `## Value Chain` table extract only: `tier` (col[0]), `chokepoint` (col[4])
- Normalize: "Yes" → "Y"; skip header/separator rows

**Ecosystem Interrelationships** (`Investing/Wiki/Reference/Ecosystem Interrelationships.md`):
- From `## Dependency Graph` extract: `from`, `from_tier`, `to`, `to_tier`, `flow`, `product`, `chokepoint`
- Keep only rows where `chokepoint === "Y"` (after normalizing "Yes" → "Y")
- Deduplicate by `(from, to)` sector pair — keep first occurrence

### Phase 2 — Write data.json

Assemble the data object and write to `Investing/Output/Dashboard/data.json`:

```json
{
  "generated": "YYYY-MM-DD",
  "sectors": [
    { "slug": "semiconductors", "name": "Semiconductors", "dimension": "D1",
      "tiers": [
        { "tier": "Silicon Wafer Production", "chokepoint": "Y", "companies": [...] }
      ]
    }
  ],
  "edges": [
    { "from": "Materials & Mining", "from_tier": "Silicon Refining",
      "to": "Semiconductors", "to_tier": "Wafer Production",
      "flow": "Material", "product": "Polysilicon → silicon wafer", "chokepoint": "Y" }
  ],
  "tech_races": [
    { "id": "nand-vs-hbm4", "name": "NAND vs. HBM4", "sector_group": "AI Ecosystem",
      "preference": "...", "conviction": "High", "last_validated": "YYYY-MM-DD",
      "status": "Active", "tickers": [...], "application_driver": "...",
      "consensus_gap": [...], "bull_case": [...], "bear_risk": [...] }
  ],
  "stack": {
    "layers": [...],
    "rails": [...],
    "connectors": [...]
  }
}
```

Slug format: lowercase, spaces and `&` → `-`, strip non-alphanumeric. E.g. `"Photonics & Optical"` → `"photonics-optical"`.

Also copy to `Investing/Output/Dashboard/[DATE]-data.json` for archival.

Do **not** modify `index.html` — it is a static shell that fetches `data.json` at runtime.

---

## `--refresh-scores` path

Token-efficient scoring update (~8–12K tokens). Reads Monitor Registry + scored analysis.md files only. Does **not** read structural source files.

### Phase 1 — Read sources (parallel)

1. `Investing/Wiki/Reference/Monitor Registry.yaml` — all active tickers + their `score`, `path`, `sector`, `next_earnings`
2. For each ticker where `score` is not null: read `[path]/analysis.md` and extract:
   - `## Scoring Summary` table → per-criterion scores (P, PP, L, FH, ME, FP), composite, label
   - `## One-Line Thesis` → `one_line_thesis`
   - `## Analyst Coverage` → current price, analyst PT, upside %, valuation label
   - `## Catalyst Timeline` → next 1–2 bullet items as `near_term_catalysts[]`
   - Check `score_history` in facts.md YAML if available

For legacy single-file tickers (no three-layer structure), read `[TICKER].md` instead of `analysis.md`.

### Phase 2 — Build scores.json

Assemble using the schema in `scores.json` (schema_version "1"). Derive `dominance` automatically:
- 1 company in tier → `"Monopoly"`
- 2 companies in tier → `"Duopoly"`
- 3+ companies with notes containing "only company", "dominant", "largest", "#1", "leads", "monopoly" → `"Leader"`
- 3+ otherwise → `"Contested"`

Set `growth_flag: true` when `criteria.future_potential >= 4`.

Write to `Investing/Output/Dashboard/scores.json`. Do **not** modify `index.html` or `data.json`.

---

## Phase 3 — Deploy to gh-pages

```bash
BRANCH=$(git rev-parse --abbrev-ref HEAD)
git fetch origin gh-pages
git checkout gh-pages
git show $BRANCH:Investing/Output/Dashboard/index.html > index.html
git show $BRANCH:Investing/Output/Dashboard/data.json > data.json
git show $BRANCH:Investing/Output/Dashboard/scores.json > scores.json
git add index.html data.json scores.json
git commit -m "Deploy ecosystem map [DATE]"
git push -u origin gh-pages
git checkout $BRANCH
```

If `--no-push` is set, stop before these steps.
