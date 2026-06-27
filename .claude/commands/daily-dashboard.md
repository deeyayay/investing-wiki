# Daily Dashboard — AI Buildout Stack Viewer

Deploys the dashboard to GitHub Pages via `gh-pages`. The HTML lives in `Investing/Output/Dashboard/index.html`. It embeds these objects:
- **`STACKS`** — a registry of the three **domain stacks** the Supply Chain tab's domain switcher toggles between. `STACK` is a `let` pointer at the active one (defaults to `ai-buildout`). Each entry is `{label, stack}`:
  - `ai-buildout` — canonical 12-layer vertical map (Application → Critical Minerals) + 3 rails (Power / Thermal / Security) + Edge & Physical AI surface. Source: `Investing/Wiki/Reference/AI Buildout Stack.md`.
  - `robotics` — 7-layer humanoid framework (AI Brains → Energy & Rare Earth Materials), no rails. Source: `Investing/Wiki/Reference/Robotics Stack.md`.
  - `healthcare` — 6-layer first-cut Healthcare & Drug Discovery stack, no rails. Source: `Investing/Wiki/Reference/Healthcare & Drug Discovery Stack.md`.
- **`DATA`** — the per-sector tier/company backbone (`sectors`, `tech_races`, `watchlist`) used by the drill-down, ticker-wiki, and search. It is **shared across all three domains** — each stack sub-box maps to a `(sector, tier)` in `DATA.sectors` (or carries `chips` that degrade gracefully for not-yet-onboarded tickers).

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

Also read these files **in the same parallel batch** (alongside the existing Phase 1 reads):

**Watchlist** (`Investing/Wiki/Reference/Watchlist.md`):
- Parse ticker rows from the three category sections:
  - `## Core Holdings (Active Positions)` → category: `"Core Holdings"`, columns: Ticker | Name | Thesis Summary | Strategy | Score
  - `## High Upside Rockets (Speculative)` → category: `"Rockets"`, columns: Ticker | Notes | Score
  - `## Compounders Watchlist` → category: `"Compounders"`, columns: Ticker | Name | Notes | Score
- Stop parsing each section at the next `---` or `##` line
- Skip header rows and separator rows (cells starting with `---`)
- Extract: ticker, name (or blank), notes/thesis_summary, strategy, raw score (null if `—` or blank)

**Monitor Registry** (`Investing/Wiki/Reference/Monitor Registry.yaml`):
- For each watchlist ticker, look up: `sector`, `score`, `next_earnings`, `exchange`, `path`

**Per-ticker analysis.md** — for each watchlist ticker where `path` exists, read `{path}/analysis.md`:
- **One-line thesis** — paragraph(s) immediately following `## One-Line Thesis` (before the next `---` or `##`)
- **Scoring summary** — rows from the markdown table under `## Scoring Summary`:
  - Criterion rows: `| Product (Love Factor) | 5/5 | ...` → extract numeric value (left side of `/`)
  - Composite row: `| **Composite** | **9.5/10** | ...` → extract float
  - Map criteria names to keys: `product`, `pricing_power`, `leadership`, `financial_health`, `macro`, `future_potential`, `composite`
- **Catalyst timeline** — next 3 unchecked items: lines matching `- [ ]` under `## Catalyst Timeline` (skip `- [x]` checked items); strip the `- [ ] ` prefix

After reading, for each watchlist ticker, derive `tier` by scanning the assembled `DATA.sectors[].tiers[].companies[]` for a matching ticker symbol, and taking the parent `tier` name.

Assemble as `DATA.watchlist` — add this key alongside `sectors`, `edges`, `tech_races` in the DATA object. Entries that are missing an analysis.md (stub tickers, foreign-listed, not yet onboarded) still appear but with `thesis: ""`, `scoring: null`, `catalysts: null`.

**Target data shape for each watchlist entry:**
```javascript
{
  ticker: "NVDA",
  name: "NVIDIA Corporation",
  category: "Core Holdings",        // from Watchlist.md section
  strategy: "Long-term hold",        // from Watchlist.md Strategy column (or "")
  sector: "Compute Hardware",        // from Monitor Registry
  tier: "Chip Design (Fabless & IDM)", // derived from DATA.sectors scan
  exchange: "NASDAQ",                // from Monitor Registry
  next_earnings: "2026-08-20",       // from Monitor Registry (or null)
  score: 9.5,                        // Watchlist.md score overrides if set; else Monitor Registry
  thesis: "The dominant AI compute platform...", // from analysis.md One-Line Thesis
  scoring: {
    product: 5, pricing_power: 5, leadership: 4,
    financial_health: 5, macro: 5, future_potential: 5,
    composite: 9.5
  },
  catalysts: [
    "Blackwell / GB200 NVL72 rack demand updates",
    "Earnings — datacenter revenue growth rate (primary metric)",
    "Export control policy changes (China, Middle East)"
  ]
}
```

Run all reads in parallel.

