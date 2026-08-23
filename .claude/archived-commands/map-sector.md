---
description: Map a sector's supply chain structure before adding any tickers. Produces a company-agnostic tier diagram with process/product depth, identifies publicly-traded nodes, and creates _Supply Chain Map.md. Run this before /add-ticker when entering a new sector. Usage: /map-sector "Sector Name" [--anchor "Central Company or Concept"]
allowed-tools: WebSearch, Read, Write, Bash
---

# Map Sector — Supply Chain First

Maps the physical structure of a sector's value chain at the process and product level, then identifies publicly-traded nodes. Produces `_Supply Chain Map.md` and appends cross-sector flows to `Ecosystem Interrelationships.md`.

**Output:** `Investing/Wiki/Sectors/[Sector]/_Supply Chain Map.md`
**Input:** `$ARGUMENTS` — `"Sector Name"` (required) + optional `--anchor "concept"`

---

## Step 1 — Parse and check

Extract `SECTOR` and optional `--anchor` from `$ARGUMENTS`.

Read `Investing/Wiki/Reference/Monitor Registry.md` — note which tickers are already registered in this sector.
Read `Investing/Wiki/Reference/Dimension Map.md` — note the dimension (D1–D5) for this sector and its current status.

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
- **Processes** — specific operations performed at this tier (not company names — operations). Be specific: name the process steps, not the function category. Examples: "photolithography, CVD/ALD deposition, ion implantation, CMP, wet/dry etch, metrology loops" not "wafer processing"
- **Key Products / Materials** — specific inputs consumed or outputs produced at this tier. Name the actual product: "ABF substrate, SiC MOSFET, 900V polypropylene film capacitor" not "components"
- **Chokepoint** — Y / N / Partial (Y = few producers, hard to substitute, no alternative process)
- **Capital Intensity** — High / Medium / Low
- **Moat Type** — Process IP · Scale · Switching cost · Certification · Ecosystem · Geographic monopoly · None
- **Margin Profile** — Very High / High / Medium / Low / Cyclical

Aim for 5–9 tiers. If the sector is unfamiliar or niche, do one web search:
`"[SECTOR]" supply chain layers value chain publicly traded`
Then build the table from results.

**Depth standard:** Each Processes cell should list 3–6 specific operations. Each Key Products / Materials cell should list 3–5 named inputs or outputs. Generic descriptions fail this standard.

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

## Step 4 — Identify cross-sector interrelationships

Before writing, determine what this sector **consumes from** and **supplies to** other sectors. Be specific at the product/process level:

**Inputs (what this sector consumes from other sectors):**
- What raw materials or processed inputs arrive from Materials & Mining?
- What components or equipment arrive from other D1 sectors?
- What power, connectivity, or infrastructure does this sector depend on from D2/D3?

**Outputs (what this sector supplies to other sectors):**
- Which specific products flow to Compute Infrastructure, Energy & Power, Robotics, etc.?
- Which outputs are structural inputs to other sectors (not just sold to end customers)?

For each identified flow, note: From Sector | From Tier | To Sector | To Tier | Flow Type (Material / Component / Service / Signal / Process) | Product / Process | Chokepoint?

---

## Step 5 — Write `_Supply Chain Map.md`

Create the sector folder if needed: `mkdir -p "Investing/Wiki/Sectors/[SECTOR]/"`

Write the file using this template:

```markdown
# [SECTOR] — Supply Chain Map
*Mapped: [TODAY'S DATE] | Anchor: [anchor concept]*
*Dimension: [D1/D2/D3/D4/D5] — [Dimension Name]*

---

## Framework Status
- [x] Supply chain mapped
- [x] Process/product depth added ([TODAY'S DATE])
- [x] Interrelationship Anchors documented ([TODAY'S DATE])
- [ ] Nodes registered (`/add-ticker TICKER --layer "Layer"` for each below)
- [ ] Ground truth pulled (`/stock-research TICKER` per node)
- [ ] Customer matrix built (`/build-customer-matrix "[SECTOR]"`)
- [ ] Sector Framework written (only after above steps complete)

---

## Value Chain

| Tier | Function | Processes | Key Products / Materials | Chokepoint | Capital Intensity | Moat Type | Margin Profile |
|------|----------|-----------|--------------------------|------------|-------------------|-----------|----------------|
[rows — each Processes cell: 3–6 specific operations; each Key Products cell: 3–5 named inputs/outputs]

---

## Publicly-Traded Nodes

| Tier | Ticker | Company | Mkt Cap | In Registry | Notes |
|------|--------|---------|---------|-------------|-------|
[rows — gaps shown as: | Tier | — | *No public player* | — | — | ⚠️ Structural gap |]

---

## Structural Gaps
[One paragraph per chokepoint tier with no public player: what occupies this space privately, why it's hard to substitute, what to watch for.]

---

## Key Questions to Answer Before Writing the Sector Framework
[3–6 unresolved structural questions that materially affect the investment thesis for this sector.]

---

## Interrelationship Anchors

### Inputs (this sector consumes from)
| From Sector | From Tier | Product / Signal |
|---|---|---|
[rows]

### Outputs (this sector supplies to)
| To Sector | To Tier | Product / Signal |
|---|---|---|
[rows]

---

## Research Log
- **[TODAY'S DATE]** — map-sector run. [N] tiers, [N] chokepoints, [N] structural gaps. New candidates not yet in registry: [list].
```

---

## Step 6 — Append to Ecosystem Interrelationships

Read `Investing/Wiki/Reference/Ecosystem Interrelationships.md`.

For each cross-sector flow identified in Step 4, append a row to the Dependency Graph table:
```
| [From Sector] | [From Tier] | [To Sector] | [To Tier] | [Flow Type] | [Product / Process description] | [Y/N/Partial] | [Notes if any] |
```

Do not duplicate rows that already exist. If a row already exists for the same From/To/Product combination, skip it or add a note variant.

---

## Step 7 — Update Dimension Map status

Read `Investing/Wiki/Reference/Dimension Map.md`. Update the Status column for this sector from `planned` or `framework-only` to `partial` (map exists with process/product depth, nodes not yet fully registered).

---

## Step 8 — Register candidates and print summary

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
   🔗 [N] cross-sector flows appended to Ecosystem Interrelationships.md

   New candidates: [TICKER] ([Tier]) · [TICKER] ([Tier]) ...

   Next: /add-ticker TICKER --layer "Layer" for each candidate you want to track
```

---

## Rules

- **Search last.** Use model knowledge first; search only when the sector is unfamiliar or node coverage feels thin. Maximum 2 searches per run.
- **Process and product specificity is required.** Generic tier descriptions ("components are assembled here") do not meet the depth standard. Name the operations and name the products.
- **Never overwrite** an existing `_Supply Chain Map.md` without explicit user confirmation.
- **Gaps are signal.** A chokepoint with no public player is the most important output — don't paper over it.
- **Stubs only** in Monitor Registry. Full rows require `/add-ticker`.
- **Always append** cross-sector flows to `Ecosystem Interrelationships.md` — never skip this step.
