---
description: Generate self-contained HTML dashboard from supply chain maps; educational 3-layer ecosystem viewer (D1–D6 dimensions, sector cards → tier list → tier detail). Usage: /daily-dashboard [--date YYYY-MM-DD] [--no-push]
allowed-tools: Read, Write, Bash
---

# Daily Dashboard — Ecosystem Map Viewer

Generates `Investing/Output/Dashboard/index.html` — a self-contained, zero-dependency HTML page
that teaches the AI supply chain stack from the ground up. Three navigation layers:
- **Layer 0** — D1–D6 dimension rows, each containing sector cards
- **Layer 1** — Sector detail: ordered tier list with function descriptions
- **Layer 2** — Tier detail: full function paragraph + investment angle breakdown

---

## Phase 1 — Parse Dimension Map

Read `Investing/Wiki/Reference/Dimension Map.md`.

From the Sector Registry table, collect every row where **both** of these are true:
- Folder Slug is not `*(reserved)*`
- Status is not `planned`

For each qualifying row record: `name` (Sector column), `dimension` (D1–D6), `slug` (Folder Slug value, strip backticks).

Sort the list by dimension ascending (D1 first), then alphabetically within each dimension.

---

## Phase 2 — Read supply chain maps

For each sector from Phase 1, read:
`Investing/Wiki/Sectors/[slug]/_Supply Chain Map.md`

**A. Anchor text (sector description)**

The file's second or third line matches the pattern:
```
*Mapped: ... | Anchor: [text]*
```
Extract everything after `Anchor: ` and before the closing `*`. This is `description`.

**B. Tier data**

Parse the markdown table under `## Value Chain`. For each data row (skip the header row and the `|---|` separator row), extract these columns by position:

| Position | Field | Notes |
|----------|-------|-------|
| 1 | `tier` | Short tier name |
| 2 | `fn` | One-sentence function description |
| 5 | `chokepoint` | `"Y"`, `"N"`, or `"Partial"` |
| 6 | `capital_intensity` | e.g. `"High"`, `"Medium"`, `"Low"` |
| 7 | `moat_type` | e.g. `"Process IP · Scale"` |
| 8 | `margin_profile` | e.g. `"Very High"`, `"High"` |

Skip columns 3 (Processes) and 4 (Key Products) — not needed.

Store each row as: `{ tier, fn, chokepoint, capital_intensity, moat_type, margin_profile }`

---

## Phase 3 — Build DATA object

Assemble the JavaScript constant that will be embedded in the HTML:

```
const DATA = {
  generated: "YYYY-MM-DD",
  sectors: [
    {
      slug: "semiconductors",
      name: "Semiconductors",
      dimension: "D1",
      description: "packaged chip ready for system assembly",
      tiers: [
        { tier: "Raw Materials & Specialty Chemicals", fn: "Produce the ...", chokepoint: "Partial", capital_intensity: "Medium", moat_type: "Process IP + Geographic monopoly", margin_profile: "Medium–High" },
        ...
      ]
    },
    ...
  ]
};
```

Rules:
- `slug` — lowercase the sector name, replace spaces with hyphens, strip special characters
- `generated` — today's date in YYYY-MM-DD
- Preserve the exact text from the supply chain map (do not paraphrase fn, tier names, chokepoint values, etc.)

---

## Phase 4 — Write HTML file

Ensure `Investing/Output/Dashboard/` directory exists (create with `mkdir -p` if needed).

