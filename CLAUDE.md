# Investing Wiki

Investment research knowledge base. All paths are relative to the repo root.

## Folder Structure

```
Investing/
  Raw/
    Inbox/Tweets.md          ← staging area for sentiment ingestion
    Inbox/watchlist-refresh-digest.json ← headline digest written by scripts/watchlist_refresh_fetch.py
    Sentiment/               ← individual signal notes (one .md per signal)
    Filings/                 ← SEC filing documents by ticker
  Output/
    Digest/                  ← datestamped daily news digests (YYYY-MM-DD-daily-news.md)
    Dashboard/               ← generated HTML dashboards (index.html + YYYY-MM-DD.html)
  Wiki/
    Reference/
      Monitor Registry.yaml        ← master ticker index (machine-readable YAML)
      Topics.yaml                  ← theme registry (news themes, not tickers)
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
        _Supply Chain Map.md ← company-agnostic tier diagram (legacy; /map-sector archived)
        _Customer Matrix.md  ← supplier × end-customer dependency table
        _Sector Framework.md ← sector thesis — written LAST, after map + matrix exist
scripts/
  watchlist_refresh_fetch.py ← zero-token news + filings + topics fetcher for /brief (stdlib only)
  test_watchlist_fetch.py    ← guard tests for the fetcher (no network)
  repair_registry.py         ← rewrite registry path/sector/layout to match disk
  check_registry.py          ← verify the registry; exit 1 on any error
gemini-scribe/
  Prompts/                   ← reusable prompt templates
  Scheduled-Tasks/           ← scheduled task state (JSON)
.claude/
  commands/                  ← the three loaded skills (brief, dig, track)
  archived-commands/         ← 13 unloaded skills kept for reference
  settings.json              ← project-level permission allowlist
```

## Three-Layer Architecture

Each ticker has three files in a dedicated folder. Skills read only the layers they need.

| Layer | File | Format | Contents | Update cadence |
|-------|------|--------|----------|----------------|
| 1 — Facts KB | `facts.md` | YAML frontmatter | Company identity, management, earnings history, SEC filings, moat classification, score metrics | Earnings events, new filings, material changes only |
| 2 — Analysis | `analysis.md` | Structured markdown | One-Line Thesis, Investment Thesis, Scoring Summary, Conviction Log, Cross-Ticker Signals, Catalyst Timeline, Analyst Coverage | After scoring runs, conviction events, analyst moves |
| 3 — Signals | `signals.md` | Append-only log | News & Alpha Log, Social Mentions, Research Log | Daily / on-demand (high frequency) |

**Token efficiency:** Skills read only the layers they need. `/brief` reads one pre-filtered digest and then only the analysis.md of tickers it actually writes to. `/dig` is the only skill that reads facts.md, filings, or the web — and only for one ticker at a time.

**Obsidian:** facts.md YAML frontmatter renders as a Properties panel in Obsidian. analysis.md and signals.md render as standard markdown.

## Available Skills

Three skills. Everything else was archived on 2026-08-23 to
`.claude/archived-commands/` — unloaded, not deleted; see the README there.

| Skill | Usage | When |
|-------|-------|------|
| `/brief` | `/brief [--all] [--hours H] [--tickers CSV] [--no-topics] [--no-push]` | **The daily pass.** Script fetches news + SEC filings + topic themes at zero model tokens; Claude triages the digest against each One-Line Thesis. Material → signals.md, drift → analysis.md, summary → Output/Digest. Also files social signals staged in Tweets.md. Never searches. |
| `/dig` | `/dig TICKER [--filings-only] [--score] [--no-push]` | On-demand deep dive when `/brief` flags something a headline cannot settle. Reads actual filings, re-tests the thesis leg by leg. The expensive one — use it on a handful of names. |
| `/track` | `/track TICKER [--sector "S"] [--tier core\|rocket\|compounder] [--note "why"]` | Put a name on the watchlist: registry entry + one-file page + Watchlist row. No three-layer scaffolding, no research pass. |

### The loop

```
/brief                  → daily; flags what moved and what drifted
  ├─ discovered: TICK   → /track TICK      (a lead worth watching)
  └─ deep-pass: TICK    → /dig TICK        (a question headlines can't answer)
/dig TICKER --score     → establishes a thesis, scores it, updates the registry
```

A name earns depth rather than starting with it: `/track` costs a row, `/dig`
costs a research pass, and only names that survive both get three-layer files.

## Key Reference Files

### Topics — theme coverage alongside tickers

`Investing/Wiki/Reference/Topics.yaml` tracks **themes**, which the ticker-keyed registry cannot:
a subject stays invisible until you already own a name in it. Seven topics today. Each carries a
news `query`, the registered `tickers` it bears on, and `gaps` — names that matter to the theme but
are not registered, which doubles as the `/track` queue.

The daily pass scans topics alongside tickers into the same digest (`--no-topics` to skip). Topic
headlines also feed a **discovery funnel**: company names are matched against SEC's registrant list
(10,403 companies, cached weekly at `Investing/Raw/Inbox/.sec-company-tickers.json`) and anything
untracked lands in the digest's `discovered` list. These are candidates for triage, deliberately
*not* auto-written into the registry — a regex match is a lead, not a decision.

