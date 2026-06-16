# AI Model Infrastructure — Supply Chain Map
*Mapped: 2026-05-31 | Anchor: Foundation model training, optimization, and serving*
*Dimension: D4 — AI Enablement*

---

## Framework Status
- [x] Supply chain mapped
- [x] Process/product depth added (2026-05-31)
- [x] Interrelationship Anchors documented (2026-05-31)
- [ ] Nodes registered (`/add-ticker TICKER --layer "Layer"` for each below)
- [ ] Ground truth pulled (`/stock-research TICKER` per node)
- [ ] Customer matrix built (`/build-customer-matrix "AI Model Infrastructure"`)
- [ ] Sector Framework written (only after above steps complete)

---

## Value Chain

| Tier | Function | Processes | Key Products / Materials | Chokepoint | Capital Intensity | Moat Type | Margin Profile |
|------|----------|-----------|--------------------------|------------|-------------------|-----------|----------------|
| Training Data & Curation | Acquire, clean, deduplicate, and prepare large-scale datasets for model pre-training, RLHF, and fine-tuning | Web crawl ingestion (Common Crawl pipeline), exact/near-dedup (MinHash LSH), quality filtering (perplexity scoring, classifier-based filtering), PII scrubbing (NER + regex redaction), multimodal alignment (image-caption pairing, ASR transcription), instruction dataset construction (preference annotation, red-teaming), synthetic data generation (teacher-student distillation) | Pre-training corpora (RedPajama, The Pile, ROOTS), RLHF preference datasets, instruction-tuning sets (FLAN, ShareGPT, OpenHermes), multimodal image-text pairs, synthetic reasoning traces | Partial | Low–Medium | Ecosystem (data flywheel) | Low (services) / High (proprietary data assets) |
| Distributed Training Orchestration | Orchestrate GPU/TPU clusters at scale for model pre-training and reinforcement learning using parallelism strategies that saturate interconnect bandwidth | Distributed data-parallel (DDP/FSDP), tensor parallelism (Megatron-LM TP), pipeline parallelism (GPipe/1F1B), 3D hybrid parallelism (DP+TP+PP), ZeRO optimizer state sharding (DeepSpeed ZeRO-1/2/3), gradient checkpointing, BF16/FP8 mixed-precision training, fault-tolerant checkpoint (FSDP/Gemini), custom CUDA kernel development (FlashAttention-2/3, SDPA) | PyTorch FSDP checkpoints (BF16 weight shards), DeepSpeed engine configs, NVLink/InfiniBand RDMA topology maps, NCCL collectives library, Megatron-LM training scripts, GPU memory profiling traces | Partial | High | Process IP + Ecosystem | High (cloud training revenue) |
| Foundation Model Development | Design neural architectures, execute pre-training runs, and establish base model capabilities across language, vision, and multimodal tasks | Transformer architecture design (attention variants: MHA/GQA/MLA), MoE router training (top-K, expert capacity), tokenizer training (BPE/unigram via SentencePiece), pre-training curriculum (data mixing ratios, learning rate cosine/WSD schedule), evaluation harness benchmarking (MMLU, HumanEval, BIG-bench, HELM, GPQA), model card authorship, safety pre-processing (SFT warm-start before RLHF) | Foundation model weight checkpoints (GPT-4, Claude 3.x, Llama 3.x, Gemini 1.5/2.x, Mistral, Qwen), tokenizer vocabularies (32K–128K vocab), evaluation benchmark result sets, model cards, BF16/FP32 master weight files | Y | Very High | Process IP + Ecosystem + Switching cost | Very High (API revenue per token once amortized) |
| Alignment & Safety Tuning | Adapt foundation models to be helpful, harmless, and honest via supervised fine-tuning, preference learning, and safety evaluation | Supervised fine-tuning (SFT) on instruction datasets, reward model training (Bradley-Terry preference model), RLHF (PPO with KL penalty), DPO (direct preference optimization, no RM needed), Constitutional AI (rule-based reward, RLAIF), PEFT (LoRA rank-4/8/16, QLoRA, prefix tuning, adapters), domain fine-tuning (code/medical/legal SFT), automated red-teaming (LLM-as-judge, jailbreak probing) | SFT weight checkpoints, LoRA adapter weight files (rank-4/8/16 delta tensors), reward model checkpoints, RLHF preference datasets, safety evaluation benchmark results (StrongREJECT, HarmBench), Constitutional AI principle sets | N | Low–Medium | Process IP | Medium (fine-tuning services) / High (embedded in API margin) |
| Model Optimization & Compilation | Reduce model size, latency, and compute cost for production inference without unacceptable quality loss | Post-training quantization (PTQ: INT8, INT4, FP8, AWQ, GPTQ, SmoothQuant), quantization-aware training (QAT with simulated quantization), knowledge distillation (teacher-student SFT, speculative decoding with draft model), structured pruning (attention head pruning, layer dropping via importance scoring), unstructured magnitude/movement pruning, hardware-specific operator fusion (CUDA kernel fusion, Flash Decoding), model compilation (torch.compile, XLA, Apache TVM, MLIR) | Quantized GGUF model files (Q4_K_M, Q8_0), AWQ INT4 checkpoints, GPTQ INT8 checkpoints, TensorRT engine files (.trt), ONNX model files, distilled student models (Phi-3-mini, Gemma-2B, DistilBERT), compiled XLA HLO graphs | N | Low | Process IP (proprietary inference kernels) + Switching cost | Medium–High (embedded in inference efficiency) |
| Inference Serving & Scaling | Serve model inference at scale with low P50/P95 latency, high throughput (tokens/second), and cost-efficient GPU utilization | Continuous batching (dynamic batching window, in-flight batching), PagedAttention KV cache management (vLLM), tensor parallelism across multi-GPU inference nodes, speculative decoding (Medusa / draft-then-verify), KV cache prefix caching (prompt caching, context reuse), KV cache offload to CPU/NVMe, request router + load balancer, GPU auto-scaling (spot pool + SLO-aware bin packing), streaming token delivery (SSE chunked transfer), SLO enforcement (P50/P95 latency budgets) | vLLM / TGI / SGLang / TensorRT-LLM serving instances, KV cache DRAM and NVMe tiers, NVIDIA Triton Inference Server configs, Kubernetes HPAs for GPU nodes, streaming inference API endpoint (REST/SSE/WebSocket), per-model GPU memory allocation profiles | Y | High | Ecosystem + Process IP + Switching cost | High (per-token margin scales with cluster utilization) |
| MLOps & Model Lifecycle Management | Manage the end-to-end model lifecycle: experiment tracking, versioning, CI/CD pipelines, feature management, drift monitoring, and automated retraining | Experiment tracking (metric/artifact logging, hyperparameter sweep: Optuna/Ray Tune), model registry (version tagging, stage transitions: staging → production → archived), automated model CI/CD (data validation → model validation → shadow deployment → canary → full rollout), online/offline feature store management (point-in-time correct joins), A/B test and multi-armed bandit deployment, data drift detection (PSI, KS-test, MMD), concept drift and model performance decay alerting, automated retraining triggers, data/model lineage DAG tracking | MLflow/W&B run artifacts, model registry manifests (BentoML, Seldon, KServe), feature store schemas (Feast, Tecton), evaluation dashboards, deployment Helm charts, Prometheus/Grafana performance dashboards, lineage graphs | N | Low–Medium | Switching cost + Ecosystem | Medium (SaaS per-seat / per-compute) |
| Model API & Developer Platform | Expose model capabilities via standardized APIs, SDKs, and developer tooling consumed by application builders and enterprise integrators | API gateway management (rate limiting, auth token validation, per-request token counting, tiered usage billing), SDK generation (Python/JS/Go/Rust client libraries), prompt versioning and management systems, function-calling / tool-use schema validation (JSON schema, OpenAPI spec), RAG pipeline orchestration (chunking strategies, embedding API routing, ANN retrieval: HNSW/IVF), streaming token delivery via SSE/WebSocket, batch inference job queue, fine-tuning API endpoint (LoRA-based), model router / gateway aggregation (multi-model fallback, latency-based routing) | OpenAI-compatible REST API spec, Anthropic Messages API, Google Gemini API, AWS Bedrock API, Python/JS SDK packages, prompt template libraries, LiteLLM / OpenRouter gateway configs, embedding API endpoints (text-embedding-3, Cohere Embed), fine-tuning job metadata, batch inference result files (JSONL) | Partial | Low | Ecosystem + Switching cost | Very High (software margin on token API revenue) |

