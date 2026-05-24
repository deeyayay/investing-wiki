---
description: Scan for structural technology and architectural shifts affecting sector supply chains. Identifies process-level changes not yet reflected in supply chain maps, appends new rows to Ecosystem Interrelationships.md, and flags affected tiers. Run monthly or after major industry events. Usage: /detect-shifts [--sector "Sector"] [--all]
allowed-tools: WebSearch, Read, Write
---

# Detect Shifts — Structural Technology & Architectural Change Scanner

Scans for technology and architectural shifts that change *how* a sector operates at the process/product level — not just news about companies. Compares against existing supply chain tier definitions. Appends new cross-sector flows and logs identified shifts.

**Outputs:**
- New rows appended to `Investing/Wiki/Reference/Ecosystem Interrelationships.md` (Technology Shift Log + Dependency Graph)
- Drift notes appended to affected `_Supply Chain Map.md` files (under a `## Technology Shifts` section)
- Summary printed to console

**Input:** `$ARGUMENTS` — optional `--sector "Sector Name"` to target one sector, or `--all` to scan all sectors with existing supply chain maps.

---

## Step 1 — Determine scope

Parse `$ARGUMENTS`:
- `--sector "Name"` → scan only that sector
- `--all` → scan all sectors listed in `Investing/Wiki/Reference/Dimension Map.md` with status `partial` or `complete`
- No flag → default to `--all`

Read `Investing/Wiki/Reference/Dimension Map.md` to get the sector list and their current status.
Read `Investing/Wiki/Reference/Ecosystem Interrelationships.md` — note the Technology Shift Log to avoid re-logging known shifts.

---

## Step 2 — Define shift search targets per sector

For each sector in scope, derive search queries targeting *structural process/architectural changes*, not company news. Examples:

| Sector | Example shift queries |
|---|---|
| Semiconductors | "wafer fab process change 2025 2026" · "advanced packaging architecture shift" · "EUV high-NA adoption timeline" · "gate-all-around vs FinFET transition" |
| Compute Infrastructure | "data center power architecture 800VDC" · "direct liquid cooling vs air cooling inflection" · "co-packaged optics CPO timeline" · "AI server rack power density" |
| Energy & Power | "grid-scale battery chemistry shift LFP vs NMC" · "nuclear SMR data center power purchase" · "HVDC transmission adoption" |
| Photonics & Optical | "silicon photonics vs InP transceiver transition" · "co-packaged optics CPO vs pluggable" · "800G 1.6T transceiver architecture" |
| Electronic Components | "ABF substrate supply capacity expansion" · "MLCC dielectric technology shift" · "glass substrate vs organic substrate" |
| Materials & Mining | "SiC substrate alternatives gallium oxide" · "rare earth processing technology" |
| Robotics & Edge AI | "edge AI inference architecture" · "humanoid robot actuator technology" |
| Cybersecurity | "post-quantum cryptography migration timeline" · "AI-native security architecture shift" |

Formulate 2 search queries per sector. Prioritize queries that would surface process/architecture changes, not earnings news.

---

## Step 3 — Search and extract shifts

For each sector, run up to 2 web searches. Scan results for:

**Qualifying as a structural shift (log it):**
- A process is being replaced by a materially different process (e.g., FinFET → GAA transistors; AC UPS → HVDC UPS; pluggable optics → co-packaged optics)
- A new material or product is displacing an incumbent at the component level (e.g., glass substrates beginning to displace organic ABF for advanced packaging)
- An architectural change that requires simultaneous re-spec of multiple tiers (e.g., 800VDC data center architecture)
- A geopolitical or supply event that creates a new structural chokepoint not previously documented

**Not qualifying (skip):**
- Earnings results, guidance changes, stock price moves
- New product launches that fit within existing tier definitions
- Analyst price target changes
- Partnership announcements without structural process implications

For each qualifying shift, note:
- Which sector(s) and tier(s) are affected
- What the old process/product was vs. the new one
- Which other sectors are downstream or upstream (cross-sector impact)
- Impact level: High (affects multiple tiers or sectors) / Medium (affects one tier significantly) / Low (incremental)
- Whether it's already in the Technology Shift Log (skip if yes)

---

## Step 4 — Check against existing tier definitions

For each identified shift, read the relevant `_Supply Chain Map.md`. Compare the shift against the Processes and Key Products / Materials columns for the affected tier.

Ask: Does the current tier definition accurately reflect this shift, or is it describing the old process?

- If the tier definition is **already current** → no update needed; log in Technology Shift Log only if not already there
- If the tier definition is **outdated** → flag with a drift note (see Step 5)
- If the shift **creates a new tier** that doesn't exist → flag as a structural addition needed

---

## Step 5 — Write drift notes to affected supply chain maps

For each supply chain map with outdated tier definitions, append a `## Technology Shifts` section (or append to it if it already exists):

```markdown
## Technology Shifts

### [Shift Name] — Identified [TODAY'S DATE]
**Affected tier:** [Tier Name]
**Status:** Emerging / In transition / Broadly adopted
**Old process/product:** [what the tier definition currently says]
**Emerging process/product:** [what is replacing it]
**Cross-sector impact:** [which other sectors are affected and how]
**Impact level:** High / Medium / Low
**Action:** Run `/map-sector "[SECTOR]" --refresh` to update the tier definition when the transition is sufficiently mature.
```

Do not rewrite existing tier rows — append drift notes only.

---

## Step 6 — Append to Ecosystem Interrelationships

Read `Investing/Wiki/Reference/Ecosystem Interrelationships.md`.

1. **Technology Shift Log** — append a new row for each qualifying shift not already logged:
   `| [TODAY'S DATE] | [Shift description] | [Sectors affected] | [High/Medium/Low] | [Tiers affected] |`

2. **Dependency Graph** — append new rows for any new cross-sector flows created or modified by the shift. Use the same format as existing rows. Skip rows that already exist.

---

## Step 7 — Print summary

```
✅ Detect Shifts — [TODAY'S DATE]

   Sectors scanned: [N]
   Shifts identified: [N] ([N] new, [N] already logged)

   New shifts:
   • [Sector] — [Shift name] (Impact: High/Medium/Low)
     Tiers affected: [Tier names]
     Cross-sector: [sectors]

   Drift notes written to:
   • [path to _Supply Chain Map.md] — [N] tiers flagged

   Interrelationships updated:
   • [N] rows added to Technology Shift Log
   • [N] rows added to Dependency Graph

   Recommended next steps:
   • /map-sector "[SECTOR]" --refresh  ← for sectors where shift is broadly adopted
```

---

## Rules

- **Structural changes only.** Company news and earnings are handled by `/ticker-monitor` and `/daily-news`. This skill targets process/architecture shifts that change tier definitions.
- **Append-only.** Never rewrite existing tier rows in supply chain maps. Drift notes are addendums.
- **Log known shifts once.** Check the Technology Shift Log before appending — do not duplicate rows.
- **Maximum 2 searches per sector.** This skill is designed to run across many sectors; token efficiency matters.
- **Don't trigger a map rebuild prematurely.** A shift that is "discussed" but not yet in production does not warrant a tier rewrite — it warrants a drift note flagged as "Emerging."
