# Drug Safety Evidence Integration Contract

## 1. Purpose

This document defines the interface and authority boundaries of the Drug Safety Evidence Integration capability.

The capability is designed to operate independently before any live attachment to the wider BHIV Biotech runtime.

---

## 2. Integration Flow

The intended evidence flow is:

Source Evidence
    ->
Ingestion
    ->
Normalization
    ->
Drug/Product Matching
    ->
Validation
    ->
Duplicate Detection
    ->
Conflict Detection
    ->
Human Review Flag
    ->
Structured Output

---

## 3. Inputs

The capability accepts structured evidence records from supported source representations.

Input records should provide, where applicable:

- Evidence ID
- Source
- Source Organisation
- Evidence Type
- Drug/Product Identifier
- Observation
- Date
- Population/Context
- Measurement/Result
- Supporting Documentation
- Evidence Provenance
- Evidence Quality
- Validation Status
- Limitations
- Reviewer Action
- Human Review Flag

---

## 4. Source and Provenance Requirements

Each evidence record should retain enough information to identify its origin.

Important provenance information includes:

- original source
- source organisation
- source identifier
- original evidence identifier
- ingestion information
- transformation or normalization information
- normalized record

Normalization must not silently remove the source identity.

---

## 5. Normalized Output

The normalized evidence representation should preserve the distinction between:

### Observation

What the source actually reports.

### Interpretation

A derived interpretation of the observation, where applicable.

### Evidence Quality

The quality or completeness assessment of the evidence record.

### Validation State

The result of structural/data-quality validation.

### Human Review State

Whether additional human review is required.

These states must not be treated as interchangeable.

---

## 6. Drug/Product Matching

The matching layer uses deterministic matching rules.

The implementation must distinguish:

- exact matches
- normalized exact matches
- unmatched records
- ambiguous matches

A substring relationship must not automatically establish product identity.

For example:

`Drug A`

must not silently become:

`Drug AB`

simply because one string contains another.

Ambiguous or unmatched cases may require human review.

---

## 7. Duplicate Handling

Duplicate detection may identify:

- duplicate Evidence IDs
- same source plus source identifier
- equivalent evidence content where applicable
- duplicate records produced through multi-source ingestion

Duplicate records must not be silently deleted.

The relationship between records should remain traceable.

---

## 8. Conflict Handling

The capability may identify materially different observations or states.

When a conflict is identified:

- both evidence records remain preserved
- relevant evidence identifiers remain available
- source information remains available
- the conflict relationship is recorded
- human review may be required

The system does not automatically determine the scientific winner.

---

## 9. Validation

Validation evaluates data structure and quality conditions.

Examples include:

- missing required fields
- invalid evidence type
- invalid validation status
- incomplete provenance
- invalid identifiers
- duplicate identifiers
- malformed records
- empty datasets

Validation does not establish clinical causality or medical safety.

---

## 10. Human Review

The system may generate:

`HUMAN_REVIEW_REQUIRED`

Examples include:

- conflicting evidence
- ambiguous drug/product match
- incomplete provenance
- incomplete evidence
- duplicate requiring confirmation
- invalid or uncertain source information

Human review remains separate from automated validation.

---

## 11. Outputs

The capability can produce structured machine-readable output containing, as applicable:

- query
- evidence summary
- normalized evidence records
- validation states
- duplicate relationships
- conflict relationships
- human-review flags
- provenance information

The output schema is versioned/documented separately as applicable.

---

## 12. Dependencies

The capability depends on:

- Python runtime
- project Python modules
- project datasets
- project test suite
- supported structured evidence inputs

External sources are not assumed to be live dependencies unless explicitly configured and documented.

---

## 13. Reproducibility

Identical input and identical processing configuration should produce logically equivalent structured output.

The project includes deterministic replay testing to verify this behaviour.

---

## 14. Authority Boundaries

The capability may:

- ingest evidence
- normalize evidence
- validate structure
- identify duplicates
- identify conflicts
- identify ambiguous entity matches
- flag human review
- preserve provenance
- produce structured output

The capability may not:

- establish medical causality automatically
- diagnose patients
- make clinical treatment decisions
- approve or reject medicines
- replace pharmacovigilance professionals
- make regulatory decisions

---

## 15. Live Integration Status

The capability is designed to be independently executable and testable before live integration.

This repository should not claim live BHIV Biotech runtime integration unless that integration has been explicitly attached and tested.

The current implementation therefore treats isolated execution, reproducibility and evidence traceability as the basis for integration readiness.

---

## 16. Integration Verification

Before live integration, another developer should be able to:

1. Execute the documented entry point.
2. Provide known evidence input.
3. Obtain normalized structured output.
4. Trace records to their source.
5. Reproduce validation results.
6. Identify duplicates.
7. Identify conflicts.
8. Identify human-review requirements.
9. Consume the documented output schema.

---

## 17. Known Limitations

The integration contract describes the capability boundary and does not by itself prove live runtime integration.

Structural validation does not scientifically validate source evidence.

Human-review flags indicate review requirements and are not clinical conclusions.

Conflict detection does not resolve causality or determine which evidence is scientifically correct.