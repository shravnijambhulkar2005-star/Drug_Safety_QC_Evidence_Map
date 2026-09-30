# CODE PACKET INDEX

## 1. Purpose

This document identifies the critical implementation files included in the evidence packet for the BHIV Biotech Drug Safety Evidence Integration capability.

The code packet contains the implementation components required for canonical evidence processing, normalization, validation, matching, duplicate detection, conflict detection, human review, integration orchestration, and structured output.

## 2. Code Packet Location

```text
/evidence_packet/code_packet/
```

## 3. Critical Code Index

| Path                                                  | Purpose                                                                                  | Entry Point                  | Dependency / Relationship                                                                       | Review Relevance                                             |
| ----------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| `evidence_packet/code_packet/evidence_integration.py` | Orchestrates the integrated evidence-processing flow and structured output generation    | Integration execution flow   | Coordinates normalization, validation, matching, duplicate/conflict checks, and review handling | Primary integration entry point                              |
| `evidence_packet/code_packet/normalize_evidence.py`   | Normalizes source evidence into the canonical evidence structure                         | Normalization function       | Uses canonical schema concepts and preserves provenance                                         | Verifies source-to-canonical transformation                  |
| `evidence_packet/code_packet/validate_evidence.py`    | Performs structural and evidence-quality validation                                      | Validation function          | Applies required-field, type, status, and provenance rules                                      | Verifies validation behavior and TEST-01 to TEST-12 coverage |
| `evidence_packet/code_packet/detect_duplicates.py`    | Detects duplicate evidence relationships while retaining original records                | Duplicate detection function | Operates on normalized evidence records                                                         | Verifies duplicate preservation and detection                |
| `evidence_packet/code_packet/detect_conflicts.py`     | Detects potentially conflicting evidence records without silently deleting either record | Conflict detection function  | Operates on normalized evidence records                                                         | Verifies conflict preservation and review triggering         |
| `evidence_packet/code_packet/drug_matcher.py`         | Performs deterministic drug/product identity matching                                    | Drug matching function       | Uses normalized product identities                                                              | Verifies exact, unmatched, and ambiguous matching behavior   |
| `evidence_packet/code_packet/human_review.py`         | Determines when records require human review                                             | Human-review function        | Receives uncertainty, conflict, ambiguity, or validation conditions                             | Verifies human-review safeguards                             |
| `evidence_packet/code_packet/canonical_schema.json`   | Defines the versioned canonical evidence structure                                       | Schema definition            | Referenced by evidence-processing requirements                                                  | Verifies schema version `1.0.0` and required fields          |

## 4. Primary Execution Relationship

```text
Source Evidence
      ↓
Evidence Normalization
      ↓
Drug/Product Matching
      ↓
Validation
      ↓
Duplicate Detection
      ↓
Conflict Detection
      ↓
Human Review Flag
      ↓
Structured Evidence Output
```

## 5. Review Notes

* Original evidence and provenance are preserved during processing.
* Duplicate and conflicting records are not silently deleted.
* Ambiguous or uncertain cases can be flagged for human review.
* The system does not automatically determine clinical causality.
* The system does not make clinical or regulatory decisions.
* The code packet represents the local implementation reviewed for this test; it does not by itself constitute production deployment evidence.
