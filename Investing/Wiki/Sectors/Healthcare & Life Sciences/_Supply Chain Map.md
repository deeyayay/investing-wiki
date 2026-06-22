# Healthcare & Life Sciences — Supply Chain Map
*Mapped: 2026-06-22 | Anchor: Drug Discovery & Clinical AI*
*Vertical sector — L01-adjacent with unique biological discovery supply chain*

---

## Framework Status
- [x] Supply chain mapped
- [x] Process/product depth added (2026-06-22)
- [x] Interrelationship Anchors documented (2026-06-22)
- [ ] Nodes registered (`/add-ticker TICKER --sector "Healthcare & Life Sciences"` for each below)
- [ ] Ground truth pulled (`/stock-research TICKER` per node)
- [ ] Customer matrix built (`/build-customer-matrix "Healthcare & Life Sciences"`)
- [ ] Sector Framework written (only after above steps complete)

---

## Value Chain

| Tier | Function | Processes | Key Products / Materials | Chokepoint | Capital Intensity | Moat Type | Margin Profile |
|------|----------|-----------|--------------------------|------------|-------------------|-----------|----------------|
| **Genomics & Biological Measurement** | Generate raw biological data through sequencing, imaging, and molecular analysis instruments | Short-read NGS (sequencing-by-synthesis, SBS flow cell); long-read sequencing (PacBio SMRT HiFi / ONT nanopore strand sensing); single-cell RNA-seq (microfluidic GEM droplet encapsulation, cDNA library prep); spatial transcriptomics (in-situ hybridization + NGS readout); high-content imaging (automated fluorescence Z-stack); LC-MS/MS proteomics (trypsin digestion, reverse-phase nanoflow separation, tandem MS detection) | Illumina NovaSeq X+ (short-read sequencer); PacBio Revio (HiFi long-read); 10x Genomics Chromium scRNA-seq kit; Bruker timsTOF Pro2 mass spectrometer; FASTQ / BAM output data files | Y | High | Scale + switching cost (reagent & workflow lock-in) | High (instruments) + recurring reagents (razor-blade model) |
| **Biological Data Aggregation & Curation** | Collect, link, and structure genomic, proteomic, and clinical data at scale for AI model training | FASTQ alignment + variant calling (BWA-MEM / GATK HaplotypeCaller); EHR extraction + de-identification (Safe Harbor / Expert Determination); phenotype–genotype linkage (PheWAS, GWAS pipeline); multi-omic integration (MOFA+, late-integration fusion); DICOM image ingestion + structured annotation; drug response dataset curation (PRISM, CCLE) | Annotated genomic VCF cohorts; de-identified EHR datasets (ICD-10 + CPT-coded); DICOM-linked pathology/radiology image libraries; longitudinal multi-omic patient profiles; drug response matrices | Partial | Medium | Data network effect + proprietary dataset breadth | High (SaaS-like once assembled) |
| **AI Drug Discovery & Molecular Design** | Apply physics-based simulation and deep learning to identify therapeutic targets, design molecules, and predict ADMET properties | FEP+ free energy perturbation MD simulation; AlphaFold 3 / RoseTTAFold structure prediction; generative molecular design (diffusion models, graph neural nets); genome-wide CRISPR loss-of-function screens (pooled Cas9); high-content phenotypic screening (384-well automated imaging); ML ADMET property prediction (DMPK models) | Drug candidate structures (SMILES / SDF files); binding affinity predictions (ΔG, IC₅₀ values); protein-ligand co-crystal structures (PDB); CRISPR guide RNA designs; ML-predicted ADMET profiles | Partial | Medium | Process IP + data flywheel (training set scale) | High (software) / Medium (integrated wet lab) |
| **AI Diagnostics & Precision Medicine** | Apply AI to biomarker and clinical data for early disease detection, patient stratification, and companion diagnostics | ctDNA sequencing (hybrid capture, Guardant LUNAR-2); extracellular RNA liquid biopsy (small RNA-seq, exoRNA profiling); whole slide image AI analysis (patch-based CNN / ViT); methylation-based multi-cancer early detection profiling (bisulfite sequencing); CDx analytical + clinical biomarker validation (per FDA IVD / LDT pathway) | Guardant360 CDx ctDNA panel; multi-cancer early detection (MCED) liquid biopsy test; Oncotype DX genomic recurrence score; Signatera ctDNA MRD assay; FDA-approved companion diagnostic (CDx) label | Partial | Medium | Regulatory certification + proprietary algorithms + lab network | High (clinical laboratory) |
| **Therapeutics (AI-Designed)** | Develop AI-optimized therapeutic products using mRNA, gene editing, and cell engineering platforms | mRNA sequence optimization (codon usage, 5′/3′ UTR design, N1-methyl-pseudouridine modification); LNP microfluidic formulation + encapsulation (ionizable lipid / DSPC / cholesterol / PEG-lipid mixing); CRISPR RNP LNP delivery or electroporation; AAV triple transfection + downstream chromatographic purification; CAR-T lentiviral transduction + GMP T-cell expansion; IND-enabling GLP toxicology | LNP-encapsulated mRNA drug substance; CRISPR RNP complex (SpCas9 + sgRNA); rAAV vector (AAV9 / rAAV-LK03); autologous CAR-T cell product; ionizable lipid excipients (ALC-0315, SM-102, DLin-MC3-DMA) | Partial | Very High | Regulatory approval + manufacturing IP + delivery patent estate | Very High (approved biologic) / Negative (pre-revenue) |
| **Clinical Research & Real-World Evidence** | Design and operate clinical trials; generate regulatory evidence and post-market real-world data | Adaptive trial design (Bayesian adaptive platform, master protocol / MAMS); AI-powered patient recruitment + site selection; electronic data capture (EDC, eCTD assembly); pharmacovigilance signal detection (PSUR, PBRER); RWE study design using claims + EHR data (propensity score matching, synthetic control arms) | Clinical study report (CSR); IND / NDA / BLA dossier; post-market RWE study; integrated summary of safety (ISS); patient registry dataset; HEOR economic model | N | Medium | Therapeutic expertise + site network breadth | Medium (service model) |
| **Surgical & Physical Delivery** | Deploy AI-guided robotic surgical systems and precision interventional devices at point of care | Robotic kinematics + EndoWrist articulation engineering; real-time AI tissue recognition + surgical step detection; image-guided intervention (intraoperative fluoroscopy, MRI/CT fusion); haptic feedback calibration + motion scaling; capital equipment installation + surgeon credentialing and proctoring | da Vinci 5 robotic surgical system; Stryker Mako orthopaedic robot; single-use EndoWrist instrument kit; knee/hip prosthetic implant; procedure analytics software subscription | N | High | Installed base + switching cost (surgeon training + hospital workflow) | High (recurring instruments + procedure volume) |