---

## Publicly-Traded Nodes

| Tier | Ticker | Company | Mkt Cap | In Registry | Notes |
|------|--------|---------|---------|-------------|-------|
| Training Data & Curation | — | *No dedicated public pure-play* | — | — | ⚠️ Structural gap — Scale AI, Surge AI, Labelbox are private; Appen (APX.AX) is Australia-listed micro-cap |
| Distributed Training Orchestration | NVDA | NVIDIA Corporation | Large | Yes (Semiconductors) | Dominant via H/B-series GPUs + NVLink + NCCL + Megatron-LM; vertically integrated across training + inference |
| Distributed Training Orchestration | AMD | Advanced Micro Devices | Large | No | MI300X for training; ROCm ecosystem; gaining hyperscaler traction (Meta, Microsoft) |
| Distributed Training Orchestration | CRWV | CoreWeave | Large | No | Pure-play GPU cloud; IPO 2025; NVIDIA preferred partner; Inflection + Cohere training customer |
| Distributed Training Orchestration | MSFT | Microsoft | Large | No (candidate in AI Infrastructure) | Azure AI training (ND H100 v5); OpenAI exclusive cloud partner; custom Maia 100 ASIC |
| Distributed Training Orchestration | GOOGL | Alphabet | Large | No (candidate in AI Infrastructure) | TPU v5p training pods; GCP; Gemini training; custom silicon moat |
| Distributed Training Orchestration | AMZN | Amazon | Large | No (candidate in AI Infrastructure) | AWS Trainium 2; UltraCluster; SageMaker Training |
| Foundation Model Development | MSFT | Microsoft | Large | No (candidate in AI Infrastructure) | Economic partner in OpenAI; GPT-4/o1 API distribution via Azure; owns Copilot IP stack |
| Foundation Model Development | GOOGL | Alphabet | Large | No (candidate in AI Infrastructure) | Gemini 1.5 / 2.x family + Veo + Imagen; DeepMind integration; TPU-native training moat |
| Foundation Model Development | META | Meta Platforms | Large | No | Llama 3.x / 4 open-weight models; PyTorch custodian; FAIR research; no direct API revenue model |
| Foundation Model Development | AMZN | Amazon | Large | No (candidate in AI Infrastructure) | Amazon Nova, Titan; Bedrock distribution of Anthropic + third-party models |
| Alignment & Safety Tuning | — | *No dedicated public pure-play* | — | — | ⚠️ Structural gap — Anthropic (private), Scale AI (private), Cohere (private) dominate alignment R&D |
| Model Optimization & Compilation | NVDA | NVIDIA Corporation | Large | Yes (Semiconductors) | TensorRT, TensorRT-LLM, NIM microservices; CUDA kernel library is the de facto inference optimization standard |
| Model Optimization & Compilation | AMD | Advanced Micro Devices | Large | No | ROCm + vLLM MI300X path; competing on inference kernel quality for LLM serving |
| Inference Serving & Scaling | NVDA | NVIDIA Corporation | Large | Yes (Semiconductors) | TensorRT-LLM + Triton + NIM + H100/H200/B200 hardware; vertically integrated inference stack |
| Inference Serving & Scaling | CRWV | CoreWeave | Large | No | Managed inference clusters; OpenAI inference partner; Kubernetes-native GPU autoscaling |
| Inference Serving & Scaling | MSFT | Microsoft | Large | No (candidate in AI Infrastructure) | Azure OpenAI Service inference; Azure AI Foundry; PTU (provisioned throughput units) model |
| Inference Serving & Scaling | GOOGL | Alphabet | Large | No (candidate in AI Infrastructure) | Vertex AI inference; TPU v5p inference pods; Gemini API serving |
| Inference Serving & Scaling | AMZN | Amazon | Large | No (candidate in AI Infrastructure) | Bedrock inference; SageMaker Inference; Inferentia 2 chips |
| Inference Serving & Scaling | ORCL | Oracle | Large | No (candidate in AI Infrastructure) | OCI GPU clusters; OCI Generative AI inference; NVIDIA preferred cloud partner |
| MLOps & Model Lifecycle Management | DDOG | Datadog | Large | No | LLM Observability product; APM; model performance monitoring; AI cost attribution |
| MLOps & Model Lifecycle Management | SNOW | Snowflake | Large | No | Cortex AI (managed LLM inference + RAG); feature store (Cortex Feature Store); ML observability built into data platform |
| MLOps & Model Lifecycle Management | PLTR | Palantir Technologies | Large | No | AIP (AI Platform); Foundry + Ontology for enterprise model deployment; US govt + commercial |
| MLOps & Model Lifecycle Management | MDB | MongoDB | Mid | No | Atlas Vector Search (HNSW / ENN); document store for RAG pipeline metadata; embeddings + chunking native |
| MLOps & Model Lifecycle Management | ESTC | Elastic | Mid | No | ELSER (learned sparse retrieval model); vector search (k-NN / ANN); LLM observability in Kibana |
| Model API & Developer Platform | MSFT | Microsoft | Large | No (candidate in AI Infrastructure) | Azure OpenAI Service (GPT-4o, o1, DALL-E); Azure AI Foundry; Copilot Studio platform |
| Model API & Developer Platform | GOOGL | Alphabet | Large | No (candidate in AI Infrastructure) | Gemini API / AI Studio / Vertex AI APIs; Agent Builder; Grounding APIs |
| Model API & Developer Platform | AMZN | Amazon | Large | No (candidate in AI Infrastructure) | Amazon Bedrock (multi-model API gateway + RAG + agents); SageMaker endpoints |
| Model API & Developer Platform | SNOW | Snowflake | Large | No | Cortex AI: text_complete() + embed_text() SQL functions expose LLM + embedding APIs inside data warehouse |
| Model API & Developer Platform | CFLT | Confluent | Mid | No | Kafka-based real-time data streaming for ML feature pipelines and model event sourcing |

