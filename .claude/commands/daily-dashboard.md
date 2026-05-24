# Daily Dashboard — KB Visualization Hub

Generates a self-contained HTML knowledge base visualization — a navigable, multi-view SPA with macro → sector → ticker drill-down and ecosystem supply chain maps — then deploys it to the `gh-pages` branch.

**Dashboard URL:** `https://investing-wiki.netlify.app`
*Netlify watches the `gh-pages` branch — every push auto-deploys within ~30 seconds.*
*Cloudflare Access gates the URL — only your email can log in.*

**Input flags:**
- *(none)* — use today's digest; push to gh-pages
- `--date YYYY-MM-DD` — render a specific digest date
- `--no-push` — generate HTML locally only, skip gh-pages deployment

---

## Phase 1 — Load core references (4 parallel reads)

Run these reads in parallel:

**1A — Read Watchlist.md** (`Investing/Wiki/Reference/Watchlist.md`)

Extract:
- `portfolio[]` — tickers in Core Holdings table (active positions)
- `rockets[]` — tickers in High Upside Rockets section
- `compounders[]` — tickers in Compounders Watchlist section
- `macro_pulse` — JSON block at bottom (VIX, S&P level, backdrop, sector_regime, one_liner, timestamp). If absent, set null.

**1B — Read Monitor Registry** (`Investing/Wiki/Reference/Monitor Registry.md`)

Build map: `ticker → { company, sector, path, cik, exchange }` from all sector tables. Also extract the sector list in order.

**1C — Find and read digest**

Target date: `--date` arg if supplied, else today. Find `Investing/Output/Digest/[DATE]-daily-news.md`; if missing, glob for the most recent file in that folder. Note any date delta.

Parse:
- Summary table rows → `{ impact, ticker, category, headline, summary }`
- Per-ticker `### TICKER` blocks → `{ ticker, headline, source, summary, detail }`

**1D — Read Sentiment Index** (`Investing/Wiki/Reference/Sentiment Index.md`)

Parse the Ticker Mentions Summary table → `{ ticker, status, mentions, last_signal_date }` for each row.

Also parse the Recent Signals feed (last 30 lines) → for each entry extract the date and ticker list.

---

## Phase 2 — Read sector maps, matrices, and ecosystem files (parallel)

Run all reads in this phase in parallel.

**2A — Read Supply Chain Maps**

For each sector in the registry, attempt to read `Investing/Wiki/Sectors/[Sector]/_Supply Chain Map.md`.

If found, parse:
- **Value Chain table** (`## Value Chain` section) → each row: `{ tier, function, chokepoint, capital_intensity, moat_type, margin_profile }`
- **Publicly-Traded Nodes table** (`## Publicly-Traded Nodes` section) → each row: `{ tier, ticker, company, mkt_cap, in_registry, notes }`. Gap rows (ticker = "—") → `{ tier, ticker: null, gap: true, notes }`
- **Structural Gaps section** → array of `{ tier_name, description }` strings
- **Framework Status checklist** → `{ mapped, nodes_registered, ground_truth, matrix_built, framework_written }` — each `true` if the line is `- [x]`, else `false`

Store as `supply_chains[sector_name] = { tiers, nodes, gaps, framework_status }`. If file missing, store `null`.

**2B — Read Customer Matrices**

For each sector in the registry, attempt to read `Investing/Wiki/Sectors/[Sector]/_Customer Matrix.md`.

