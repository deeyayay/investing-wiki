---
description: Deploy and refresh the AI Buildout Stack dashboard — the visual, phone-friendly surface for the wiki. Renders the 12-layer vertical stack map, per-sector drill-downs, ticker pages, and the daily brief's digest (news, filings, themes, discovered names). Deploys to GitHub Pages. Usage: /dashboard [--refresh-data] [--stack-only]
allowed-tools: Bash(git:*), Bash(python3 scripts/check_registry.py:*), Read, Edit, Write, Glob, Grep
---

# Daily Dashboard — AI Buildout Stack Viewer

Deploys the dashboard to GitHub Pages via `gh-pages`. The HTML lives in `Investing/Output/Dashboard/index.html`. It embeds two objects:
- **`STACK`** — the canonical 12-layer vertical map (Application → Critical Minerals), mapped word-for-word from the *AI Buildout Supply Chain* blueprint graphic, wrapped by 3 cross-cutting rails (Power / Thermal / Security) + the Edge & Physical AI deployment surface, rendered as the homepage. Source of truth: the JSON block in `Investing/Wiki/Reference/AI Buildout Stack.md`.
- **`DATA`** — the per-sector tier/company backbone (`sectors`, `tech_races`) used by the drill-down, ticker-wiki, and search. Each `STACK` sub-box maps to a `(sector, tier)` in `DATA.sectors`.

**Dashboard URL:** `https://deeyayay.github.io/investing-wiki/`
*GitHub Pages watches `gh-pages` — every push auto-deploys within ~1 minute.*

## What this surfaces from the daily brief

The Watchlist tab fetches `Investing/Raw/Inbox/watchlist-refresh-digest.json` from `master` at
page load, so **a `/brief` push updates the deployed dashboard without redeploying the HTML.**
That is the whole delivery path — there is no separate digest destination.

The digest keys the tab renders:

| Key | Renders as |
|---|---|
| `tickers[].headlines[]` | per-ticker news list; `kind:"filing"` items are badged and linked to the SEC document, and sort above news |
| `topics[]` | the Themes section — `tickers` as chips, `gaps` as the unregistered names |
| `discovered[]` | untracked names matched in theme coverage, each with a `/track` command |
| `providers{}` | per-provider item counts in the banner; a provider with zero items raises a visible "digest is incomplete" warning |
| `drift_index{}` | the thesis-drift flag on every ticker card — `ticker -> drift status` for **every scanned ticker**, not just the ones with news, so the flag doesn't blink in and out with the news cycle |

### The Dig button

Every ticker card and the ticker drill-down carry a **Dig** button that copies
`/dig TICKER --score` to the clipboard, to paste into a Claude Code session.

**It copies rather than fires, and that is a constraint, not a shortcut.** The
dashboard is a static GitHub Pages document with no backend, and the Routines
API cannot be called from a browser: its `/fire` endpoint answers `OPTIONS` with
`405` and no `Access-Control-Allow-Origin`, so the preflight fails before the
POST is sent. Verified 2026-08-28. Firing directly would need either a proxy
holding the token server-side (a Cloudflare Worker will do) or a token embedded
in a public page, which is not an option.

The click handler prefers `navigator.clipboard` and falls back to a hidden
textarea plus `execCommand`, which is still the only path in some mobile
webviews; if both fail it prints the command for manual copying rather than
silently doing nothing.

### Thesis drift flags

Each ticker card carries a flag derived from its `**Drift status:**` line in `analysis.md`:

| Status head | Flag | Card accent |
|---|---|---|
| `On track, accelerating` / `strengthened` | ▲ Strengthening (green) | green rail |
| `On track` (incl. `evolving`) | ▶ On track (grey) | none |
| `New` | ● New (grey) | none |
| `Drifting` / `Material change` | ▼ Drifting (amber) | amber rail |
| `Broken` | ▼ Broken (red) | red rail |

Only the states that need attention get a card accent, so scanning the list surfaces
exactly the names that moved.

**This encodes drift, not price direction.** "On track" means the thesis is holding —
which is not the same as bullish, and would be actively wrong for a cautious or avoid
thesis. Classification reads the **status head only** (the text before the em dash),
because the explanation after it is prose: "On track — AI storage demand accelerating"
is on track, not strengthening.

**If you change the digest schema in `scripts/watchlist_refresh_fetch.py`, update the tab.**
The dashboard fails silently on a key it does not know — it renders nothing rather than erroring,
which is how a whole section can quietly disappear.

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
- Parse ticker rows from the four category sections (rebuilt 2026-08-23):
  - `## Core Holdings (Active Positions)` → `"Core Holdings"`, columns: Ticker | Name | Tier | Thesis Summary | Score
  - `## High Conviction` → `"High Conviction"`, columns: Ticker | Name | Sector | Score | One-Line Thesis
  - `## Drift Watch` → `"Drift Watch"`, columns: Ticker | Name | Score | Drift Status
  - `## Active Coverage` → `"Active Coverage"`, columns: Ticker | Name | Sector | Score | One-Line Thesis
- Core Holdings is owner-maintained and often empty — that is expected, not a parse failure.
  The other three are derived from each `analysis.md`, so they change as theses do.
- The pre-2026-08 sections (`Rockets`, `Compounders`, `Watching`) are still parsed by
  `index.html` for backwards compatibility, but are no longer written.
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

**AI Buildout Stack** (`Investing/Wiki/Reference/AI Buildout Stack.md`) — **canonical taxonomy**:
- Parse the fenced ```json block. Copy it verbatim into the `const STACK = …` assignment in `index.html` (layers, connectors, rails). The JSON is valid JS — paste it as-is.
- Sub-box **labels are canonical** (verbatim from the graphic) — never rename them to match a tier; instead wire the box to the closest `(slug, tier)`.
- A box with `"gap": true` is an intentional **coverage gap** (blueprint category the KB doesn't cover yet): it has **no** `slug`/`tier`, renders muted ("unmapped"), and is non-clickable. Leave it as a gap — do **not** invent a tier to fill it.
- A non-gap box's `slug` + `tier` must match a sector/tier in `DATA.sectors` (below) so the drill-down resolves. If a referenced tier is missing, fix the slug/tier in `AI Buildout Stack.md` — do not invent tiers.
- `"group"` on a box is a **visual tag** that clusters boxes into a labeled band within a layer (e.g. L07 Scale-Up/Out/Across/Components, L10 Lithography). It is *not* a drill-down level — preserve it.
- Rails carry `"flow"` (`in`/`out`/`wrap` → drives the "power in / heat out / wraps" badge) and an optional `"kind":"surface"` (Edge & Physical AI deployment surface). Each rail group holds a `"boxes"` array of individual sub-boxes — same `{label, slug, tier, chips, gap, choke}` shape as layer boxes — rendered as compact cards that drill into their KB tier (or render as `gap`). Do not collapse them back into a flat `items` list.
- `chips[]` are ticker symbols; they need not all be onboarded (candidates render and degrade gracefully to a "run /track" notice).

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
2. Locate `const STACK=` and replace the entire object (through its matching closing `};`) with the JSON block from `AI Buildout Stack.md` (the JSON is JS-compatible — paste as `const STACK=<json>;`). Keep the `generated` field; the render code ignores it. Do not strip `gap`/`group`/`flow`/`kind`/`items` fields — the renderer relies on them.
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
    // One entry per row in Watchlist.md (Core Holdings / High Conviction / Drift Watch / Active Coverage).
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
