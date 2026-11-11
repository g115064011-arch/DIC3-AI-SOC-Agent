# Spec Delta: incident-triage

## Purpose

Enables automated ingestion, parsing, and calibrated multi-class severity classification of security incidents across True Positive, Benign Positive, and False Positive categories.

## ADDED Requirements

### Requirement: Incident Ingestion and Schema Validation
The system SHALL ingest structured incident requests containing an incident identifier or a batch of security alerts, validating that all required entity attributes adhere to the canonical schema.

#### Scenario: Valid incident payload ingestion
- **WHEN** a valid incident request with non-empty alert records is submitted
- **THEN** the system parses the payload into a validated TriageRequest object with status READY

#### Scenario: Malformed incident payload rejection
- **WHEN** an incident payload is submitted with missing identifier or unparseable alert records
- **THEN** the system rejects the input and returns a structured validation error response

### Requirement: Multi-Class Incident Triage Prediction
The system SHALL compute calibrated prediction probabilities across True Positive (TP), Benign Positive (BP), and False Positive (FP) classes using a trained Gradient Boosted Decision Tree model.

#### Scenario: Successful triage inference
- **WHEN** preprocessed incident feature vectors are passed to the analytics model
- **THEN** the model returns a probability distribution vector (p_TP, p_BP, p_FP) that sums to 1.0

#### Scenario: Missing feature imputation
- **WHEN** certain optional telemetry features are null or missing in the incident
- **THEN** the model imputes missing values using pre-computed training medians and executes inference without failure

