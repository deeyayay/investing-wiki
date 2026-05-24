---
description: Map a sector's supply chain structure before adding any tickers. Produces a company-agnostic tier diagram, identifies publicly-traded nodes, and creates _Supply Chain Map.md. Run this before /add-ticker when entering a new sector. Usage: /map-sector "Sector Name" [--anchor "Central Company or Concept"]
allowed-tools: WebSearch, WebFetch, Read, Write, Edit, Glob, Bash
---

# Map Sector — Supply Chain First

Maps the physical structure of a sector's value chain before any companies are named. Produces `_Supply Chain Map.md` — the foundational document for sector-first research. Companies are discovered in Step 3; the sector structure is established independently in Steps 1–2.

**Output path:** `Investing/Wiki/Sectors/[Sector]/_Supply Chain Map.md`
**Monitor Registry:** `Investing/Wiki/Reference/Monitor Registry.md`

**Input:** `$ARGUMENTS`
- `"Sector Name"` — required. Must match or closely match an existing sector folder, or be a new sector.
- `--anchor "..."` — optional. The central company, product, or concept the supply chain flows toward (e.g., `--anchor "AI GPU"` for Semiconductors). If omitted, infer from sector name.

---

## Step 1 — Parse arguments and orient

Extract from `$ARGUMENTS`:
- `SECTOR` — sector name string (e.g., `Semiconductors`, `Photonics & Optical`)
- `--anchor` — optional anchor concept

Read the Monitor Registry to check if this sector already has a table. Note:
- How many tickers are already registered in this sector
- Whether `_Supply Chain Map.md` already exists at `Investing/Wiki/Sectors/[SECTOR]/_Supply Chain Map.md`

If `_Supply Chain Map.md` already exists, print:
```
⚠️  Supply Chain Map already exists for [SECTOR] at:
    Investing/Wiki/Sectors/[SECTOR]/_Supply Chain Map.md

    Options:
    • To refresh the node list from registry, re-run with --refresh (not yet implemented — edit the file manually)
    • To proceed and overwrite, confirm explicitly
    Aborting.
```
Then stop unless the user has explicitly confirmed overwrite.

Determine the anchor concept if not provided:
- `Semiconductors` → "packaged chip ready for electronic assembly"
- `Photonics & Optical` → "optical data transmission from source to receiver"
- `AI Infrastructure` → "end-to-end AI compute and inference delivery"
- `Clean Energy` → "electricity generated from non-fossil sources delivered to grid"
- `Robotics & Edge AI` → "autonomous robotic action driven by on-device AI"
- `Cybersecurity` → "detection and prevention of unauthorized access to digital systems"
- `Fintech & E-Commerce` → "digital financial transaction from initiation to settlement"
- `Metals & Mining` → "refined critical mineral delivered to industrial end user"
- `Space & Comms` → "data transmitted from ground through space and back"
- For any other sector: infer from the name and state your interpretation before continuing

Print your working definition:
```
Sector:  [SECTOR]
Anchor:  [anchor concept — what the supply chain delivers]
Existing tickers in registry: [N]

Mapping supply chain structure...
```

---

## Step 2 — Map the company-agnostic structure (3 parallel searches)

Run these three searches in parallel. Do not name specific companies yet — focus on understanding the physical and economic structure.

**Search A — Physical process:**
`"[SECTOR]" supply chain steps process flow "from [raw input] to [finished product]"`

Also search: `"[anchor concept]" value chain layers upstream downstream`

Extract: What are the major discrete steps or stages required to produce/deliver the anchor product? List them in sequential order.

**Search B — Capital intensity and chokepoints:**
`"[SECTOR]" supply chain chokepoints bottlenecks capital intensive barriers to entry`

Also search: `"[anchor concept]" where does value concentrate supply chain`

Extract: Which steps require the most capital? Which have the fewest viable producers? Which steps, if disrupted, halt the entire chain?

**Search C — Industry structure:**
`"[SECTOR]" industry structure oligopoly monopoly fragmented competitive dynamics`

Also search: `"[anchor concept]" market structure moat types by layer`

