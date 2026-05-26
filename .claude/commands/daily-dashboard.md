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

For each row extract **ONLY** these fields (do NOT extract Processes or Key Products — those columns are intentionally omitted to stay within output token budget):
```
{
  tier: col[0],
  function: first sentence of col[1] only, truncated to 120 chars max,
  chokepoint: col[4],         // "Y", "Partial", or "No"
  capital_intensity: col[5],
  moat_type: col[6],
  margin_profile: col[7]
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
  product: col[5],      // keep as-is
  chokepoint: col[6],   // "Yes", "Y", "Partial", or "No"
}
```

Skip header rows, separator rows, and section headings (lines not starting with `|`).
Normalize chokepoint: treat "Yes" and "Y" as "Y".
Omit the `notes` column entirely.

Store as `edges[]` (flat array).

---

## Phase 3 — Assemble data model

Build the JS data object to embed in the HTML. **Omit `processes` and `key_products` entirely** — they are not present in the trimmed DATA model:

```javascript
const DATA = {
  generated: "YYYY-MM-DD",
  sectors: [
    {
      slug: "semiconductors",
      name: "Semiconductors",
      dimension: "D1",
      tiers: [
        { tier, fn, chokepoint, capital_intensity, moat_type, margin_profile }
        // NOTE: use "fn" not "function" (reserved keyword in JS)
      ]
    }
  ],
  edges: [
    { from, from_tier, to, to_tier, flow, product, chokepoint }
  ]
};
```

**Slugs:** lowercase display name, spaces and `&` → `-`, remove special chars.
Examples: "Photonics & Optical" → `photonics-optical`, "Fintech & Commerce AI" → `fintech-commerce-ai`, "Space & Communications" → `space-communications`.

**Chokepoint normalization:** "Yes"/"Y" → `"Y"`, "Partial" → `"Partial"`, anything else → `"No"`.

Dimension order for rendering: D1 → D2 → D3 → D4 → D5.

---

## Phase 4 — Generate HTML in 4 bash heredoc chunks

**CRITICAL: Do not attempt to write the entire HTML file in a single Write or cat command.** The output is too large. Instead, write in exactly 4 sequential bash heredoc calls to `Investing/Output/Dashboard/index.html`.

---

### Chunk A — Write HTML/CSS shell (cat > creates the file)

