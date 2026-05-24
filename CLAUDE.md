# Investing Wiki

Investment research knowledge base. All paths are relative to the repo root.

## Folder Structure

```
Investing/
  Raw/
    Inbox/Tweets.md          ← staging area for sentiment ingestion
    Sentiment/               ← individual signal notes (one .md per signal)
    Filings/                 ← SEC filing documents by ticker
  Output/
    Digest/                  ← datestamped daily news digests (YYYY-MM-DD-daily-news.md)
    Dashboard/               ← generated HTML dashboards (index.html + YYYY-MM-DD.html)
  Wiki/
    Reference/
      Monitor Registry.md           ← master list of tracked tickers (ticker → file path map)
      Sentiment Index.md            ← aggregated sentiment tracking
      Watchlist.md                  ← core holdings + speculative + compounders
      Dimension Map.md              ← D1–D5 taxonomy: sector → dimension → status
      Ecosystem Interrelationships.md ← cross-sector dependency graph (source of truth for flow diagram)
      _Ticker Template.md           ← template for new ticker pages
      _Signal Template.md           ← template for signal notes
      Ecosystem Maps/               ← supply chain and ecosystem diagrams
    Sectors/
      [Sector Name]/
        [TICKER].md          ← individual ticker wiki page
        _Supply Chain Map.md ← company-agnostic tier diagram (created by /map-sector)
        _Customer Matrix.md  ← supplier × end-customer dependency table
        _Sector Framework.md ← sector thesis — written LAST, after map + matrix exist
gemini-scribe/
  Prompts/                   ← reusable prompt templates
  Scheduled-Tasks/           ← scheduled task state (JSON)
.claude/
  commands/                  ← project skills (add-ticker, stock-research, etc.)
  settings.json              ← project-level permission allowlist
```

## Available Skills

| Skill | Usage | When to use |
|-------|-------|-------------|
| `/map-sector` | `/map-sector "Sector Name" [--anchor "Concept"]` | **Start here for a new sector.** Maps the supply chain structure company-agnostically, identifies publicly-traded nodes, creates `_Supply Chain Map.md` |
| `/add-ticker` | `/add-ticker TICKER [--sector "Sector"] [--layer "Layer"]` | Onboard a specific company: creates wiki page, registers in Monitor Registry, runs stock research |
| `/stock-research` | `/stock-research TICKER [--refresh]` | Populate Investment Thesis, Management & Leadership, One-Line Thesis for one ticker |
| `/stock-research-all` | `/stock-research-all [--refresh] [--sector SECTOR]` | Batch research across all tickers (5 concurrent agents) |
| `/ticker-monitor` | `/ticker-monitor [--force] [--dry-run] [--sector SECTOR] [--deep TICKER]` | Weekly update pass: SEC filings, earnings, analyst moves, catalysts — append-only |
| `/ingest-sentiment` | `/ingest-sentiment [--source article\|musing] [--author "@handle"]` | Parse Tweets.md staging dump into signal notes; update Social Mentions on ticker pages |
| `/score-ticker` | `/score-ticker TICKER [--refresh]` | Score a ticker on the 6-criterion Unrivaled Investing rubric; writes Scoring Summary to ticker page, updates Monitor Registry and Watchlist |
| `/daily-news` | `/daily-news [--all] [--sector "Sector"] [--hours N]` | Daily news digest: scans watchlist tickers, scores 1–5 by impact, writes datestamped digest to `Investing/Output/Digest/`, appends high-impact items to ticker pages |
| `/build-customer-matrix` | `/build-customer-matrix "Sector Name"` | Build supplier × end-customer dependency matrix; writes `_Customer Matrix.md` with scored cells and JSON heat map metadata for the dashboard |
| `/daily-dashboard` | `/daily-dashboard [--date YYYY-MM-DD] [--no-push]` | Generate self-contained HTML dashboard from latest digest + KB; analyst-style HOLD/ADD/TRIM/WATCH recommendations for portfolio holdings; deploy to GitHub Pages |
| `/detect-shifts` | `/detect-shifts [--sector "Sector"] [--all]` | Scan for structural technology and architectural shifts affecting sector supply chains. Searches recent news for process-level changes, compares against current tier definitions, appends new rows to `Ecosystem Interrelationships.md` and flags affected tiers in supply chain maps. Run monthly or after major industry events. |

