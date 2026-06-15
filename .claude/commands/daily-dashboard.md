# Daily Dashboard — AI Buildout Stack Viewer

Deploys the dashboard to GitHub Pages via `gh-pages`. The HTML lives in `Investing/Output/Dashboard/index.html`. It embeds two objects:
- **`STACK`** — the canonical 12-layer vertical map (Application → Critical Minerals), mapped word-for-word from the *AI Buildout Supply Chain* blueprint graphic, wrapped by 3 cross-cutting rails (Power / Thermal / Security) + the Edge & Physical AI deployment surface, rendered as the homepage. Source of truth: the JSON block in `Investing/Wiki/Reference/AI Buildout Stack.md`.
- **`DATA`** — the per-sector tier/company backbone (`sectors`, `tech_races`) used by the drill-down, ticker-wiki, and search. Each `STACK` sub-box maps to a `(sector, tier)` in `DATA.sectors`.

**Dashboard URL:** `https://deeyayay.github.io/investing-wiki/`
*GitHub Pages watches `gh-pages` — every push auto-deploys within ~1 minute.*

**Flags:**
- *(none)* — deploy existing `index.html` to gh-pages as-is
- `--refresh-data` — re-read source files, update the `DATA` block in `index.html`, then deploy
- `--no-push` — write changes locally only, skip deployment

---

## Default path (no flags)

Run the deploy steps in Phase 3. No file reads needed.

---

## `--refresh-data` path

### Phase 1 — Read source files (parallel, up to 12 reads)

Run all reads in parallel.

**AI Buildout Stack** (`Investing/Wiki/Reference/AI Buildout Stack.md`) — **canonical taxonomy**:
- Parse the fenced ```json block. Copy it verbatim into the `const STACK = …` assignment in `index.html` (layers, connectors, rails). The JSON is valid JS — paste it as-is.
- Sub-box **labels are canonical** (verbatim from the graphic) — never rename them to match a tier; instead wire the box to the closest `(slug, tier)`.
- A box with `"gap": true` is an intentional **coverage gap** (blueprint category the KB doesn't cover yet): it has **no** `slug`/`tier`, renders muted ("unmapped"), and is non-clickable. Leave it as a gap — do **not** invent a tier to fill it.
- A non-gap box's `slug` + `tier` must match a sector/tier in `DATA.sectors` (below) so the drill-down resolves. If a referenced tier is missing, fix the slug/tier in `AI Buildout Stack.md` — do not invent tiers.
- `"group"` on a box is a **visual tag** that clusters boxes into a labeled band within a layer (e.g. L07 Scale-Up/Out/Across/Components, L10 Lithography). It is *not* a drill-down level — preserve it.
- Rails carry `"flow"` (`in`/`out`/`wrap` → drives the "power in / heat out / wraps" badge), an optional `"kind":"surface"` (Edge & Physical AI deployment surface), and per-group `"items"` (verbatim component lists) alongside `chips[]`.
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
- Add `tech_races: [...]` to the DATA object alongside `sectors` and `edges`

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

### Phase 2 — Update STACK + DATA in index.html

Read `Investing/Output/Dashboard/index.html`.

1. Locate `const STACK=` and replace the entire object (through its matching closing `};`) with the JSON block from `AI Buildout Stack.md` (the JSON is JS-compatible — paste as `const STACK=<json>;`). Keep the `generated` field; the render code ignores it. Do not strip `gap`/`group`/`flow`/`kind`/`items` fields — the renderer relies on them.
2. Locate `const DATA = {` and replace the entire `DATA` object (through the matching closing `};`) with the newly assembled object:

```javascript
const DATA = {
  generated: "YYYY-MM-DD",
  sectors: [
    { slug: "semiconductors", name: "Semiconductors", dimension: "D1",
      tiers: [
        { tier: "Silicon Wafer Production", chokepoint: "Y" },
        // ...
      ]
    },
    // one entry per active sector, D1→D5 order
  ],
  edges: [
    { from: "Materials & Mining", from_tier: "Silicon Refining",
      to: "Semiconductors", to_tier: "Wafer Production",
      flow: "Material", product: "Polysilicon → silicon wafer", chokepoint: "Y" },
    // ~12 Y-chokepoint edges
  ],
  tech_races: [
    { id: "nand-vs-hbm4", name: "NAND vs. HBM4", sector_group: "AI Ecosystem",
      preference: "NAND over HBM4 for the agentic AI demand wave",
      conviction: "High", last_validated: "YYYY-MM-DD", status: "Active",
      tickers: [
        { ticker: "SNDK", technology: "NAND Flash", exposure: "Primary", weighting: "Overweight vs. memory peers" }
        // ... one entry per row in the Ticker Exposure Map table
      ],
      application_driver: "...",  // paragraph text from Application-Layer Driver section
      consensus_gap: [["Market belief", "Reality"], ...],  // rows from table
      bull_case: ["bullet 1", "bullet 2", ...],
      bear_risk: ["bullet 1", "bullet 2", ...]
    }
    // ... one entry per ### Race block in Technology Preferences.md
  ]
};
```

Slug format: lowercase, spaces and `&` → `-`, strip non-alphanumeric. E.g. `"Photonics & Optical"` → `"photonics-optical"`.

Write the updated file back to `Investing/Output/Dashboard/index.html` and copy to `Investing/Output/Dashboard/[DATE].html`.

---

## Phase 3 — Deploy to gh-pages

```bash
git fetch origin gh-pages
git checkout gh-pages
git show [CURRENT_BRANCH]:Investing/Output/Dashboard/index.html > index.html
git add index.html
git commit -m "Deploy ecosystem map [DATE]"
git push -u origin gh-pages
git checkout [CURRENT_BRANCH]
```

If `--no-push` is set, stop before these steps.