**Three domain stack files** — read all three in the same parallel batch:
- `Investing/Wiki/Reference/AI Buildout Stack.md` → `ai-buildout` (label "AI Buildout")
- `Investing/Wiki/Reference/Robotics Stack.md` → `robotics` (label "Robotics")
- `Investing/Wiki/Reference/Healthcare & Drug Discovery Stack.md` → `healthcare` (label "Healthcare & Drug Discovery")

For each: parse the fenced ```json block and copy it **verbatim** into that domain's `stack` slot in the `const STACKS = {…}` registry in `index.html`. The JSON is valid JS — paste as-is. Notes that apply to the **AI Buildout** stack (canonical taxonomy):
- Sub-box **labels are canonical** (verbatim from the graphic) — never rename them to match a tier; instead wire the box to the closest `(slug, tier)`.
- A box with `"gap": true` is an intentional **coverage gap** (blueprint category the KB doesn't cover yet): it has **no** `slug`/`tier`, renders muted ("unmapped"), and is non-clickable. Leave it as a gap — do **not** invent a tier to fill it.
- A non-gap box's `slug` + `tier` must match a sector/tier in `DATA.sectors` (below) so the drill-down resolves. If a referenced tier is missing, fix the slug/tier in `AI Buildout Stack.md` — do not invent tiers.
- `"group"` on a box is a **visual tag** that clusters boxes into a labeled band within a layer (e.g. L07 Scale-Up/Out/Across/Components, L10 Lithography). It is *not* a drill-down level — preserve it.
- Rails carry `"flow"` (`in`/`out`/`wrap` → drives the "power in / heat out / wraps" badge) and an optional `"kind":"surface"` (Edge & Physical AI deployment surface). Each rail group holds a `"boxes"` array of individual sub-boxes — same `{label, slug, tier, chips, gap, choke}` shape as layer boxes — rendered as compact cards that drill into their KB tier (or render as `gap`). Do not collapse them back into a flat `items` list.
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
- Folder slug overrides: **none required** — sector folder names now match layer names directly (1:1). `SECTOR_FOLDER` is `{}`.

**Supply chain maps** — for each active sector read `Investing/Wiki/Sectors/[folder]/_Supply Chain Map.md`:
- From the `## Value Chain` table extract only: `tier` (col[0]), `chokepoint` (col[4])
- Normalize: "Yes" → "Y"; skip header/separator rows

**Ecosystem Interrelationships** (`Investing/Wiki/Reference/Ecosystem Interrelationships.md`):
- From `## Dependency Graph` extract: `from`, `from_tier`, `to`, `to_tier`, `flow`, `product`, `chokepoint`
- Keep only rows where `chokepoint === "Y"` (after normalizing "Yes" → "Y")
- Deduplicate by `(from, to)` sector pair — keep first occurrence

### Phase 2 — Update STACK + DATA in index.html

Read `Investing/Output/Dashboard/index.html`.

1. Locate the hardcoded `<span class="gen-date">Generated: YYYY-MM-DD</span>` in the HTML and replace the date with today's date (format: `YYYY-MM-DD`).
2. Locate `const STACKS=` and replace the entire object (through its matching closing `};` that precedes `let STACK=STACKS["ai-buildout"].stack;`) with the reassembled registry:
   ```js
   const STACKS={
   "ai-buildout":{"label":"AI Buildout","stack":<json from AI Buildout Stack.md>},
   "robotics":{"label":"Robotics","stack":<json from Robotics Stack.md>},
   "healthcare":{"label":"Healthcare & Drug Discovery","stack":<json from Healthcare & Drug Discovery Stack.md>}
   };
   let STACK=STACKS["ai-buildout"].stack;
   let currentDomain="ai-buildout";
   ```
   Paste each stack's JSON verbatim. Keep the `generated`/`intro` fields (the renderer reads `intro`, ignores `generated`). Do not strip `gap`/`group`/`flow`/`kind`/`items`/`rails` fields — the renderer relies on them; robotics and healthcare carry `rails:[]` (no rails) and an `intro` string, and `renderL0()` renders rail-less stacks as a single centered column. The domain switcher (`setDomain()` / `_domainSwitcher()`) and `let STACK`/`let currentDomain` declarations already exist in `index.html` — leave them intact.
3. Locate `const DATA = {` and replace the entire `DATA` object (through the matching closing `};`) with the newly assembled object:

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
  ],
  watchlist: [
    // One entry per row in Watchlist.md (Core Holdings / Rockets / Compounders sections).
    // Tickers not yet in Monitor Registry or without an analysis.md still appear;
    // set thesis:"", scoring:null, catalysts:null for those.
    { ticker: "NVDA", name: "NVIDIA Corporation", category: "Core Holdings",
      strategy: "Long-term hold", sector: "Compute Hardware",
      tier: "Chip Design (Fabless & IDM)", exchange: "NASDAQ",
      next_earnings: "2026-08-20", score: 9.5,
      thesis: "The dominant AI compute platform company...",
      scoring: { product:5, pricing_power:5, leadership:4, financial_health:5, macro:5, future_potential:5, composite:9.5 },
      catalysts: ["Blackwell / GB200 NVL72 rack demand updates", "..."] }
    // ... one entry per watchlist row
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
