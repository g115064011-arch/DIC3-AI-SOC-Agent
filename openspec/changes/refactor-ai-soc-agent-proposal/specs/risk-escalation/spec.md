# Spec Delta: risk-escalation

## Purpose

Enforces safety-first decision synthesis across machine learning probabilities and agentic reasoning, executing automated escalation to human analysts when uncertainty or risk is detected.

## ADDED Requirements

### Requirement: Evidence Fusion and Multi-Modal Decision Synthesis
The system SHALL combine machine learning classification probabilities and LLM reasoning confidence into a unified final prediction score using calibrated decision weights.

#### Scenario: Weighted score calculation
- **WHEN** model probabilities p and LLM categorical confidence q are supplied to the fusion engine
- **THEN** the engine calculates synthesized score vector s = w_ml * p + w_llm * q and assigns the argmax class

### Requirement: Automated Human-in-the-Loop Escalation Policy
The system MUST escalate an incident to a human security analyst whenever prediction confidence falls below threshold tau, high-risk rules are active, or evidence is insufficient.

#### Scenario: Low confidence escalation
- **WHEN** the synthesized classification confidence score falls below calibrated threshold tau
- **THEN** the system sets triage status to NEEDS_HUMAN_REVIEW and documents the low confidence margin

#### Scenario: Insufficient evidence escalation
- **WHEN** the planner completes multi-hop retrieval with budget exhausted while critical evidence remains missing
- **THEN** the system sets triage status to NEEDS_HUMAN_REVIEW and specifies the missing telemetry scope

### Requirement: Conflict Detection and Dispute Annotation
The system SHALL compare the predicted class from the machine learning model against the conclusion of the LLM reasoner, flagging any discrepancy as a priority dispute for analyst review.

#### Scenario: Conflicting classification detection
- **WHEN** the ML model predicts True Positive while the LLM reasoning agent predicts False Positive
- **THEN** the system flags the incident with CONFLICT status and highlights the exact divergence rationale