---

## Publicly-Traded Nodes

| Tier | Ticker | Company | Mkt Cap | In Registry | Notes |
|------|--------|---------|---------|-------------|-------|
| Genomics & Biological Measurement | ILMN | Illumina | Large | No | ~80% short-read NGS market share; NovaSeq X+ dominant; reagent razor-blade model |
| Genomics & Biological Measurement | PACB | Pacific Biosciences | Small | No | Long-read HiFi sequencing; accuracy competitor to ONT (private, LON:ONT) |
| Genomics & Biological Measurement | TXG | 10x Genomics | Small | No | scRNA-seq (Chromium) + spatial transcriptomics (Visium, Xenium); dominant in single-cell workflows |
| Genomics & Biological Measurement | BRKR | Bruker Corporation | Mid | No | Mass spec (timsTOF), NMR, X-ray crystallography, cryo-EM |
| Genomics & Biological Measurement | TMO | Thermo Fisher Scientific | Large | No | Broadest life sciences tools platform: Orbitrap MS, Applied Biosystems sequencing, Cytiva bioprocessing |
| Genomics & Biological Measurement | DHR | Danaher | Large | No | Life sciences instruments via Cytiva, Beckman Coulter, Leica Biosystems, SCIEX |
| Biological Data Aggregation & Curation | TEM | Tempus AI | Mid | No | Clinical genomics data platform + AI diagnostics + RWE; spans Tiers 2 and 4 |
| Biological Data Aggregation & Curation | VEEV | Veeva Systems | Large | No | Life sciences CRM + Vault Clinical (EDC, eTMF, CTMS) |
| Biological Data Aggregation & Curation | IQV | IQVIA Holdings | Large | No | Largest health data repository (OCEANS, LAAD) + global CRO; dual role: Tier 2 + Tier 6 |
| AI Drug Discovery & Molecular Design | SDGR | Schrödinger | Mid | No | Physics-based FEP+ simulation + ML; software platform + proprietary internal drug pipeline |
| AI Drug Discovery & Molecular Design | RXRX | Recursion Pharmaceuticals | Mid | No | Biological foundation models (Phenom-β) + BioHive-2 supercomputer + wet lab automation |
| AI Diagnostics & Precision Medicine | GH | Guardant Health | Mid | No | ctDNA liquid biopsy: Guardant360 CDx + LUNAR-2; Shield multi-cancer early detection |
| AI Diagnostics & Precision Medicine | EXAS | Exact Sciences | Large | No | Cologuard CRC screening test + Oncotype DX recurrence score |
| AI Diagnostics & Precision Medicine | NTRA | Natera | Mid | No | Signatera ctDNA MRD monitoring; Panorama NIPT; oncology + reproductive health |
| AI Drug Discovery & Molecular Design | EXAI | Exscientia | Small | No | AI-native small molecule drug design (ML-generated candidates); Oxford-based; ⚠️ acquired by Recursion (RXRX) ~2024 — verify listing status before onboarding |
| Therapeutics (AI-Designed) | MRNA | Moderna | Large | No | mRNA platform: COVID-19/flu/RSV vaccines + mRNA-4157/V940 personalized cancer vaccine (with MSD) |
| Therapeutics (AI-Designed) | CRSP | CRISPR Therapeutics | Mid | No | Casgevy (exa-cel): first approved CRISPR therapy (SCD/β-thal); CTX112 allogeneic CAR-T |
| Therapeutics (AI-Designed) | NTLA | Intellia Therapeutics | Small-Mid | No | In vivo CRISPR: NTLA-2001 (TTR amyloidosis); liver-targeted LNP delivery platform |
| Therapeutics (AI-Designed) | BEAM | Beam Therapeutics | Small | No | Base editing platform; BEAM-101 (SCD), BEAM-302 (AAT deficiency) |
| Clinical Research & RWE | CRL | Charles River Laboratories | Mid | No | Preclinical CRO: GLP safety pharmacology, toxicology, DMPK, in vitro biology |
| Clinical Research & RWE | MEDP | Medpace Holdings | Mid | No | Therapeutic-focus clinical CRO; oncology/CV/metabolic; high-touch model |
| Clinical Research & RWE | ICLR | ICON plc | Large | No | Full-service global CRO; PRA acquisition; ~$7B revenue |
| Surgical & Physical Delivery | ISRG | Intuitive Surgical | Large | No | da Vinci 5; ~70% MIS robotic surgery market share; 10M+ procedures performed; cross-link → Edge & Physical AI |
| Surgical & Physical Delivery | SYK | Stryker | Large | No | Mako robotic orthopaedic surgery (knee/hip); trauma + implant devices |
| Surgical & Physical Delivery | MDT | Medtronic | Large | No | Hugo RAS surgical robot; neuromodulation; cardiac devices; spine surgery |

