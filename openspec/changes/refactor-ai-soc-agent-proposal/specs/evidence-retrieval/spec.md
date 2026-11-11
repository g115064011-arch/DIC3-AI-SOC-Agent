# Spec Delta: evidence-retrieval

## Purpose

Provides budget-controlled, multi-hop forensic evidence gathering across relational telemetry tables and incident evidence stores under the Assume Breach operational doctrine.

## ADDED Requirements

### Requirement: Multi-Hop Evidence Acquisition
The system SHALL retrieve contextual forensic evidence for accounts, hosts, and network entities associated with the incident from relational log stores using read-only queries.

#### Scenario: Successful entity context retrieval
- **WHEN** the planner requests process and authentication telemetry for an entity
- **THEN** the retrieval engine executes read-only queries and returns records with explicit source metadata

#### Scenario: SQL injection prevention
- **WHEN** a natural language query attempts to execute non-read-only commands or unauthorized mutations
- **THEN** the retrieval engine aborts query execution and raises a security constraint violation

### Requirement: Query Budget and Termination Control
The system MUST track total tool invocations and token consumption against configurable budget limits, terminating multi-hop gathering when the budget limit is reached.

#### Scenario: Budget boundary termination
- **WHEN** the number of tool execution steps reaches the predefined maximum budget B
- **THEN** the planner halts further queries, flags the state as budget-exhausted, and proceeds to analytics

#### Scenario: Early termination upon sufficiency
- **WHEN** the evidence gathering satisfies sufficiency criteria before exhausting budget B
- **THEN** the planner stops iterative retrieval immediately and transitions to feature extraction

### Requirement: Incomplete Log Detection under Assume Breach
The system SHALL evaluate whether an empty query result stems from absence of malicious activity or from telemetry log disruption, refusing to treat empty queries as benign proof.

#### Scenario: Log discontinuity detected
- **WHEN** a log query for a specific time window returns empty records but adjacent heartbeat telemetry is missing
- **THEN** the system marks the incident evidence state as INSUFFICIENT_EVIDENCE rather than benign