Extract: Which layers are consolidated (1–3 players) vs. fragmented (many players)? Where do margins concentrate?

---

## Step 3 — Build the tier table (company-agnostic)

From the Search A/B/C results, construct the value chain as a sequence of tiers. Each tier represents a distinct layer where value is added.

Format each tier with:
- **Tier name** — short functional label (e.g., "Raw Materials", "Wafer Fabrication", "Chip Packaging", "Testing & QA", "System Integration")
- **What happens here** — one sentence: the physical or economic transformation at this layer
- **Chokepoint** — Y / N / Partial. Y = few viable producers, hard to substitute; N = many players, commoditized
- **Capital intensity** — High / Medium / Low
- **Moat type** — the dominant moat at this layer (e.g., Process IP, Scale, Switching cost, Certification, Ecosystem lock-in, Geographic monopoly, None)
- **Margin profile** — Very High / High / Medium / Low / Cyclical

Aim for 5–10 tiers. More granular is better than too coarse — you can always merge, not split later.

---

## Step 4 — Identify publicly-traded nodes (3 parallel searches)

Now map companies onto the tier structure. For each tier from Step 3, search:

`publicly traded companies "[tier name]" "[SECTOR]" stock ticker`

Also: `"[SECTOR]" "[tier name]" segment revenue publicly listed`

For each company found, record:
- Ticker symbol (or `?` if uncertain)
- Company name
- Which tier they occupy
- Exchange / market cap tier (Large >$10B / Mid $1B–$10B / Small $100M–$1B / Micro <$100M)
- Whether they're already in the Monitor Registry (cross-reference)

**Prioritization filter:** Focus on companies that meet at least 2 of 3:
1. Market cap >$500M (liquid, easier data)
2. Covered by institutional investors (13F filings, analyst reports)
3. Mentioned in major customer earnings calls (validation they matter to the chain)

Flag but don't exclude smaller names if they occupy a chokepoint tier with few alternatives.

---

## Step 5 — Identify gaps

For each chokepoint tier (Step 3), check: is there a publicly-traded company identified in Step 4?

If a chokepoint tier has no public players, flag it as a **Structural Gap**:
- No investable public company exists at this chokepoint
- Either: privately held, government-owned, vertically integrated inside a larger conglomerate, or pre-IPO
- Investment implication: monitor for IPOs/spin-offs; watch for customer earnings mentions of this bottleneck

---

## Step 6 — Write `_Supply Chain Map.md`

Determine output path: `Investing/Wiki/Sectors/[SECTOR]/_Supply Chain Map.md`

If the sector folder doesn't exist: `mkdir -p "Investing/Wiki/Sectors/[SECTOR]/"`

Write the file using this exact structure:

```markdown
# [SECTOR] — Supply Chain Map
*Mapped: [TODAY'S DATE] | Review: quarterly or after major sector event*
*Anchor product: [anchor concept from Step 1]*

---

## Framework Status
- [x] Supply chain mapped
- [ ] Nodes identified in Monitor Registry
- [ ] Ground truth pulled (filings, earnings calls)
- [ ] Customer matrix built (`_Customer Matrix.md`)
- [ ] Sector Framework written (`_Sector Framework.md`)

*Check off each step as you complete the sector-first research sequence.*

---

## Value Chain — Tier Structure

| Tier | Function | Chokepoint | Capital Intensity | Moat Type | Margin Profile |
|------|----------|------------|-------------------|-----------|----------------|
[rows from Step 3]

**Reading this table:**
- **Chokepoint Y** = few viable producers; disruption here halts the chain
- **Moat Type** drives whether value accrues to the tier durably or competes away
- Invest where: Chokepoint = Y + Moat ≠ None + Margin = High or Very High

---

## Node Map — Publicly Traded Companies by Tier

| Tier | Ticker | Company | Exchange | Mkt Cap | In Registry | Notes |
|------|--------|---------|----------|---------|-------------|-------|
[rows from Step 4 — sorted by tier, then market cap descending]
[gap rows formatted as: | [Tier] | — | *No public player* | — | — | — | ⚠️ Structural gap at chokepoint tier |]

---

## Structural Gaps

[For each chokepoint tier with no public company, write a short paragraph:]

### Gap: [Tier Name]
*No publicly traded pure-play exists at this layer.* [1–2 sentences on who occupies this space privately or why it's embedded in larger conglomerates.] **Watch for:** [IPO signals, spin-off candidates, or customer earnings mentions that reveal the bottleneck.]

[If no gaps exist, write: "No structural gaps identified — all chokepoint tiers have at least one publicly traded player."]

---

## Key Questions to Answer Before Writing the Sector Framework

1. Which tier has the highest pricing power and why?
2. Which tier is most at risk of commoditization over the next 3–5 years?
3. Where does the end customer (hyperscaler / OEM / consumer) have the most leverage over suppliers?
4. Which tiers are currently supply-constrained vs. demand-constrained?
5. What technology shift (if any) is most likely to restructure the value chain?

*Answer these in `_Sector Framework.md` after completing ground-truth research on registered tickers.*

---

## Research Log
- **[TODAY'S DATE]** — map-sector run. [N] tiers mapped, [N] public nodes identified, [N] structural gaps flagged. Tickers not yet registered: [list any net-new tickers found that aren't in the registry].
```