```bash
cat > Investing/Output/Dashboard/index.html << 'HTMLEOF'
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>AI Ecosystem Map — [DATE]</title>
<style>
:root{
  --bg:#0d1117;--bg2:#161b22;--bg3:#21262d;
  --text:#e6edf3;--muted:#8b949e;--border:#30363d;
  --amber:#d4a017;--green:#3fb950;--blue:#58a6ff;
  --orange:#e3812b;--purple:#bc8cff;--pink:#ff7b72;
}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--text);font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;overflow:hidden}
#app{display:flex;flex-direction:column;height:100vh}
#hdr{height:48px;min-height:48px;background:var(--bg2);border-bottom:1px solid var(--border);
  display:flex;align-items:center;padding:0 14px;gap:12px;overflow-x:auto;white-space:nowrap;z-index:10}
.logo{font-size:15px;font-weight:700;color:var(--text);flex-shrink:0}
.logo span{color:var(--amber)}
#filters{display:flex;gap:6px;flex-shrink:0}
.fb{padding:4px 10px;border-radius:20px;border:1px solid var(--border);background:transparent;
  color:var(--muted);font-size:11px;cursor:pointer;transition:all .15s}
.fb:hover,.fb.active{background:var(--bg3);color:var(--text);border-color:var(--muted)}
#main{display:flex;flex:1;overflow:hidden}
#gp{width:50%;overflow:auto;position:relative;border-right:1px solid var(--border)}
#dp{flex:1;overflow-y:auto;padding:16px;background:var(--bg)}
/* Mobile bottom sheet */
@media(max-width:768px){
  #gp{width:100%;border-right:none}
  #dp{position:fixed;bottom:0;left:0;right:0;height:72vh;background:var(--bg2);
    border-radius:14px 14px 0 0;transform:translateY(100%);transition:transform .3s cubic-bezier(.25,.46,.45,.94);
    z-index:30;padding:0 16px 16px;overflow-y:auto}
  #dp.open{transform:translateY(0)}
  #dp::before{content:'';display:block;width:36px;height:4px;background:var(--border);
    border-radius:2px;margin:10px auto 14px}
}
/* SVG graph */
.sector-node{cursor:pointer}
.sector-node rect{transition:fill .15s,stroke .15s,opacity .15s}
@keyframes flowFwd{to{stroke-dashoffset:-22}}
.anim{stroke-dasharray:6 4;animation:flowFwd 1.4s linear infinite}
.slow{animation-duration:2.2s}
.fast{animation-duration:.7s}
.eco-edge{transition:opacity .2s}
/* Detail panel */
.bc{font-size:11px;color:var(--muted);margin-bottom:12px}
.bc a{color:var(--blue);cursor:pointer;text-decoration:none}
.bc a:hover{text-decoration:underline}
.dh{font-size:22px;font-weight:700;margin-bottom:6px;display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.dh.tier{font-size:18px}
.dd{font-size:13px;color:var(--muted);line-height:1.6;margin-bottom:16px}
.sec-label{font-size:11px;font-weight:600;color:var(--muted);text-transform:uppercase;
  letter-spacing:.07em;margin:18px 0 8px;padding-bottom:6px;border-bottom:1px solid var(--border)}
/* Tier cards */
.tc{display:flex;align-items:center;gap:10px;padding:10px 12px;border-radius:8px;
  background:var(--bg2);border:1px solid var(--border);margin-bottom:6px;cursor:pointer;transition:background .15s}
.tc:hover{background:var(--bg3)}
.tc.ck-Y{border-left:3px solid var(--amber)}
.tc.ck-P{border-left:3px solid #7a5c00}
.tc-body{flex:1;min-width:0}
.tc-name{font-size:13px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.tc-fn{font-size:11px;color:var(--muted);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;margin-top:2px}
.tc-arr{color:var(--muted);font-size:14px;flex-shrink:0}
/* Edge cards */
.ec{display:flex;flex-wrap:wrap;gap:6px;align-items:center;padding:8px 12px;border-radius:8px;
  background:var(--bg2);border:1px solid var(--border);margin-bottom:6px;font-size:12px}
.ec-prod{flex:1 1 100%;font-size:11px;color:var(--muted);margin-top:2px}
.ec-sec{cursor:pointer;color:var(--blue)}
.ec-sec:hover{text-decoration:underline}
/* Meta pills */
.meta-row{display:flex;flex-wrap:wrap;gap:6px;margin:10px 0 16px}
.pill{padding:3px 9px;border-radius:12px;font-size:11px;background:var(--bg3);color:var(--muted);border:1px solid var(--border)}
/* Badges */
.badge{display:inline-block;padding:2px 7px;border-radius:10px;font-size:10px;font-weight:600;line-height:1.6}
.bD1{background:#2d1f47;color:var(--purple)}
.bD2{background:#1a2a47;color:var(--blue)}
.bD3{background:#1a3027;color:var(--green)}
.bD4{background:#3a2a00;color:var(--amber)}
.bD5{background:#3a1a1a;color:var(--pink)}
.bCY{background:#3a2a00;color:var(--amber)}
.bCP{background:#2a2200;color:#9a7a20}
.bMat{background:#3a2010;color:var(--orange)}
.bCom{background:#1a2a47;color:var(--blue)}
.bSvc{background:#1a3027;color:var(--green)}
.bSig{background:#2d1f47;color:var(--purple)}
.bPrc{background:#3a2a00;color:var(--amber)}
/* Empty state */
.empty{display:flex;flex-direction:column;align-items:center;justify-content:center;
  height:100%;color:var(--muted);font-size:13px;gap:8px;padding:20px;text-align:center}
.empty-icon{font-size:32px;opacity:.4}
/* Mobile back button */
.back-btn{display:none;padding:6px 12px;border-radius:6px;border:1px solid var(--border);
  background:transparent;color:var(--muted);font-size:12px;cursor:pointer;margin-bottom:12px}
@media(max-width:768px){.back-btn{display:inline-block}}
</style>
</head>
<body>
<div id="app">
<header id="hdr">
  <span class="logo">AI Ecosystem <span>Map</span></span>
  <div id="filters">
    <button class="fb active" onclick="setFilter('all')">All Flows</button>
    <button class="fb" onclick="setFilter('Y')">⬥ Chokepoints</button>
    <button class="fb" onclick="setFilter('Material')">Material</button>
    <button class="fb" onclick="setFilter('Component')">Component</button>
    <button class="fb" onclick="setFilter('Service')">Service</button>
    <button class="fb" onclick="setFilter('Signal')">Signal</button>
  </div>
</header>
<div id="main">
  <div id="gp"></div>
  <div id="dp"><div class="empty"><div class="empty-icon">◈</div><div>Click a sector node to explore its supply chain and cross-sector flows</div></div></div>
</div>
</div>
<script>
HTMLEOF
```

