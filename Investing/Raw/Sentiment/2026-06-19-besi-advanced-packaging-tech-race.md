---
date: 2026-06-19
source: tweet
tickers: [BESI, AMKR]
sectors: [Advanced Packaging]
author: ""
url: "https://x.com/i/status/2067964372530434146"
tags: [tech-race, advanced-packaging, hbm, chiplets, moore's-law, yield, bandwidth-wall]
relationships:
  # No direct directed edges — this is a sector-level educational thread
---

Advanced packaging is so so so important.

From first principles:

The whole semiconductor industry runs on one engine: Moore's Law.

Every couple of years, you could shrink transistors, pack 2x as many onto a chip...and get more compute for the same cost.

But the cost of moving a bit of data from one place to another doesn't improve at the same rate as the computation gains.

Mainly because moving electrons vast distances costs time/energy. And going off-chip and into another package is super expensive.

And ofc you can't just build one giant chips because yields fall exponentially w/ area. Even if you 2x chip size, you can lose most of the yield.

This is where you stop thinking about the chip itself, but more about the package.

Advanced packaging.

Very simply: 

If you can't make one big chip, make loads of smaller ones + connect them so tightly that they act like one big chip.

You get the benefits of a giant chip without paying the yield penalty.

By decreasing power consumption + increasing speed.

And today, bandwidth is probably the defining problem for AI accelerators especially.

Advanced packaging provides that bandwidth by putting HBM next to the logic + wiring it together with a higher volume of shorter/denser connections. 

You literally can't route enough wires across a circuit board to feed a modern GPU cos the bandwidth those chips need only exists if the memory is packaged right up against the compute.

There's ofc more depth to this like specific advanced packaging components or technologies. 

Including HBM's role in the whole thing and stuff like glass substrates too.

But that's a short story if anyone wanted to learn a bit more rather than getting a bunch of random ticker symbols.

But fwiw, my favourite pure-play advanced packaging equipment name is $BESI that I hold. 

If anyone was curious and wanted to do more research.

---

## Fact-Check

**Claim 1 — Moore's Law: 2× transistors every ~2 years**
✅ **Accurate.** Gordon Moore's 1965 observation; still roughly holds at leading nodes (TSMC N3/N2). The tweet correctly distinguishes transistor density gains from cost/performance improvements (Dennard Scaling, which broke down ~2005–2007) — using them interchangeably is a simplification, but not misleading for the argument being made.

**Claim 2 — Moving data off-chip costs more energy/time than compute gains**
✅ **Accurate.** Well-documented "memory wall" / "bandwidth wall." Energy per bit: on-chip SRAM ~1–5 pJ/bit; off-package DRAM ~20–50 pJ/bit; over PCB ~100+ pJ/bit. Bandwidth growth has lagged compute FLOP/s growth by a large margin since ~2000.

**Claim 3 — Yield falls exponentially with die area**
✅ **Accurate (reasonable simplification).** Poisson yield model: Y = e^(−D₀·A) where D₀ = defect density (~0.01–0.1/cm²) and A = area. Murphy's more accurate model adds clustering terms but the directional result is the same: doubling die area dramatically cuts yield. The tweet's "exponential" framing is defensible.

**Claim 4 — Advanced packaging = small chips + tight connections ≈ one big chip**
✅ **Accurate.** This is the chiplet architecture thesis implemented by TSMC CoWoS (CoW on Substrate), InFO, SoIC, Intel Foveros, AMD EMIB. NVIDIA H100/B100/B200 are textbook examples: GPU die + HBM stacks on a silicon interposer.

**Claim 5 — HBM placed adjacent to logic with denser/shorter connections**
✅ **Accurate.** In 2.5D CoWoS packages, HBM3e stacks sit on a silicon interposer ~mm away from the GPU die. TSV density enables ~3.2 TB/s bandwidth at lower power per bit than any PCB-based memory solution.

**Claim 6 — Can't route enough PCB wires to feed a modern GPU**
✅ **Accurate.** H100/B200 need >3 TB/s. DDR5 per-channel bandwidth is ~51 GB/s; you would need 60+ channels just to match — physically impossible and thermally untenable. PCB trace density cannot approach TSV density by orders of magnitude.

**Claim 7 — BESI = "pure-play advanced packaging equipment"**
✅ **Broadly accurate.** BE Semiconductor Industries N.V. (BESI.AS, Euronext Amsterdam) manufactures die attach equipment, flip chip bonders, and hybrid bonding systems. Unlike AMAT/KLAC/LRCX (deposition, etch, metrology), BESI's revenue is concentrated in back-end packaging equipment. "Pure-play" framing is legitimate. Note: foreign-listed (Netherlands); not US exchange.

**Overall verdict: All claims technically sound. Tweet is a high-quality, accurate first-principles explainer on advanced packaging. BESI pick is defensible and adds a non-US pure-play angle on the equipment side of L08.**
