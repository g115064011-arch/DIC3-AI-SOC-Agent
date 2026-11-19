# 【A4 橫式 高密度 NUMBERING 資訊圖表】AI SOC Analyst Agent 系統總覽

> **格式規格**：A4 Landscape（297mm × 210mm）高密度資訊圖表  
> **編號規範**：階層式全景編號（`[01]`～`[08]` 模組、`[M1]`～`[M5]` 思維、`[C1]`～`[C3]` 爭論、`[R1]`～`[R5]` 規則、`[E1]`～`[E5]` 實驗）  
> **對應專案**：AI SOC Analyst Agent (DIC3 Proposal Refactor)  

```
=============================================================================================================================================================
[A4 LANDSCAPE INFOGRAPHIC] AI SOC ANALYST AGENT: SPEC-DRIVEN ARCHITECTURE & EXPERIMENTAL BLUEPRINT
=============================================================================================================================================================
┌──────────────────────────────────────────────┬─────────────────────────────────────────────────────────────┬──────────────────────────────────────────────┐
│  SECTION 1: CORE MOTIVATION & DATASETS       │  SECTION 2: 8-MODULE REASONING & FUSION ARCHITECTURE        │  SECTION 3: KILL CHAIN & ESCALATION POLICY   │
├──────────────────────────────────────────────┼─────────────────────────────────────────────────────────────┼──────────────────────────────────────────────┤
│ 1.1 REAL-WORLD SECURITY CRISIS [2025-2026]   │ 2.1 EIGHT-MODULE PIPELINE [01] -> [08]                      │ 3.1 PROGRAMMATIC KILL CHAIN RULES (R1-R5)    │
│  [D01] 2.63M Probes/day: Taiwan NSB 2026     │  ┌────────────────────────────────────────────────────────┐ │  [R1] Exfiltration/Impact (T1048/T1486)      │
│  [D02] $4.99M Breach Cost: IBM 2026 (+12%)   │  │ [01] Analyst / SIEM Queue: Alert Ingestion & Batching  │ │       -> Forced High Risk; Overrides ML Low  │
│  [D03] 14-122 Days Dwell: Mandiant M-Trends  │  │   v                                                    │ │  [R2] Credential Dump + Lateral Move       │
│  [D04] 40.4% LLM Miss Rate: AIDA Alert-Bench │  │ [02] Query/Input: Schema Normalization & Validation    │ │       -> T1003 + T1021; Escalation Priority│
│  [D05] 90%+ Dismissed are Benign (BP!=FP)    │  │   v                                                    │ │  [R3] Initial Access + Persistence          │
│                                              │  │ [03] Planner & Reasoning Agent (ReAct Loop)            │ │       -> T1566 + T1547; Flag Correlation   │
│ 1.2 DUAL PUBLIC BENCHMARK DATASETS           │  │   <-> [04] Retrieval Engine: DuckDB Multi-Hop Logs     │ │  [R4] Indicator Removal on Host (T1070)    │
│  [DS1] Microsoft GUIDE (Kaggle CDLA-2.0)     │  │   <-> [05] Analytics Engine: GBDT + TreeSHAP Explain   │ │       -> Flag Defense Evasion Log Tamper   │
│   - 13,000,000 Evidences / 1,000,000 Incid.  │  │   <-> [06] Domain Knowledge: ATT&CK STIX 2.1 + NIST    │ │  [R5] Multi-Stage Progression (>=3 Tactics)│
│   - 6,100 Enterprise Orgs (Train: 5,769)     │  │   v                                                    │ │       -> Critical Threat Elevation         │
│   - Ground Truth TP / BP / FP Labels         │  │ [07] Decision Fusion & Safety Escalation Policy        │ │                                            │
│  [DS2] ExCyTIn-Bench (ICML 2026)             │  │   v                                                    │ 3.2 AUDITABLE ESCALATION POLICY (ALGORITHM 2)│
│   - 57 Log Tables / 8 Real Attack Chains     │  │ [08] Output: Dual Audit Reports + Streamlit UI          │ │  Status = NEEDS_HUMAN_REVIEW IF:           │
│   - 7,542 Generated Investigation Qs         │  └────────────────────────────────────────────────────────┘ │   (1) Confidence < tau (Default: 0.80)       │
│   - Current SOTA Reward: 0.606 (Full DB:0.248│                                                             │   (2) Conflict: Argmax(P_ml) != Argmax(Q_llm)│
│                                              │ 2.2 EVIDENCE FUSION FORMULATION (ALGORITHM 2)               │   (3) High-Risk Kill Chain Trigger (R1-R5)   │
│ 1.3 FIVE CORE DOMAIN MINDSETS (M1-M5)        │  Score s = w_ml * P_ml(TP) + w_llm * Q_llm(TP)              │   (4) Budget Exhausted (B) & Uncertainty Open│
│  [M1] Assume Breach: Empty query != Clean    │  Safety Rule: IF (R1..R5 Active) AND (P_ml >= tau_safety)   │                                            │
│  [M2] Context Awareness: Attack Chain pos.   │               THEN Verdict = True Positive (Override)       │ 3.3 THREE CORE CONTROVERSIES (C1-C3)         │
│  [M3] Asymmetric Cost: FN cost >>> FP cost   │  Attribution: Local SHAP phi_i = E[f(x)|x_S] - E[f(x)|x_S\i]│  [C1] Triage: ML Stability vs LLM Context    │
│  [M4] Pyramid of Pain: TTPs over Hash/IP     │                                                             │  [C2] Complacency vs Analyst Verification    │
│  [M5] Human-in-the-Loop: Agent as Copilot    │ 2.3 ASSUME BREACH INVESTIGATION (ALGORITHM 1)               │  [C3] Benchmark Bias vs Proprietary Telemetry│
│                                              │  Loop budget B; Check heartbeat telemetry on empty queries; │                                              │
│                                              │  Discontinuity -> Mark INSUFFICIENT_EVIDENCE (No early close│                                              │
└──────────────────────────────────────────────┴─────────────────────────────────────────────────────────────┴──────────────────────────────────────────────┘
┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│  SECTION 4: VERIFIED RESEARCH LANDSCAPE & ARTICLE SUMMARY TABLE [50% AI TECH : 50% DOMAIN KNOW-HOW] (ALL 16 PAPERS VERIFIED)                            │
├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ [Ref] [Year] [AI / Domain Category]        [Method / Technology]       [Dataset / Evaluation Scope]       [Key Empirical Findings]          [Verified]    │
│ ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── │
│ [01]   2024  AI: ML-Based Alert Triage     GBDT (CGR), Defender XDR    GUIDE (13M rows, 1M inc, 6.1k org) Macro-F1 0.87, Prec 0.87, Rec 0.86     Y (arXiv)   │
│ [02]   2025  AI: Multi-Agent Investigation Multi-Agent LLM (CORTEX)    10+ enterprise investigation tracesActionable F1 0.66->0.78, FP 24.9%->14.2%  Y (arXiv)   │
│ [03]   2026  AI: Reasoning & Escalation    AIDA (Challenger + Judge)   ALERT-BENCH (1,247 attack alerts)  Baselines miss >=40.4%; AIDA F1 0.958, FNR 3.1%Y (arXiv)   │
│ [04]   2026  AI: Threat Investigation BenchLLM Agent + SQL Tools       Azure Tenant (57 tables, 7,542 Qs) Best Reward 0.606; Drops to 0.248 on full DB   Y (ICML)    │
│ [05]   2025  AI: Security Reasoning Bench  CyberSOCEval (CyberSecEval4)Malware (609 Qs), TI (588 Qs/45 rpt)Malware Acc 15-28%; TI 43-53%; Scaling flat Y (arXiv)   │
│ [06]   2025  AI: Domain RAG for ATT&CK     TechniqueRAG (ACL Findings) Procedures / Expert Benchmarks     Procedures F1 91.09%; Expert Multi-label ~50%  Y (ACL)     │
│ [07]   2026  AI: Queue Prioritization      Modified BM25 Ranking (AIP) 1k orgs, 473k queues, GUIDE+9.9k  Precision@10 92.8%; View interaction +17.5%    Y (arXiv)   │
│ [26]   2026  AI: SOC Field Deployment      ReAct Agent Field Study     University SOC (14-month study)    >90% report reuse; 30-50% time saved for top-3 Y (arXiv)   │
│ ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── │
│ [08]   2026  Domain: Alert Fatigue Survey  Cognitive SOC 4-Stage Model 87 core studies (2015-2026)        4 gaps: Ops validation, Robustness, General.   Y (Survey)  │
│ [09]   2025  Domain: LLM in SOC Workflows  Kitchenham Systematic ReviewLLM in Triage, Logs, Intel         First comprehensive survey of LLM SOC adoption Y (Survey)  │
│ [10]   2025  Domain: Kill Chain Attack GraphMulVAL + CALDERA Testbed   10 hosts, 5 scenarios, 475 seq     Sequence classification AUC 0.95; Threshold 80%Y (JISA)    │
│ [11]   2025  Domain: ATT&CK Correlation    ROSCA Alert Graph Matching  Hospital SOC (382 EDR, 37 IDS)     Correlates 382 alerts in 0.12s; Beats MATE     Paywall-OK  │
│ [12]   2026  Domain: Automation ComplacencyPLS Structural Equation     4 SOCs, 696 analysts, 29 interview Automation reduces vigilance; Verification fixesPaywall-OK  │
│ [13]   2025  Domain: Incident Response Std NIST SP 800-61 Rev. 3       CSF 2.0 Community Profile (6 Func) RS.MA-02 mandates risk triage, replaces FIFO  Y (NIST)    │
│ [24]   2022  Domain: Analyst Alert Triage  Qualitative Study (REACT)   7 SOCs, 21 practitioners, 20 survey90%+ dismissed alerts are Benign Positives (BP)Y (USENIX)  │
│ [25]   2025  Domain: Tier-1 Investigation  Think-Aloud Experiment/AISS Commercial SOC (5 analysts, 400 inv)Escalations require greater evidence diversity Y (USEC)    │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────┬─────────────────────────────────────────────────────────────┬──────────────────────────────────────────────┐
│  SECTION 5: SPEC-DRIVEN DEVELOPMENT (OPENSPEC│  SECTION 6: EXPERIMENTAL EVALUATION SUITE                   │  SECTION 7: DELIVERABLES & HANDOVER PACKAGE  │
├──────────────────────────────────────────────┼─────────────────────────────────────────────────────────────┼──────────────────────────────────────────────┤
│ 5.1 OPENSPEC CAPABILITIES MATRIX             │ 6.1 PLANNED EXPERIMENTS (E1 - E5)                           │ 7.1 VERIFIED ARTIFACTS IN REPOSITORY         │
│  [CAP-1] incident-triage                     │  [E1] Multi-Class Triage Accuracy (Macro-F1, FNR by class)  │  [F01] README.md (Comprehensive guide)       │
│   - RFC 2119: Schema validate, GBDT proba    │  [E2] Safety Escalation Trade-off (Miss Rate vs Esc. Rate)  │  [F02] DESIGN.md (Complete 8-module specs)   │
│  [CAP-2] evidence-retrieval                  │  [E3] Agentic Investigation Faithfulness (ExCyTIn-Bench)    │  [F03] docs/proposal.md (Formal bilingual RFC│
│   - RFC 2119: Read-only SQL, Assume Breach   │  [E4] Report Quality & Verifiability (Analyst + LLM Judge)  │  [F04] docs/DIC3_CHECKLIST.md (5/5 verified) │
│  [CAP-3] domain-knowledge-reasoning          │  [E5] Cost & Operational Latency (Token/Alert, Sec/Alert)   │  [F05] docs/NBLM_A2Z_ANALYSIS.md (26 letters)│
│   - RFC 2119: ATT&CK STIX search, R1-R5 rules│                                                             │  [F06] docs/INFOGRAPHIC_A4_LANDSCAPE.md      │
│  [CAP-4] risk-escalation                     │ 6.2 RIGOROUS DATA SPLIT STRATEGY                            │  [F07] docs/infographic_a4_landscape.html    │
│   - RFC 2119: Algorithm 2 fusion, Escalation │  - GroupKFold Partitioning by OrgId + IncidentId            │  [F08] experiments/e0_profile_guide.py       │
│  [CAP-5] explainability-reporting            │  - Strictly prevents cross-organization telemetry leakage   │  [F09] experiments/results/guide_profile.json│
│   - RFC 2119: TreeSHAP weights, Dual reports │                                                             │  [F10] openspec/ (Strictly Validated Active) │
│                                              │ 6.3 VERIFIED LOCAL PROFILING (TASK 1.1 COMPLETED)           │                                              │
│ 5.2 ZERO PHANTOM IMPLEMENTATION POLICY       │  - 707,108 Incidents / 5,769 Organizations                  │ 7.2 GIT VERSION CONTROL                      │
│  - Active Change: refactor-ai-soc-agent-prop.│  - 9,516,837 Evidence Rows processed cleanly                │  - Current Branch: dic3-refactor             │
│  - STRICT VALIDATION: Valid (Exit Code 0)    │  - Class Distribution: 66.8% TP, 20.3% BP, 12.9% FP         │  - Target Release: main (Fast-Forward Ready) │
│  - ARCHIVE STATUS: DEFERRED until full code  │  - Script: experiments/e0_profile_guide.py                  │  - Remote: g115064011-arch/DIC3-AI-SOC-Agent │
└──────────────────────────────────────────────┴─────────────────────────────────────────────────────────────┴──────────────────────────────────────────────┘
=============================================================================================================================================================
```

