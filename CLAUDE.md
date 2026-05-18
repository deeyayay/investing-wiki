# Investing Wiki

Investment research knowledge base. All paths are relative to the repo root.

## Folder Structure

```
Investing/
  Raw/
    Inbox/Tweets.md          ← staging area for sentiment ingestion
    Sentiment/               ← individual signal notes (one .md per signal)
    Filings/                 ← SEC filing documents by ticker
  Wiki/
    Reference/
      Monitor Registry.md    ← master list of tracked tickers (ticker → file path map)
      Sentiment Index.md     ← aggregated sentiment tracking
      Watchlist.md           ← core holdings + speculative + compounders
      _Ticker Template.md    ← template for new ticker pages
      _Signal Template.md    ← template for signal notes
      Ecosystem Maps/        ← supply chain and ecosystem diagrams
    Sectors/
      [Sector Name]/
        [TICKER].md          ← individual ticker wiki page
        _Sector Framework.md ← sector thesis and competitive landscape
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
| `/add-ticker` | `/add-ticker TICKER [--sector "Sector"]` | Onboard a new name: creates wiki page, registers in Monitor Registry, runs stock research |
| `/stock-research` | `/stock-research TICKER [--refresh]` | Populate Investment Thesis, Management & Leadership, One-Line Thesis for one ticker |
| `/stock-research-all` | `/stock-research-all [--refresh] [--sector SECTOR]` | Batch research across all tickers (5 concurrent agents) |
| `/ticker-monitor` | `/ticker-monitor [--force] [--dry-run] [--sector SECTOR] [--deep TICKER]` | Weekly update pass: SEC filings, earnings, analyst moves, catalysts — append-only |
| `/ingest-sentiment` | `/ingest-sentiment [--source article\|musing] [--author "@handle"]` | Parse Tweets.md staging dump into signal notes; update Social Mentions on ticker pages |

## Ticker Workflow

```
/add-ticker TICKER          → creates page + populates fundamentals
/ticker-monitor --deep TICKER  → pulls recent filings, news, analyst coverage
/ingest-sentiment           → files social signals from Tweets.md
/ticker-monitor             → weekly pass across all tickers
```

## Key Reference Files

- **Monitor Registry** (`Investing/Wiki/Reference/Monitor Registry.md`) — authoritative ticker → sector → file path map. All skills read this to locate wiki pages.
- **Sentiment Index** (`Investing/Wiki/Reference/Sentiment Index.md`) — social signal counts and recency by ticker.
- **Watchlist** (`Investing/Wiki/Reference/Watchlist.md`) — curated view of holdings, rockets, and compounders with one-line theses.

## Existing Sectors

- AI Infrastructure
- Clean Energy
- Cybersecurity
- Fintech & E-Commerce
- Metals & Mining
- Photonics & Optical
- Robotics & Edge AI
- Semiconductors
- Space & Comms

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
