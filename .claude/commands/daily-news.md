---
description: Daily news digest for watchlist tickers. Scans all fully-onboarded tickers on the official watchlist for breaking news, scores each item 1–5 by impact, and writes a datestamped digest to Investing/Output/Digest/. Scores 4–5 also append to the ticker's News & Alpha Log and Research Log. Token-efficient — one search per ticker, no wiki page reads. Usage: /daily-news [--all] [--sector "Sector Name"] [--hours N]
allowed-tools: WebSearch, Read, Write, Edit, Glob, Agent
---

# Daily News — Watchlist News Scanner

Generates a daily news digest for all official watchlist tickers. Scores each ticker 1–5 by news impact, writes a full per-ticker digest to `Investing/Output/Digest/`, and appends high-impact items (score ≥ 4) to the relevant ticker wiki pages.

**Input flags (`$ARGUMENTS`):**
- *(none)* — scan all tickers that appear in BOTH Watchlist.md and Monitor Registry (fully onboarded only)
- `--all` — scan all Monitor Registry tickers regardless of watchlist membership
- `--sector "Name"` — limit to one sector (uses Monitor Registry sector groupings)
- `--hours N` — lookback window in hours (default: 24)

---

## Phase 1 — Build ticker list (read-only, no searches)

1. Read `Investing/Wiki/Reference/Watchlist.md`.
   - Extract all ticker symbols from tables in: **Core Holdings**, **High Upside Rockets**, **Compounders Watchlist**, and any Photonics subsections (Compounders / High Upside Rockets).
   - Result: `watchlist_tickers` — a flat set of ticker symbols.

2. Read `Investing/Wiki/Reference/Monitor Registry.md`.
   - Parse each sector table. For each row, extract: `ticker`, `company`, `sector`, `path`, `CIK`.
   - Result: `registry` — map of ticker → {company, sector, path, cik}.

3. Build the **scan list**:
   - Default (no flags): intersection of `watchlist_tickers` and `registry` keys. These are fully onboarded tickers the user actively tracks.
   - `--all`: use all `registry` keys.
   - `--sector "Name"`: filter `registry` to the named sector, then intersect with `watchlist_tickers` (or skip intersection if `--all` also passed).

4. Print the scan list before proceeding:

```
Scanning N tickers: TICKER1, TICKER2, ...
Lookback: 24h | Mode: watchlist | Date: YYYY-MM-DD
```

If the scan list is empty, report and stop.

---

## Phase 2 — Parallel news search (1 search per ticker)

Run all searches in parallel — one `WebSearch` per ticker.

**Query template:**
```
[TICKER] [CompanyName] stock news [TODAY'S DATE]
```

For each search, collect: up to 5 result titles and snippets. Do **not** fetch full article URLs — snippets are sufficient.

Collect all results before Phase 3.

---

## Phase 3 — Score and synthesize

For each ticker, analyze its search results and produce:

| Field | Description |
|-------|-------------|
| `headline` | The single most material headline from the results |
| `source` | Publication name and date if available |
| `summary` | One-line explanation of what happened (≤ 20 words) |
| `detail` | 2–4 sentences covering what happened, why it matters to the thesis, and any forward implications |
| `snippet` | Best raw excerpt from search results (verbatim, ≤ 60 words) |
| `impact` | Integer 1–5 (see rubric below) |
| `category` | One of: `earnings` \| `analyst` \| `filing` \| `product` \| `macro` \| `regulatory` \| `insider` \| `quiet` |

**Impact scoring rubric:**
- **5 — Major catalyst:** Earnings beat/miss with guidance move, M&A announcement, CEO/CFO departure, FDA/regulatory decision, material contract win/loss
- **4 — Significant:** Analyst upgrade/downgrade with PT move ≥ 10%, guidance revision standalone, product launch with revenue implications, large insider buy/sell (> $1M)
- **3 — Moderate:** Product announcement, sector news with direct ticker read-through, small analyst note, earnings date confirmed
- **2 — Minor:** Routine SEC filing (10-K/10-Q cover, proxy), small price target trim, generic sector article mentioning ticker
- **1 — Quiet:** No material news in lookback window, only old articles recycled, or search returned nothing relevant

**Rules:**
- If results are entirely older than the `--hours` window, score = 1 / category = `quiet`.
- Score the most impactful item found, not the average.
- Prefer specificity: a concrete earnings number beats a vague "positive sentiment" article.

---

## Phase 4 — Write-back for high-impact news (score ≥ 4)

For any ticker with impact ≥ 4, locate its wiki page via the `path` from Monitor Registry.

**Append to News & Alpha Log** (after the last existing row):
```
| [YYYY-MM-DD] | [CATEGORY] | [Headline, max 25 words] | [Summary, 1 sentence] | — |
```

**Append to Research Log** (at the bottom):
```
- **[YYYY-MM-DD]** — 📰 DAILY-NEWS | [Headline, max 15 words] (impact [N])
```

Rules:
- Append-only. Never modify existing rows.
- Check the existing News & Alpha Log for the same headline before appending (no duplicates).
- If the wiki page path does not exist or cannot be read, skip the write-back and note the error in the digest.

---

## Phase 5 — Write digest file

Determine the output path: `Investing/Output/Digest/[YYYY-MM-DD]-daily-news.md`

If a file already exists at that path (e.g., skill run twice in one day), append a `-2` suffix: `[YYYY-MM-DD]-daily-news-2.md`.

**File structure:**

```markdown
# Daily News Digest — [YYYY-MM-DD]

**Scanned:** N tickers | **Lookback:** Xh | **High-impact (≥4):** N tickers

## Summary Table

| Impact | Ticker | Category | Headline | Summary |
|--------|--------|----------|----------|---------|
| 5 🔴 | TICKER | earnings | ... | ... |
| 3 🟡 | TICKER | product | ... | ... |
| 1 ⚪ | TICKER | quiet | No material news | — |

---

## Per-Ticker Detail

### [TICKER] — [CompanyName] — Impact [N] [emoji]

**Headline:** ...
**Source:** ..., [YYYY-MM-DD]
**Summary:** ...
**Detail:** ...
**Snippet:** "..."

*(Repeat for each ticker, sorted by impact descending, then alphabetically.)*

### [TICKER] — [CompanyName] — Impact 1 ⚪

No material news in the past Xh.

---

## Write-backs

*Tickers where News & Alpha Log was updated:*
- [TICKER] — [Headline]

*(Or: "None — no tickers scored ≥ 4 today.")*
```

**Emoji legend:** 🔴 = impact 4–5 | 🟡 = impact 2–3 | ⚪ = impact 1

After writing the file, **also print the Summary Table to the conversation** for immediate viewing. Do not print the full per-ticker detail to the conversation (it's in the file).

---

## Rules

- **Token-efficient.** One search per ticker. No ticker wiki page reads. No full article fetches.
- **Append-only on wiki pages.** Never modify or delete existing rows or log entries.
- **No duplicates.** Before any wiki write-back, confirm the headline is not already present.
- **Quiet is valid.** A score of 1 is not an error — it means the skill ran cleanly and found nothing material.
- **Fail gracefully.** If a search fails for a ticker, score = 1 / category = `quiet`, note the failure in the digest. Do not halt the full run.
- **Foreign-listed tickers** (SIVE, POET): news search still runs; just note that SEC-specific results may be absent.
