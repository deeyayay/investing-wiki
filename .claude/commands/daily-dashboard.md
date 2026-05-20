# Daily Dashboard — Investing Intelligence Hub

Generates a self-contained HTML dashboard from the latest daily news digest and ticker wiki pages, then deploys it to the `gh-pages` branch for viewing at `https://investing-wiki.netlify.app`.

**Dashboard URL:** `https://investing-wiki.netlify.app` (or your custom Netlify subdomain)
*Netlify watches the `gh-pages` branch — every push auto-deploys within ~30 seconds.*
*Cloudflare Access gates the URL — only your email can log in.*

**Input flags (``):**
- *(none)* — use today's digest; push to gh-pages
- `--date YYYY-MM-DD` — render a specific digest date instead of today's
- `--no-push` — generate HTML locally only, skip git branch switching and push

---

## Phase 1 — Load context (reads only, no searches)

### 1A — Read Watchlist.md
Read `Investing/Wiki/Reference/Watchlist.md`.

Extract:
- **`portfolio[]`** — all tickers from the **Core Holdings** table (these are active positions the user owns)
- **`watchlist[]`** — all other tickers from all other tables (High Upside Rockets, Compounders, Photonics subsections)
- **`macro_pulse`** — the JSON block at the bottom of the file (VIX, backdrop, top_catalysts, sector_regime, one_liner, timestamp). If not present, set to null.

### 1B — Read Monitor Registry
Read `Investing/Wiki/Reference/Monitor Registry.md`.

Build map: `ticker → { company, sector, path, cik, exchange }` from all sector tables.

### 1C — Find and read digest
Determine the target date:
- If `--date YYYY-MM-DD` is supplied, use that date.
- Otherwise, use today's date.

Look for `Investing/Output/Digest/[DATE]-daily-news.md`. If not found, use Glob to find the most recent digest file in `Investing/Output/Digest/`. Note any date delta in the dashboard header (e.g., "Digest from 2 days ago").

Read the digest file. Parse:
- **Summary table**: each row → `{ impact, ticker, category, headline, summary }`
- **Per-ticker detail blocks**: each `### TICKER` section → `{ ticker, headline, source, summary, detail, snippet }`

If no digest file exists at all: render the dashboard without the digest feed section, and note the absence in the header.

---

## Phase 2 — Read ticker wiki pages (parallel)

### Portfolio tickers — full read (~5 tickers, Core Holdings)
For each ticker in `portfolio[]` that appears in the registry map:

Read its wiki page at the `path` from the registry. Extract:
- **one_line_thesis** — the sentence under `## One-Line Thesis`
- **drift_status** — the `Drift status:` line from the Investment Thesis block (format: "On track — [reason]" or "Drifting — [reason]" or "Broken — [reason]")
- **last_validated** — date from `Last validated:` line
- **conviction_log** — last 3 rows of the Conviction Log table: `{ date, event, direction (↑/↓/→), why }`
- **catalysts_pending** — first 2 unchecked `- [ ]` items from Catalyst Timeline
- **news_latest** — latest 2 entries from News & Alpha Log (date + headline + why_it_matters)
- **scoring_composite** — composite score from Scoring Summary table if populated (not `—`)
- **analyst_coverage** — last 1–2 lines from Analyst Coverage section

### Watchlist tickers — light read
For each ticker in `watchlist[]` that appears in the registry map:

Read its wiki page. Extract:
- **one_line_thesis**
- **drift_status** (just the status word: "On track" / "Drifting" / "Broken" / "—")
- **last_research_log_entry** — last line of Research Log

---

## Phase 3 — Synthesize analyst recommendations

For each portfolio holding, generate a recommendation using the data extracted in Phase 2.

### Signal logic

Apply this decision matrix in order (first match wins):

| Drift status | Conviction trend (last 3) | Today's news impact | → Signal |
|---|---|---|---|
| Broken | any | any | TRIM |
| Drifting | ↓ majority | any | TRIM |
| Drifting | any | any | WATCH |
| On track | ↑ majority | ≥ 4 | ADD |
| On track | ↑ majority | 1–3 | HOLD |
| On track | → neutral | any | HOLD |
| On track | ↓ majority | any | WATCH |
| — (not set) | any | any | HOLD |

**Conviction trend**: from the last ≤3 conviction log entries. Count ↑ vs ↓ — if ↑ > ↓ → bullish; ↓ > ↑ → cautionary; otherwise neutral. If conviction log is empty, treat as neutral.

**Today's news impact**: look up this ticker in the digest summary table. Use its impact score. If not in digest, treat as 1.

### Confidence level

- **High**: drift status is set + conviction log has ≥2 entries + scoring composite is populated
- **Medium**: drift status is set + conviction log has ≥1 entry (or scoring composite populated)
- **Low**: most fields are empty/default

