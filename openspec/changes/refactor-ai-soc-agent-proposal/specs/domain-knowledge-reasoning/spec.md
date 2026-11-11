# Spec Delta: domain-knowledge-reasoning

## Purpose

Integrates structured cybersecurity domain knowledge from MITRE ATT&CK and NIST SP 800-61 Rev. 3 to evaluate attack chain progression and prescribe defensive mitigation actions.

## ADDED Requirements

### Requirement: MITRE ATT&CK Semantic Retrieval
The system SHALL retrieve relevant MITRE ATT&CK tactics, techniques, sub-techniques, and mitigation guidelines from a vectorized STIX knowledge base using semantic search.

#### Scenario: Technique matching from alert telemetry
- **WHEN** an incident contains alerts with MITRE technique identifiers or adversarial procedure descriptions
- **THEN** the retrieval component returns matching ATT&CK technique entities and defense mitigation records

#### Scenario: Unmapped technique fallback
- **WHEN** incoming alert data lacks explicit ATT&CK technique tags
- **THEN** the system generates semantic embedding queries to retrieve the top-3 closest candidate techniques

### Requirement: Cyber Kill Chain Tactical Progression Mapping
The system SHALL assess the tactical progression of an incident across the unified Kill Chain, identifying whether adversarial actions have advanced to late-stage impact phases.

#### Scenario: Late stage tactic detection
- **WHEN** an incident contains confirmed evidence matching Exfiltration or Impact tactics
- **THEN** the reasoning engine raises a HIGH_RISK_STAGE flag and mandates priority handling

#### Scenario: Lateral movement correlation
- **WHEN** an incident links Credential Access on host A with subsequent Remote Services on host B
- **THEN** the engine annotates the incident with active Lateral Movement multi-stage progression

### Requirement: Incident Response Playbook Alignment
The system SHALL map the identified attack techniques and incident severity to recommended response actions compliant with NIST SP 800-61 Rev. 3 response guidelines.

#### Scenario: Actionable response recommendation
- **WHEN** an incident is triaged as a True Positive with account compromise techniques
- **THEN** the system outputs structured containment steps including account session revocation and host isolation