---

## Structural Gaps

**EHR / Health Information Exchange (Tier 2 — Data Aggregation):** Epic Systems (private, estimated >$100B) and Oracle Health (Cerner, acquired by Oracle 2022 for $28B) collectively control structured inpatient and outpatient data for ~75% of U.S. hospital beds. This is the deepest data access chokepoint in the sector — TEM, IQV, and RXRX must negotiate de-identification and data-sharing agreements with Epic-anchored health systems. No dedicated public pure-play EHR company of scale exists in the U.S. Investors gain partial exposure via ORCL (Oracle Health subsidiary) or through data aggregators (TEM, IQV) negotiating bulk access. Watch for TEM hospital partnership announcements as the proxy for data access trajectory.

**Lab Automation & Robotic Liquid Handling (Tiers 2–3):** High-throughput robotic liquid handling underpins wet lab screening and sample-prep workflows at RXRX, SDGR, and every drug discovery CRO. Tecan (TECN.SW, Swiss exchange, ~CHF 3B) is the only sizeable pure-play public company; Hamilton and CyBio are private; Beckman Coulter is a Danaher (DHR) subsidiary with no standalone exposure. No U.S. large-cap pure-play lab automation company exists at this tier.

**LNP / Drug Delivery Formulation (Tier 5 — Therapeutics):** Lipid nanoparticle (LNP) formulation is the gating delivery technology for both mRNA and in vivo CRISPR therapeutics. Alnylam Pharmaceuticals (ALNY) holds the broadest LNP IP estate but operates as a therapeutic company, not a platform licensor. Precision NanoSystems (Cytiva/DHR subsidiary) makes the NanoAssemblr microfluidic mixing equipment used by MRNA, CRSP, and NTLA. No standalone public pure-play LNP formulation platform exists; IP cross-licensing between MRNA, BNTX, and ALNY controls commercial access.

**Viral Vector Manufacturing CMO (Tier 5 — Therapeutics):** AAV and lentiviral manufacturing capacity remains a structural bottleneck for gene therapy programs at NTLA, BEAM, and EDIT. Oxford Biomedica (OXB.L, London AIM-listed) is the most direct public play. Catalent (delisted, acquired by Novo Holdings 2024 for ~$16B) removed the largest standalone CDMO from the public market. No U.S. large-cap public viral vector CMO exists. Monitor Thermo Fisher's Cytiva gene therapy tools segment as a partial proxy.

---

## Key Questions to Answer Before Writing the Sector Framework

