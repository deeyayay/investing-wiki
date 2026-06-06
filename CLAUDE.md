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
      Monitor Registry.yaml        ← master ticker index (machine-readable YAML)
      Sentiment Index.md           ← aggregated sentiment tracking
      Watchlist.md                 ← core holdings + speculative + compounders
      Dimension Map.md             ← D1–D5 taxonomy: sector → dimension → status
      Ecosystem Interrelationships.md ← cross-sector dependency graph
      _facts-template.md           ← Layer 1 template (YAML frontmatter schema)
      _analysis-template.md        ← Layer 2 template (thesis + conviction)
      _signals-template.md         ← Layer 3 template (news + audit trail)
      _Signal Template.md          ← template for signal notes
      Ecosystem Maps/              ← supply chain and ecosystem diagrams
    Sectors/
      [Sector Name]/
        [TICKER]/
          facts.md     ← Layer 1: YAML frontmatter (machine-readable KB facts)
          analysis.md  ← Layer 2: thesis, conviction, scoring, catalysts
          signals.md   ← Layer 3: news log, sentiment, research audit trail
        _Supply Chain Map.md ← company-agnostic tier diagram (created by /map-sector)
        _Customer Matrix.md  ← supplier × end-customer dependency table
        _Sector Framework.md ← sector thesis — written LAST, after map + matrix exist
gemini-scribe/
  Prompts/                   ← reusable prompt templates
  Scheduled-Tasks/           ← scheduled task state (JSON)
.claude/
  commands/                  ← project skills (add-ticker, ticker-monitor, etc.)
  settings.json              ← project-level permission allowlist
