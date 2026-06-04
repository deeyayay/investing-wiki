---
target: Investing/Output/Dashboard/index.html
total_score: 27
p0_count: 0
p1_count: 1
p2_count: 3
timestamp: 2026-05-27T21-52-34Z
slug: investing-output-dashboard-index-html
---
## Design Health Score

| # | Heuristic | Score | Key Issue |
|---|-----------|-------|-----------|
| 1 | Visibility of System Status | 3 | Breadcrumbs and sticky header anchor location well; no loading states or animated transitions between layers |
| 2 | Match System / Real World | 4 | Domain language ("chokepoint", supply-chain tier names) is precise and exact; no metaphor mismatch |
| 3 | User Control and Freedom | 3 | Breadcrumb back-nav works; no forward-jump, no search, no sibling navigation between sectors at the same level |
| 4 | Consistency and Standards | 4 | Hover states, typography scale, color roles, and interaction affordances are consistent throughout |
| 5 | Error Prevention | 2 | Clicking a tier wipes the sector scroll position instantly; no undo; no confirmation on state-wipes |
| 6 | Recognition Rather Than Recall | 3 | Tier and sector names are always visible; the D1–D6 dimension legend is not persistently on-screen |
| 7 | Flexibility and Efficiency | 2 | No keyboard navigation, no search, no URL fragments, no direct-access shortcuts for any tier |
| 8 | Aesthetic and Minimalist Design | 3 | Restrained and purposeful; the right-aligned dim-desc on L0 carries visual weight without clear hierarchy payoff |
| 9 | Error Recovery | 2 | Back button only; scroll position resets on tier click; no breadcrumb-based undo |
| 10 | Help and Documentation | 1 | No tooltips, no glossary, no dimension legend, no "why is D4 empty" explanation |
| **Total** | | **27/40** | **Solid product baseline; scaffolding gaps hold it back** |

## Anti-Patterns Verdict

LLM assessment: Pass. OKLCH color calibration is deliberate. No gradient text, no glassmorphism, no hero-metric layout, no side-stripe borders (cleaned in layout pass), no purple-blue gradients.

Deterministic scan: unavailable (bundled detector missing). Manual grep scan: clean.

One contextual flag: sector cards on L0 are identical structure. False positive — navigation anchors, not marketing content.

## Overall Impression

Research instrument that earns trust through restraint. Brilliant structure-surfacing; goes quiet when action is needed. The single biggest opportunity is bridging reading a tier detail to doing something with it.

## What's Working

1. OKLCH color system is strategic and calibrated — hue stepping across D1-D6, amber earned as critical signal, colorblind-safe via symbol+text redundancy.
2. Three-layer IA matches analyst mental model exactly — dimension → sector → tier → company maps naturally.
3. Typography is invisible in the best way — 22px→15px→13px→11px scale reads clearly without theatrics.

## Priority Issues

**[P1] No search or direct access** — No search field, no URL fragments. Finding any specific tier requires 3-4 clicks every time. Fix: sticky header search box filtering tier/sector/ticker names.

**[P2] Terminal L2: no next action** — After reading tracked companies (NVDA, ASML), nothing happens. No ticker links, no wiki page links, no watchlist. Fix: make ticker symbols `<a>` tags linking to wiki pages.

**[P2] Help and documentation: D1-D6 legend not persistent** — Legend disappears on L1/L2. No glossary for "chokepoint", no explanation for empty D4. Fix: "?" icon in header; show dimension label in breadcrumb area on L1/L2.

**[P2] Scroll position resets on tier click** — Returning from L2 to L1 resets scroll to top. On 12-tier sectors, user loses their place every time. Fix: save/restore scroll offset per layer in JS (4-line fix).

**[P3] Tier order in supply chain is implicit** — Top-to-bottom represents raw materials → finished product, but no visual cue. Fix: subtle tier index label (e.g., "3 / 11") on each tier card.

## Persona Red Flags

**Alex (Power User):** No keyboard shortcuts; revisiting a specific tier takes 3 clicks minimum; no link from company list to wiki pages; scroll-position reset on back-nav; dim-desc occupies real estate without earning it.

**Cross-Reference Analyst (hypothetical second reader):** No context for D1-D6 numbering system; browser back button resets entire SPA state; no URL to share specific tier state; "Small cap" badge has no legend.

## Minor Observations

- Browser back button resets SPA state; pushState() on layer transitions would fix this
- dim-desc right-aligned 12px text is hidden on mobile and likely unread on desktop — consider removing or elevating
- translateY(-1px) hover lift is barely perceptible at standard DPI; 2px would read more decisively
- Internal skill command "/map-sector" leaks into user-facing empty-dim message
- Monospace font on ticker symbols is a tasteful touch

## Questions to Consider

1. What if tickers were hyperlinks? Clicking NVDA could open the wiki page — the terminal-L2 problem dissolves.
2. Does the dashboard need to be read-only? Even a local-storage annotation layer would transform this from map to working document.
3. What does this look like at 30 sectors? L0's dimension-group layout may need a tabbed sidebar filter at scale.
