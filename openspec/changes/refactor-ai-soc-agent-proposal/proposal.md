# Proposal: Refactor AI SOC Agent Proposal with OpenSpec

## Why

Modern enterprise Security Operations Centers (SOCs) face acute operational overload, processing tens of thousands of daily alerts where only a tiny fraction represent true attacks [2]. According to the IBM Cost of a Data Breach Report 2026 [14], average breach costs have reached an unprecedented $4.99 million with an average dwell/containment lifecycle of 247 days. Meanwhile, Mandiant M-Trends 2026 [15] highlights a global median attacker dwell time of 14 days (up to 122 days for cyber espionage), and Taiwan National Security Bureau [23] telemetry notes 2.63 million daily cyber probes on critical infrastructure. 

Existing machine learning alert triage systems [1][7] provide high throughput but lack Kill Chain context. Conversely, recent empirical studies reveal that mainstream tool-using LLM agents miss at least 40.4% of attack-related alerts due to premature termination upon empty query results [3], and achieve an investigation reward of only 0.606 on ExCyTIn-Bench [4]. Furthermore, excessive opaque automation induces severe analyst automation complacency [12]. 

To bridge this research gap, this change establishes a formal, verifiable specification framework for an **AI SOC Analyst Agent** that combines machine learning probability estimation, MITRE ATT&CK domain reasoning, TreeSHAP explainability, and calibrated human-in-the-loop escalation.

## What Changes

This change transforms the capstone design into an OpenSpec specification-driven development workflow, introducing five core capabilities:
- **`incident-triage`**: Ingestion, schema validation, and multi-class probability prediction (TP / BP / FP) across incident evidence.
- **`evidence-retrieval`**: Budget-constrained, multi-hop investigation across evidence stores and relational SQL logs following Assume Breach principles.
- **`domain-knowledge-reasoning`**: Vectorized MITRE ATT&CK STIX retrieval, NIST SP 800-61 Rev. 3 incident response playbook mapping, and Kill Chain risk evaluation.
- **`risk-escalation`**: Systematic human-in-the-loop escalation triggered by prediction uncertainty, ML-LLM conflicts, evidence insufficiency, or late-stage tactics.
- **`explainability-reporting`**: Local feature attribution via TreeSHAP, full audit evidence chains, structured incident reporting (JSON/Markdown), and analyst feedback ingestion.

## Capabilities

### New Capabilities
- `incident-triage`: Ingestion of structured alert batches and incidents, calibrated multi-class GBDT triage prediction across TP, BP, and FP classes.
- `evidence-retrieval`: Multi-hop evidence acquisition with tool-call budget constraints, relational SQL log exploration, and incomplete log detection under Assume Breach.
- `domain-knowledge-reasoning`: Vector retrieval of MITRE ATT&CK tactics/techniques, Kill Chain progression scoring, and NIST SP 800-61 Rev. 3 playbook recommendation.
- `risk-escalation`: Calibrated safety thresholding, conflict arbitration between ML priors and LLM outputs, and automated escalation to Tier-1/Tier-2 human analysts.
- `explainability-reporting`: Local feature explanation generation via TreeSHAP, transparent citation of telemetry sources, structured incident report formatting, and analyst feedback tracking.

### Modified Capabilities
None. This change initializes the baseline capabilities for the AI SOC Analyst Agent system.

## Impact

- **Architecture**: Enforces the eight-module decomposition (① User/Scenario through ⑧ Output/Interaction) defined in `DESIGN.md`.
- **Codebase**: Creates tracking contracts for data preprocessing pipelines (`experiments/e0_profile_guide.py`), model training scripts, and future `src/soc_agent/` modules.
- **Verification**: Establishes strict behavioral acceptance criteria via Gherkin-style Scenarios and RFC 2119 requirements.
- **Lifecycle**: Establishes active change status during proposal refactor phase; formal archive deferred until full empirical implementation.

