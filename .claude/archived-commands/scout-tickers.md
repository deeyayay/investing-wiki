---
description: Research and recommend publicly-traded tickers for empty supply chain tiers in a sector. Pre-populates the dashboard DATA and queues candidates in the Monitor Registry for full onboarding. Usage: /scout-tickers "Sector Name" [--tier "Tier Name"] [--no-push]
allowed-tools: WebSearch, WebFetch, Read, Write, Edit, Bash
---

# Scout Tickers — Discover & Fill Empty Supply Chain Tiers

Research which publicly-traded companies belong in each empty or thin tier of a sector's supply chain, then immediately surface them in the dashboard and queue them for onboarding.

**Sits between:** `/map-sector` (creates tier structure) and `/add-ticker` (creates full wiki pages).  
**Vault path:** `Investing/Wiki/`  
**Dashboard:** `Investing/Output/Dashboard/index.html`  
**Monitor Registry:** `Investing/Wiki/Reference/Monitor Registry.yaml`

**Input:** `$ARGUMENTS` — the sector name (required), plus optional `--tier "Tier Name"` to focus on one tier, and optional `--no-push` to skip git deployment.

---

## Step 1 — Parse arguments

Extract from `$ARGUMENTS`:
- **SECTOR** (required) — the sector display name, e.g. `"Semiconductors"` or `"Cybersecurity"`
- **TIER** (optional) — if `--tier "Tier Name"` is present, restrict research to that tier only
- **NO_PUSH** — if `--no-push` is present, skip the final git commit and deploy step

---

## Step 2 — Validate sector and load context

1. Read `Investing/Wiki/Reference/Dimension Map.md`. Find the row matching SECTOR to get the folder slug (e.g., `"Compute Infrastructure"` → folder `AI Infrastructure`). If no match, print an error and stop.

2. Read `Investing/Output/Dashboard/index.html`. In the DATA object, find the sector object with `name: "[SECTOR]"` and extract the full tiers array. Note which tiers have `companies: []` (empty) and which have only 1 company (thin). If `--tier` is set, filter to just that tier.

3. Read `Investing/Wiki/Sectors/[FOLDER]/_Supply Chain Map.md` if it exists. Extract:
   - The **Publicly-Traded Nodes table** — candidates already identified for each tier
   - The **Structural Gaps section** — tiers where no public player exists (skip these in research)

4. Read `Investing/Wiki/Reference/Monitor Registry.yaml`. Extract all entries from the `candidates:` list where `sector` matches SECTOR — these are tickers already identified but not yet onboarded.

Build a working list: for each target tier, compile (a) any existing Nodes table entries, (b) any Registry CANDIDATE comments, and (c) companies already in the dashboard for that tier.

---

## Step 3 — Research each empty or thin tier

Work through each target tier in priority order: **Chokepoint: Y first**, then **Partial**, then **N**.

For each tier:

**A. Check existing sources**

- If the _Supply Chain Map Publicly-Traded Nodes table has entries for this tier, record them.
- If the Monitor Registry has CANDIDATE comments for this tier, record them.
- If both sources are empty, proceed to web search.

**B. Web search (when no existing candidates)**

Run 1–2 targeted searches:
- `"[SECTOR]" "[TIER NAME]" publicly traded company stock`
- `[key process or product from tier function] company ticker NYSE NASDAQ`

From results, identify 2–4 publicly-traded companies that materially operate in this tier. Prefer companies where this tier represents a significant portion of revenue (not just tangential exposure).

**C. Qualify each candidate**

For each candidate:
- Confirm it is listed on a major exchange (NYSE, NASDAQ, TSX, LSE, TSE, TWSE, ASX, Euronext)
- Determine market cap tier: Large (>$10B), Mid ($1B–$10B), Small (<$1B)
- Check if a wiki page already exists at `Investing/Wiki/Sectors/[FOLDER]/[TICKER].md`
- Check if it is already in the dashboard DATA for this sector and tier
- Assign status: `In wiki`, `CANDIDATE (Registry)`, or `Net new`
- Write a differentiation note (20–30 words): what sets this company apart from tier-mates? Lead with the competitive differentiator, not a product list. Use plain language.

If no credible publicly-traded company fits a tier, note it as a **structural gap** and move on. Do not invent companies.

---

## Step 4 — Print scout report

Print a structured report to the conversation before making any changes:

