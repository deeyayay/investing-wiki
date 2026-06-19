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
      AI Buildout Stack.md         ← canonical 12-layer taxonomy + dashboard JSON
      Dimension Map.md             ← sector registry, folder slugs, D1–D5 → layer crosswalk
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
| `/research-ticker` | `/research-ticker TICKER [--question "..."]` | **Full-KB investment view.** Reads all three layers + Raw/Sentiment files + Sentiment Index + Sector Framework. Use for any buy/sell/hold/thesis question. |
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
- **AI Buildout Stack** (`Investing/Wiki/Reference/AI Buildout Stack.md`) — canonical 12-layer taxonomy (Application → Critical Minerals), mapped word-for-word from the *AI Buildout Supply Chain* blueprint graphic, + 3 cross-cutting rails and the Edge & Physical AI deployment surface. Holds the machine-readable JSON that `/daily-dashboard` renders as the vertical stack map. Sub-box labels are canonical; `gap` boxes flag KB coverage gaps; `group` tags cluster boxes visually (no extra depth).
- **Dimension Map** (`Investing/Wiki/Reference/Dimension Map.md`) — sector registry, folder slugs, supply chain map status, and the legacy D1–D5 → layer crosswalk.
- **Ecosystem Interrelationships** (`Investing/Wiki/Reference/Ecosystem Interrelationships.md`) — cross-sector dependency graph. Source of truth for flow diagram rendering and multi-sector signal propagation.

## Taxonomy (12-Layer AI Buildout Stack)

The AI buildout is modeled as a **single vertical dependency stack** — 12 layers from Application (top) down to Critical Minerals (bedrock) — wrapped by 3 cross-cutting rails and capped by the Edge & Physical AI deployment surface. Each layer *runs on* the layer below it. The taxonomy is mapped **word-for-word from the *AI Buildout Supply Chain* blueprint graphic**. See `Investing/Wiki/Reference/AI Buildout Stack.md` for the authoritative layer definitions + the machine-readable JSON the dashboard consumes.

```
L01 Application              ← AI assistants · agentic platforms · enterprise SaaS · vertical apps
L02 AI Model                 ← foundation models · fine-tuned · inference serving · orchestration
L03 Software Infrastructure  ← ML frameworks · GPU kernels · training · orchestration · inference opt
L04 Cloud Infrastructure     ← hyperscalers · neoclouds · edge/inference · colocation
L05 Compute Hardware         ← training/inference GPUs · custom ASICs · server CPUs · networking ASICs
L06 Memory                   ← HBM · HBF · DRAM · NAND · LPDDR
L07 Interconnect             ← scale-up · scale-out · scale-across · components
L08 Advanced Packaging       ← CoWoS/SoIC · HBM stacking · FC-BGA · glass core · TIM
L09 Semiconductor Foundry    ← leading-edge · specialty/mature · silicon photonics · compound · OSAT
L10 Semiconductor Equipment  ← lithography (EUV/DUV/NIL) · deposition · etch · metrology · test
L11 Semiconductor Materials  ← wafers · SOI · InP/GaAs/SiC substrates · gases · photoresist
L12 Critical Minerals & Raw Elements  ← Si · Cu · Ga · In · Ge · Hf · Ta · Co · Li · rare earths (bedrock)

Cross-cutting rails:  Power Infrastructure (left, power in) · Thermal (right, heat out) · Security (right, wraps)
Deployment surface:   Edge & Physical AI (right) — physical-world deployment + parallel-compute paradigms
```

**Word-for-word + gaps:** sub-box labels are canonical (verbatim from the graphic). Where the blueprint names a category the KB doesn't cover yet, the sub-box is a `gap` (renders "unmapped") — a queue for `/map-sector` / `/scout-tickers`. Intra-layer `group` tags (e.g. L07 Scale-Up/Out/Across, L10 Lithography) are visual bands, not a third drill-down level.

**Sectors → layers:** the 11 sector folders are unchanged — they remain the physical home of each ticker (keyed in `Monitor Registry.yaml`). Layers are the canonical *organizing/navigation* structure; each non-gap layer sub-box maps to one `(sector, tier)`. The legacy **D1–D5 dimension codes are superseded** but crosswalk cleanly to layers — see `Dimension Map.md`, which now holds the sector registry + slug↔display-name mapping + the D1–D5 → layer crosswalk.

## Ad-Hoc Research Protocol

**When a user asks any investment question about a specific ticker — buy/sell/hold, thesis review, risk assessment, "what has changed," price comparison — always run the full-KB read before answering, even if `/research-ticker` is not explicitly invoked.**

Full-KB read means, in order:
1. `Monitor Registry.yaml` → resolve path and sector
2. `[path]/facts.md` → structured fundamentals (Layer 1)
3. `[path]/analysis.md` → thesis, conviction, scoring, catalysts (Layer 2)
4. `[path]/signals.md` → news log, social mention stubs, research audit (Layer 3)
5. `Glob Investing/Raw/Sentiment/*[TICKER]*` → read **every** matching file (this is where tweet/article content lives — signals.md only has links)
6. `Investing/Wiki/Reference/Sentiment Index.md` → ticker's aggregated sentiment score
7. `Investing/Wiki/Sectors/[sector]/_Sector Framework.md` → cycle phase, archetype, valuation matrix

**Skipping any of these layers produces an incomplete answer.** The Raw/Sentiment files and signals.md are the layers most commonly missed in freeform Q&A — they contain market intelligence (specific quotes, dilution figures, revenue targets, risk flags) that does not appear in the structured YAML or analysis.md.

If a ticker is not in Monitor Registry.yaml, say so and suggest `/add-ticker` before answering.

## Notes

- All skills are append-only on existing content (YAML arrays, markdown tables, log sections). Never rewrite or delete existing entries.
- Foreign-listed tickers (SIVE, POET) are not SEC filers — `cik: null` in facts.md; skip EDGAR steps.
- `ingest-sentiment` uses the Obsidian MCP tools if available; falls back to Read/Write otherwise.
- Stub ticker pages (social mentions only, not yet in Monitor Registry.yaml) have a `signals.md` file with a note to run `/add-ticker` to onboard fully.
- **Migration:** Existing single-file `[TICKER].md` pages are old-format. Run `/ticker-monitor --deep TICKER` to migrate each one to the three-layer structure. Old files are detected automatically by skills and flagged with a migration notice.
