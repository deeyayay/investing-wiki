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

Write a complete self-contained HTML file. All CSS and JS inline. No CDN links. Must work at `file://` and on GitHub Pages.

### Design system

```css
:root {
  --bg: #0d1117; --bg2: #161b22; --bg3: #21262d;
  --text: #e6edf3; --muted: #8b949e; --border: #30363d;
  --amber: #d4a017; --green: #3fb950; --blue: #58a6ff;
  --red: #f85149; --orange: #e3812b; --purple: #bc8cff;
  --pink: #ff7b72;
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
- Y → `--amber` background, dark text, bold `⬥`
- Partial → `#5a4200` background, `--amber` text
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

```html
<header id="hdr">
  <span class="site-title">ECOSYSTEM MAP · [DATE]</span>
  <div class="filters">
    <button class="filter-btn active" data-filter="all">All edges</button>
    <button class="filter-btn" data-filter="Y">⬥ Chokepoints only</button>
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

### SVG edge drawing

Define SVG arrowhead markers in `<defs>`:
```svg
<defs>
  <marker id="arrow-amber" ...><path d="M0,0 L8,4 L0,8 Z" fill="#d4a017"/></marker>
  <marker id="arrow-blue" ...><path d="M0,0 L8,4 L0,8 Z" fill="#58a6ff"/></marker>
  <marker id="arrow-green" ...><path d="M0,0 L8,4 L0,8 Z" fill="#3fb950"/></marker>
</defs>
```

Edge drawing function `drawEdges(selectedSlug, activeFilter)`:
1. Clear all `<path>` elements from the SVG
2. For the selected sector, find all edges where `edge.from === selectedSlug_name || edge.to === selectedSlug_name`
3. Apply `activeFilter` to narrow edges (if filter === "Y", only show chokepoint === "Y"; if filter is a flow type, only show that flow)
4. For each visible edge:
   - Get `sourceCard = document.querySelector('[data-slug="'+fromSlug+'"]')`
   - Get `targetCard = document.querySelector('[data-slug="'+toSlug+'"]')`
   - Get bounding rects relative to `#stack-panel` (subtract panel's `scrollTop` and `getBoundingClientRect`)
   - `sx = sourceRect.right - panelRect.left`, `sy = sourceRect.top + sourceRect.height/2 - panelRect.top + panel.scrollTop`
   - `tx = targetRect.left - panelRect.left`, `ty = targetRect.top + targetRect.height/2 - panelRect.top + panel.scrollTop`
   - If source and target are in the same dimension row, use center-to-center with vertical offsets
   - Control points: `cx1 = sx + (tx-sx)*0.5, cy1 = sy; cx2 = cx1, cy2 = ty`
   - Stroke: amber if chokepoint Y, blue if from === selected (outbound), green if to === selected (inbound)
   - Stroke-width: 2.5px if Y, 1.5px otherwise
   - Marker-end: matching arrow marker
   - Append `<path d="M sx sy C cx1 cy1 cx2 cy2 tx ty" stroke="..." stroke-width="..." fill="none" marker-end="url(#arrow-...)" opacity="0.85"/>`
5. On window resize: call `drawEdges(currentSelected, activeFilter)` if a sector is selected

