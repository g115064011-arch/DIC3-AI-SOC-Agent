# Tasks: Refactor AI SOC Analyst Agent with OpenSpec

## 1. Data Ingestion and Profiling Infrastructure

- [x] 1.1 Implement and verify GUIDE dataset exploratory profiling script  
  - **Purpose**: Verify integrity, label distribution, missing rates, and anonymization of GUIDE training data.
  - **Requirement**: `incident-triage` / Incident Ingestion and Schema Validation
  - **Files**: `experiments/e0_profile_guide.py`, `experiments/results/guide_train_profile.json`
  - **Content**: Stream large GUIDE CSV using pandas chunks, calculate row counts, unique incidents, organizations, and label distributions.
  - **Verification**: Script execution outputs valid JSON matching 707,108 incidents across 5,769 organizations.
  - **Completion Condition**: Output JSON generated and validated.
  - **Status**: Already Implemented

- [ ] 1.2 Implement canonical incident ingestion pipeline and schema validation  
  - **Purpose**: Ingest and validate alert batches into structured `TriageRequest` objects.
  - **Requirement**: `incident-triage` / Incident Ingestion and Schema Validation
  - **Files**: `src/soc_agent/schemas.py`, `tests/test_schemas.py`
  - **Content**: Define Pydantic models for `TriageRequest`, `AlertRecord`, and `EntityContext` with validation constraints.
  - **Verification**: Unit tests pass validating correct payloads and rejecting malformed records.
  - **Completion Condition**: Schemas serialize and deserialize valid GUIDE payloads without errors.
  - **Status**: Planned

## 2. Machine Learning Triage and Feature Attribution

- [ ] 2.1 Train and evaluate GBDT multi-class triage classifier  
  - **Purpose**: Compute calibrated probabilities across TP, BP, and FP classes on incident features.
  - **Requirement**: `incident-triage` / Multi-Class Incident Triage Prediction
  - **Files**: `src/soc_agent/analytics/triage_model.py`, `experiments/e1_triage.py`
  - **Content**: Extract aggregated incident features and train LightGBM/XGBoost models using GroupKFold on `OrgId` + `IncidentId`.
  - **Verification**: Run `python experiments/e1_triage.py` and verify Macro-F1 and TP recall exceed baseline heuristics.
  - **Completion Condition**: Calibrated probability outputs satisfy $\sum p = 1.0$.
  - **Status**: Planned

- [ ] 2.2 Implement TreeSHAP local feature explanation engine  
  - **Purpose**: Provide local feature attribution weights for every triage classification.
  - **Requirement**: `explainability-reporting` / Local Feature Attribution via TreeSHAP
  - **Files**: `src/soc_agent/analytics/explain.py`, `tests/test_explain.py`
  - **Content**: Wrap TreeExplainer to compute top-5 positive and negative contributing features for each incident.
  - **Verification**: Unit tests confirm SHAP values match model output probability shift.
  - **Completion Condition**: SHAP summary dictionary attached to classification results.
  - **Status**: Planned

## 3. Evidence Retrieval and Log Investigation Engine

- [ ] 3.1 Build DuckDB incident evidence store and SQL log query tool  
  - **Purpose**: Enable fast read-only forensic queries across large incident evidence tables.
  - **Requirement**: `evidence-retrieval` / Multi-Hop Evidence Acquisition
  - **Files**: `src/soc_agent/data/evidence_store.py`, `src/soc_agent/tools/log_query.py`
  - **Content**: Set up indexed DuckDB tables and implement a read-only query tool enforcing `SELECT`-only constraints.
  - **Verification**: Integration test queries execute under 100ms and block mutation statements.
  - **Completion Condition**: Tool returns structured tabular records with source file and row metadata.
  - **Status**: Planned

- [ ] 3.2 Implement ReAct planner with budget limits and Assume Breach log check  
  - **Purpose**: Coordinate multi-hop evidence acquisition with termination controls under Assume Breach.
  - **Requirement**: `evidence-retrieval` / Query Budget and Termination Control, Incomplete Log Detection under Assume Breach
  - **Files**: `src/soc_agent/agent/planner.py`, `tests/test_planner.py`
  - **Content**: Implement ReAct loop checking `IsSufficient(E)`, enforcing tool budget $B$, and detecting log discontinuity.
  - **Verification**: Planner terminates when budget $B$ is reached or data sufficiency is met; empty query with broken heartbeat triggers insufficient evidence.
  - **Completion Condition**: Automated test verifies planner loop correctly halts and flags missing telemetry.
  - **Status**: Planned

## 4. Domain Knowledge Integration and Kill Chain Reasoning

- [ ] 4.1 Construct Chroma vector store for MITRE ATT&CK STIX 2.1 knowledge  
  - **Purpose**: Provide semantic search over ATT&CK tactics, techniques, and mitigation guidance.
  - **Requirement**: `domain-knowledge-reasoning` / MITRE ATT&CK Semantic Retrieval
  - **Files**: `src/soc_agent/knowledge/attack_kb.py`, `scripts/build_attack_kb.py`
  - **Content**: Parse official MITRE ATT&CK Enterprise STIX 2.1 data, generate embeddings, and store in persistent Chroma DB.
  - **Verification**: Query test for "credential dumping" retrieves T1003 with cosine similarity > 0.8.
  - **Completion Condition**: Top-3 relevant techniques and mitigation playbooks retrieved accurately.
  - **Status**: Planned