---

### Chunk B — Append DATA block (cat >> appends)

Generate the DATA constant from the parsed sectors and edges. Use `cat >> Investing/Output/Dashboard/index.html << 'DATAEOF'` ... `DATAEOF`.

The DATA object must exactly follow this structure:
```javascript
const DATA={generated:"[DATE]",sectors:[...],edges:[...]};
```

Write it as a single minified JS line or compact multi-line block. Use `fn` (not `function`) for the tier function field. Emit only the fields in the trimmed model: `slug, name, dimension, tiers:[{tier,fn,chokepoint,capital_intensity,moat_type,margin_profile}], edges:[{from,from_tier,to,to_tier,flow,product,chokepoint}]`.

End the heredoc after the semicolon that closes `const DATA`.

---

### Chunk C — Append JS visualization (cat >> appends)

Write all visualization JS using `cat >> Investing/Output/Dashboard/index.html << 'JSEOF'` ... `JSEOF`.

Include all of the following, in order:

```javascript
// ── helpers ──────────────────────────────────────────────────────────────────
let selSlug=null,activeF='all';
const DIM_COLORS={D1:'#bc8cff',D2:'#58a6ff',D3:'#3fb950',D4:'#d4a017',D5:'#ff7b72'};
const DIM_BG={D1:'rgba(188,140,255,.04)',D2:'rgba(88,166,255,.04)',D3:'rgba(63,185,80,.04)',D4:'rgba(212,160,23,.04)',D5:'rgba(255,123,114,.04)'};
const FLOW_COLOR={Material:'#e3812b',Component:'#58a6ff',Service:'#3fb950',Signal:'#bc8cff',Process:'#d4a017'};
const FLOW_BADGE={Material:'bMat',Component:'bCom',Service:'bSvc',Signal:'bSig',Process:'bPrc'};
function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;')}
function nslug(name){const s=DATA.sectors.find(x=>x.name===name);return s?s.slug:null}
function sname(slug){const s=DATA.sectors.find(x=>x.slug===slug);return s?s.name:slug}
function sec(label){return`<div class="sec-label">${esc(label)}</div>`}
function flBadge(f){return`<span class="badge ${FLOW_BADGE[f]||'bPrc'}">${esc(f)}</span>`}
function ckBadge(c){if(c==='Y')return'<span class="badge bCY">⬥ CHOKEPOINT</span>';if(c==='Partial')return'<span class="badge bCP">⬥ PARTIAL</span>';return''}
function dimBadge(d){return`<span class="badge b${d}">${esc(d)}</span>`}
function filt(arr){
  if(activeF==='all')return arr;
  if(activeF==='Y')return arr.filter(e=>e.chokepoint==='Y');
  return arr.filter(e=>e.flow===activeF);
}
function bc(parts){
  return'<div class="bc">'+parts.map((p,i)=>{
    if(i===parts.length-1)return`<span>${esc(p.label)}</span>`;
    return`<a onclick="${esc(p.action)}">${esc(p.label)}</a>`;
  }).join(' › ')+'</div>';
}

// ── filter ────────────────────────────────────────────────────────────────────
function setFilter(f){
  activeF=f;
  document.querySelectorAll('.fb').forEach(b=>b.classList.toggle('active',b.textContent.trim().replace('⬥ ','')===
    ({all:'All Flows',Y:'Chokepoints',Material:'Material',Component:'Component',Service:'Service',Signal:'Signal'}[f]||f)));
  applyFilter();
  if(selSlug)renderSec(selSlug);
}
function applyFilter(){
  document.querySelectorAll('.eco-edge').forEach(el=>{
    const chk=el.dataset.chk,flow=el.dataset.flow;
    let show=true;
    if(activeF==='Y')show=chk==='Y';
    else if(activeF!=='all')show=flow===activeF;
    el.style.display=show?'':'none';
  });
}

// ── node states ───────────────────────────────────────────────────────────────
function applyStates(slug,isSelected){
  const upNames=new Set(DATA.edges.filter(e=>nslug(e.to)===slug).map(e=>nslug(e.from)));
  const dnNames=new Set(DATA.edges.filter(e=>nslug(e.from)===slug).map(e=>nslug(e.to)));
  document.querySelectorAll('.sector-node').forEach(g=>{
    const s=g.dataset.slug,r=g.querySelector('rect');
    if(s===slug&&isSelected){r.setAttribute('fill','#21262d');r.setAttribute('stroke','#d4a017');r.setAttribute('stroke-width','2')}
    else if(upNames.has(s)){r.setAttribute('stroke','#3fb950');r.setAttribute('stroke-width','1.5');r.setAttribute('fill','#161b22')}
    else if(dnNames.has(s)){r.setAttribute('stroke','#58a6ff');r.setAttribute('stroke-width','1.5');r.setAttribute('fill','#161b22')}
    else if(isSelected){r.setAttribute('fill','#161b22');r.setAttribute('stroke','#30363d');r.setAttribute('stroke-width','1');g.style.opacity='0.12'}
    else{r.setAttribute('fill','#161b22');r.setAttribute('stroke','#30363d');r.setAttribute('stroke-width','1');g.style.opacity='1'}
  });
  document.querySelectorAll('.eco-edge').forEach(el=>{
    const show=!isSelected||(el.dataset.from===slug||el.dataset.to===slug);
    el.style.opacity=show?'0.92':'0.07';
  });
}

// ── graph ─────────────────────────────────────────────────────────────────────
function buildGraph(){
  const gp=document.getElementById('gp');
  const W=gp.clientWidth||window.innerWidth/2;
  const NODE_H=78,ROW_H=140,PAD_X=16,PAD_Y=38,GAP_X=10;
  const dims=['D1','D2','D3','D4','D5'];
  const pos={};

  dims.forEach((d,di)=>{
    const row=DATA.sectors.filter(s=>s.dimension===d);
    const nodeW=Math.min(182,Math.floor((W-2*PAD_X-(row.length-1)*GAP_X)/row.length));
    const totalW=row.length*nodeW+(row.length-1)*GAP_X;
    const startX=(W-totalW)/2;
    const y=PAD_Y+di*ROW_H+24;
    row.forEach((s,i)=>{
      const x=startX+i*(nodeW+GAP_X);
      pos[s.slug]={x,y,cx:x+nodeW/2,cy:y+NODE_H/2,nw:nodeW};
    });
  });

  const SVG_H=PAD_Y+5*ROW_H+NODE_H+20;
  let svg=`<svg width="${W}" height="${SVG_H}" xmlns="http://www.w3.org/2000/svg">`;

  // defs: arrowhead markers per flow type
  svg+=`<defs>`;
  Object.entries(FLOW_COLOR).forEach(([f,c])=>{
    svg+=`<marker id="arr-${f}" viewBox="0 0 10 6" refX="9" refY="3" markerWidth="7" markerHeight="5" orient="auto"><path d="M0,0 L10,3 L0,6 Z" fill="${c}"/></marker>`;
  });
  svg+=`<marker id="arr-chk" viewBox="0 0 10 6" refX="9" refY="3" markerWidth="7" markerHeight="5" orient="auto"><path d="M0,0 L10,3 L0,6 Z" fill="#d4a017"/></marker>`;
  svg+=`</defs>`;

  // dimension band backgrounds + labels
  dims.forEach((d,di)=>{
    const y=PAD_Y+di*ROW_H;
    svg+=`<rect x="0" y="${y+18}" width="${W}" height="${NODE_H+12}" fill="${DIM_BG[d]}"/>`;
    svg+=`<text x="${PAD_X}" y="${y+14}" font-size="10" fill="${DIM_COLORS[d]}" font-weight="600">${d} — ${{D1:'AI Mfg Base',D2:'AI Connectivity',D3:'AI Infrastructure',D4:'AI Enablement',D5:'AI Applications'}[d]}</text>`;
  });

  // edges
  DATA.edges.forEach((e,ei)=>{
    const fg=nslug(e.from),tg=nslug(e.to);
    if(!fg||!tg||!pos[fg]||!pos[tg])return;
    const sp=pos[fg],tp=pos[tg];
    const isChk=e.chokepoint==='Y';
    const col=isChk?'#d4a017':(FLOW_COLOR[e.flow]||'#58a6ff');
    const sw=isChk?2.5:1.5;
    const mId=isChk?'arr-chk':`arr-${e.flow}`;
    const animClass=e.flow==='Material'?'slow':e.flow==='Signal'?'fast':'';
    let d2;
    if(sp.y===tp.y){
      // same row — horizontal arc
      const x1=sp.x+sp.nw,y1=sp.cy,x2=tp.x,y2=tp.cy;
      const cy=y1-40;
      d2=`M${x1},${y1} C${x1+30},${cy} ${x2-30},${cy} ${x2},${y2}`;
    } else if(sp.y<tp.y){
      // source above target
      const x1=sp.cx,y1=sp.y+NODE_H,x2=tp.cx,y2=tp.y;
      const dy=y2-y1;
      d2=`M${x1},${y1} C${x1},${y1+dy*.42} ${x2},${y2-dy*.42} ${x2},${y2}`;
    } else {
      // source below target
      const x1=sp.cx,y1=sp.y,x2=tp.cx,y2=tp.y+NODE_H;
      const dy=y1-y2;
      d2=`M${x1},${y1} C${x1},${y1-dy*.42} ${x2},${y2+dy*.42} ${x2},${y2}`;
    }
    svg+=`<path class="eco-edge anim ${animClass}" d="${d2}" fill="none" stroke="${col}" stroke-width="${sw}" marker-end="url(#${mId})" data-from="${fg}" data-to="${tg}" data-flow="${esc(e.flow)}" data-chk="${e.chokepoint}" opacity="0.75"/>`;
  });

  // nodes
  DATA.sectors.forEach(s=>{
    const p=pos[s.slug];
    if(!p)return;
    const outE=DATA.edges.filter(e=>nslug(e.from)===s.slug).length;
    const inE=DATA.edges.filter(e=>nslug(e.to)===s.slug).length;
    const chkE=DATA.edges.filter(e=>(nslug(e.from)===s.slug||nslug(e.to)===s.slug)&&e.chokepoint==='Y').length;
    const words=s.name.split(' ');
    let line1=s.name,line2='';
    if(s.name.length>14){
      const mid=Math.ceil(words.length/2);
      line1=words.slice(0,mid).join(' ');
      line2=words.slice(mid).join(' ');
    }
    svg+=`<g class="sector-node" data-slug="${s.slug}" onclick="selSec('${s.slug}')" transform="translate(${p.x},${p.y})">`;
    svg+=`<rect class="node-bg" width="${p.nw}" height="${NODE_H}" rx="8" fill="#161b22" stroke="#30363d" stroke-width="1"/>`;
    if(line2){
      svg+=`<text x="${p.nw/2}" y="22" text-anchor="middle" font-size="12" font-weight="600" fill="#e6edf3">${esc(line1)}</text>`;
      svg+=`<text x="${p.nw/2}" y="36" text-anchor="middle" font-size="12" font-weight="600" fill="#e6edf3">${esc(line2)}</text>`;
      svg+=`<text x="${p.nw/2}" y="52" text-anchor="middle" font-size="9" fill="${DIM_COLORS[s.dimension]}">${s.dimension}</text>`;
      svg+=`<text x="${p.nw/2}" y="65" text-anchor="middle" font-size="9" fill="#8b949e">${inE+outE} flows${chkE?' · ⬥'+chkE:''}</text>`;
    } else {
      svg+=`<text x="${p.nw/2}" y="28" text-anchor="middle" font-size="12" font-weight="600" fill="#e6edf3">${esc(s.name)}</text>`;
      svg+=`<text x="${p.nw/2}" y="44" text-anchor="middle" font-size="9" fill="${DIM_COLORS[s.dimension]}">${s.dimension}</text>`;
      svg+=`<text x="${p.nw/2}" y="60" text-anchor="middle" font-size="9" fill="#8b949e">${inE+outE} flows${chkE?' · ⬥'+chkE:''}</text>`;
    }
    svg+=`</g>`;
  });

  svg+=`</svg>`;
  gp.innerHTML=svg;

  // hover handlers
  document.querySelectorAll('.sector-node').forEach(g=>{
    g.addEventListener('mouseenter',()=>{if(!selSlug)applyStates(g.dataset.slug,false)});
    g.addEventListener('mouseleave',()=>{if(!selSlug)applyStates(null,false)});
  });

  applyFilter();
  if(selSlug)applyStates(selSlug,true);
}

// ── sector detail ─────────────────────────────────────────────────────────────
function selSec(slug){
  selSlug=slug;
  applyStates(slug,true);
  renderSec(slug);
  const dp=document.getElementById('dp');
  dp.classList.add('open');
  dp.scrollTop=0;
}

function renderSec(slug){
  const s=DATA.sectors.find(x=>x.slug===slug);
  if(!s)return;
  const outE=filt(DATA.edges.filter(e=>nslug(e.from)===slug));
  const inE=filt(DATA.edges.filter(e=>nslug(e.to)===slug));
  let h='';
  h+=`<button class="back-btn" onclick="goHome()">← Back</button>`;
  h+=bc([{label:'Ecosystem',action:'goHome()'},{label:s.name}]);
  h+=`<div class="dh">${esc(s.name)} ${dimBadge(s.dimension)}</div>`;
  h+=sec(`Supply Chain — ${s.tiers.length} Tiers`);
  s.tiers.forEach((t,i)=>{
    const cls=t.chokepoint==='Y'?'ck-Y':t.chokepoint==='Partial'?'ck-P':'';
    h+=`<div class="tc ${cls}" onclick="selTier('${esc(slug)}',${i})">`;
    h+=`<div class="tc-body"><div class="tc-name">${esc(t.tier)}</div>`;
    h+=`<div class="tc-fn">${esc(t.fn)}</div></div>`;
    if(t.chokepoint!=='No')h+=ckBadge(t.chokepoint);
    h+=`<span class="tc-arr">›</span></div>`;
  });
  if(outE.length){
    h+=sec(`→ Outbound Flows (${outE.length})`);
    outE.forEach(e=>{
      const tslug=nslug(e.to);
      h+=`<div class="ec">${flBadge(e.flow)}<span class="ec-sec" onclick="selSec('${esc(tslug||'')}')">${esc(e.to)}</span>${e.chokepoint==='Y'?'<span class="badge bCY">⬥Y</span>':''}`;
      h+=`<div class="ec-prod">${esc(e.product)}</div></div>`;
    });
  }
  if(inE.length){
    h+=sec(`← Inbound Flows (${inE.length})`);
    inE.forEach(e=>{
      const fslug=nslug(e.from);
      h+=`<div class="ec">${flBadge(e.flow)}<span class="ec-sec" onclick="selSec('${esc(fslug||'')}')">${esc(e.from)}</span>${e.chokepoint==='Y'?'<span class="badge bCY">⬥Y</span>':''}`;
      h+=`<div class="ec-prod">${esc(e.product)}</div></div>`;
    });
  }
  document.getElementById('dp').innerHTML=h;
}

// ── tier detail ───────────────────────────────────────────────────────────────
function selTier(sectorSlug,idx){
  const s=DATA.sectors.find(x=>x.slug===sectorSlug);
  if(!s)return;
  const t=s.tiers[idx];
  if(!t)return;
  const tierEdges=DATA.edges.filter(e=>e.from_tier===t.tier||e.to_tier===t.tier);
  let h='';
  h+=`<button class="back-btn" onclick="selSec('${esc(sectorSlug)}')">← Back</button>`;
  h+=bc([{label:'Ecosystem',action:'goHome()'},{label:s.name,action:`selSec('${esc(sectorSlug)}')`},{label:t.tier}]);
  h+=`<div class="dh tier">${esc(t.tier)} ${ckBadge(t.chokepoint)}</div>`;
  h+=`<div class="dd">${esc(t.fn)}</div>`;
  h+=`<div class="meta-row">`;
  h+=`<span class="pill">Moat: ${esc(t.moat_type)}</span>`;
  h+=`<span class="pill">CapEx: ${esc(t.capital_intensity)}</span>`;
  h+=`<span class="pill">Margin: ${esc(t.margin_profile)}</span>`;
  h+=`</div>`;
  if(tierEdges.length){
    h+=sec(`Cross-Sector Flows Through This Tier (${tierEdges.length})`);
    tierEdges.forEach(e=>{
      const isOut=e.from_tier===t.tier;
      const counterSlug=isOut?nslug(e.to):nslug(e.from);
      const counterName=isOut?e.to:e.from;
      h+=`<div class="ec">${isOut?'→':'←'} ${flBadge(e.flow)}<span class="ec-sec" onclick="selSec('${esc(counterSlug||'')}')">${esc(counterName)}</span>${e.chokepoint==='Y'?'<span class="badge bCY">⬥Y</span>':''}`;
      h+=`<div class="ec-prod">${esc(e.product)}</div></div>`;
    });
  } else {
    h+=sec('Cross-Sector Flows');
    h+=`<div class="ec"><span style="color:var(--muted);font-size:12px">No cross-sector flows mapped to this tier</span></div>`;
  }
  const dp=document.getElementById('dp');
  dp.innerHTML=h;
  dp.scrollTop=0;
}

// ── navigation ────────────────────────────────────────────────────────────────
function goHome(){
  selSlug=null;
  document.getElementById('dp').classList.remove('open');
  document.getElementById('dp').innerHTML='<div class="empty"><div class="empty-icon">◈</div><div>Click a sector node to explore its supply chain and cross-sector flows</div></div>';
  document.querySelectorAll('.sector-node').forEach(g=>{
    const r=g.querySelector('rect');
    r.setAttribute('fill','#161b22');r.setAttribute('stroke','#30363d');r.setAttribute('stroke-width','1');g.style.opacity='1';
  });
  document.querySelectorAll('.eco-edge').forEach(el=>{el.style.opacity='0.75'});
}

// ── init ──────────────────────────────────────────────────────────────────────
window.addEventListener('DOMContentLoaded',buildGraph);
let _rt;
window.addEventListener('resize',()=>{clearTimeout(_rt);_rt=setTimeout(()=>{buildGraph();if(selSlug)applyStates(selSlug,true)},120)});
JSEOF
```

---

### Chunk D — Append closing tags (cat >> appends)

```bash
cat >> Investing/Output/Dashboard/index.html << 'CLOSEEOF'
</script>
</body>
</html>
CLOSEEOF
```

---

## Phase 5 — Write dated copy and deploy

### 5A — Write dated copy

```bash
cp Investing/Output/Dashboard/index.html Investing/Output/Dashboard/[DATE].html
```

### 5B — If `--no-push` flag is set, stop here.

### 5C — Deploy to `gh-pages`:

```bash
git stash
git checkout gh-pages
cp Investing/Output/Dashboard/index.html index.html
git add index.html
git commit -m "Deploy ecosystem map [DATE]"
git push -u origin gh-pages
git checkout -
git stash pop
```

### 5D — Commit dashboard files to the current feature branch:

```bash
git add Investing/Output/Dashboard/index.html Investing/Output/Dashboard/[DATE].html
git commit -m "Dashboard: ecosystem map [DATE]"
git push -u origin HEAD
```