### Rationale

Write 2–3 sentences synthesizing:
1. Thesis drift and conviction direction — what the KB says about where this name stands
2. Most relevant near-term catalyst (next unchecked item) or latest news signal
3. What would change the signal (threshold for upgrade or downgrade)

Keep it crisp. No filler. Active voice. Treat this as a sell-side morning note bullet.

---

## Phase 4 — Generate HTML dashboard

Produce a **single self-contained HTML file** — no external CDN links, no imports, no build step. All CSS and JS are inline. Must render correctly when opened directly from the filesystem (file://) or served by GitHub Pages.

### Global design

- **Dark theme** by default: `#0d1117` background (GitHub dark), `#e6edf3` text, `#161b22` card backgrounds, `#30363d` borders
- **Accent colors**:
  - Portfolio items: `#d4a017` amber border (2px left border on cards)
  - Signal ADD: `#3fb950` green
  - Signal HOLD: `#58a6ff` blue
  - Signal TRIM: `#f85149` red
  - Signal WATCH: `#d29922` amber/yellow
  - Impact 5: `#f85149`; Impact 4: `#e3812b`; Impact 3: `#d29922`; Impact 1–2: `#6e7681`
- **Font**: system-ui stack (`-apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`)
- **Responsive**: CSS Grid for portfolio cards (auto-fill, min 300px), flexbox for digest rows

### Page structure

#### Header bar (always visible, sticky)
```
INVESTING BRIEF · [Date]
[VIX value if available] · [macro backdrop one-liner] · [N high-impact alerts]
```
Right side: small "Generated [datetime]" timestamp.

#### Navigation tabs
Four tabs: **Portfolio** | **Digest** | **Watchlist** | **Signals**

Tab switching via JS (show/hide divs — no page reload). Active tab underline in amber.

---

#### Tab 1: Portfolio

Section header: "Portfolio — Core Holdings" with subtext: "[N positions] · Recommendations generated from KB + latest digest"

Grid of recommendation cards, one per Core Holding. Each card:

```
┌─ [SIGNAL badge] ─────────────────── [Confidence] ┐
│ TICKER   CompanyName              [Sector tag]   │
│ [one-line thesis, italic]                         │
├───────────────────────────────────────────────────┤
│ RATIONALE (2-3 sentences, body text)              │
├───────────────────────────────────────────────────┤
│ Drift: [status] · Last validated: [date]          │
│ Conviction: [↑ / ↓ / →] [last event, 10 words]   │
│ Next catalyst: [first unchecked item]             │
│ Latest news: [headline from News & Alpha Log]     │
└───────────────────────────────────────────────────┘
```

Signal badge styling:
- ADD: green background `#3fb950`, white text, bold
- HOLD: blue background `#1f6feb`, white text
- TRIM: red background `#da3633`, white text
- WATCH: amber background `#9e6a03`, white text

Cards are sorted: TRIM first (most urgent), then WATCH, then ADD, then HOLD.

If today's digest has a news entry for this ticker with impact ≥ 4: add a small 🔴 alert indicator on the card with the headline.

---

#### Tab 2: Digest

Section header: "Today's Digest — [date]" with subtext from digest header (N tickers scanned, N high-impact)

Full digest feed, impact-sorted descending. Each row:

```
[Impact pill] [Ticker] [PORTFOLIO or WATCHLIST badge] [Category tag] [Headline]
              [Summary line in muted text]
```

Clicking a row expands it inline to show: Detail paragraph + Snippet (blockquote style).

Portfolio tickers get a gold `[PORTFOLIO]` badge. Watchlist tickers get a gray `[WATCHLIST]` badge. This is the primary visual distinction.

Impact pills:
- 5 🔴: `#f85149` red
- 4 🔴: `#e3812b` orange
- 3 🟡: `#d29922` yellow, dark text
- 2 ⚪: `#6e7681` gray
- 1 ⚪: `#6e7681` gray, "quiet"

Tickers not in registry (not fully onboarded) are still shown if they appear in the digest, labeled `[UNTRACKED]`.

---

#### Tab 3: Watchlist

Section header: "Watchlist — Monitored Names"

Sub-tabs or collapsible sections by sector (from Monitor Registry groupings).

Each watchlist ticker is a compact row (not a full card):
```
TICKER · CompanyName · [Drift status badge] · [one-line thesis]
[last research log entry in muted text, max 80 chars]
```

Drift status badges:
- "On track": green pill
- "Drifting": amber pill
- "Broken": red pill
- "—" or not set: gray pill "Not tracked"

Portfolio tickers are excluded from this tab (they appear in Tab 1).

---

#### Tab 4: Cross-Ticker Signals

Section header: "Ecosystem Signals"

Flat table with all cross-ticker signal data surfaced today. Source: parse each ticker's detail block in the digest for any ecosystem implication lines; also include the Cross-Ticker Signals tables from portfolio ticker wiki pages (extracted in Phase 2).

Table columns: Date | Source Ticker | Direction | Target Ticker | Signal (≤10 words) | Implication

Filter to signals from the last 7 days. Sort by date descending.

If no signals are found, show: "No cross-ticker signals logged in the past 7 days."

---

### JavaScript behavior

```javascript
// Tab switching
function showTab(name) {
  document.querySelectorAll('.tab-content').forEach(el => el.style.display = 'none');
  document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
  document.getElementById('tab-' + name).style.display = 'block';
  document.querySelector('[data-tab="' + name + '"]').classList.add('active');
}

// Digest row expand/collapse
document.querySelectorAll('.digest-row').forEach(row => {
  row.addEventListener('click', () => {
    row.querySelector('.digest-detail').classList.toggle('hidden');
  });
});
```

All JS is inline in the HTML file. No external scripts.

---

## Phase 5 — Write files and deploy

### 5A — Write to local output folder
1. Write `Investing/Output/Dashboard/index.html` (always overwrite — this is the "latest" copy)
2. Write `Investing/Output/Dashboard/[DATE].html` where DATE is the digest date (YYYY-MM-DD)
   - If this file already exists (duplicate run), append `-2` suffix

### 5B — Deploy to gh-pages (skip if `--no-push`)

**Check if gh-pages branch exists:**
```bash
git ls-remote --heads origin gh-pages
```
If no output: branch doesn't exist yet. Create it:
```bash
git checkout --orphan gh-pages
git rm -rf .
echo "# Investing Dashboard" > README.md
git add README.md
git commit -m "Init gh-pages"
git push origin gh-pages
git checkout -  # return to previous branch
```

**Deploy the dashboard:**

The dashboard is at `Investing/Output/Dashboard/index.html` inside the vault working tree. The gh-pages branch lives in the same repo but only holds dashboard files in its root.

Use `git worktree` to deploy without switching branches (safe for the active worktree):

```bash
# Add a temporary worktree for gh-pages
git worktree add /tmp/gh-pages-deploy gh-pages

# Copy dashboard files into it
cp "Investing/Output/Dashboard/index.html" /tmp/gh-pages-deploy/index.html
cp "Investing/Output/Dashboard/[DATE].html" /tmp/gh-pages-deploy/[DATE].html

# Commit and push
cd /tmp/gh-pages-deploy
git add index.html [DATE].html
git commit -m "Dashboard [DATE]"
git push origin gh-pages

# Cleanup
cd -
git worktree remove /tmp/gh-pages-deploy
```

Note: `git worktree add` must be run from the **main repo root** (not from inside the `.claude/worktrees/` worktree path). Use absolute path:
```bash
git -C "C:/Users/alexd/OneDrive/Documents/Obsidian Vault" worktree add /tmp/gh-pages-deploy gh-pages
```

### 5C — Print completion summary

```
✅ Dashboard generated — [DATE]

   📊 Portfolio:   N positions · N recommendations
   📰 Digest:      N tickers · N high-impact
   👁 Watchlist:   N tickers across N sectors
   🔗 Signals:     N cross-ticker signals

   📁 Local:    Investing/Output/Dashboard/index.html
   🌐 Live:     https://investing-wiki.netlify.app

   Portfolio recommendations:
   • TICKER — ADD  (Confidence: High) — [rationale first sentence]
   • TICKER — HOLD (Confidence: Medium)
   ...
```

---

## Rules

- **Self-contained HTML.** No CDN links, no external scripts, no web fonts. The file must render correctly in any browser, including offline.
- **No wiki page writes.** This skill is read-only on the vault — it never appends to ticker pages or the registry.
- **Graceful degradation.** If a ticker page doesn't exist or can't be read, skip it and note the gap in the dashboard header rather than failing the entire run.
- **Portfolio first.** Core Holdings always appear in Tab 1 regardless of whether they had news today. Never demote a portfolio holding to watchlist-only view.
- **No hallucinated prices.** Do not fabricate current stock prices, market cap, or percentage changes. Only display data that appears explicitly in the digest or wiki pages.
- **Date accuracy.** The dashboard date reflects the digest date, not necessarily today's date. Always display both if they differ.
- **Worktree awareness.** The skill runs inside the `.claude/worktrees/` worktree. All file read/write paths are relative to the repo root inside that worktree. Git deployment commands must reference the main repo root at `C:/Users/alexd/OneDrive/Documents/Obsidian Vault`.