---

## Structural Gaps

**Training Data & Curation (No public pure-play):** The highest-quality human annotation and data curation companies are uniformly private. Scale AI ($13B+ valuation), Surge AI, Labelbox, and Appen (ASX-listed micro-cap) control proprietary annotation pipelines. The moat is operational: recruiting and managing vetted annotator pools at scale is not easily replicated. The closest public exposure is META (largest proprietary web-scale data corpus via Facebook/Instagram user data) and GOOGL (YouTube, Search, Maps corpora). Watch for an Scale AI IPO or secondary listing as a potential pure-play entry.

**Alignment & Safety Tuning (No public pure-play):** Anthropic, Cohere, and Mistral — the organizations most focused on alignment research as a core competency — are private. Frontier alignment work (constitutional AI, scalable oversight, interpretability) is concentrated in a handful of labs with combined headcount under 2,000. The public market exposure is indirect: MSFT via OpenAI RLHF, and GOOGL via DeepMind alignment. No near-term IPO catalyst is visible.

**Inference Kernel & Compiler Stack (Partial gap):** Open-source tools (vLLM, llama.cpp, SGLang, HuggingFace TGI) have democratized inference serving, but NVIDIA's closed TensorRT-LLM remains the highest-performance path on H100/B200. No independent pure-play inference software company has achieved public scale — Groq (private, LPU architecture) and SambaNova (private) are the closest analogs. The structural gap is that software inference value is being captured by the hardware vendor (NVDA).

