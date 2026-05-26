# Daily Dashboard — Ecosystem Map Viewer

Generates a self-contained interactive HTML visualization of the D1→D5 sector ecosystem — supply chain tiers, cross-sector dependencies, and chokepoint analysis — then deploys to the `gh-pages` branch.

**Dashboard URL:** `https://investing-wiki.netlify.app`
*Netlify watches the `gh-pages` branch — every push auto-deploys within ~30 seconds.*
*Cloudflare Access gates the URL — only your email can log in.*

**Input flags:**
- *(none)* — generate and push to gh-pages
- `--no-push` — generate HTML locally only, skip deployment
- `--date YYYY-MM-DD` — stamp the output with a specific date

**Token budget: 12 file reads total. Do not read ticker pages, watchlist, news digest, or sentiment.**

---

## Phase 1 — Read Dimension Map (1 read)

Read `Investing/Wiki/Reference/Dimension Map.md`.

Parse the Sector Registry table → for each row extract:
- `name` — display name (e.g., "Compute Infrastructure")
- `dimension` — D1/D2/D3/D4/D5
- `folder` — actual folder slug (may differ from display name; if a "Folder" column exists use it, else derive from display name)
- `status` — complete/partial/planned

**Folder slug mapping** (apply when no explicit folder column):
| Display Name | Folder |
|---|---|
| Compute Infrastructure | AI Infrastructure |
| Energy & Power | Clean Energy |
| Materials & Mining | Metals & Mining |
| Space & Communications | Space & Comms |
| Fintech & Commerce AI | Fintech & E-Commerce |
| All others | same as display name |

Skip sectors with status `planned`.

Store as `sectors[]` ordered by dimension (D1 first, D5 last).

---

## Phase 2 — Read supply chain maps + interrelationships (parallel, 11 reads)

Run ALL of these reads in parallel.

### 2A — Supply Chain Maps (10 reads, one per active sector)

For each sector with status ≠ `planned`, read:
`Investing/Wiki/Sectors/[folder]/_Supply Chain Map.md`

Parse the **Value Chain table** under `## Value Chain`. The table has 8 columns:
`Tier | Function | Processes | Key Products / Materials | Chokepoint | Capital Intensity | Moat Type | Margin Profile`

For each row extract:
```
{
  tier: col[0],
  function: col[1],
  processes: col[2],          // may be long — keep full text
  key_products: col[3],       // may be long — keep full text
  chokepoint: col[4],         // "Y", "Partial", or "No"
  capital_intensity: col[5],
  moat_type: col[6],
  margin_profile: col[7]
}
```

Skip header row and separator rows (lines starting with `|---`).

Also check for a `## Publicly-Traded Nodes` table or `<!-- CANDIDATE ... -->` HTML comments. Extract any `{ tier, ticker, company }` mappings found. This is optional — if absent, leave nodes empty.

Store as `supply_chains[sector_name] = { tiers: [...], nodes: [...] }`. If file missing, store `{ tiers: [], nodes: [] }`.

### 2B — Ecosystem Interrelationships (1 read)

Read `Investing/Wiki/Reference/Ecosystem Interrelationships.md`.

Parse the **Dependency Graph table** under `## Dependency Graph`. The table has 8 columns:
`From Sector | From Tier | To Sector | To Tier | Flow Type | Product / Process | Chokepoint? | Notes`

For each row extract:
```
{
  from: col[0],
  from_tier: col[1],
  to: col[2],
  to_tier: col[3],
  flow: col[4],         // "Material", "Component", "Service", "Signal", "Process"
  product: col[5],
  chokepoint: col[6],   // "Yes", "Y", "Partial", or "No"
  notes: col[7]
}
```

Skip header rows, separator rows, and section headings (lines not starting with `|`).
Normalize chokepoint: treat "Yes" and "Y" as "Y".

Store as `edges[]` (flat array).

---

## Phase 3 — Assemble data model

Build the JS data object to embed in the HTML:

```javascript
const DATA = {
  generated: "YYYY-MM-DD",   // today or --date arg
  sectors: [
    {
      slug: "semiconductors",         // kebab-case of display name
      name: "Semiconductors",
      dimension: "D1",
      tiers: [                        // from supply_chains
        { tier, function, processes, key_products, chokepoint,
          capital_intensity, moat_type, margin_profile }
      ],
      nodes: [{ tier, ticker, company }]  // may be empty
    }
  ],
  edges: [
    { from, from_tier, to, to_tier, flow, product, chokepoint, notes }
  ]
};
```

Dimension order for rendering: D1 → D2 → D3 → D4 → D5.

---

## Phase 4 — Generate HTML