If found, parse the `## Heat Map Metadata` JSON block (the fenced ```json block at the bottom of the file) → parse as JSON directly into `customer_matrices[sector_name]`. Structure: `{ sector, built, customers: [], rows: [{ ticker, company, layer, cells: { CustomerName: { score, display, source, note } } }] }`.

If the JSON block is missing or malformed, fall back to parsing the `## Dependency Table` markdown table rows manually: extract ticker, layer, and cell values (star ratings → numeric: ★=1, ★★=2, ★★★=3, ★★★★=4, ★★★★★=5, blank=0).

If file missing, store `null`.

**2C — Read ecosystem map files**

List all files matching `Investing/Wiki/Reference/Ecosystem Maps/*.md`.

For each file found, read it and parse:
- File name → derive the ecosystem name (e.g., "NVDA Ecosystem Map.md" → ecosystem `nvda`, anchor ticker `NVDA`)
- **Tier tables**: each `## Tier N` section → tier label + table rows of `{ ticker, company, relationship, notes }`
- **Shockwave / functional category sections**: any `##` section after the tiers → category name + table rows
- Store as `ecosystems[name] = { anchor, tiers: { 1: [...], 2: [...], ... }, categories: { name: [...] } }`

If no ecosystem map files exist, continue with empty `ecosystems = {}`.

---

## Phase 3 — Read sector frameworks (parallel)

For each sector in the registry, read `Investing/Wiki/Sectors/[Sector]/_Sector Framework.md`.

Extract:
- First non-header paragraph → `sector_description` (1–3 sentences)
- Any "Value Chain" or "Archetype" section → `value_chain_summary` (first sentence or bullet)

Store as `sector_meta[sector_name] = { description, value_chain_summary }`.

If a framework file is missing for a sector, set description to null and continue.

---

## Phase 4 — Read all monitored ticker pages (parallel batches of 8)

For each ticker in the Monitor Registry `path` map, read the wiki page. Run in parallel batches of 8.

For **portfolio tickers** (in `portfolio[]`), extract all of:
- `one_line_thesis` — sentence under `## One-Line Thesis`
- `drift_status` — `Drift status:` line value ("On track — ...", "Drifting — ...", "Broken — ...", or "—")
- `last_validated` — `Last validated:` date
- `scoring` — from Scoring Summary section: composite score + all 6 criterion scores. If section is blank or absent, set `scoring: null`.
- `catalysts` — all items from Catalyst Timeline, each as `{ text, checked: true/false }`
- `conviction_log` — last 3 rows of Conviction Log table: `{ date, event, direction, why }`
- `news` — last 5 entries from News & Alpha Log: `{ date, headline, detail, impact }`. Parse impact number from any "impact N" annotation.
- `earnings` — most recent row from Earnings & Financials table: `{ period, revenue, eps, guidance }`
- `analyst_coverage` — all rows from Analyst Coverage table (may be empty)
- `cross_ticker_signals` — all rows from Cross-Ticker Signals table: `{ date, source, direction, target, signal, implication }`
- `social_mentions` — last 5 rows from Social Mentions table: `{ date, signal_slug, source }`
- `investment_thesis` — full text of Investment Thesis section (first 400 chars for detail page; preserve paragraphs)
- `management` — Management & Leadership table rows: `{ name, role, note }`

For **watchlist/rocket/compounder tickers** (not in portfolio), extract a lighter set:
- `one_line_thesis`, `drift_status`, `scoring` (composite only), `news` (last 2 entries), `social_mentions` (last 2), `cross_ticker_signals`

For **any ticker in the digest not in the registry**: skip wiki read; mark as `{ tracked: false }`.

### Recommendation signal (portfolio tickers only)

Apply decision matrix (first match wins):

| Drift status | Conviction trend (last 3) | Digest impact | → Signal |
|---|---|---|---|
| Broken | any | any | TRIM |
| Drifting | ↓ majority | any | TRIM |
| Drifting | any | any | WATCH |
| On track | ↑ majority | ≥ 4 | ADD |
| On track | ↑ majority | 1–3 | HOLD |
| On track | → neutral | any | HOLD |
| On track | ↓ majority | any | WATCH |
| — (not set) | any | any | HOLD |

**Conviction trend**: count ↑ vs ↓ in last 3 conviction log entries. ↑ > ↓ → bullish; ↓ > ↑ → cautionary; else neutral.

**Confidence**:
- High: drift_status set + conviction_log ≥ 2 entries + scoring populated
- Medium: drift_status set + (conviction_log ≥ 1 entry OR scoring populated)
- Low: otherwise

**Rationale**: 2–3 sentences synthesizing drift, latest catalyst, and what changes the signal. Active voice, no filler.

---

## Phase 5 — Build unified data model

Assemble the `KB` object that will be embedded as JSON in the HTML:

```
KB = {
  meta: {
    date,                    // digest date
    generated_at,            // ISO timestamp
    vix,                     // from macro_pulse or null
    market_level,            // S&P from macro_pulse or null
    regime_label,            // e.g. "Tech-Favorable / Goldilocks"
    regime_color             // "green" | "amber" | "red" based on VIX
  },
  digest: {
    date,
    items: [{ impact, ticker, category, headline, summary, detail, sector }]
  },
  sectors: [
    {
      slug,                  // kebab-case, e.g. "semiconductors"
      name,                  // display name from registry
      description,           // from sector framework
      value_chain,           // from sector framework
      ticker_symbols,        // all tickers registered in this sector
      top_news,              // digest items where ticker is in this sector
      supply_chain: {        // from _Supply Chain Map.md — null if file absent
        tiers,               // [{ tier, function, chokepoint, capital_intensity, moat_type, margin_profile }]
        nodes,               // [{ tier, ticker, company, mkt_cap, in_registry, notes, gap }]
        gaps,                // [{ tier_name, description }]
        framework_status     // { mapped, nodes_registered, ground_truth, matrix_built, framework_written }
      },
      customer_matrix        // parsed JSON from _Customer Matrix.md — null if file absent
                             // { customers[], rows[{ ticker, layer, cells }] }
    }
  ],
  tickers: {                 // keyed by symbol
    "NVDA": {
      symbol, name, sector, sector_slug,
      layer,                 // supply chain tier label from _Supply Chain Map.md nodes table — null if absent
      chokepoint,            // true/false from supply chain tiers table — null if absent
      tracked: true,
      in_portfolio, in_rockets, in_compounders,
      one_line_thesis,
      investment_thesis,
      drift_status,
      last_validated,
      scoring,               // { composite, criteria: { moat, management, growth, balance_sheet, valuation, momentum } } or null
      catalysts,             // [{ text, checked }]
      conviction_log,        // [{ date, event, direction, why }] last 3
      news,                  // [{ date, headline, detail, impact }] last 5
      earnings,              // { period, revenue, eps, guidance }
      analyst_coverage,      // [{ firm, analyst, pt, rating, date }]
      cross_ticker_signals,  // [{ date, source, direction, target, signal, implication }]
      social_mentions,       // [{ date, signal_slug, source }]
      social_mention_count,  // from Sentiment Index
      social_last_signal,    // from Sentiment Index
      management,            // [{ name, role, note }]
      recommendation: { signal, confidence, rationale },  // portfolio only
      ecosystem: {
        upstream: [{ symbol, relationship, implication }],
        downstream: [{ symbol, relationship, implication }]
      }
    }
  },
  ecosystem_graph: {
    nodes: [{ id, label, sector, in_portfolio, in_watchlist }],
    edges: [                 // all relationship edges from all sources
      {
        source, target,
        type,               // "cross_ticker_signal" | "ecosystem_map" | "sentiment_relationship"
        direction,          // "emits" | "receives"
        relationship_type,  // "supplier" | "customer" | "design_win" | "investor" | "partner" | null
        implication
      }
    ],
    ecosystems: {            // keyed by anchor ticker symbol
      "NVDA": {
        tiers: { "1": [{ ticker, company, relationship, notes }], ... },
        tier_labels: { "1": "Direct Supply Chain", ... }
      }
    }
  },
  sentiment: {
    hot_tickers: [...],      // top 5 by mentions in last 7 days
    by_ticker: {             // keyed by symbol
      "NVDA": { mentions, last_signal_date, velocity_label }
      // velocity_label: "↑ active" | "→ steady" | "↓ quiet"
    }
  }
}
```

**Building ecosystem edges:**

1. From each ticker's `cross_ticker_signals`: each row → one edge `{ source: signal.source, target: signal.target, type: "cross_ticker_signal", direction: signal.direction, implication: signal.implication }`
2. From ecosystem map tiers: each ticker in a tier → edge from that tier's anchor (e.g., NVDA) with `type: "ecosystem_map"` and `relationship_type` from the Relationship column
3. From sentiment signal notes (read the 10 most recent `.md` files in `Investing/Raw/Sentiment/` that have non-empty `relationships:` fields): each relationship entry → edge with `type: "sentiment_relationship"` and `relationship_type` from the `type` field

**Building each ticker's upstream/downstream:**
- `upstream`: all edges where `target === this ticker` → each entry's source, with its relationship and implication
- `downstream`: all edges where `source === this ticker` → each entry's target, with its relationship and implication

**Building sentiment.hot_tickers:**
- From Sentiment Index data: filter to signals with `last_signal_date` within last 7 days; sort by `mentions` descending; take top 5.
- For `velocity_label`: compare `last_signal_date` to 14 days ago — if signal within 7 days → "↑ active"; within 14 days → "→ steady"; older → "↓ quiet".

---

## Phase 6 — Generate HTML

Produce a **single self-contained HTML file** — no CDN links, no external scripts. All CSS and JS inline. Must work at `file://` and on GitHub Pages.

### Design system

```css
:root {
  --bg:      #0d1117;
  --bg2:     #161b22;
  --bg3:     #21262d;
  --text:    #e6edf3;
  --muted:   #8b949e;
  --border:  #30363d;
  --amber:   #d4a017;
  --green:   #3fb950;
  --blue:    #58a6ff;
  --red:     #f85149;
  --orange:  #e3812b;
  --yellow:  #d29922;
  --purple:  #bc8cff;
  --pink:    #ff7b72;
}
```

Signal badge colors:
- ADD → `--green` bg, dark text
- HOLD → `--blue` bg, dark text (use `#1f6feb` for the bg, white text)
- TRIM → `--red` bg, white text
- WATCH → `--yellow` bg, dark text

Impact pill colors (impact 5→1): `--red`, `--orange`, `--yellow`, `--muted`, `--muted`

Relationship edge colors in ecosystem:
- `ecosystem_map` edge: `--amber`
- `cross_ticker_signal` edge: `--blue`
- `sentiment_relationship` edge: `--purple`

### SPA architecture

Embed the full `KB` JSON as `const KB = {...};` in a `<script>` block.

Implement a hash router:

```javascript
function navigate(hash) {
  history.pushState(null, '', hash || '#');
  renderView(hash);
}

window.addEventListener('hashchange', () => renderView(location.hash));
window.addEventListener('load', () => renderView(location.hash));

function renderView(hash) {
  const app = document.getElementById('app');
  if (!hash || hash === '#' || hash === '#macro') {
    renderMacro(app);
  } else if (hash.startsWith('#sector/')) {
    const slug = hash.slice(8);
    renderSector(app, slug);
  } else if (hash.startsWith('#ticker/')) {
    const sym = hash.slice(8).toUpperCase();
    renderTicker(app, sym);
  } else {
    renderMacro(app);
  }
}
```

**Navigation links**: all internal `<a>` tags use `href="#sector/slug"` or `href="#ticker/SYMBOL"`. Never reload the page.

**Back breadcrumb**: rendered at top of each view. Sector view: `Macro > [Sector]`. Ticker view: `Macro > [Sector] > [TICKER]`. Each segment is a clickable link.

### Global structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Investing KB · [Date]</title>
  <style>/* all CSS inline */</style>
</head>
<body>
  <header id="site-header"><!-- sticky header --></header>
  <div id="app"><!-- view rendered here by JS --></div>
  <script>
    const KB = /* JSON data */;
    /* router + view functions */
  </script>
</body>
</html>
```

**Sticky header** (always visible):
```
INVESTING KB · [Date]         [VIX badge] [S&P badge] [Regime label]
```
Right side on desktop: VIX value with color (green <20, amber 20–30, red >30), S&P level, regime label. On mobile: stacks vertically, smaller text.

---

### View 1: Macro (landing)

```
[Breadcrumb: you are here]

╔══════════════════════════════════════════════════╗
║  MARKET PULSE                                    ║
║  [Regime label]  [VIX]  [S&P]  [Backdrop text]  ║
╚══════════════════════════════════════════════════╝

HOT SIGNALS (last 7 days)
[Ticker chip] [Ticker chip] [Ticker chip] ...
(from sentiment.hot_tickers — each chip links to #ticker/SYMBOL)

PORTFOLIO QUICK VIEW
[Horizontal scrollable strip of core holding cards]
Each card: TICKER · SIGNAL badge · one_line_thesis (truncated)
Click → #ticker/SYMBOL

TODAY'S DIGEST — [date]
[List of digest items, impact-sorted, max 15]
Each item: [Impact pill] [Ticker chip → #ticker/SYMBOL] [Sector chip → #sector/slug] [Headline]
           [Summary in muted text]

SECTORS
[Responsive grid: 3 cols desktop, 2 tablet, 1 mobile]
Each sector card:
  ┌─────────────────────────────────┐
  │ [Sector name]    [N tickers]   │
  │ [Health dot] [sector_description truncated to 80 chars]
  │ ─────────────────────────────── │
  │ Top news: [headline] (if any)  │
  └─────────────────────────────────┘
  Click → #sector/slug
  Health dot: green = no digest items with impact≥3; amber = highest impact 3–4; red = highest impact 5
```

**Portfolio quick view card** (compact, horizontal scroll on mobile):
- Width: ~280px fixed
- Signal badge (top right)
- Ticker symbol (bold, large)
- One-line thesis (italic, 2 lines max, truncated with ellipsis)
- Amber left border for portfolio items

**Sector card** styling:
- `--bg2` background, `--border` border
- Sector name in `--text`, description in `--muted`
- Health dot: 8px circle, colored
- Hover: `--bg3` background, slight lift (box-shadow)

---

### View 2: Sector

```
[Breadcrumb: Macro > [Sector Name]]

[Sector name heading]
[sector_description]
[value_chain_summary in muted text]
[N tickers registered]

[Tab bar: CHAIN MAP | CUSTOMER MATRIX | TICKERS | NEWS ]
                                           (default tab: CHAIN MAP if supply_chain data exists, else TICKERS)
```

#### Tab: CHAIN MAP

Render only if `sector.supply_chain` is non-null. If null, show: *"No supply chain map yet — run `/map-sector [Sector]` to generate one."*

**Swim-lane diagram** — CSS grid, one column per tier:

```
RAW MATERIALS   WAFER PROD    EDA / IP     EQUIPMENT    FOUNDRY    PACKAGING    DESIGN       TEST
──────────────  ──────────    ────────     ─────────    ───────    ─────────    ──────       ────
[4369.T]        [4043.T]      [SNPS]  ◆   [ASML]  ◆   [TSM]  ◆  [AMKR]       [NVDA]  ◆   [AEHR]  ◆
[ENTG]          [SK Hynix]    [CDNS]  ◆   [LRCX]      [GFS]      [ASX]        [AMD]        [COHU]
[ICHR]                        [ARM]   ◆   [AMAT]      [INTC]                  [MRVL]
                                          [KLAC]                              [MU]

[-- gap --]                                                                                  [-- gap --]
EUV Photoresist                                                                          Packaged Device Test
```

**Layout rules:**
- Each tier is a `<div class="tier-col">` with a header label at top
- Chokepoint tiers (`chokepoint: "Y"`) get a `--amber` top border on the column header; non-chokepoint get `--border`
- Each node is a `<button class="node-chip">` — clicking navigates to `#ticker/SYMBOL` if ticker is in KB; otherwise cursor is default and chip is dimmed
- Portfolio tickers: `--amber` left border on chip; rockets: `--orange`
- Gap nodes: dashed border, `--muted` text, not clickable — hover shows gap description as tooltip
- Chokepoint node badge: a small `◆` icon in `--amber` appended to the ticker label

**Relationship highlighting (JS, no SVG lines):**
When a node chip is clicked or hovered (desktop: hover; mobile: tap to toggle):
1. All edges in `ecosystem_graph.edges` + cross_ticker_signals where `source === TICKER` or `target === TICKER` are extracted
2. Upstream nodes (they supply to this ticker) → ring color `--green`
3. Downstream nodes (this ticker supplies to them) → ring color `--blue`
4. All unrelated nodes → opacity 0.25
5. A small tooltip appears below the hovered chip listing: upstream tickers (green label) and downstream tickers (blue label) with their implication text (truncated to 60 chars)
6. Click elsewhere / second tap → clears highlight state

**Relationship legend** (below diagram):
```
● Hover a node to highlight supply relationships
◆ Chokepoint tier    [amber border col header]
[green ring] = supplies this node    [blue ring] = this node supplies
[dashed box] = no public player (structural gap)
```

**Mobile (< 640px):** Tiers stack vertically (one tier per row, full width). Each tier header becomes a full-width label. Node chips wrap horizontally within their tier block. Highlight behavior unchanged.

**Framework status bar** — shown below the diagram as a compact progress strip:
```
[ ✓ Mapped ] [ ✓ Nodes ] [ ○ Ground Truth ] [ ○ Matrix ] [ ○ Framework ]
```
Each step is a small pill: `--green` if true, `--muted` if false. Clicking a false step shows a tooltip: "Run [command] to complete this step."

---

#### Tab: CUSTOMER MATRIX

Render only if `sector.customer_matrix` is non-null. If null, show: *"No customer matrix yet — run `/build-customer-matrix "[Sector]"` to generate one."*

**Heat map table:**

```
             │ Google │ Amazon │ Microsoft │ Meta │ Apple │ TSMC │ ...
─────────────┼────────┼────────┼───────────┼──────┼───────┼──────┼────
NVDA  Design │  ████  │  ███   │   ████    │  ██  │   █   │      │
ASML  Equip  │        │        │           │      │       │ █████│
LRCX  Equip  │        │        │           │      │       │ ████ │
MU    Memory │  ███   │  ████  │   ███     │  ██  │  ███  │      │
AMKR  OSAT   │        │        │           │      │       │ ████ │
```

- Each cell is a `<td>` with a filled bar: width proportional to score (score/5 × 100%), color from `--amber` (score 1–2) → `--orange` (score 3) → `--red` (score 4–5)
- Score 0 → empty cell, `--bg2` background
- Hover any cell → tooltip: `{ display, source, note }` from the JSON metadata
- Row header = `[TICKER]` + small `[Layer]` badge
- Column headers = customer names
- Click row header → navigate to `#ticker/SYMBOL`

**Critical Paths block** — below the table, show the `## Critical Paths` text from the matrix file (if present) in a styled callout box with `--amber` left border.

**Built date** shown as muted text below the table: *"Matrix built [date] — refresh with `/build-customer-matrix "[Sector]"`"*

---

#### Tab: TICKERS

Existing ticker grid, unchanged:

```
[Responsive grid: 3 cols desktop, 2 tablet, 1 mobile]
Each ticker card:
  ┌───────────────────────────────────┐
  │ TICKER [Signal badge if portfolio]│
  │ [Company name]  [Layer badge]     │
  │ [Score badge if scored: N.N/10]   │
  │ [Sentiment badge: N signals ↑]    │
  │ ─────────────────────────────────│
  │ [one_line_thesis, 2 lines max]    │
  └───────────────────────────────────┘
  Click → #ticker/SYMBOL
```

**Layer badge** — new addition: small `--bg3` pill showing the supply chain tier label (e.g., `Equipment`, `Design`, `Foundry`). Shown only if `ticker.layer` is non-null.

**Ticker card** styling (unchanged except layer badge):
- Portfolio tickers: `--amber` left border (2px)
- Rockets: `--orange` left border
- Unregistered (stub): `--muted` left border, italic
- Score badge: small pill, color-coded: ≥8.0 `--green` · 6.0–7.9 `--blue` · 4.0–5.9 `--yellow` · <4.0 `--red`
- Sentiment badge: `--purple` if "↑ active", `--muted` if steady/quiet

---

#### Tab: NEWS

```
LATEST NEWS
[All digest items for this sector's tickers, impact-sorted]
Each: [Impact pill] [Ticker chip → #ticker/SYMBOL] [Category tag] [Headline]
      [Summary]
```

(Previously the only content in the sector view — now one of four tabs.)

---

### View 3: Ticker Detail

```
[Breadcrumb: Macro > [Sector] > [TICKER]]

┌─ Header ──────────────────────────────────────────────────┐
│ TICKER  CompanyName                                        │
│ [Sector chip] [In Portfolio / Rocket / Watchlist badge]   │
│ [Signal badge] [Confidence pill]  if portfolio            │
└───────────────────────────────────────────────────────────┘

[Rationale block — 2-3 sentences] if portfolio ticker

SUPPLY CHAIN POSITION   [if ticker.layer is non-null]
[Layer badge: e.g. "Equipment"] [Chokepoint ◆ badge if chokepoint=true]
[Sector name → #sector/slug] › [Layer label]
(Click the sector link to open the Chain Map tab pre-highlighted on this ticker)

ONE-LINE THESIS
[one_line_thesis]

INVESTMENT THESIS
[investment_thesis text, up to 400 chars, with "Read more" toggle for full text]
Drift: [drift_status value] · Last validated: [last_validated]

MANAGEMENT
[Table: Name | Role | Note]
(if management data present; else omit section)

SCORING   [if scoring !== null]
Composite: N.N / 10 · [label: Unrivaled / Strong / Moderate / Developing]
[6-criterion grid:]
  Moat: N/10    Management: N/10    Growth: N/10
  Balance Sheet: N/10    Valuation: N/10    Momentum: N/10
[Each criterion shown as a labeled bar: filled portion colored by value]
[if scoring is null:]
Scoring not yet run — use /score-ticker [SYMBOL] to populate.

CATALYST TIMELINE
[Checkbox list of all catalysts]
[Unchecked items in --text; checked items in --muted with strikethrough]

EARNINGS & FINANCIALS
[Table: Period | Revenue | EPS | Guidance]
(if empty: "No earnings data logged yet")

NEWS & ALPHA LOG (last 5)
[Each entry:]
  [Date badge] [Impact pill if available]
  [Headline — bold]
  [Detail text in --muted]

CONVICTION LOG (last 3)
[Each entry:]
  [Date] [Direction arrow ↑/↓/→ colored green/red/gray]
  [Event name]
  [Why, in muted text]

ANALYST COVERAGE
[Table: Firm | Analyst | Rating | PT | Date]
(if empty: "No analyst coverage logged")

SOCIAL SENTIMENT
[N total signals] [velocity_label badge]  [Last: date]
[Last 5 signal slugs as a compact list]

ECOSYSTEM — SUPPLY CHAIN RELATIONSHIPS
[See ecosystem panel spec below]
```

**"Read more" toggle for investment thesis**: Show first 400 chars + "… [expand]" link. Click reveals full text. Pure CSS `<details><summary>` element for zero JS.

**Scoring criterion bar**: 40px-wide label + `<div>` bar scaled to N/10. Bar fill colors:
- ≥8: `--green`; 6–7: `--blue`; 4–5: `--yellow`; <4: `--red`

---

### Ecosystem Panel (within ticker detail view)

**Case A: Ticker has an explicit ecosystem map** (e.g., NVDA)

Render a **responsive SVG tier diagram**:

```
Tier 1 — Direct Supply Chain
  [Chip] [Chip] [Chip] [Chip]

Tier 2 — Infrastructure & Deployment
  [Chip] [Chip] [Chip] [Chip]

Tier 3 — Networking & Interconnect
  [Chip] [Chip] [Chip]

Tier 4 — Power & Energy
  [Chip] [Chip] [Chip]

Tier 5 — Software & Platforms
  [Chip] [Chip] [Chip] [Chip]
```

Each "Chip" is a `<button>` styled as a rounded rectangle:
- Background: sector color (assign each sector a distinct muted hue derived from `--bg3` + sector index offset)
- Text: ticker symbol (bold) + company name (smaller, muted) on hover via tooltip `<title>` + `rel`
- If ticker is in KB: `onclick="navigate('#ticker/SYMBOL')"` and a small arrow indicator
- If ticker is NOT in KB: dimmed, no click, tooltip shows company name only
- Width: fit-content (min 80px, max 160px); wrap within tier row

Layout:
- Desktop: each tier is a horizontal flex row with `flex-wrap: wrap` and a left-aligned label
- Mobile (< 640px): each tier label is full-width, chips wrap below it — same layout but tighter spacing
- Anchor ticker (e.g., NVDA): shown as a large centered chip between Tier 2 and Tier 3 with `--amber` border, labeled "● THIS POSITION"

Connecting lines: Use a `<canvas>` overlay or pure CSS `::before`/`::after` to draw subtle vertical dotted lines between tiers (optional — omit if it adds significant complexity; the tier labels convey hierarchy clearly enough).

**Case B: Ticker has cross-ticker signal edges only**

Render a **3-zone layout** (no SVG canvas needed):

```
UPSTREAM (supplies to / enables [TICKER])
  ┌──────────┐    ┌──────────┐
  │  SYMBOL  │    │  SYMBOL  │
  │ rel type │    │ rel type │
  └──────────┘    └──────────┘

              ● [TICKER]
         [This position]

DOWNSTREAM ([TICKER] enables / supplies to)
  ┌──────────┐    ┌──────────┐    ┌──────────┐
  │  SYMBOL  │    │  SYMBOL  │    │  SYMBOL  │
  │ rel type │    │ rel type │    │ rel type │
  └──────────┘    └──────────┘    └──────────┘
```

Chips in 3-zone view use same styling as Case A. The implication text from the edge is shown as a `<span title="...">` tooltip on hover (truncated to 60 chars inline).

A **legend** below the ecosystem panel shows edge source types with their colors (amber = ecosystem map, blue = cross-ticker signal, purple = sentiment signal).

**If no ecosystem edges at all**: show "No ecosystem relationships logged yet. Run /ticker-monitor --deep [SYMBOL] to scan for supply chain links."

**Mobile responsive for 3-zone**: Upstream and downstream chip groups stack vertically above/below the center ticker chip, maintaining the visual hierarchy.

---

## Phase 7 — Write files and deploy

### 7A — Write local output

1. Write `Investing/Output/Dashboard/index.html` (always overwrite)
2. Write `Investing/Output/Dashboard/[DATE].html` (if exists, append `-2`)

### 7B — Deploy to gh-pages (skip if `--no-push`)

Check if `gh-pages` branch exists:
```bash
git ls-remote --heads origin gh-pages
```

If not found, create it:
```bash
git checkout --orphan gh-pages
git rm -rf .
echo "# Investing Dashboard" > README.md
git add README.md
git commit -m "Init gh-pages"
git push origin gh-pages
git checkout -
```

Deploy via worktree (safe — does not switch the active branch):
```bash
git worktree add /tmp/gh-pages-deploy gh-pages
cp "Investing/Output/Dashboard/index.html" /tmp/gh-pages-deploy/index.html
cp "Investing/Output/Dashboard/[DATE].html" /tmp/gh-pages-deploy/[DATE].html
cd /tmp/gh-pages-deploy
git add index.html [DATE].html
git commit -m "Dashboard [DATE]"
git push -u origin gh-pages
cd -
git worktree remove /tmp/gh-pages-deploy
```

### 7C — Print completion summary

```
✅ Dashboard generated — [DATE]

   📊 Portfolio:    N positions · N recommendations
   🗺  Sectors:     N sectors · N monitored tickers
   🏗️  Chain maps:  N sectors with supply chain map · N structural gaps flagged
   🔥 Matrices:    N sectors with customer matrix · N high-concentration cells
   📰 Digest:       N tickers · N high-impact
   🔗 Ecosystem:    N edges (M from maps, K from signals, J from sentiment)
   🔥 Hot signals:  [ticker list]

   📁 Local:   Investing/Output/Dashboard/index.html
   🌐 Live:    https://investing-wiki.netlify.app

   Portfolio:
   • TICKER — ADD  (High) — [rationale first sentence]
   • TICKER — HOLD (Medium)
   ...
```

---

## Rules

- **Self-contained HTML.** No CDN links, no external scripts or fonts. Must render offline and on GitHub Pages.
- **No wiki page writes.** Read-only on the vault — never appends to ticker pages or registry.
- **Graceful degradation.** Missing wiki page → skip, note gap in header. Missing ecosystem map → fall back to cross-ticker signals. Missing scoring → show "not yet scored" block. Missing digest → render without digest section.
- **Portfolio first.** Core Holdings always appear in the portfolio strip regardless of digest coverage.
- **No hallucinated prices.** Only display prices, market caps, or percentage changes that appear explicitly in the digest or wiki pages.
- **Date accuracy.** Display digest date and generation date separately if they differ.
- **Mobile first.** All layouts must work at 375px viewport. Use `min-width` media queries to add columns for larger screens.
- **Accessible chips.** All clickable chips must be `<button>` or `<a>` elements, never `<div>` with click handlers. Include `aria-label` attributes.
- **Worktree awareness.** Git deployment commands must reference the main repo root. All file read/write paths are relative to the repo root.