1. **Clinical validation of AI-designed drugs:** Do AI-first discovery approaches (Schrödinger FEP+, Recursion phenomics) produce measurably higher Phase 2 success rates than traditional HTS? The first head-to-head clinical readouts in 2026–2028 define the sector's investment thesis.
2. **EHR data moat dynamics:** Can TEM, IQV, or any aggregator assemble a dataset that neutralizes Epic's structural lock — or does the moat permanently concentrate data returns at the hospital system level?
3. **ILMN sequencing dominance vs. long-read:** How quickly does PACB / ONT long-read penetrate clinical applications where ILMN short-read currently dominates? ONT UX800 at ~$500/genome threatens ILMN's pricing power in the clinical market.
4. **mRNA platform generalization:** Does the mRNA platform generalize beyond vaccines into oncology (mRNA-4157/V940 personalized cancer vaccine with MSD) and rare disease (PA, MMA)? Timing of first non-vaccine mRNA approval defines MRNA's terminal multiple.
5. **CRISPR delivery beyond the liver:** LNP delivery currently confines in vivo CRISPR/base editing to liver targets (TTR, PCSK9, ALAS1). What delivery modality unlocks muscle, lung, and CNS? This determines the addressable TAM for CRSP, NTLA, and BEAM by 2030.
6. **Surgical robotics competitive dynamics:** ISRG holds ~70% market share but MDT Hugo, SYK Mako (soft tissue), and J&J Ottava are entering. How does ASP pricing evolve as global installed base expands from ~10,000 toward 50,000 systems?

---

## Interrelationship Anchors

### Inputs (this sector consumes from)
| From Sector | From Tier | Product / Signal |
|---|---|---|
| Cloud Infrastructure | GPU Cluster / Distributed Training | GPU compute hours (A100/H100/H200) → biological foundation model training at RXRX BioHive-2, TEM genomics pipelines, SDGR FEP+ simulation clusters |
| Compute Hardware | AI Accelerator Design | NVIDIA H100/H200 SXM module allocations → AI drug discovery training and inference; demand signal from RXRX and TEM growing compute footprints |
| AI Model | Foundation Model Development | Protein structure prediction APIs (AlphaFold 3, ESMFold) consumed by SDGR/RXRX; LLM APIs (clinical NLP, note summarization, genomic report generation at TEM) |
| Software Infrastructure | ML Frameworks + MLOps | PyTorch / JAX → biological model training pipelines; W&B / MLflow → AI experiment tracking at RXRX and SDGR |
| Critical Minerals | Rare Earth Separation + Isotope Processing | Gadolinium (Gd) → MRI contrast agents; Lutetium-177 (Lu-177) → radioligand therapy (PLUVICTO-type); Nb-Ti wire → MRI superconducting magnet windings |
| Electronic Components | Precision Optical + Detection Sensors | Custom CMOS image sensors → Illumina sequencing-by-synthesis optical detection (flow cell readout); TOF and ion trap detectors → mass spectrometry instruments |
| Power Infrastructure | Primary Power + Thermal | Hospital/laboratory UPS + clean power for bioreactors; -80°C cold storage and cryogenic equipment (LN₂, LHe for MRI and cryo-EM) |

### Outputs (this sector supplies to)
| To Sector | To Tier | Product / Signal |
|---|---|---|
| AI Model | Foundation Model Development | Biological training datasets (protein sequences, genomic VCF, cell imaging phenotypes, drug response matrices) → training data for ESM / Evo / AlphaFold next-generation biological foundation models |
| Cloud Infrastructure | Demand Signal | Bio AI workload growth (RXRX BioHive-2 expansion, SDGR compute scaling, TEM data processing) → GPU cluster demand pull |
| Edge & Physical AI | Surgical Robotics + Physical AI Deployment | ISRG da Vinci 5, SYK Mako deployed at point of care → AI-guided surgical systems; direct cross-link to Edge & Physical AI deployment surface |
| Application | AI-Native Vertical Applications | Clinical decision support APIs (TEM genomics reports, Guardant360 CDx) → AI healthcare vertical application layer at L01 |
| Security | Identity & Access Management | HIPAA-regulated health data access → elevated IAM + zero-trust security requirements; drives healthcare-vertical cybersecurity spend |

---

## Research Log
- **2026-06-22** — map-sector run. 7 tiers · 2 full chokepoints (ILMN NGS dominance; EHR/Epic structural gap) · 4 structural gaps (EHR/Epic, lab automation, LNP formulation, viral vector CMO). New candidates not yet in registry: ILMN · PACB · TXG · BRKR · TMO · DHR · TEM · VEEV · IQV · SDGR · RXRX · GH · EXAS · NTRA · EXAI · MRNA · CRSP · NTLA · BEAM · CRL · MEDP · ICLR · ISRG · SYK · MDT.