Write a **complete self-contained HTML file**. All CSS and JS inline. No CDN links. Must work at `file://` and on GitHub Pages. The design is ecosystem-mapping only — no portfolio, ticker, or sentiment data.

### Scope

- **Layer 0 (Global):** D1→D5 SVG node graph with animated bezier edges. All 10 sector nodes positioned in 5 dimension rows. Edges colored by flow type, weight by chokepoint severity. Filter bar at top.
- **Layer 1 (Sector):** Click a node → right panel shows sector description + clickable tier list + outbound/inbound edge cards. On mobile: bottom sheet slides up.
- **Layer 2 (Tier):** Click a tier card → right panel shows tier detail (function, moat type, capital intensity, margin profile, cross-sector edges mapped to this tier). Breadcrumb navigates back.

### Design system

```
--bg:#0d1117  --bg2:#161b22  --bg3:#21262d
--text:#e6edf3  --muted:#8b949e  --border:#30363d
--amber:#d4a017  --green:#3fb950  --blue:#58a6ff
--orange:#e3812b  --purple:#bc8cff  --pink:#ff7b72
```

Dimension colors: D1=purple, D2=blue, D3=green, D4=amber, D5=pink.
Flow badge colors: Material=orange, Component=blue, Service=green, Signal=purple, Process=amber.
Chokepoint Y = amber badge `⬥ CHOKEPOINT`. Partial = muted amber `⬥ PARTIAL`.

### Shell layout

```
#app (flex-column, height:100vh)
  header#hdr (48px, sticky) — logo + horizontal-scroll filter bar
  div#main (flex-row, flex:1, overflow:hidden)
    div#gp  (50% width, overflow:auto) — SVG graph
    div#dp  (flex:1, overflow-y:auto) — detail panel
```

Mobile (`max-width:768px`): `#gp` takes 100% width; `#dp` is `position:fixed; bottom:0; height:72vh; border-radius:14px 14px 0 0; transform:translateY(100%); transition:.3s`. Adding class `.open` slides it into view. Add `::before` drag handle (36×4px `--border` pill, `margin:10px auto`).

### SVG graph — `buildGraph()`

Compute node positions:
```
NODE_H = 78, ROW_H = 140, PAD_X = 16, PAD_Y = 38, GAP_X = 10
For each dimension row (D1..D5):
  row = sectors where dimension === dim.id
  nodeW = min(182, floor((panelWidth - 2*PAD_X - (row.length-1)*GAP_X) / row.length))
  totalW = row.length*nodeW + (row.length-1)*GAP_X
  startX = (panelWidth - totalW) / 2
  y = PAD_Y + dimIndex*ROW_H + 24   ← +24 for dim label above
  each sector: x = startX + i*(nodeW+GAP_X)
  store pos[slug] = {x, y, cx:x+nodeW/2, cy:y+NODE_H/2, nw:nodeW}
```

SVG total height = `PAD_Y + 5*ROW_H + NODE_H + 20`. Set `width` and `height` attributes on the SVG element so `#gp` scrolls if needed.

Dimension bands: for each dim, draw a `<rect>` spanning full width at that row's y position using the dim's bg color (low opacity), then a `<text>` label above in the dim's color.

Arrow markers in `<defs>`: one per flow type + one for chokepoint. `viewBox="0 0 10 6" refX="9" refY="3" markerWidth="7" markerHeight="5" orient="auto"` with a filled triangle `<path d="M0,0 L10,3 L0,6 Z"/>`.

Edge routing per edge `{from, to, flow, chokepoint}`:
- Resolve src/tgt sectors by name; look up `pos[slug]`
- Same dimension → route `right-center of source → left-center of target` with horizontal bezier arcing 40px above
- Source above target (sp.y < tp.y) → bottom-center of source to top-center of target, control points at 42% of dy
- Source below target → top-center of source to bottom-center of target

Edge styling: chokepoint Y → stroke `#d4a017`, width 2.5; otherwise flow color, width 1.5. Class `eco-edge anim` plus `slow` (Material) or `fast` (Signal) for animation speed.

CSS animation: `@keyframes flowFwd{to{stroke-dashoffset:-22}}`. Class `.anim{stroke-dasharray:6 4;animation:flowFwd 1.4s linear infinite}`.

Node SVG: `<g class="sector-node" data-slug="..." onclick="selSec('...')">`. Inside: `<rect class="node-bg" width="{nw}" height="78" rx="8" fill="#161b22" stroke="#30363d"/>`. Three `<text>` lines: name (font-size 12, font-weight 600, y≈26), dimension badge text (font-size 9, y≈44), edge count + ⬥ chokepoint count (font-size 9.5, muted, y≈60). For sector names longer than 14 chars, split at word boundary into two `<tspan>` lines.

