# Spec Delta: explainability-reporting

## Purpose

Generates transparent, verifiable triage reports with TreeSHAP local feature attribution and provides mechanisms for analyst feedback ingestion to mitigate automation complacency.

## ADDED Requirements

### Requirement: Local Feature Attribution via TreeSHAP
The system SHALL compute local feature attribution values using TreeSHAP for each evaluated incident, ranking and presenting the top contributing telemetry features.

#### Scenario: SHAP feature ranking generation
- **WHEN** an incident is triaged by the GBDT classifier
- **THEN** the explainability engine computes SHAP values and outputs the top-5 influential features with positive and negative weights

#### Scenario: Visual feature attribution rendering
- **WHEN** a report is rendered in the interactive analyst dashboard
- **THEN** the system visualizes the feature contribution waterfall diagram showing baseline shift

### Requirement: Structured Audit Evidence Report Generation
The system SHALL generate comprehensive incident reports in both structured JSON and formatted Markdown formats, embedding verifiable citations to all evidence sources.

#### Scenario: Markdown and JSON report delivery
- **WHEN** decision fusion and playbook mapping conclude for an incident
- **THEN** the system outputs a TriageReport containing classification verdict, confidence, ATT&CK techniques, and evidence links

#### Scenario: Verifiable source citation check
- **WHEN** an analyst inspects an individual claim or conclusion within the incident report
- **THEN** each claim displays a clickable reference pointing to the exact underlying log record or knowledge article

### Requirement: Analyst Feedback Ingestion and Policy Fine-Tuning
The system SHALL record corrections, rating overrides, and notes submitted by human analysts, updating historical case repositories for future retrieval.

#### Scenario: Analyst verdict correction logging
- **WHEN** an analyst overrides an automated triage verdict from False Positive to True Positive
- **THEN** the system persists the corrected label, analyst remarks, and timestamp into the feedback audit store