## Sector-First Workflow (preferred for entering a new sector)

```
1. /map-sector "Sector Name"              → _Supply Chain Map.md (company-agnostic tier structure)
2. /add-ticker TICKER --layer "Layer"     → wiki page + registry row (repeat per node)
3. /stock-research TICKER                 → ground truth: thesis, management, filings
4. /build-customer-matrix "Sector Name"  → _Customer Matrix.md (supplier × end-customer)
5. /ticker-monitor --sector "Sector"     → ongoing weekly cadence
6. Write _Sector Framework.md manually   → only after steps 1–4 are complete
7. /score-ticker TICKER                  → conviction scoring
```

The Sector Framework is written **last** — it's the synthesis output, not the starting point.

## Ticker-Add Workflow (for a company you already know)

```
/add-ticker TICKER --layer "Layer"   → creates page + fundamentals
/ticker-monitor --deep TICKER        → pulls recent filings, news, analyst coverage
/ingest-sentiment                    → files social signals from Tweets.md
/ticker-monitor                      → weekly pass across all tickers
```

## Key Reference Files

- **Monitor Registry** (`Investing/Wiki/Reference/Monitor Registry.md`) — authoritative ticker → sector → file path map. All skills read this to locate wiki pages.
- **Sentiment Index** (`Investing/Wiki/Reference/Sentiment Index.md`) — social signal counts and recency by ticker.
- **Watchlist** (`Investing/Wiki/Reference/Watchlist.md`) — curated view of holdings, rockets, and compounders with one-line theses.
- **Dimension Map** (`Investing/Wiki/Reference/Dimension Map.md`) — D1–D5 taxonomy, sector slugs, and supply chain map status per sector.
- **Ecosystem Interrelationships** (`Investing/Wiki/Reference/Ecosystem Interrelationships.md`) — cross-sector dependency graph at the process/product level. Source of truth for flow diagram rendering and multi-sector signal propagation.

## Sector Taxonomy (Five-Dimension Stack)

Sectors are organized into a D1–D5 vertical stack. See `Investing/Wiki/Reference/Dimension Map.md` for the authoritative registry with status per sector.

```
D5 — AI Applications:    Robotics & Edge AI · Fintech & Commerce AI · Defense & Space (planned)
D4 — AI Enablement:      Cybersecurity · Data & Software Platforms (planned)
D3 — AI Infrastructure:  Compute Infrastructure (folder: AI Infrastructure) · Energy & Power (folder: Clean Energy)
D2 — AI Connectivity:    Photonics & Optical · Space & Communications (folder: Space & Comms)
D1 — AI Mfg Base:        Semiconductors · Electronic Components (planned) · Materials & Mining (folder: Metals & Mining)
```

**Folder slugs are unchanged** — display names differ from folder names for some sectors (e.g., "Compute Infrastructure" maps to `AI Infrastructure/`). The Dimension Map is the source of truth for slug ↔ display name mapping.

## Ticker Page Structure

Each `Investing/Wiki/Sectors/[Sector]/[TICKER].md` contains:
- One-Line Thesis
- Investment Thesis (with Thesis Drift block)
- Management & Leadership
- Earnings & Financials (table)
- SEC Filings (table)
- News & Alpha Log
- Analyst Coverage
- Conviction Log (table)
- Cross-Ticker Signals (table)
- Catalyst Timeline (checklist)
- Social Mentions (table — populated by ingest-sentiment)
- Research Log (append-only audit trail)

## Notes

- All skills are append-only on existing content (Research Log, tables). Never rewrite or delete existing rows.
- Foreign-listed tickers (SIVE, POET) are not SEC filers — skip EDGAR steps for them.
- `ingest-sentiment` uses the Obsidian MCP tools if available; falls back to Read/Write otherwise.
- Stub ticker pages (social mentions only, not yet in Monitor Registry) live at `Investing/Wiki/Sectors/[sector]/[TICKER].md` with a note to run `/add-ticker` to onboard fully.
