# Project Context: AI SOC Analyst Agent

> **Project Name**: AI SOC Analyst Agent (DIC3 Proposal Refactor)  
> **Course / Stage**: AIoT Capstone — Proposal Refactor with OpenSpec  
> **Baseline Group**: Group 16 ([https://github.com/susuannie/proposal.git](https://github.com/susuannie/proposal.git))  
> **Personal Repo**: [https://github.com/g115064011-arch/DIC3-AI-SOC-Agent.git](https://github.com/g115064011-arch/DIC3-AI-SOC-Agent.git)  

---

## 1. Project Background & Problem Statement

Modern Security Operations Centers (SOCs) are inundated by tens of thousands of alerts daily, of which only a small fraction represent actual cyber intrusions. Massive volumes of false positives and benign triggers lead to pervasive analyst alert fatigue.

This project designs a **Domain AI SOC Analyst Agent** combining Machine Learning (ML), MITRE ATT&CK domain knowledge, and Large Language Model (LLM) reasoning to provide evidence-backed, explainable incident triage across True Positive (TP), Benign Positive (BP), and False Positive (FP) categories, with an explicit Human-in-the-Loop escalation mechanism.

---

## 2. Technical Stack & Tools

- **Language & Runtime**: Python 3.14+, Node.js v22.14.0+
- **Data Analytics & Storage**: DuckDB, pandas, PyArrow
- **Machine Learning**: LightGBM, XGBoost, Scikit-learn
- **Explainability**: SHAP (TreeSHAP)
- **Knowledge Base & Vector Store**: MITRE ATT&CK STIX 2.1, Chroma Vector DB, `mitreattack-python`
- **Agent Framework**: LLM Tool Use / ReAct loop (Planner & Reasoner)
- **User Interface**: Streamlit Dashboard (planned)
- **Specification System**: OpenSpec 1.17.0 (Spec-Driven Development)

---

## 3. Datasets & Benchmarks

1. **Microsoft GUIDE** (Kaggle CDLA-2.0):
   - Primary triage dataset: ~13M evidence rows, 1.6M alerts, 1M incidents across 6,100 enterprise organizations.
   - Analyst ground-truth labels: TP (20.6%), BP (49.0%), FP (30.4%).
2. **ExCyTIn-Bench** (ICML 2026 / microsoft/SecRL):
   - Agent cyber threat investigation benchmark in Azure environment: 57 relational log tables, 8 authentic attack chains, 7,542 questions.
3. **MITRE ATT&CK Framework**:
   - Enterprise STIX 2.1 matrix: 14 Tactics, 200+ Techniques, Sub-techniques, Mitigations.

---

## 4. Architectural Modules (①–⑧)

- **① User / Scenario**: SOC Tier-1 / Tier-2 analysts, alert queue processing.
- **② Query / Input**: Structured `TriageRequest` (Incident ID / Alert batch) and natural language queries.
- **③ Planner & Reasoning Agent**: ReAct-style LLM decomposing tasks, invoking tools, maintaining budgets.
- **④ Data Acquisition / Retrieval**: Evidence store (DuckDB) and read-only SQL log queries.
- **⑤ Analytics Engine**: GBDT classifier (predicting TP/BP/FP), TreeSHAP feature explanations, k-NN similar incidents.
- **⑥ Domain Knowledge Integration**: ATT&CK vector database, NIST SP 800-61 Rev. 3 playbooks, Kill Chain risk rules (R1–R5).
- **⑦ Decision / Recommendation**: Evidence fusion engine, confidence calibration ($\tau$), and escalation triggers.
- **⑧ Output & Interaction**: Structured `TriageReport` (JSON/Markdown), Streamlit dashboard, feedback loop.

---

## 5. Naming & Engineering Conventions

- **OpenSpec Capabilities**: kebab-case (`incident-triage`, `evidence-retrieval`, `domain-knowledge-reasoning`, `risk-escalation`, `explainability-reporting`).
- **Data Models**: PascalCase schemas (`TriageRequest`, `TriageReport`, `IncidentFeature`, `EvidenceRecord`).
- **Requirements**: MUST follow RFC 2119 with explicit `SHALL` or `MUST`.
- **Scenarios**: Gherkin-inspired `WHEN ... THEN ...` verification blocks.
- **Lifecycle Policy**: During Proposal Refactor (DIC3), changes remain **active** (`openspec/changes/refactor-ai-soc-agent-proposal/`). No `openspec archive` until actual code implementation and test passes.