```

## Three-Layer Architecture

Each ticker has three files in a dedicated folder. Skills read only the layers they need.

| Layer | File | Format | Contents | Update cadence |
|-------|------|--------|----------|----------------|
| 1 — Facts KB | `facts.md` | YAML frontmatter | Company identity, management, earnings history, SEC filings, moat classification, score metrics | Earnings events, new filings, material changes only |
| 2 — Analysis | `analysis.md` | Structured markdown | One-Line Thesis, Investment Thesis, Scoring Summary, Conviction Log, Cross-Ticker Signals, Catalyst Timeline, Analyst Coverage | After scoring runs, conviction events, analyst moves |
| 3 — Signals | `signals.md` | Append-only log | News & Alpha Log, Social Mentions, Research Log | Daily / on-demand (high frequency) |

**Token efficiency:** Skills read only the files they need. `score-ticker` reads facts.md + analysis.md only (~700 tokens). `ticker-monitor --news-only` reads Monitor Registry.yaml only (~30 tokens per ticker lookup). Full-page reads of legacy monolithic .md files (1,500–3,000 tokens each) are replaced.

**Obsidian:** facts.md YAML frontmatter renders as a Properties panel in Obsidian. analysis.md and signals.md render as standard markdown.

## Available Skills

| Skill | Usage | When to use |
|-------|-------|-------------|
| `/map-sector` | `/map-sector "Sector Name" [--anchor "Concept"]` | **Start here for a new sector.** Maps supply chain structure, creates `_Supply Chain Map.md` |
| `/add-ticker` | `/add-ticker TICKER [--sector "Sector"] [--refresh-research]` | Onboard a new company: creates three-layer folder, registers in Monitor Registry.yaml, populates facts.md + analysis.md with research |
| `/stock-research-all` | `/stock-research-all [--refresh] [--sector SECTOR]` | Batch refresh facts.md + analysis.md thesis across all tickers (5 concurrent agents) |
| `/ticker-monitor` | `/ticker-monitor [--force] [--dry-run] [--sector SECTOR] [--deep TICKER] [--news-only]` | Weekly update pass: earnings/filings → facts.md; conviction/analyst/catalyst → analysis.md; news → signals.md. Use `--news-only` for daily lightweight news pass |
| `/ingest-sentiment` | `/ingest-sentiment [--source article\|musing] [--author "@handle"]` | Parse Tweets.md into signal notes; update Social Mentions in signals.md |
| `/score-ticker` | `/score-ticker TICKER [--refresh]` | Score on 6-criterion rubric; writes Scoring Summary to analysis.md, updates facts.md metrics + Monitor Registry.yaml |
| `/build-customer-matrix` | `/build-customer-matrix "Sector Name"` | Build supplier × end-customer dependency matrix from facts.md + analysis.md; writes `_Customer Matrix.md` |
| `/daily-dashboard` | `/daily-dashboard [--date YYYY-MM-DD] [--no-push]` | Generate HTML dashboard; deploy to GitHub Pages |
| `/detect-shifts` | `/detect-shifts [--sector "Sector"] [--all]` | Scan for structural technology/architectural shifts; appends to `Ecosystem Interrelationships.md` and flags affected supply chain maps |
| `/scout-tickers` | `/scout-tickers "Sector Name" [--tier "Tier Name"] [--no-push]` | Discover publicly-traded companies for empty supply chain tiers; appends CANDIDATE entries to Monitor Registry.yaml |
| `/screen-stocks` | `/screen-stocks --insider \| --thematic "criteria" \| --value` | Top-of-funnel screener: EDGAR insider cluster buying, thematic criteria, or value screen. Appends hits as CANDIDATE entries to Monitor Registry.yaml |

## Sector-First Workflow (preferred for entering a new sector)

```
1. /map-sector "Sector Name"              → _Supply Chain Map.md (company-agnostic tier structure)
2. /add-ticker TICKER --sector "Sector"  → three-layer folder + fundamentals (repeat per node)
3. /build-customer-matrix "Sector Name"  → _Customer Matrix.md (supplier × end-customer)
4. /ticker-monitor --sector "Sector"     → ongoing weekly cadence
5. Write _Sector Framework.md manually   → only after steps 1–3 are complete
6. /score-ticker TICKER                  → conviction scoring
```

The Sector Framework is written **last** — it's the synthesis output, not the starting point.

## Ticker-Add Workflow (for a company you already know)

```
/add-ticker TICKER --sector "Sector"  → three-layer folder + fundamentals populated
/ticker-monitor --deep TICKER         → pulls recent SEC filings, news, analyst coverage
/ingest-sentiment                     → files social signals from Tweets.md
/ticker-monitor --news-only           → daily lightweight news pass
/ticker-monitor                       → weekly full pass
```

## Weekly Screening Workflow (new discovery)

```
/screen-stocks --insider              → EDGAR Form 4 cluster buys → CANDIDATE entries
/screen-stocks --thematic "criteria" → web search + classify → CANDIDATE entries
Review Monitor Registry.yaml candidates
/add-ticker TICKER --sector "Sector" → onboard any high-conviction hits
```

## Key Reference Files

- **Monitor Registry** (`Investing/Wiki/Reference/Monitor Registry.yaml`) — machine-readable YAML index. All skills read this to locate ticker folder paths. Format: `TICKER → { sector, path, score }` + `candidates:` list.
- **Sentiment Index** (`Investing/Wiki/Reference/Sentiment Index.md`) — social signal counts and recency by ticker.
- **Watchlist** (`Investing/Wiki/Reference/Watchlist.md`) — curated view of holdings, rockets, and compounders with one-line theses.
- **Dimension Map** (`Investing/Wiki/Reference/Dimension Map.md`) — D1–D5 taxonomy, sector slugs, and supply chain map status per sector.
- **Ecosystem Interrelationships** (`Investing/Wiki/Reference/Ecosystem Interrelationships.md`) — cross-sector dependency graph. Source of truth for flow diagram rendering and multi-sector signal propagation.

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

## Notes

- All skills are append-only on existing content (YAML arrays, markdown tables, log sections). Never rewrite or delete existing entries.
- Foreign-listed tickers (SIVE, POET) are not SEC filers — `cik: null` in facts.md; skip EDGAR steps.
- `ingest-sentiment` uses the Obsidian MCP tools if available; falls back to Read/Write otherwise.
- Stub ticker pages (social mentions only, not yet in Monitor Registry.yaml) have a `signals.md` file with a note to run `/add-ticker` to onboard fully.
- **Migration:** Existing single-file `[TICKER].md` pages are old-format. Run `/ticker-monitor --deep TICKER` to migrate each one to the three-layer structure. Old files are detected automatically by skills and flagged with a migration notice.