### Node highlight states — `applyStates(slug, isSelected)`

For each `.sector-node`: classify as target / upstream (edges where `to===name`) / downstream (edges where `from===name`) / unrelated. Apply:
- Target + selected: `fill #21262d, stroke #d4a017, stroke-width 2`
- Upstream: `stroke #3fb950, stroke-width 1.5`
- Downstream: `stroke #58a6ff, stroke-width 1.5`
- Unrelated when selected: `opacity 0.12`

For each `.eco-edge`: `opacity 0.92` if `data-from===slug || data-to===slug`, else `0.07`.

On hover (mouseenter/mouseleave without selection), call same logic with `isSelected=false` — no fill change, just edge/opacity feedback.

### Filter logic — `applyFilter(f)`

For each `.eco-edge`: if `f==='Y'` show only `data-chk==='Y'`; if `f` is a flow type show only `data-flow===f`; otherwise show all. Set `style.display=''` or `'none'`.

### Sector detail — `renderSec(slug)` — writes into `#dp`

```
breadcrumb: [Ecosystem → slug.name]
dh: sector name (22px bold) + dim badge
dd: sector.description
sec: "Supply Chain — N Tiers"
  tier-list: one .tc card per tier
    .tc class: ck-Y (amber left border) or ck-P (partial)
    inside: .tc-body (name bold 13px + function 11px muted truncated) + ckBadge + › arrow
    onclick: selTier(slug, idx)
sec: "→ Outbound Flows (N)" — edge cards, filtered by activeF
sec: "← Inbound Flows (N)" — edge cards, filtered by activeF
```

Edge card: `.ec` div, flex-wrap. Contains: flow badge, sector name (clickable → `selSec`), ⬥Y if chokepoint, product text (full width, muted 11px).

### Tier detail — `selTier(sectorSlug, idx)` — writes into `#dp`

```
breadcrumb: [Ecosystem → sectorName → tier.tier]
dh: tier.tier (18px bold) + ckBadge
fn-text: tier.function (13px, 1.65 line-height)
meta-row: pills for moat_type, capital_intensity, margin_profile
sec: "Cross-Sector Flows Through This Tier"
  edge cards for DATA.edges where from_tier===tier.tier||to_tier===tier.tier
  direction arrow (→ or ←) prepended to sector name
```

### Navigation helpers

```javascript
function goHome() — clear selection, reset #dp to empty state, remove .open class
function bc(parts) — returns breadcrumb HTML; all but last item are <a onclick=...>
function nslug(name) — sector name → slug lookup
function sname(slug) — slug → name
function esc(s) — HTML-escape string
function flBadge(f) — flow badge span
function ckBadge(c) — chokepoint badge span
function dimBadge(d) — dimension badge span
function filt(edges) — filter edges array by activeF state
```

### DATA block

Assemble from Phase 3 output exactly matching this structure:
```javascript
const DATA = {
  generated: "[DATE]",
  sectors: [
    { slug, name, dimension, description,
      tiers: [{ tier, function, processes, key_products,
                chokepoint, capital_intensity, moat_type, margin_profile }] }
  ],
  edges: [
    { from, from_tier, to, to_tier, flow, product, chokepoint }
  ]
};
```

Slugs: lowercase display name, spaces and `&` → `-`, remove special chars (e.g. "Photonics & Optical" → "photonics-optical").
Chokepoint normalization: "Yes"/"Y" → "Y", "Partial" → "Partial", anything else → "No".

Embed `const DATA = {...};` as the first script block. All visualization JS follows.

### Init

```javascript
window.addEventListener('DOMContentLoaded', buildGraph);
let _rt;
window.addEventListener('resize', () => {
  clearTimeout(_rt);
  _rt = setTimeout(() => { buildGraph(); if (selSlug) applyStates(selSlug, true); }, 120);
});
```

---

## Phase 5 — Write and deploy

1. **Write** the complete HTML to `Investing/Output/Dashboard/index.html`
2. **Write** a dated copy to `Investing/Output/Dashboard/[DATE].html`
3. If `--no-push` flag is set, stop here.
4. Otherwise, deploy to `gh-pages`:
   ```bash
   git checkout gh-pages
   cp Investing/Output/Dashboard/index.html index.html
   git add index.html
   git commit -m "Deploy ecosystem map [DATE]"
   git push -u origin gh-pages
   git checkout master
   ```
5. Commit the dashboard files to `master` as well:
   ```bash
   git add Investing/Output/Dashboard/index.html Investing/Output/Dashboard/[DATE].html
   git commit -m "Dashboard: ecosystem map [DATE]"
   git push -u origin master
   ```