Write `Investing/Output/Dashboard/index.html` using **exactly** the template below.
Replace the `/* DATA */` comment with the full `const DATA = {...};` from Phase 3.
Replace `YYYY-MM-DD` in the header with today's date.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI Ecosystem Map</title>
<style>
:root{--bg:#0f1117;--bg2:#1a1d27;--bg3:#252836;--border:#2e3244;--text:#e2e8f0;--muted:#8892a4;--amber:#f59e0b;--amber-bg:rgba(245,158,11,0.12);--d1:#6366f1;--d2:#22c55e;--d3:#3b82f6;--d4:#a855f7;--d5:#ef4444;--d6:#f97316}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--text);font:14px/1.5 system-ui,sans-serif}
#hdr{display:flex;align-items:center;justify-content:space-between;padding:14px 24px;border-bottom:1px solid var(--border);background:var(--bg2);position:sticky;top:0;z-index:10}
.logo{font-weight:700;font-size:16px}.gen-date{color:var(--muted);font-size:12px}
#l0,#l1,#l2{padding:24px;max-width:1200px;margin:0 auto}
.dim-row{margin-bottom:32px}
.dim-label{display:flex;align-items:center;gap:10px;margin-bottom:12px;flex-wrap:wrap}
.dim-pill{font-size:11px;font-weight:700;padding:3px 10px;border-radius:99px;color:#fff;letter-spacing:.05em;flex-shrink:0}
.dim-pill.D1{background:var(--d1)}.dim-pill.D2{background:var(--d2);color:#000}
.dim-pill.D3{background:var(--d3)}.dim-pill.D4{background:var(--d4)}
.dim-pill.D5{background:var(--d5)}.dim-pill.D6{background:var(--d6)}
.dim-name{font-weight:600;font-size:14px}
.dim-desc{color:var(--muted);font-size:12px;margin-left:auto;max-width:480px;text-align:right}
.sec-cards{display:flex;flex-wrap:wrap;gap:12px}
.sec-card{background:var(--bg2);border:1px solid var(--border);border-radius:8px;padding:14px 16px;cursor:pointer;width:clamp(160px,22%,240px);transition:border-color .15s,transform .1s}
.sec-card:hover{border-color:#4a5568;transform:translateY(-1px)}
.sec-card-name{font-weight:600;font-size:13px;margin-bottom:4px}
.sec-card-desc{color:var(--muted);font-size:11px;line-height:1.4;margin-bottom:8px}
.sec-meta{display:flex;align-items:center;gap:8px}
.tier-badge{font-size:10px;background:var(--bg3);padding:2px 7px;border-radius:99px;color:var(--muted)}
.choke-dot{width:7px;height:7px;border-radius:50%;background:var(--amber);display:inline-block}
.empty-dim{color:var(--muted);font-size:12px;padding:8px 0;font-style:italic}
.breadcrumb{font-size:12px;color:var(--muted);margin-bottom:20px;cursor:pointer;display:inline-block;padding:4px 0}
.breadcrumb:hover{color:var(--text)}
.sector-hdr{display:flex;align-items:center;gap:12px;margin-bottom:8px}
.sector-title{font-size:22px;font-weight:700}
.sector-desc-full{color:var(--muted);font-size:13px;margin-bottom:6px}
.dim-ctx{font-size:12px;color:var(--muted);margin-bottom:24px;font-style:italic}
.tier-card{background:var(--bg2);border:1px solid var(--border);border-left:3px solid var(--border);border-radius:6px;padding:14px 16px;margin-bottom:10px;cursor:pointer;transition:border-color .15s}
.tier-card:hover{border-color:#4a5568}
.tier-card.choke-y{border-left-color:var(--amber)}
.tier-card.choke-p{border-left-color:#78716c}
.tier-top{display:flex;align-items:flex-start;justify-content:space-between;gap:12px;margin-bottom:8px}
.tier-name{font-weight:600;font-size:13px}
.choke-badge{font-size:10px;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;flex-shrink:0}
.choke-badge.y{background:var(--amber-bg);color:var(--amber)}
.choke-badge.p{background:rgba(120,113,108,.15);color:#a8a29e}
.tier-fn{color:var(--muted);font-size:12px;line-height:1.5;margin-bottom:10px}
.tier-pills{display:flex;flex-wrap:wrap;gap:6px}
.pill{font-size:10px;background:var(--bg3);padding:2px 8px;border-radius:99px;color:var(--muted)}
.tier-detail-name{font-size:20px;font-weight:700;margin-bottom:16px}
.tier-fn-full{font-size:15px;line-height:1.6;color:var(--text);margin-bottom:28px}
.invest-section h3{font-size:13px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--muted);margin-bottom:12px}
.invest-rows{display:flex;flex-direction:column;gap:8px;margin-bottom:20px}
.invest-row{display:flex;gap:12px;font-size:13px}
.invest-label{color:var(--muted);width:140px;flex-shrink:0}
.invest-val{color:var(--text)}
.choke-box{background:var(--amber-bg);border:1px solid rgba(245,158,11,.3);border-radius:6px;padding:12px 16px;margin-bottom:20px}
.choke-box p{font-size:13px;color:var(--amber)}
.choke-box-partial{background:rgba(120,113,108,.1);border:1px solid rgba(120,113,108,.25);border-radius:6px;padding:12px 16px;margin-bottom:20px}
.choke-box-partial p{font-size:13px;color:#a8a29e}
@media(max-width:600px){.sec-card{width:100%}.dim-desc{display:none}#l0,#l1,#l2{padding:16px}}
</style>
</head>
<body>
<div id="app">
<header id="hdr">
  <span class="logo">AI Ecosystem Map</span>
  <span class="gen-date">Generated: YYYY-MM-DD</span>
</header>
<div id="l0"></div>
<div id="l1" hidden></div>
<div id="l2" hidden></div>
</div>
<script>
/* DATA */

const DIM_LABEL={D1:'AI Manufacturing Base',D2:'AI Connectivity',D3:'AI Infrastructure',D4:'AI Model Infrastructure',D5:'AI Enablement',D6:'AI Applications'};
const DIM_DESC={
  D1:'The foundational physical layer — raw materials, components, and chips that everything above depends on.',
  D2:'The connection layer — optical, wireless, and satellite links that move data between AI compute nodes.',
  D3:'The compute and power layer — data centers, GPUs, and clean energy that run AI workloads.',
  D4:'The model infrastructure layer — MLOps platforms, vector databases, data annotation, model serving, and orchestration tools that surround foundation models.',
  D5:'The software and security layer — platforms and tools that enable safe, governed AI deployment.',
  D6:'The application layer — AI-native products in robotics, fintech, defense, and enterprise.'
};
const DIMS=['D1','D2','D3','D4','D5','D6'];

let activeSector=null;

function showLayer(n){
  document.getElementById('l0').hidden=n!==0;
  document.getElementById('l1').hidden=n!==1;
  document.getElementById('l2').hidden=n!==2;
}

function renderL0(){
  const el=document.getElementById('l0');
  el.innerHTML=DIMS.map(dim=>{
    const secs=DATA.sectors.filter(s=>s.dimension===dim);
    const cards=secs.length===0
      ?'<div class="empty-dim">No sectors mapped yet</div>'
      :secs.map(s=>{
        const hasChoke=s.tiers.some(t=>t.chokepoint==='Y');
        return `<div class="sec-card" onclick="openSector('${s.slug}')">
          <div class="sec-card-name">${s.name}</div>
          <div class="sec-card-desc">${s.description}</div>
          <div class="sec-meta">
            <span class="tier-badge">${s.tiers.length} tier${s.tiers.length!==1?'s':''}</span>
            ${hasChoke?'<span class="choke-dot" title="Contains chokepoint tiers"></span>':''}
          </div>
        </div>`;
      }).join('');
    return `<div class="dim-row">
      <div class="dim-label">
        <span class="dim-pill ${dim}">${dim}</span>
        <span class="dim-name">${DIM_LABEL[dim]}</span>
        <span class="dim-desc">${DIM_DESC[dim]}</span>
      </div>
      <div class="sec-cards">${cards}</div>
    </div>`;
  }).join('');
}

function openSector(slug){
  activeSector=DATA.sectors.find(s=>s.slug===slug);
  renderL1();
  showLayer(1);
}

function renderL1(){
  const s=activeSector;
  const tiers=s.tiers.map((t,i)=>{
    const cls=t.chokepoint==='Y'?'choke-y':t.chokepoint==='Partial'?'choke-p':'';
    const badge=t.chokepoint==='Y'
      ?'<span class="choke-badge y">⬥ CHOKEPOINT</span>'
      :t.chokepoint==='Partial'
      ?'<span class="choke-badge p">⬥ PARTIAL</span>'
      :'';
    return `<div class="tier-card ${cls}" onclick="openTier(${i})">
      <div class="tier-top"><div class="tier-name">${t.tier}</div>${badge}</div>
      <div class="tier-fn">${t.fn}</div>
      <div class="tier-pills">
        <span class="pill">${t.moat_type}</span>
        <span class="pill">${t.capital_intensity} capex</span>
        <span class="pill">${t.margin_profile} margins</span>
      </div>
    </div>`;
  }).join('');
  document.getElementById('l1').innerHTML=`
    <div class="breadcrumb" onclick="showLayer(0)">← Ecosystem</div>
    <div class="sector-hdr">
      <span class="dim-pill ${s.dimension}">${s.dimension}</span>
      <span class="sector-title">${s.name}</span>
    </div>
    <div class="sector-desc-full">${s.description}</div>
    <div class="dim-ctx">${DIM_LABEL[s.dimension]} — ${DIM_DESC[s.dimension]}</div>
    ${tiers}`;
}

function openTier(idx){
  const s=activeSector;
  const t=s.tiers[idx];
  const chokeBlock=t.chokepoint==='Y'
    ?'<div class="choke-box"><p>⬥ Supply chain chokepoint — limited substitutes in this tier. Capacity constraints here propagate up the stack.</p></div>'
    :t.chokepoint==='Partial'
    ?'<div class="choke-box-partial"><p>⬥ Partial chokepoint — some alternatives exist, but switching carries meaningful cost or lead time.</p></div>'
    :'';
  document.getElementById('l2').innerHTML=`
    <div class="breadcrumb" onclick="openSector('${s.slug}')">← ${s.name}</div>
    ${chokeBlock}
    <div class="tier-detail-name">${t.tier}</div>
    <div class="tier-fn-full">${t.fn}</div>
    <div class="invest-section">
      <h3>Investment Angle</h3>
      <div class="invest-rows">
        <div class="invest-row"><span class="invest-label">Competitive moat</span><span class="invest-val">${t.moat_type}</span></div>
        <div class="invest-row"><span class="invest-label">Capital intensity</span><span class="invest-val">${t.capital_intensity}</span></div>
        <div class="invest-row"><span class="invest-label">Margin profile</span><span class="invest-val">${t.margin_profile}</span></div>
        <div class="invest-row"><span class="invest-label">Chokepoint status</span><span class="invest-val">${t.chokepoint==='Y'?'Yes — critical supply constraint':t.chokepoint==='Partial'?'Partial — some alternatives exist':'No — competitive market'}</span></div>
      </div>
    </div>`;
  showLayer(2);
}

renderL0();
</script>
</body>
</html>
```

---

## Phase 5 — Verify and report

After writing the file, confirm:
- File exists at `Investing/Output/Dashboard/index.html`
- DATA object contains all sectors from Phase 1 (print count)
- Print a summary: `Generated dashboard: N sectors, D1–D6 layout`

If `--no-push` flag is not present, run:
```
git add Investing/Output/Dashboard/index.html Investing/Wiki/Reference/Dimension\ Map.md
git commit -m "Regenerate ecosystem dashboard: educational 3-layer viewer, D1-D6 taxonomy"
git push -u origin claude/ecosystem-mapping-viz-ly9r4
```

If `--no-push` is set, skip the git commands and print: `Dashboard written. Run git add/commit/push manually.`