Topic hits do **not** count as content for the empty-digest guard. A run whose ticker pass wholly
failed is broken even if the themes came back fine.

### News + filings providers

`scripts/watchlist_refresh_fetch.py` fetches from independent providers so one blocked host
degrades a run instead of killing it. Both cost **zero model tokens**.

| Provider | Source | Emits |
|---|---|---|
| `googlenews` | Google News RSS | `kind: news` |
| `edgar` | SEC `browse-edgar` atom feed per CIK | `kind: filing` |

Filings rank above headlines in the digest — a primary source outranks a story about it. Tickers
with `cik: null` (foreign listings) skip EDGAR silently; that is not an error.

**`WebSearch` is deliberately not a provider.** It is a model tool, so its results land in
context — roughly two orders of magnitude more expensive per run than this script. Reserve it for
a single ticker on demand, never the daily loop.

**SEC requires a contact email in the User-Agent** or it answers 403. The default is a placeholder;
set `SEC_USER_AGENT="your-name your@email"` so SEC can reach you before they rate-limit you.

Exit status: `0` ran clean · `1` a provider was dead, or an empty digest would have overwritten a
good one. A provider that answers 200 with zero items counts as dead — that silent mode is how the
pipeline stayed broken for seven weeks. Run `python3 scripts/test_watchlist_fetch.py` after
touching any of this.

- **Monitor Registry** (`Investing/Wiki/Reference/Monitor Registry.yaml`) — machine-readable YAML index. All skills read this to locate ticker folder paths. Format: `TICKER → { sector, path, layout, score }` + `candidates:` list.

### Registry path convention

Sector folders are **layer-prefixed on disk** (`L05 Compute Hardware`, `L07 Interconnect`); the
un-prefixed folders `Edge & Physical AI`, `Power`, `Security`, `Space & Comms` sit outside the
12-layer stack and stay as-is. The registry's `sector:` is that top-level folder name with any
`Lxx ` prefix stripped — so `sector` and `path` can never disagree.

Each ticker carries a `layout:` field naming what its `path:` points at:

| `layout` | `path:` points to | Meaning |
|---|---|---|
| `three-layer` | a folder | holds `facts.md` + `analysis.md` + `signals.md` |
| `legacy` | a single `.md` file | not yet migrated — run `/dig TICKER` |
| `unpaged` | (stale, ignore) | registered but no page exists on disk yet |

**Renaming a sector folder breaks every skill.** After any rename, re-run the repair and check:

```bash
python3 scripts/repair_registry.py   # rewrite path/sector/layout to match disk
python3 scripts/check_registry.py    # verify; exit 1 on any error
```

`check_registry.py` also warns about ticker pages on disk that no registry entry claims.
- **Sentiment Index** (`Investing/Wiki/Reference/Sentiment Index.md`) — social signal counts and recency by ticker.
- **Watchlist** (`Investing/Wiki/Reference/Watchlist.md`) — **the scope input for the daily pass.** Every ticker named in one of its tables gets scanned; a ticker absent from it is not watched daily (`--all` widens to the full registry). Core Holdings is owner-maintained and intentionally empty — positions are not inferable from scores. High Conviction / Drift Watch / Active Coverage are derived from each `analysis.md`.
- **Topics** (`Investing/Wiki/Reference/Topics.yaml`) — theme registry + discovery funnel. See above.
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

**Word-for-word + gaps:** sub-box labels are canonical (verbatim from the graphic). Where the blueprint names a category the KB doesn't cover yet, the sub-box is a `gap` (renders "unmapped") — a coverage queue, now tracked as `gaps:` in `Topics.yaml`. Intra-layer `group` tags (e.g. L07 Scale-Up/Out/Across, L10 Lithography) are visual bands, not a third drill-down level.

**Sectors → layers:** the 11 sector folders are unchanged — they remain the physical home of each ticker (keyed in `Monitor Registry.yaml`). Layers are the canonical *organizing/navigation* structure; each non-gap layer sub-box maps to one `(sector, tier)`. The legacy **D1–D5 dimension codes are superseded** but crosswalk cleanly to layers — see `Dimension Map.md`, which now holds the sector registry + slug↔display-name mapping + the D1–D5 → layer crosswalk.

## Notes

- All skills are append-only on existing content (YAML arrays, markdown tables, log sections). Never rewrite or delete existing entries.
- Foreign-listed tickers (SIVE, POET) are not SEC filers — `cik: null` in facts.md; skip EDGAR steps.
- `ingest-sentiment` uses the Obsidian MCP tools if available; falls back to Read/Write otherwise.
- Stub ticker pages (social mentions only, not in Monitor Registry.yaml) are invisible to every skill until registered — `scripts/check_registry.py` lists them. Run `/track TICKER` to register one.
- **Migration is no longer the goal.** 80 legacy single-file pages sit alongside 35 three-layer folders; finishing the migration is not planned. Three layers are for names actually held — `layout:` in the registry says which shape a ticker has, and skills branch on it.
