---
description: Map a sector's supply chain structure before adding any tickers. Produces a company-agnostic tier diagram, identifies publicly-traded nodes, and creates _Supply Chain Map.md. Run this before /add-ticker when entering a new sector. Usage: /map-sector "Sector Name" [--anchor "Central Company or Concept"]
allowed-tools: WebSearch, Read, Write, Bash
---

# Map Sector — Supply Chain First

Maps the physical structure of a sector's value chain, then identifies publicly-traded nodes. Produces `_Supply Chain Map.md`. Token-efficient: uses model knowledge for well-known sectors; searches only to fill gaps or verify.

**Output:** `Investing/Wiki/Sectors/[Sector]/_Supply Chain Map.md`
**Input:** `$ARGUMENTS` — `"Sector Name"` (required) + optional `--anchor "concept"`

---

## Step 1 — Parse and check

Extract `SECTOR` and optional `--anchor` from `$ARGUMENTS`.

Read `Investing/Wiki/Reference/Monitor Registry.md` — note which tickers are already registered in this sector.

If `Investing/Wiki/Sectors/[SECTOR]/_Supply Chain Map.md` already exists, print:
```
⚠️  Supply Chain Map already exists for [SECTOR]. Aborting.
    Edit the file directly or run with --refresh to overwrite.
```
Then stop.

---

## Step 2 — Build the supply chain from knowledge

Using your training knowledge, construct the value chain for this sector. No search needed for established sectors (Semiconductors, Photonics, AI Infrastructure, Clean Energy, etc.).

For each tier, determine:
- **Tier name** — short functional label
- **Function** — one sentence: what happens here
- **Chokepoint** — Y / N / Partial (Y = few producers, hard to substitute)
- **Capital Intensity** — High / Medium / Low
- **Moat Type** — Process IP · Scale · Switching cost · Certification · Ecosystem · Geographic monopoly · None
- **Margin Profile** — Very High / High / Medium / Low / Cyclical

Aim for 5–9 tiers. If the sector is unfamiliar or niche, do one web search:
`"[SECTOR]" supply chain layers value chain publicly traded`
Then build the table from results.

---

## Step 3 — Map publicly-traded nodes

From knowledge, populate companies for each tier. Focus on:
- Market cap >$500M (prioritize, but don't exclude chokepoint plays below this)
- Names mentioned in customer earnings calls or institutional 13Fs

Do **one** web search only if coverage feels thin:
`"[SECTOR]" supply chain publicly traded companies by segment site:fool.com OR site:seekingalpha.com OR site:reuters.com`

For each company: ticker, tier, exchange, rough market cap tier (Large/Mid/Small), and whether they're already in the Monitor Registry.

Flag tiers where no public player exists as **Structural Gaps** — these are as informative as the companies themselves.

---

## Step 4 — Write `_Supply Chain Map.md`

Create the sector folder if needed: `mkdir -p "Investing/Wiki/Sectors/[SECTOR]/"`

Write the file:

```markdown
# [SECTOR] — Supply Chain Map
*Mapped: [TODAY'S DATE] | Anchor: [anchor concept]*

---

## Framework Status
- [x] Supply chain mapped
- [ ] Nodes registered (`/add-ticker TICKER --layer "Layer"` for each below)
- [ ] Ground truth pulled (`/stock-research TICKER` per node)
- [ ] Customer matrix built (`/build-customer-matrix "[SECTOR]"`)
- [ ] Sector Framework written (only after above steps complete)

---

## Value Chain

| Tier | Function | Chokepoint | Capital Intensity | Moat Type | Margin Profile |
|------|----------|------------|-------------------|-----------|----------------|
[rows]

---

## Publicly-Traded Nodes

| Tier | Ticker | Company | Mkt Cap | In Registry | Notes |
|------|--------|---------|---------|-------------|-------|
[rows — gaps shown as: | Tier | — | *No public player* | — | — | ⚠️ Structural gap |]

---

## Structural Gaps
[One line per chokepoint tier with no public player: what occupies this space privately and what to watch for.]

---

## Research Log
- **[TODAY'S DATE]** — map-sector run. [N] tiers, [N] nodes identified, [N] gaps. New candidates not yet in registry: [list].
```

---

## Step 5 — Register candidates and print summary

For each ticker found in Step 3 that is **not** in the Monitor Registry, append a comment stub to the correct sector table in the Registry (do not add a full row):
```
<!-- CANDIDATE (/map-sector [DATE]): [TICKER] ([Company]) — [Tier] layer. Run /add-ticker [TICKER] --sector "[SECTOR]" --layer "[Tier]" to onboard. -->
```

Update the `*Last updated:` line in the Registry.

Print:
```
✅ Supply Chain Map — [SECTOR]

   📄 Investing/Wiki/Sectors/[SECTOR]/_Supply Chain Map.md
   🏗️  [N] tiers · [N] chokepoints · [N] structural gaps
   🔵 [N] public nodes identified ([N] already in registry, [N] new candidates)

   New candidates: [TICKER] ([Tier]) · [TICKER] ([Tier]) ...

   Next: /add-ticker TICKER --layer "Layer" for each candidate you want to track
```

---

## Rules

- **Search last.** Use model knowledge first; search only when the sector is unfamiliar or node coverage feels thin. Maximum 2 searches per run.
- **Never overwrite** an existing `_Supply Chain Map.md` without explicit user confirmation.
- **Gaps are signal.** A chokepoint with no public player is the most important output — don't paper over it.
- **Stubs only** in Monitor Registry. Full rows require `/add-ticker`.
