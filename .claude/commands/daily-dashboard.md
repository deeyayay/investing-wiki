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

Parse the **Value Chain table** under `## Value Chain`.

For each row extract only:
```
{
  tier: col[0],        // tier name
  chokepoint: col[4],  // "Y", "Partial", or "No" — normalize "Yes" to "Y"
}
```

Skip header row and separator rows (lines starting with `|---`).

Store as `supply_chains[sector_name] = { tiers: [...] }`. If file missing, store `{ tiers: [] }`.

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

**Keep only edges where chokepoint === "Y"** after normalization. Discard all Partial and No edges.
Deduplicate edges with the same (from, to) sector pair — keep only the first occurrence.

Store as `edges[]` (flat array, typically 10–15 entries).

---

## Phase 3 — Assemble data model

Build the JS data object to embed in the HTML:

```javascript
const DATA = {
  generated: "YYYY-MM-DD",   // today or --date arg
  sectors: [
    {
      slug: "semiconductors",   // kebab-case of display name
      name: "Semiconductors",
      dimension: "D1",
      tiers: [
        { tier: "Silicon Wafer Production", chokepoint: "Y" },
        // one entry per tier, only tier name + chokepoint
      ]
    }
    // one entry per active sector, D1→D5 order
  ],
  // Only Y-chokepoint cross-sector edges, deduplicated by (from, to) pair
  edges: [
    { from, from_tier, to, to_tier, flow, product, chokepoint: "Y" }
  ]
};
```

Dimension order for rendering: D1 → D2 → D3 → D4 → D5.

---

## Phase 4 — Generate HTML

Write a complete self-contained HTML file. All CSS and JS inline. No CDN links. Must work at `file://` and on GitHub Pages.

### Design system

```css
:root {
  --bg: #ffffff; --bg2: #f6f8fa; --bg3: #eaeef2;
  --text: #1f2328; --muted: #57606a; --border: #d0d7de;
  --amber: #9a6700; --green: #1a7f37; --blue: #0969da;
  --red: #cf222e; --orange: #bc4c00; --purple: #8250df;
  --pink: #e4525b;
}
```

Dimension colors (for labels and card accents):
- D1 → `--purple`
- D2 → `--blue`
- D3 → `--green`
- D4 → `--amber`
- D5 → `--pink`

Flow type badge colors:
- Material → `--orange`
- Component → `--blue`
- Service → `--green`
- Signal → `--purple`
- Process → `--amber`

Chokepoint badge colors:
- Y → `--amber` background, white text, bold `⬥`
- Partial → `#fff3c4` background, `--amber` text
- No → `--bg3`, `--muted` text

### Layout

```html
<body>
  <header id="hdr">...</header>
  <div id="layout">
    <div id="stack-panel">     <!-- left, ~45% width -->
      <svg id="edge-svg"></svg>  <!-- absolute overlay -->
      <div id="stack">...</div>  <!-- D1..D5 rows -->
    </div>
    <div id="detail-panel">   <!-- right, ~55% width -->
      ...
    </div>
  </div>
</body>
```

CSS for layout:
```css
#layout {
  display: flex;
  height: calc(100vh - 48px);
  overflow: hidden;
}
#stack-panel {
  width: 45%;
  min-width: 320px;
  position: relative;
  overflow-y: auto;
  border-right: 1px solid var(--border);
  padding: 16px;
}
#edge-svg {
  position: absolute;
  top: 0; left: 0;
  width: 100%; height: 100%;
  pointer-events: none;
  z-index: 10;
}
#detail-panel {
  flex: 1;
  overflow-y: auto;
  padding: 20px;
}
```

**Mobile** (`max-width: 768px`): stack layout becomes column, `#stack-panel` takes full width, `#detail-panel` slides up from bottom as a fixed drawer (transforms from `translateY(100%)` to `translateY(0)` when a sector is selected).

### Header

Filter buttons allow narrowing the 12 Y-chokepoint edges by flow type. Since all stored edges are
Y-chokepoints, there is no separate "⬥ Chokepoints only" button — all shown edges are already
chokepoints.

```html
<header id="hdr">
  <span class="site-title">ECOSYSTEM MAP · [DATE]</span>
  <div class="filters">
    <button class="filter-btn active" data-filter="all">All flows</button>
    <button class="filter-btn" data-filter="Material">Material</button>
    <button class="filter-btn" data-filter="Component">Component</button>
    <button class="filter-btn" data-filter="Service">Service</button>
    <button id="reset-btn">Reset</button>
  </div>
</header>
```

### Stack panel — D1→D5 rows

For each dimension D1..D5, render a row:
```html
<div class="dim-row" data-dim="D1">
  <div class="dim-label d1-color">D1 · AI Manufacturing Base</div>
  <div class="dim-sectors">
    <div class="sector-card" data-slug="semiconductors" data-dim="D1">
      <div class="card-name">Semiconductors</div>
      <div class="card-meta">
        <span class="dim-badge d1">D1</span>
        <span class="choke-count" title="Y-chokepoint edges sourced here">⬥3</span>
        <span class="edge-count">8 edges</span>
      </div>
    </div>
    ...
  </div>
</div>
```