Convert display name to slug: lowercase, replace spaces and `&` with `-`, remove special chars. E.g., "Photonics & Optical" → "photonics-optical". Store slug on card `data-slug` and in the DATA object.

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
  // Draw SVG edges
  drawEdges(slug, activeFilter);
  // Render detail panel
  renderDetail(slug);
  // Mobile: show drawer
  if (window.innerWidth <= 768) {
    document.getElementById('detail-panel').classList.add('open');
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

```javascript
function renderDetail(slug) {
  const sector = DATA.sectors.find(s => s.slug === slug);
  const outbound = DATA.edges.filter(e => e.from === sector.name);
  const inbound = DATA.edges.filter(e => e.to === sector.name);
  
  // Apply active filter
  const filterEdges = edges => {
    if (activeFilter === 'all') return edges;
    if (activeFilter === 'Y') return edges.filter(e => e.chokepoint === 'Y');
    return edges.filter(e => e.flow === activeFilter);
  };
  
  // Tier table
  const tierRows = sector.tiers.map(t => `
    <tr class="tier-row choke-${t.chokepoint.toLowerCase()}"
        data-processes="${escHtml(t.processes)}"
        data-products="${escHtml(t.key_products)}">
      <td class="tier-name">${t.tier}</td>
      <td>${chokeBadge(t.chokepoint)}</td>
      <td class="tier-fn">${t.function}</td>
      <td class="tier-proc">${truncate(t.processes, 80)}</td>
    </tr>
  `).join('');
  
  // Edge cards (outbound)
  const outHtml = filterEdges(outbound).map(e => edgeCard(e, 'out')).join('') || '<p class="muted">None</p>';
  const inHtml = filterEdges(inbound).map(e => edgeCard(e, 'in')).join('') || '<p class="muted">None</p>';
  
  document.getElementById('detail-panel').innerHTML = `
    <div class="detail-header">
      <h2>${sector.name}</h2>
      <span class="dim-badge dim-${sector.dimension.toLowerCase()}">${sector.dimension}</span>
    </div>
    
    <section class="detail-section">
      <div class="section-title">Supply Chain Tiers</div>
      <table class="tier-table">
        <thead><tr><th>Tier</th><th>Choke</th><th>Function</th><th>Processes</th></tr></thead>
        <tbody>${tierRows}</tbody>
      </table>
      <p class="hint">Hover row for full processes &amp; key products</p>
    </section>
    
    <section class="detail-section">
      <div class="section-title">→ Outbound (${outbound.length} edges)</div>
      <div class="edge-list">${outHtml}</div>
    </section>
    
    <section class="detail-section">
      <div class="section-title">← Inbound (${inbound.length} edges)</div>
      <div class="edge-list">${inHtml}</div>
    </section>
  `;
  
  // Wire up tier row tooltips
  document.querySelectorAll('.tier-row').forEach(row => {
    row.addEventListener('mouseenter', e => showTooltip(row.dataset.processes, row.dataset.products));
    row.addEventListener('mouseleave', hideTooltip);
  });
  
  // Wire up sector chips in edge list
  document.querySelectorAll('.edge-sector-chip').forEach(chip => {
    chip.addEventListener('click', () => selectSector(chip.dataset.slug));
  });
}

function edgeCard(edge, direction) {
  const otherName = direction === 'out' ? edge.to : edge.from;
  const otherSlug = nameToSlug(otherName);
  return `
    <div class="edge-card">
      <span class="flow-badge flow-${edge.flow.toLowerCase()}">${edge.flow}</span>
      <span class="edge-sector-chip" data-slug="${otherSlug}">${otherName}</span>
      <span class="edge-product">${edge.product}</span>
      ${edge.chokepoint === 'Y' ? '<span class="choke-badge-y">⬥Y</span>' : ''}
    </div>
  `;
}
```

### Tier row tooltip

A floating `<div id="tooltip">` (fixed position, `pointer-events:none`, `z-index:1000`):
```javascript
function showTooltip(processes, products) {
  const tt = document.getElementById('tooltip');
  tt.innerHTML = `<b>Processes:</b> ${processes}<hr><b>Key Products:</b> ${products}`;
  tt.style.display = 'block';
}
document.addEventListener('mousemove', e => {
  const tt = document.getElementById('tooltip');
  tt.style.left = (e.clientX + 12) + 'px';
  tt.style.top = (e.clientY + 12) + 'px';
});
function hideTooltip() { document.getElementById('tooltip').style.display = 'none'; }
```

### Filter button logic

```javascript
let activeFilter = 'all';
document.querySelectorAll('.filter-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    activeFilter = btn.dataset.filter;
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    if (currentSelected) {
      drawEdges(currentSelected, activeFilter);
      renderDetail(currentSelected); // re-render edge lists with filter applied
    }
  });
});
document.getElementById('reset-btn').addEventListener('click', () => {
  currentSelected = null;
  document.querySelectorAll('.sector-card').forEach(c => {
    c.classList.remove('selected','upstream','downstream','dimmed');
  });
  document.getElementById('edge-svg').innerHTML = '<defs>...</defs>'; // keep defs, clear paths
  document.getElementById('detail-panel').innerHTML = `<div class="detail-empty">Select a sector to explore its supply chain tiers and ecosystem connections.</div>`;
  if (window.innerWidth <= 768) document.getElementById('detail-panel').classList.remove('open');
});
```

### Mobile drawer

```css
@media (max-width: 768px) {
  #layout { flex-direction: column; height: auto; overflow: visible; }
  #stack-panel { width: 100%; border-right: none; border-bottom: 1px solid var(--border); }
  #detail-panel {
    position: fixed; bottom: 0; left: 0; right: 0;
    height: 65vh; background: var(--bg2);
    border-top: 1px solid var(--border); border-radius: 12px 12px 0 0;
    overflow-y: auto; padding: 20px;
    transform: translateY(100%); transition: transform .3s ease;
    z-index: 50;
  }
  #detail-panel.open { transform: translateY(0); }
}
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
