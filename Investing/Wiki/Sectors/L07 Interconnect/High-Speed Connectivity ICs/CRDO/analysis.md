# CRDO — Analysis
*Layer 2 — Thesis, conviction, and scoring.*
*Last updated: 2026-06-07 (migrated from legacy CRDO.md)*

---

## One-Line Thesis
Full-stack SerDes IP owner that has become the de facto AEC standard inside AI GPU clusters — FY2026 revenue tripled to $1.34B at 68% gross margins, now vertically integrating into optical via the $1.3B DustPhotonics acquisition (silicon photonics PICs) alongside the smaller Hyperlume (microLED) deal.

---

## Investment Thesis

> **Thesis established:** May 19, 2026
> **Last validated:** 2026-09-02 (deep pass)
> **Drift status:** On track, evolving — /dig confirms the 09-01 8-K was Q1 FY2027 earnings (period ended 2026-08-01, reported on time; the standing "09-09" date was simply wrong, now corrected). Revenue and non-GAAP margin both beat/held ($479.0M, +114.7% YoY; 68.0% non-GAAP GM vs. 68.3% prior Q); the -11.8% reaction and GAAP-margin "miss" trace entirely to $11.0M/quarter of non-cash purchase-accounting amortization from the DustPhotonics acquisition (closed 2026-05-28), not operational or demand weakness. DustPhotonics — a $750M-cash-plus-stock deal, ~8x Hyperlume's size — was never previously logged; it's a materially larger optical-expansion vehicle than the thesis's Hyperlume framing suggested.

Credo designs SerDes (serializer/deserializer) chips, retimers, and Active Electrical Cables (AECs) — the components that move data at 400G/800G/1.6T between GPUs, switches, and storage within AI data center racks. As hyperscalers build 100,000+ GPU clusters for AI training and inference, intra-rack connectivity has become a first-order engineering constraint. Credo's AECs address it: a chip-embedded-in-cable approach that extends signal reach while consuming roughly half the power of optical transceivers, with 100× the reliability. FY2026 revenue tripled to $1.34B at ~68% non-GAAP gross margins — a fabless semiconductor company compounding revenue at hyperscale rates while sustaining margins that would be exceptional even for a software business.

The primary growth engine is the AI cluster buildout cycle. Credo is estimated to hold ~75% market share in the AI AEC market — every Blackwell or future NVIDIA rack contains hundreds of intra-rack connections, each one a Credo AEC or a competitor's solution. The 1.6T switch transition expected in H2 2026 triggers a full AEC replacement across installed clusters (400G and 800G cables cannot run 1.6T traffic), creating a step-function revenue event. PCIe retimers represent a second TAM of >$1B by 2027 as backplanes require signal conditioning at PCIe Gen 6 data rates. A fifth hyperscaler entered qualification in FY2026, meaningfully reducing customer concentration. Two acquisitions extend the stack into optical: the smaller Hyperlume deal ($92M, closed by Q4 FY2026) adds microLED-based optical interconnect, while the much larger DustPhotonics acquisition ($750M cash + stock, announced 2026-04-13, closed 2026-05-28) brings silicon photonics PIC (SiPho PIC) technology in-house — the component previously externally sourced for Credo's ZeroFlap optical transceivers, spanning 400G/800G/1.6T with a 3.2T roadmap and feeding Credo's NPO/CPO design wins (LightCounting estimates the SiPho PIC TAM at $6B by 2030). The DustPhotonics deal, not Hyperlume, is now the primary vehicle for Credo's copper-to-optical hedge.

The moat is end-to-end proprietary SerDes IP: Credo owns the full stack from IP core through retimer IC to AEC system, now extending to silicon photonics PICs post-DustPhotonics. Design wins at hyperscalers are co-developed over 12–18 month qualification cycles, creating per-customer switching costs that neither Marvell nor Astera Labs can displace mid-cycle. CEO Bill Brennan (since 2014) has compounded revenue from ~$59M to $1.34B. Co-founders CTO Chi Fung Cheng (3.95% ownership) and COO Yat Tung Lam (2.01%) remain deeply embedded. The CEO PSU plan, granted in June 2026 alongside CFO Dan Fleming's performance-based award, ties long-duration compensation to revenue and margin targets rather than time-vesting.

