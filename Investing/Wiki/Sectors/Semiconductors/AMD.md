# AMD
*Social mentions only — not yet in Monitor Registry. Run `/add-ticker AMD` to onboard fully.*

---

## One-Line Thesis
AMD is taking durable server CPU share from Intel via EPYC while rapidly scaling MI-series AI GPUs as a cost-competitive alternative to NVIDIA in hyperscaler data centers.

---

## Investment Thesis
AMD has executed one of the most consequential turnarounds in semiconductor history, moving from near-bankruptcy in 2014 to a serious dual-threat challenger in both data center CPUs and AI accelerators. The EPYC server CPU franchise reached a record 46.2% server CPU revenue share in Q1 2026 (up from ~27% unit share, reflecting strong ASPs), driven by superior performance-per-watt on TSMC N4/N3 processes versus Intel's ongoing foundry recovery struggles. Data Center segment revenue hit $5.8 billion in Q1 2026, up 57% year-over-year. The CPU moat is durable: AMD's process technology lead translates into genuine TCO advantages for cloud and enterprise customers, and Intel's recovery timeline remains uncertain.

On the AI GPU side, the MI300X delivered a step-change in inference economics with 192 GB HBM3 (2.4x H100) and 5.3 TB/s bandwidth, enabling Microsoft Azure and Meta (running 100% of live Llama 405B traffic) to deploy at scale. The MI350/MI355X line posted MLPerf Inference 6.0 results within single-digit percentage points of the B200. The upcoming Helios rack-scale platform unifies EPYC "Venice" CPUs, MI400-series GPUs, and Pensando "Vulcano" AI NICs under ROCm software into a fully integrated solution, and a 6-gigawatt agreement with Meta for MI450-based deployments beginning H2 2026 represents the largest AI infrastructure commitment in AMD's history. AMD has committed a strategic $10B+ investment in U.S.-based manufacturing and R&D through the CHIPS Act framework, and is making a $150M strategic investment in Nutanix to deepen enterprise AI software integration.

The core risk is software ecosystem. NVIDIA's CUDA moat is wide and self-reinforcing — TensorRT-LLM, FlashAttention 3, and the broader CUDA developer toolchain give NVIDIA a sticky advantage in training workloads and with teams that cannot afford re-optimization cost. AMD's ROCm achieves near-parity on PyTorch/vLLM inference stacks but lags on specialized training frameworks. AMD must ship competitive new GPU architectures every 12–18 months to maintain relevance; any execution slip hands NVIDIA pricing power. Hyperscaler custom ASICs (Google TPU, AWS Trainium, Microsoft Maia) represent secular share-loss risk for both AMD and NVIDIA, and rising HBM memory costs compress AI GPU margins.

**Key moat:** EPYC's process-node advantage over Intel yields durable server CPU share at premium ASPs; MI-series HBM capacity leads at the memory-bandwidth-bound inference tier.
**Key risks:** ROCm software ecosystem lag vs. CUDA; hyperscaler ASIC in-sourcing; HBM cost inflation; geopolitical supply-chain exposure; execution risk on annual GPU cadence.

---

## Management & Leadership

| Role | Name | Notes |
|------|------|-------|
| CEO | Lisa Su | Engineer-operator; joined 2012, CEO since 2014; engineered AMD's full turnaround. |
| CFO | Jean Hu | Joined 2022; prior CFO at Marvell; deep semiconductor finance background. |

**Execution track record:** Lisa Su took AMD from near-insolvency to a $200B+ company through disciplined product roadmap execution (Zen CPU architecture, CDNA GPU line) and shrewd manufacturing partnerships with TSMC; the team has delivered consistent beats on data center guidance over the past three years.
**Insider ownership / alignment:** Lisa Su beneficially owns ~3.77M shares (~0.23% of ~1.62B shares outstanding per 2026 DEF 14A filed March 27, 2026); executives are net sellers under pre-planned 10b5-1 programs, consistent with large equity compensation packages — no open-market buys on record in the past year.

---

## Social Mentions

| Date | Signal | Source |
|------|--------|--------|
| 2026-05-17 | [[2026-05-17-sive-when-i-see]] | tweet |
| 2026-05-18 | [[2026-05-18-amd-cpu-bottleneck-three-ways]] | tweet |
| 2026-05-22 | [[2026-05-22-amd-a-ton-of]] | article |

---

## Research Log

- **2026-05-22** — stock-research run. Fundamental sections populated from web research and SEC DEF 14A.