---

## Step 7 — Update Monitor Registry with new node candidates

Read the Monitor Registry.

For any ticker found in Step 4 that is **not already in the registry**, append a comment block at the bottom of the correct sector table (or create the sector table if it doesn't exist):

```markdown
<!-- CANDIDATE (from /map-sector [DATE]) — not yet onboarded: [TICKER] ([Company]) at [Tier] layer. Run /add-ticker [TICKER] --sector "[SECTOR]" --layer "[Tier]" to onboard. -->
```

Do not add full registry rows — only the comment stub. Full onboarding requires `/add-ticker`.

If the sector has no existing table in the Registry, create one with just the header and the comment stubs:
```markdown
## [SECTOR]

| Ticker | Company | CIK | Exchange | Path | Score |
|--------|---------|-----|----------|------|-------|

<!-- CANDIDATE (from /map-sector [DATE]): [list each] -->
```

Update the `*Last updated:` line at the top of the Monitor Registry.

---

## Step 8 — Print summary

```
✅ Supply Chain Map created — [SECTOR]

   📄 File:    Investing/Wiki/Sectors/[SECTOR]/_Supply Chain Map.md
   🏗️  Tiers:   [N] layers mapped ([N] chokepoints, [N] commoditized)
   🔵 Nodes:   [N] publicly traded companies identified
   ⚠️  Gaps:    [N] structural gaps at chokepoint tiers
   📋 Registry: [N] new candidates added as stubs

   Already in registry: [list tickers already registered, with their tier]
   Net new candidates:  [list new tickers found, with their tier]

   Next steps:
   1. Review the Supply Chain Map and confirm tier structure is accurate
   2. Run /add-ticker [TICKER] --sector "[SECTOR]" --layer "[Tier]" for each candidate you want to track
   3. Run /stock-research [TICKER] for each added ticker to pull ground truth
   4. Run /build-customer-matrix "[SECTOR]" once ≥5 tickers are registered
   5. Write _Sector Framework.md after customer matrix is complete
```

---

## Rules

- **Company-agnostic first.** The tier structure (Step 2–3) must be completed before any company names are introduced (Step 4). Do not collapse these steps.
- **Never overwrite an existing `_Supply Chain Map.md`** unless the user has explicitly confirmed. Print the warning from Step 1 and stop.
- **Mark gaps explicitly.** A chokepoint tier with no public player is valuable signal — do not paper over it with a large conglomerate that happens to have minor exposure. The gap itself is the insight.
- **Stay in the sector.** Do not add tickers from adjacent sectors even if they have some exposure. Cross-sector signals belong in ticker pages, not the supply chain map.
- **Stubs only in Registry.** Do not write full registry rows for unvetted candidates. The comment stub preserves the signal without polluting the registry with unresearched names.
- **Fail gracefully.** If web search returns thin results for a niche sector, write what's available, note the gaps explicitly in the Research Log, and suggest analyst report searches the user can run manually.