**Key moat:** Full-stack proprietary SerDes IP (IP core → retimer IC → AEC system → silicon photonics PIC post-DustPhotonics); hyperscaler co-development qualification cycles creating switching costs; ~75% AEC market share with ZeroFlap reliability moat; DustPhotonics + Hyperlume optical adjacency hedging the long-term copper displacement risk.

**Key risks:** Customer concentration (~88% from top 3 hyperscalers as of FY2026); revenue highly sensitive to a single hyperscaler's capex timing; Astera Labs as a credible pure-play competitor with overlapping retimer roadmap; Broadcom/Marvell can bundle competing solutions with switch silicon at scale; DustPhotonics integration execution risk ($750M+ deal, ~10x Hyperlume's size, plus Hyperlume's own $92M integration with no commercial product yet); GAAP gross margin now structurally ~4pt below non-GAAP going forward from DustPhotonics intangible amortization — a headline-margin optics risk even when the underlying (non-GAAP) economics hold.

---

### Deep Pass — 2026-09-02

Triggered by `/brief`'s 09-01-evening escalation: an 8-K (items 2.02/9.01) showed shares -11.8% on "margin guidance," conflicting with a standing note that earnings were due 09-09. Read the 8-K body, the Q1 FY2027 earnings press release (Exhibit 99.1) including its full GAAP-to-non-GAAP reconciliation tables, the 04-13 8-K (ATM offering + DustPhotonics agreement), and the balance sheet across the last two quarters. One targeted web search confirmed the DustPhotonics deal's name/terms/close date against the SEC primary source.

| Thesis claim | Verdict | Source |
|---|---|---|
| Full-stack SerDes IP owner (IP core → retimer → AEC) | CONFIRMED | Unaffected; extended by DustPhotonics SiPho PIC integration (SEC 8-K EX-99.1, 2026-04-13) |
| De facto AEC standard, ~75% market share | INTACT | No new share data this cycle; revenue growth (+114.7% YoY) consistent with continued share, not independently re-measured |
| FY2026 revenue tripled to $1.34B | CONFIRMED | Established fact, unaffected; Q1 FY2027 continues the trajectory ($479.0M, +114.7% YoY per 8-K EX-99.1, 2026-09-01) |
| ~68% non-GAAP gross margins | CONFIRMED | 68.0% actual this quarter vs. 68.3% prior quarter (immaterial decline); 67.0–69.0% guided for Q2 FY2027 — the reconciliation table (8-K EX-99.1) shows the GAAP-level "miss" (64.5% vs. 68.2% prior Q) is $11.0M of new DustPhotonics intangible amortization in COGS, not a pricing or operating change |
| Earnings due 2026-09-09 (standing registry/catalyst note) | BROKEN (the note, not the thesis) | 8-K confirms results were for the quarter ended 2026-08-01, reported on time 2026-09-01; "09-09" was simply an incorrect date, now corrected in facts.md and the Catalyst Timeline |
| "Expanding to optical via Hyperlume" | CONFIRMED, thesis statement updated | Hyperlume ($92M) is real but is not the dominant optical vehicle it was framed as — DustPhotonics ($750M cash + stock, closed 2026-05-28, previously **never logged** in this KB) is ~8x larger and is the load-bearing fact for the copper-to-optical hedge going forward (SEC 8-K EX-99.1, 2026-04-13; balance sheet reconciliation, 8-K EX-99.1, 2026-09-01) |

**The one thing that matters:** the -11.8% stock reaction and "margin guidance" headlines were a real but misdiagnosed signal — the actual news buried under it was a $750M-plus acquisition (DustPhotonics, silicon photonics) that this KB had never recorded, discovered only by reconciling the balance sheet across two quarters. Nothing in the thesis is weakened; the optical-hedge leg is materially stronger than previously understood, and the margin story is a non-cash accounting artifact of the deal, not a demand or pricing-power problem.

**Thesis action:** drift updated (Drifting → On track, evolving); One-Line Thesis and Investment Thesis paragraph rewritten to name DustPhotonics; facts.md gets a new `acquisitions:` block, corrected `next_earnings`, and the missing FY2026 10-K (filed 2026-06-15) added to `filings:`.

---