---

## Key Questions to Answer Before Writing the Sector Framework

1. **Inference economics at scale:** As model quantization (FP8, INT4) and speculative decoding drive inference efficiency gains of 3–5x, does the per-token price floor compress inference revenue for hyperscalers, or does demand elasticity absorb efficiency gains through volume growth?
2. **Open-weight commoditization risk:** Llama 3.x and Mistral have demonstrated near-frontier quality at zero marginal cost. At what capability threshold does open-weight model quality make closed-API pricing structurally unsustainable for mid-tier foundation model providers?
3. **Inference silicon diversification:** NVIDIA controls ~85% of deployed inference compute. AMD ROCm and custom ASICs (Google TPU, Amazon Inferentia, Meta MTIA) are the only credible alternatives. How fast does the non-NVDA share grow, and which companies capture the incremental allocation?
4. **MLOps consolidation:** The MLOps toolchain is fragmented across ~30 point solutions (tracking, registry, feature store, monitoring, serving). Hyperscalers are bundling (SageMaker, Vertex AI, Azure ML). Does the independent MLOps market sustain multiple public companies (DDOG, SNOW, PLTR) or consolidate into hyperscaler bundles?
5. **RAG vs. long-context trade-off:** As context windows expand to 1M+ tokens (Gemini 1.5, Claude 3.5), does retrieval-augmented generation (RAG) — the primary use case for vector databases (MDB, ESTC) — diminish in importance, or does document volume growth keep RAG essential?
6. **Sovereign AI / on-prem inference demand:** Governments and regulated industries (finance, healthcare, defense) are mandating on-premises or sovereign cloud model deployment. This creates demand for locally-deployable inference stacks (Ollama, vLLM self-hosted) and on-prem GPU infrastructure — a potentially structurally different market from the hyperscaler API model.