Dimension label text:
- D1 → "D1 · AI Manufacturing Base"
- D2 → "D2 · AI Connectivity"
- D3 → "D3 · AI Infrastructure"
- D4 → "D4 · AI Enablement"
- D5 → "D5 · AI Applications"

Chokepoint count = number of edges where `from === sector.name && edge.chokepoint === "Y"`.
Edge count = total edges where `from === sector.name || to === sector.name`.

### SVG edge drawing (desktop only)

On mobile (`max-width: 768px`) the `#edge-svg` is `display:none`. SVG drawing only runs on desktop.

Two arrowhead markers — blue (outbound from selected) and green (inbound to selected):
```svg
<defs>
  <marker id="arr-blue" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
    <path d="M0,0 L8,4 L0,8 Z" fill="#0969da"/>
  </marker>
  <marker id="arr-green" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
    <path d="M0,0 L8,4 L0,8 Z" fill="#1a7f37"/>
  </marker>
</defs>
```

**`drawEdges(slug, filter)`:**
1. Return immediately if `window.innerWidth <= 768`
2. Clear SVG paths (preserve `<defs>`)
3. Filter `DATA.edges` to those where `from === sector.name || to === sector.name`
4. If `filter !== 'all'`, further filter by `edge.flow === filter`
5. For each edge, compute bounding rects of source/target cards relative to `#stack-panel`:
   - `sx = srcCard.getBoundingClientRect().right - panelRect.left`
   - `sy = srcCard vertical center - panelRect.top + panel.scrollTop`
   - `tx = tgtCard.getBoundingClientRect().left - panelRect.left`
   - `ty = tgtCard vertical center - panelRect.top + panel.scrollTop`
   - `cx = sx + (tx-sx)*0.5` (single midpoint control)
6. Draw `<path d="M sx,sy C cx,sy cx,ty tx,ty">` — cubic bezier
   - Outbound (from === selected): stroke `#0969da`, marker `arr-blue`
   - Inbound (to === selected): stroke `#1a7f37`, marker `arr-green`
   - stroke-width 2, opacity 0.8
7. On `window resize`, redraw if a sector is selected

Convert display name to slug: lowercase, replace `&` → `-`, spaces → `-`, strip non-alphanumeric.
E.g., "Photonics & Optical" → `"photonics-optical"`.

### Sector card interaction

```javascript
document.querySelectorAll('.sector-card').forEach(card => {
  card.addEventListener('click', () => {
    const slug = card.dataset.slug;
    selectSector(slug);
  });
});

function selectSector(slug) {
  currentSelected = slug;
  // Update card visual states
  document.querySelectorAll('.sector-card').forEach(c => {
    const s = c.dataset.slug;
    const sectorName = DATA.sectors.find(x => x.slug === s)?.name;
    const isSelected = s === slug;
    const selectedName = DATA.sectors.find(x => x.slug === slug)?.name;
    const connectedEdges = DATA.edges.filter(e =>
      (e.from === selectedName && e.to === sectorName) ||
      (e.to === selectedName && e.from === sectorName)
    );
    const isDownstream = connectedEdges.some(e => e.from === selectedName);
    const isUpstream = connectedEdges.some(e => e.to === selectedName);
    
    c.classList.toggle('selected', isSelected);
    c.classList.toggle('upstream', !isSelected && isUpstream);
    c.classList.toggle('downstream', !isSelected && isDownstream);
    c.classList.toggle('dimmed', !isSelected && !isUpstream && !isDownstream);
  });
  // Draw SVG edges (dispatches to mobile or desktop path)
  drawEdges(slug, activeFilter);
  // Render detail panel
  renderDetail(slug);
  // Mobile: show drawer + lock body scroll
  if (window.innerWidth <= 768) {
    document.getElementById('detail-panel').classList.add('open');
    document.body.classList.add('drawer-open');
  }
}
```

CSS for card states:
```css
.sector-card { transition: opacity .2s, box-shadow .2s; }
.sector-card.selected { border-left: 3px solid var(--amber); background: var(--bg3); }
.sector-card.upstream { box-shadow: 0 0 0 2px var(--green); }
.sector-card.downstream { box-shadow: 0 0 0 2px var(--blue); }
.sector-card.dimmed { opacity: 0.2; }
```

### Detail panel rendering

Tier table shows only Tier name + Choke badge (2 columns). No tooltip. No accordion. No extra data attributes.