## Scoring Summary
_Last scored: 2026-06-07 | [[Scoring Rubric]]_

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Product (Love Factor) | 4/5 | Proprietary SerDes IP end-to-end; hyperscaler co-dev qualification creates high switching costs; copper AEC taking share from optical at short reach |
| Pricing Power | 4/5 | 67–68% non-GAAP GM sustained as revenue triples (+157% YoY Q4 FY2026); volume acceleration without margin compression |
| Leadership & Alignment | 4/5 | CEO Brennan 12yr tenure, 7x revenue compound; co-founders CTO (6.84M sh) + COO (3.47M sh) active; CEO PSU with stretch milestones; 3 consecutive beats |
| Financial Health | 4/5 | GAAP profitable FY2025 ($52M net income +284%); fabless light capex; $736M net cash raised via ATM; non-GAAP GM expanding to ~68% |
| Macro Environment | 4/5 | AI cluster buildout is Already Fired forcing function; 2nd-order mandatory component in every GPU rack; 1 manageable headwind: optical displacement risk at future generations |
| Future Potential | 4/5 | 1.6T AEC cycle H2 2026, PCIe retimer TAM >$1B by 2027, new hyperscaler design wins — 2-3 adjacencies with confirmed near-term catalyst |
| **Composite** | **8.0/10** | **Unrivaled** |

**Valuation:** Expensive (growth premium) | Forward P/E est. ~45–55x at Q4 run rate | Analyst consensus PT ~$278 (4 firms post-Q4 FY2026: Roth $300, Mizuho $290, Jefferies $270, JPMorgan $250)
**Growth Potential:** High — 1.6T transition and PCIe retimer represent two distinct step-functions in FY2027

---

## Conviction Log