---

## Interrelationship Anchors

### Inputs (this sector consumes from)
| From Sector | From Tier | Product / Signal |
|---|---|---|
| Compute Infrastructure | Server Assembly + Hyperscaler Operation | GPU compute hours (H100/B200 DGX clusters) → model pre-training and fine-tuning runs |
| Compute Infrastructure | Networking | 400G / 800G InfiniBand + Ethernet spine → RDMA collective communication during distributed training |
| Compute Infrastructure | Storage Systems | NVMe SSD arrays + object storage (S3 / GCS) → training dataset streaming and checkpoint storage |
| Energy & Power | Primary Generation + Power Conversion | Megawatt-scale power feeds → training cluster power draw (100–300 MW per large training run) |
| Semiconductors | Design (Compute) | GPU / TPU / custom ASIC die → packaged training and inference accelerator |
| Semiconductors | Design (Memory) | HBM3e / HBM4 → on-package GPU memory for large-batch training and KV cache |
| Cybersecurity | Identity & Access Management | API key auth, IAM policies, secrets management → model endpoint and training job security |
| Electronic Components | PCB Assembly + Networking | High-layer PCBs, QSFP-DD connectors → GPU server backplane and NIC assembly |

### Outputs (this sector supplies to)
| To Sector | To Tier | Product / Signal |
|---|---|---|
| Robotics & Edge AI | AI Model Training + Edge Inference | Foundation model weights (Llama, Gemini Nano) + inference APIs → robot perception, planning, and language understanding |
| Fintech & Commerce AI | AI Model Serving + Fraud & Risk | LLM inference API (GPT-4o, Claude 3.5 Sonnet) → real-time credit scoring, fraud detection, commerce personalization |
| Cybersecurity | Security Operations + Threat Intelligence | LLM-powered code analysis, anomaly pattern reasoning, alert triage → AI-augmented SOC operations |
| Compute Infrastructure | Demand Signal | Model training and inference workload growth → GPU capex demand pull for hyperscaler infrastructure build |
| Space & Communications | Ground Segment + Payload Integration | AI model inference APIs → satellite telemetry anomaly detection, autonomous ground station operations |

---

## Research Log
- **2026-05-31** — map-sector run. 8 tiers, 2 chokepoints (Foundation Model Development, Inference Serving & Scaling), 2 structural gaps (Training Data annotation, Alignment & Safety). New candidates not yet in registry: AMD, CRWV, MSFT (cross-listed), GOOGL (cross-listed), META, AMZN (cross-listed), ORCL (cross-listed), DDOG, SNOW, PLTR, MDB, ESTC, CFLT.
