---
description: Top-of-funnel stock screener. Three modes — insider activity (EDGAR Form 4 cluster buying), thematic criteria (moat + competition + geography filters), and value screen (P/B near book). Appends hits as CANDIDATE entries to Monitor Registry.yaml. Does NOT auto-onboard. Usage: /screen-stocks --insider | --thematic "criteria" | --value [--source finviz]
allowed-tools: WebSearch, WebFetch, Read, Edit
---

# Screen Stocks — Top-of-Funnel Screener

Proactive outbound scanner that surfaces net-new tickers meeting investment criteria. Designed to run weekly. Outputs CANDIDATE entries to `Monitor Registry.yaml` — user reviews and calls `/add-ticker TICKER` manually to onboard.

**Registry:** `Investing/Wiki/Reference/Monitor Registry.yaml`

**Input:** `$ARGUMENTS` — one required mode flag plus optional qualifiers:
- `--insider` — EDGAR Form 4 cluster buying screen
- `--thematic "criteria string"` — web search + LLM classification against user criteria
- `--value [--source finviz]` — P/B near-book screen with financial quality filters

**Token budget:** max 3 searches per mode. Outputs up to 5 candidates per run.

---

## Step 1 — Parse arguments and check duplicates

Extract mode and qualifiers from `$ARGUMENTS`.

Read `Investing/Wiki/Reference/Monitor Registry.yaml`. Build:
- `existing_tickers` — set of all tickers under `tickers:` key
- `existing_candidates` — set of all tickers under `candidates:` list

Any ticker already in either set is skipped as a duplicate in output.

---

## Mode A — `--insider` (EDGAR Form 4 cluster buying)

Goal: find tickers where ≥2 distinct insiders filed open-market purchases in the last 30 days with meaningful size (>0.5% of their prior holdings).

### Search 1 — EDGAR full-text Form 4 feed
Fetch the EDGAR full-text search for recent Form 4 filings:
`https://efts.sec.gov/LATEST/search-index?q=%22transaction+code%22+%22P%22&dateRange=custom&startdt=[TODAY-30d]&enddt=[TODAY]&forms=4`

If the EDGAR feed is unavailable, fall back to:
`SEC EDGAR Form 4 insider purchases cluster buying open market last 30 days 2026`

### Search 2 — Filter and enrich
For each issuer with 2+ Form 4 "P" (purchase) entries from different individuals, run:
`[TICKER] insider buying cluster Form 4 SEC 2026 open market purchase`

Extract per issuer:
- Ticker symbol
- Number of distinct insiders who bought
- Approximate total $ value purchased
- Whether purchases were open-market ("P" code) vs. option exercises ("M" code) — only keep "P"
- Company name and sector (approximate)

### Qualify candidates
For each Form 4 cluster, check:
- ≥2 distinct insiders (different names/CIK) within 30 days
- All are open-market purchases (transaction code "P")
- Not already in `existing_tickers` or `existing_candidates`
- Company is publicly traded on a major exchange (NYSE, NASDAQ, TSX, etc.)

Select up to 5 qualifying tickers, ranked by number of distinct buyers.

---

## Mode B — `--thematic "criteria"`

Goal: find publicly-traded companies matching user-supplied criteria using web search + LLM classification.

The `criteria` string from `--thematic` drives the searches. Parse it for key themes (geography, sector, moat type, competitive position).

### Search 1 — Broad thematic scan
`[criteria] publicly traded company stock NYSE NASDAQ 2026`

### Search 2 — Moat and competition verification
`[criteria] sole source contract pricing power low competition moat 2026`

### Search 3 (optional) — Sector-specific scan
If the criteria mentions a specific sector:
`[criteria] [sector] company stock analyst coverage 2026`

### Classify results
For each company mentioned in search results, score against:
1. **Geography match** — does it match any geography constraint in criteria? (e.g., "Made in America" → US production)
2. **Moat evidence** — is there evidence of pricing power, sole-source contracts, IP, or switching costs?
3. **Competition** — low competitive intensity? (few substitutes, regulatory moat, high capital barriers)
4. **Investability** — listed on a major exchange, market cap > $200M

Keep only companies scoring 3/4 or 4/4. Select up to 5.

---

## Mode C — `--value`

Goal: find stocks trading near or below book value with positive financial quality signals.

**Requires a data source.** If `--source finviz` is passed, use Finviz screener URL. Otherwise, use web search.

### Search 1 — Value screen
If `--source finviz`:
Fetch: `https://finviz.com/screener.ashx?v=111&f=fa_pb_u1.1,fa_fcfps_pos,fa_epsqoq_pos&ft=4`
(P/B ≤ 1.1, positive FCF/share, positive EPS QoQ)

Otherwise:
`stocks price to book value below 1.1 positive free cash flow revenue growth 2026 screener`

### Search 2 — Quality filter
For each raw candidate from Search 1:
`[TICKER] debt equity ratio revenue growth profitability 2025 2026`

### Qualify candidates
Keep tickers where:
- P/B ≤ 1.1 (near or below book)
- Positive FCF (last reported period)
- Revenue growth ≥ 0% (YoY)
- Debt/Equity ≤ 1.5
- Not already in existing_tickers or existing_candidates

Select up to 5.

---

## Step 2 — Append CANDIDATE entries to Monitor Registry.yaml

For each qualifying ticker (from whichever mode ran), append to the `candidates:` list in `Monitor Registry.yaml`:

```yaml
  - ticker: "[TICKER]"
    company: "[Company Name]"
    sector: "[Inferred sector or unknown]"
    layer: ""
    source: "screen-stocks"
    trigger: "insider"    # insider / thematic / value
    added: "[TODAY'S DATE]"
    note: "[20–30 word differentiation note explaining why this hit the screen]"
```

Use Edit to append each candidate to the `candidates:` list. Do not touch the `tickers:` section.

---

## Step 3 — Print summary

```
✅ Screen Stocks — [MODE] — [TODAY'S DATE]

   Tickers screened: [N candidates evaluated]
   New candidates:   [N appended to Registry]
   Duplicates skipped: [N already in Registry or tickers]

   Candidates added:
   • [TICKER] — [Company] | [trigger] | [note]
   • [TICKER] — [Company] | [trigger] | [note]

   Next steps:
   • Review candidates in Monitor Registry.yaml
   • Run /add-ticker TICKER --sector "Sector" to onboard any you want to track
   • Run /screen-stocks --insider again next week for fresh Form 4 activity
```

---

## Rules

- **Output candidates only — never auto-onboard.** All candidates go to Registry.yaml for human review. Do not call `/add-ticker` automatically.
- **Max 5 candidates per run.** Quality over quantity. A clean hit list is more valuable than a long one.
- **No duplicates.** Skip any ticker already in `tickers:` or `candidates:` in the Registry.
- **Open-market buys only for --insider.** Option exercises (code "M") and gifts (code "G") do not count as conviction signals.
- **Max 3 searches per mode.** This skill is designed to be token-efficient and run weekly within a single session alongside other skills.
- **Note the mechanism.** Each candidate's `note` field must explain WHY it hit the screen in plain language — not just the trigger criteria.
