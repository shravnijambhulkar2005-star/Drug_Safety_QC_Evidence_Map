# Drug Safety Evidence Integration — Architecture

## 1. Purpose

The Drug Safety Evidence Integration capability converts structured safety evidence from multiple source representations into a normalized, validated and traceable output.

The capability is designed to support deterministic evidence processing while preserving source provenance, duplicate relationships, conflict information and human-review requirements.

It does not perform clinical diagnosis, automatic causality determination or regulatory decision-making.

---

## 2. High-Level Architecture

The implemented processing flow is:

Multiple Evidence Sources
        |
        v
Multi-Source Integration
        |
        v
Evidence Normalization
        |
        v
Drug/Product Matching
        |
        v
Evidence Validation
        |
        +------------------+
        |                  |
        v                  v
Duplicate Detection   Conflict Detection
        |                  |
        +--------+---------+
                 |
                 v
          Human Review Flag
                 |
                 v
       Structured Evidence Output
                 |
                 v
       Downstream Consumption

---

## 3. Main Implementation Components

### 3.1 Main Tracker

Path:

`drug_safety_tracker.py`

Purpose:

Provides the existing Drug Safety/QC evidence tracking capability and serves as part of the foundation for the integrated evidence workflow.

---

### 3.2 Multi-Source Integration

Path:

`integration/`

Purpose:

Handles integration of structured evidence records from multiple source representations and supports conversion into the canonical evidence-processing workflow.

---

### 3.3 Evidence Normalization

Path:

`normalization/`

Purpose:

Normalizes incoming evidence records into a consistent representation while preserving source-related information.

Normalization does not remove the original source identity.

---

### 3.4 Drug/Product Matching

Path:

`matching/`

Purpose:

Performs deterministic drug/product identity matching.

The matching layer is designed to distinguish exact identity from unmatched or ambiguous cases.

Substring similarity must not be treated as confirmed product identity.

---

### 3.5 Evidence Validation

Path:

`validation/`

Purpose:

Performs deterministic structural validation of evidence records.

Validation includes checks such as required fields, accepted values, identifiers and provenance-related requirements.

Validation is a data-quality operation and does not establish clinical validity or causality.

---

### 3.6 Duplicate Detection

Path:

`duplicates/`

Purpose:

Identifies duplicate or potentially duplicate evidence records.

Detected duplicates are retained and represented as relationships rather than silently deleted.

---

### 3.7 Conflict Detection

Path:

`conflicts/`

Purpose:

Identifies materially conflicting evidence observations or states.

Conflicting records remain preserved so that the original evidence remains traceable.

The conflict detector does not select a scientific winner.

---

### 3.8 Human Review

Path:

`review/`

Purpose:

Identifies conditions requiring human review.

Examples include:

- conflicting evidence;
- ambiguous entity matching;
- incomplete evidence;
- incomplete provenance;
- duplicate records requiring confirmation;
- validation conditions requiring review.

A human-review flag is not a clinical conclusion.

---

### 3.9 Canonical Schema

Path:

`schema/`

Purpose:

Provides the schema-related implementation required to represent evidence consistently across the integration workflow.

The canonical model separates evidence observations, validation state, evidence quality and human-review state.

---

### 3.10 Automated Tests

Path:

`tests/`

Purpose:

Contains automated tests covering validation, matching, duplicate detection, conflict detection, human-review behaviour and integration behaviour.

---

## 4. Data Flow

The expected data flow is:

Source Evidence
    ->
Source / Provenance Capture
    ->
Normalization
    ->
Drug/Product Entity Matching
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

Each stage preserves the information required to trace evidence back to its originating source.

---

## 5. Provenance

The system is designed to preserve provenance information associated with evidence records.

Important provenance concepts include:

- source;
- source organisation;
- source identifier;
- evidence identifier;
- transformation/normalization information;
- normalized record;
- validation state.

Provenance preservation is necessary for reproducibility and auditability.

---

## 6. Validation Boundary

Automated validation evaluates structural and data-quality properties.

It does not establish:

- clinical causality;
- medical diagnosis;
- treatment recommendation;
- regulatory approval;
- overall clinical safety.

A validation result must therefore not be interpreted as a clinical conclusion.

---

## 7. Duplicate and Conflict Handling

Duplicate records are not silently deleted.

Conflicting records are not silently merged.

Where a duplicate or conflict is identified, the relevant evidence records remain traceable and the relationship is represented for review.

---

## 8. Human Review Boundary

The system may identify:

`HUMAN_REVIEW_REQUIRED`

It must not convert this state into:

`SAFETY_CONFIRMED`

or:

`CAUSALITY_CONFIRMED`.

Human review remains a separate step from automated validation.

---

## 9. Determinism

The integration capability is intended to provide deterministic processing.

For identical input and identical processing configuration, repeated execution should produce logically equivalent structured output.

A deterministic replay test is included in the project testing workflow.

---

## 10. Testing Architecture

The test structure includes coverage for:

- validation;
- drug/product matching;
- duplicate detection;
- conflict detection;
- human-review logic;
- integration behaviour.

The final test evidence is documented separately in:

`TEST_RESULTS.md`

---

## 11. Authority Boundaries

The capability may:

- ingest evidence;
- normalize evidence;
- validate evidence structure;
- identify duplicates;
- identify conflicts;
- identify ambiguous product matches;
- flag human review;
- preserve provenance;
- produce structured output.

The capability may not:

- establish medical causality automatically;
- make clinical decisions;
- approve or reject medicines;
- replace pharmacovigilance professionals;
- make regulatory decisions.

---

## 12. Known Limitations

The implementation is intended as a deterministic evidence-processing capability.

Automated structural validation does not scientifically validate the underlying evidence.

Conflict detection identifies conflicts according to implemented deterministic rules and does not determine which scientific interpretation is correct.

Human-review flags indicate that additional review is required and do not represent clinical conclusions.

Live integration with the wider BHIV Biotech runtime is separate from isolated capability testing and must not be claimed until independently tested.