| Date | Event | Δ Conviction | Why |
|------|-------|-------------|-----|
| 2026-09-02 | Deep pass resolves the 09-01 8-K: Q1 FY2027 beat on revenue ($479.0M, +114.7% YoY) and non-GAAP GM held at 68.0%; the -11.8% drop and GAAP-GM "miss" are entirely DustPhotonics purchase-accounting amortization, not operational | ↑ (reverses 09-01's ↓) | Primary-source reconciliation table confirms no operational margin erosion — the market's/headline reaction was to a non-cash GAAP optic, not a demand or pricing-power problem |
| 2026-09-02 | Deep pass discovers a previously unlogged $750M-cash-plus-stock DustPhotonics acquisition (announced 2026-04-13, closed 2026-05-28) — brings silicon photonics PIC technology in-house | ↑ | ~8x larger than the previously-tracked Hyperlume deal; directly strengthens and expands the optical-adjacency/copper-displacement hedge leg of the thesis with vertically-integrated SiPho PIC capability feeding CPO/NPO design wins |
| 2026-09-01 | 8-K filed (items 2.02/9.01); shares -11.8% as margin guidance dulls a reported revenue outperformance | ↓ | First negative data point on the thesis's ~68% GM leg since the Q4 FY2026 beat — but conflicts with the standing "earnings due 09-09" note, so period and magnitude are unconfirmed pending /dig |
| 2026-08-31 (evening) | Credo joins a consortium developing optical connections closer to AI chips | ↑ | Second optical-adjacency data point in the same week — corroborates the Hyperlume hedge as an active collaboration strategy, not an idle acquisition |
| 2026-08-31 | Toucan PCIe retimer achieves PCIe compliance, joins PCIe 6.x Integrators List; TSMC confirms CPO mass production H2 2026 | ↑ | Guided-to next catalyst (PCIe retimer) materializes as a concrete qualification milestone; TSMC's public CPO timeline independently corroborates the Hyperlume optical hedge |
| 2026-06-07 | Acquired Hyperlume for $92M — microLED-based optical interconnect technology | ↑ | Deploys ATM capital into optical adjacency, directly hedging the copper AEC displacement risk; expands Credo's TAM into optical interconnect and signals management is positioning for post-copper AI rack generations at 3.2T+. |
| 2026-06-01 | Q4 FY2026: $437M +157% YoY, EPS $1.16, guidance $470M midpoint | ↑ | Consecutive beat with accelerating sequential growth and above-consensus guidance confirms hyperscaler AEC demand is durable, not pull-forward. FY2026 full-year $1.34B at ~68% GM materially ahead of prior expectations. |
| 2026-06-01 | CEO William Brennan granted performance-based PSU award with stretch milestones | ↑ | PSU structure ties compensation to long-duration revenue/margin targets rather than time-vesting, strengthening CEO-shareholder alignment and reducing near-term equity overhang risk. |
| 2026-04-13 (backfilled 2026-09-02) | Announces definitive agreement to acquire DustPhotonics (SiPho PIC developer) for $750M cash + ~0.92M shares upfront, up to 3.21M contingent shares — same day as the ATM raise below, which funded it. Deep pass reads the 04-13 ATM row below as resolved by this: the raise was not "net neutral" absent a deployment — this was the deployment. | ↑ | Never logged at the time; discovered via deep-pass balance-sheet reconciliation. Explains what the 04-13 ATM raise was for and is the real driver of Q1 FY2027's GAAP margin dynamics five months later. |
| 2026-04-13 | Completed $750M ATM equity offering, raised $736.3M net via 4.8M shares | → | Raises strategic optionality (M&A, R&D, working capital) but adds ~2.8% dilution at elevated valuation; net neutral absent a specific high-return deployment announcement. |

---

## Cross-Ticker Signals

| Date | Direction | Other Ticker | Signal | Implication |
|------|-----------|-------------|--------|-------------|
| 2026-05-19 | Receives | NVDA | NVDA Q1 FY2027 earnings; CRDO named copper interconnect supplier in earnings shockwave infographic | NVDA Blackwell rack density drives intra-rack copper AEC demand — strong NVDA guidance is a direct pull signal for CRDO AEC/SerDes order book |
| 2026-06-01 | Emits | MRVL | CRDO Q4 FY2026: SerDes/AEC share gains at hyperscalers accelerating | Credo's record revenue at shared hyperscaler customers signals competitive pressure on Marvell's connectivity semiconductor portfolio at the same accounts |
| 2026-06-01 | Emits | AVGO | CRDO Q4 FY2026: copper AEC displacing optical at short-reach intra-rack | Credo's record AEC volumes suggest copper-based solutions continue taking share from short-reach optical, a headwind for Broadcom's optical interconnect revenue |
| 2026-04-13 (backfilled 2026-09-02) | Emits | POET, LITE, COHR, AAOI | Credo brings SiPho PIC development in-house via DustPhotonics ($750M cash + stock), a component previously externally sourced | A vertically-integrated hyperscaler-facing SerDes/AEC leader building its own silicon photonics capability is a long-term competitive/customer-concentration risk for standalone optical-component suppliers in the same hyperscaler AI cluster build-out |

---

## Catalyst Timeline
- [x] Q1 FY2027 earnings — reported 2026-09-01 (period ended 2026-08-01): $479.0M rev (+114.7% YoY, beat), 68.0% non-GAAP GM (in line); GAAP GM 64.5% on DustPhotonics amortization
- [ ] Q2 FY2027 earnings — est. ~2026-12-02 (pattern-based; no confirmed date given). Guided: $525-535M rev, 67-69% non-GAAP GM
- [ ] DustPhotonics SiPho PIC integration: first product announcement or design win under the Credo brand
- [ ] Hyperlume microLED integration: first product announcement or design win
- [ ] 1.6T AEC product launch and first hyperscaler volume orders (H2 2026)
- [ ] PCIe retimer revenue ramp — watch for % of total revenue in quarterly reports
- [ ] New hyperscaler design wins (beyond existing anchor customer)
- [ ] NVDA Blackwell/Rubin rack adoption of copper AEC vs. optical (competitive watch)
- [ ] Quarterly non-GAAP gross margin trend — sustaining ~67–68% confirms pricing power (GAAP GM now structurally ~4pt lower from DustPhotonics amortization; track non-GAAP, not GAAP, for the pricing-power signal)

---

## Analyst Coverage
- Goldman Sachs bullish on CRDO — cited AI connectivity tailwinds and AEC market leadership (2026).
- **2026-06** — Rothschild & Co initiates CRDO Buy, PT undisclosed (AI connectivity leadership and AEC market position; post-Q4 FY2026 initiation)
- **2026-06-02** — Roth Capital raises CRDO to Buy, PT $300 (post-Q4 beat; FY2026 revenue tripling exceeds prior estimates)
- **2026-06-02** — Mizuho raises CRDO to Buy, PT $290 (sustained hyperscaler AEC demand; Q1 FY2027 guidance above consensus)
- **2026-06-01** — Jefferies raises CRDO to Buy, PT $270 (record Q4 revenue and margin expansion support re-rating)
- **2026-06-02** — JPMorgan raises CRDO to Buy, PT $250 (strong earnings beat; positive Q1 FY2027 guidance)

---

## Ecosystem Links
See [[NVDA Ecosystem Map]] — Earnings Shockwave Map (2026-05-19): Communication — Copper Interconnect.