```
## Scout Report — [SECTOR] — [TODAY'S DATE]
*[N] empty tiers | [N] thin tiers | [N] tiers skipped (structural gap)*

---

### [TIER NAME] ⧫ CHOKEPOINT
*[Tier function — one sentence]*

| Ticker | Company | Mkt Cap | Status | Differentiation |
|--------|---------|---------|--------|-----------------|
| LRCX | Lam Research | Large | Net new | Dominates the etch equipment... |
| AMAT | Applied Materials | Large | Net new | Only equipment supplier spanning... |

---

### [TIER NAME] — Partial
*[Tier function]*

| Ticker | Company | Mkt Cap | Status | Differentiation |
|--------|---------|---------|--------|-----------------|
...

---

### Structural Gaps
- [Tier Name]: [Explanation — why no investable public company exists]
```

Status values: `In wiki` / `CANDIDATE (Registry)` / `Net new`

---

## Step 5 — Update dashboard DATA

For each ticker that is `Net new` or `CANDIDATE (Registry)` (i.e., not already in the dashboard for this tier), add a company entry to `Investing/Output/Dashboard/index.html`.

Use a Python script (via Bash) to do all insertions in one pass:

```python
import re

path = "Investing/Output/Dashboard/index.html"
with open(path) as f:
    content = f.read()

def co(ticker, name, cap, notes):
    return f'{{ ticker: "{ticker}", name: "{name}", mkt_cap: "{cap}", notes: "{notes}" }}'

# For tiers with existing companies: append after the last company entry
# Pattern: match the tier name, find its companies array, append before the closing ]
# For tiers with companies: []: replace with companies: [new entries]

# ... [generated insertions per tier] ...

with open(path, "w") as f:
    f.write(content)
```

Rules:
- Never overwrite or reorder existing company entries — append only
- Skip any ticker already present in that tier's companies array
- Use the exact notes text from Step 3 (differentiation note, 20–30 words)
- Preserve the existing JS object formatting (no trailing commas on last entry)

---

## Step 6 — Update Monitor Registry

For each `Net new` ticker (not yet in the Registry at all), append a CANDIDATE entry to the `candidates:` list in `Investing/Wiki/Reference/Monitor Registry.yaml`:

```yaml
  - ticker: "[TICKER]"
    company: "[Company Name]"
    sector: "[SECTOR]"
    layer: "[Tier Name]"
    source: "scout-tickers"
    added: "[TODAY'S DATE]"
    note: "[differentiation note, 20–30 words]"
```

Use Edit to append to the `candidates:` list. Do not modify the `tickers:` section or remove any existing candidates.

---

## Step 7 — Commit and deploy

Unless `--no-push` is set:

1. Stage the modified files:
   ```bash
   git add Investing/Output/Dashboard/index.html Investing/Wiki/Reference/Monitor\ Registry.md
   ```

2. Commit:
   ```bash
   git commit -m "scout-tickers: populate [SECTOR] tiers ([TODAY'S DATE])"
   ```

3. Deploy to gh-pages:
   ```bash
   git checkout gh-pages
   git show [BRANCH]:Investing/Output/Dashboard/index.html > index.html
   git add index.html
   git commit -m "Deploy ecosystem map [TODAY'S DATE] (scout: [SECTOR])"
   git push
   git checkout [BRANCH]
   ```

4. Push the feature branch:
   ```bash
   git push
   ```

---

## Step 8 — Print summary

Print a completion summary:

```
## Scout Complete — [SECTOR]

Added [N] companies across [N] tiers:
- [TIER NAME]: [TICKER], [TICKER]
- [TIER NAME]: [TICKER]

Structural gaps (no public company): [TIER NAME], [TIER NAME]

Next steps:
- Run /add-ticker [TICKER] --sector "[SECTOR]" to create full wiki pages with fundamental research for each candidate
```

---

## Rules

- **Append-only.** Never overwrite existing companies in the dashboard DATA or existing rows in the Monitor Registry.
- **Quality cap.** Add at most 4 companies per tier. Prefer companies where the tier represents a material revenue share, not peripheral exposure.
- **No invented companies.** If web search returns no credible publicly-traded candidate for a tier, mark it as a structural gap and skip it.
- **Differentiation-first notes.** Notes describe what sets the company apart from tier-mates — not a product list. Plain language, 20–30 words.
- **Skip already-present tickers.** If a ticker is already in the dashboard for this exact tier, do not add a duplicate even if it came from a different source.
- **Foreign-listed tickers are fine.** Include them (TSE, TWSE, LSE, etc.) with the exchange-prefixed ticker format (e.g., `4369.T`, `2308.TW`, `IQE.L`).
- **Structural gaps are valuable signal.** Document them explicitly — they identify where the supply chain has no investable public exposure, which is itself an insight.