- [ ] 4.2 Implement Cyber Kill Chain tactical risk rule engine  
  - **Purpose**: Evaluate attack chain progression and flag high-risk tactical phases (R1–R5).
  - **Requirement**: `domain-knowledge-reasoning` / Cyber Kill Chain Tactical Progression Mapping
  - **Files**: `src/soc_agent/decision/kill_chain.py`, `tests/test_kill_chain.py`
  - **Content**: Implement rules R1 (Exfiltration/Impact), R2 (Credential Access + Lateral Movement), R3 (Initial Access + Persistence), R4 (Log tampering T1070), and R5 (Multi-stage tactics).
  - **Verification**: Test cases verify high-risk flags are raised for late-stage and multi-tactic incidents.
  - **Completion Condition**: All 5 rules pass unit test assertions.
  - **Status**: Planned

- [ ] 4.3 Integrate NIST SP 800-61 Rev. 3 incident response playbooks  
  - **Purpose**: Provide structured containment and eradication steps mapped to attack techniques.
  - **Requirement**: `domain-knowledge-reasoning` / Incident Response Playbook Alignment
  - **Files**: `src/soc_agent/knowledge/playbooks/`, `src/soc_agent/knowledge/recommend.py`
  - **Content**: Define JSON playbooks covering account compromises, ransomware, and lateral movement aligned with NIST CSF 2.0 functions.
  - **Verification**: Unit tests verify generated playbooks contain concrete containment, eradication, and recovery steps.
  - **Completion Condition**: True Positive incidents receive actionable playbook actions.
  - **Status**: Planned

## 5. Multi-Modal Decision Fusion and Escalation Policy

- [ ] 5.1 Implement evidence fusion algorithm (Algorithm 2)  
  - **Purpose**: Synthesize statistical ML probabilities, LLM qualitative confidence, and Kill Chain rules.
  - **Requirement**: `risk-escalation` / Evidence Fusion and Multi-Modal Decision Synthesis
  - **Files**: `src/soc_agent/decision/fusion.py`, `tests/test_fusion.py`
  - **Content**: Implement `FuseEvidence` computing weighted score $s = w_{ml} \cdot p + w_{llm} \cdot q$ and safety threshold overrides.
  - **Verification**: Unit tests verify that high-risk flags override low ML probabilities to True Positive when $p_{TP} \ge \tau_{safety}$.
  - **Completion Condition**: Synthetic decision score and argmax label match Algorithm 2 specifications.
  - **Status**: Planned

- [ ] 5.2 Implement automated human escalation and conflict detection policy  
  - **Purpose**: Route uncertain, conflicting, or high-risk incidents to Tier-1/Tier-2 human analysts.
  - **Requirement**: `risk-escalation` / Automated Human-in-the-Loop Escalation Policy, Conflict Detection and Dispute Annotation
  - **Files**: `src/soc_agent/decision/escalation.py`, `tests/test_escalation.py`
  - **Content**: Enforce status `NEEDS_HUMAN_REVIEW` when confidence $< \tau$, conflict flag is present, high-risk rule triggers, or evidence is insufficient.
  - **Verification**: Test matrix asserts escalation triggers across all four operational boundary conditions.
  - **Completion Condition**: Escalation status and dispute explanations correctly populated in report metadata.
  - **Status**: Planned

## 6. Reporting, Interactive UI, and Analyst Feedback Loop

- [ ] 6.1 Implement dual-format structured audit report generator  
  - **Purpose**: Generate verifiable JSON and Markdown incident reports with citations to source telemetry.
  - **Requirement**: `explainability-reporting` / Structured Audit Evidence Report Generation
  - **Files**: `src/soc_agent/report.py`, `tests/test_report.py`
  - **Content**: Format classification verdict, confidence score, SHAP attribution, ATT&CK techniques, and raw evidence links.
  - **Verification**: Test outputs validate against `TriageReport` JSON schema and verify Markdown readability.
  - **Completion Condition**: Generated reports contain clickable evidence references for every conclusion.
  - **Status**: Planned

- [ ] 6.2 Develop Streamlit analyst dashboard and feedback logging mechanism  
  - **Purpose**: Render interactive triage interface and record analyst verdict corrections.
  - **Requirement**: `explainability-reporting` / Analyst Feedback Ingestion and Policy Fine-Tuning
  - **Files**: `app/dashboard.py`, `src/soc_agent/feedback.py`
  - **Content**: Build interactive Streamlit queue view showing SHAP waterfall charts, escalation alerts, and analyst feedback submission forms.
  - **Verification**: Launch dashboard locally and submit feedback record to verify disk persistence.
  - **Completion Condition**: Feedback entries successfully saved with timestamp and analyst rationale.
  - **Status**: Planned

## Workflow follow-up

- Change remains active during the proposal refactor phase (`refactor-ai-soc-agent-proposal`).
- Do not execute `openspec archive` until tasks 1.2 through 6.2 are implemented and empirical evaluations pass.
- Future archive command: `openspec archive refactor-ai-soc-agent-proposal`