```javascript
function renderDetail(slug) {
  const sector = DATA.sectors.find(s => s.slug === slug);
  const outbound = DATA.edges.filter(e => e.from === sector.name);
  const inbound  = DATA.edges.filter(e => e.to === sector.name);
  const applyFilter = arr => activeFilter === 'all' ? arr : arr.filter(e => e.flow === activeFilter);

  const tierRows = sector.tiers.map(t => `<tr>
    <td class="tier-name">${esc(t.tier)}</td>
    <td>${chokeBadge(t.chokepoint)}</td>
  </tr>`).join('');

  const fOut = applyFilter(outbound);
  const fIn  = applyFilter(inbound);

  document.getElementById('detail-panel').innerHTML = `
    <div class="detail-header">
      <div style="display:flex;align-items:center;gap:8px;flex:1">
        <h2>${esc(sector.name)}</h2>
        <span class="dim-badge dim-${sector.dimension.toLowerCase()}">${sector.dimension}</span>
      </div>
      <button class="close-drawer" onclick="closeDrawer()">✕</button>
    </div>
    <div class="detail-section">
      <div class="section-title">Supply Chain Tiers (${sector.tiers.length})</div>
      <table class="tier-table">
        <thead><tr><th>Tier</th><th>Choke</th></tr></thead>
        <tbody>${tierRows}</tbody>
      </table>
    </div>
    <div class="detail-section">
      <div class="section-title">→ Outbound chokepoint flows (${fOut.length})</div>
      <div class="edge-list">${fOut.map(e => edgeCard(e,'out')).join('') || '<p class="muted">None for this filter.</p>'}</div>
    </div>
    <div class="detail-section">
      <div class="section-title">← Inbound chokepoint flows (${fIn.length})</div>
      <div class="edge-list">${fIn.map(e => edgeCard(e,'in')).join('') || '<p class="muted">None for this filter.</p>'}</div>
    </div>`;

  document.querySelectorAll('.edge-sector-chip').forEach(chip => {
    chip.addEventListener('click', () => selectSector(chip.dataset.slug));
  });
}

function edgeCard(edge, dir) {
  const otherName = dir === 'out' ? edge.to : edge.from;
  return `<div class="edge-card">
    <span class="flow-badge flow-${esc(edge.flow)}">${esc(edge.flow)}</span>
    <span class="edge-sector-chip" data-slug="${esc(nameToSlug(otherName))}">${esc(otherName)}</span>
    <span class="edge-product">${esc(edge.product)}</span>
  </div>`;
}

function closeDrawer() {
  document.getElementById('detail-panel').classList.remove('open');
  document.body.classList.remove('drawer-open');
}
```

### Mobile layout

On mobile (`max-width: 768px`), the layout stacks vertically. `#edge-svg` is hidden (`display:none`).
The detail panel slides up as a bottom sheet. No SVG gutter, no ambient edge drawing.

```css
@media (max-width: 768px) {
  #hdr { height: auto; flex-direction: column; align-items: flex-start; padding: 8px 12px; gap: 6px; }
  .filters { overflow-x: auto; scroll-snap-type: x mandatory; -webkit-overflow-scrolling: touch;
             flex-wrap: nowrap; width: 100%; padding-bottom: 4px; }
  .filter-btn, #reset-btn { flex-shrink: 0; scroll-snap-align: start;
                             min-height: 40px; padding: 0 14px; font-size: 13px; border-radius: 20px; }
  #layout { flex-direction: column; height: auto; overflow: visible; }
  #stack-panel { width: 100%; border-right: none; padding: 12px; overflow-y: visible; }
  #edge-svg { display: none; }
  .dim-sectors { flex-direction: column; gap: 0; }
  .sector-card { margin-bottom: 8px; min-width: unset; flex: 1 1 auto; }
  #detail-panel { position: fixed; bottom: 0; left: 0; right: 0; height: 55vh;
                  background: var(--bg); border-top: 2px solid var(--border);
                  border-radius: 16px 16px 0 0; overflow-y: auto; padding: 0 16px 24px;
                  transform: translateY(100%); transition: transform .3s ease;
                  z-index: 50; box-shadow: 0 -4px 24px rgba(0,0,0,.08); }
  #detail-panel.open { transform: translateY(0); }
  #detail-panel::before { content: ''; display: block; width: 36px; height: 4px;
                          background: var(--border); border-radius: 2px; margin: 10px auto 14px; }
  .close-drawer { display: flex; }
  body.drawer-open { overflow: hidden; }
}
@media (min-width: 769px) { .close-drawer { display: none; } }
```

Swipe-to-dismiss: track `touchstart` Y on `#detail-panel`; on `touchend` if delta > 60px call `closeDrawer()`.

---

## Phase 5 — Write and deploy

1. **Write** the complete HTML to `Investing/Output/Dashboard/index.html`
2. **Write** a dated copy to `Investing/Output/Dashboard/[DATE].html`
3. If `--no-push` flag is set, stop here.
4. Otherwise, deploy to `gh-pages`:
   ```bash
   git fetch origin gh-pages
   git checkout gh-pages
   git show [CURRENT_BRANCH]:Investing/Output/Dashboard/index.html > index.html
   git add index.html
   git commit -m "Deploy ecosystem map [DATE]"
   git push -u origin gh-pages
   git checkout [CURRENT_BRANCH]
   ```
5. Commit the dashboard files to `master` as well:
   ```bash
   git add Investing/Output/Dashboard/index.html Investing/Output/Dashboard/[DATE].html
   git commit -m "Dashboard: ecosystem map [DATE]"
   git push -u origin master
   ```
