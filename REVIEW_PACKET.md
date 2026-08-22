# Review Packet

## Drug Safety & QC Evidence Mapping Foundation

### Biotech Learnship – Test 1

**Prepared by:** Shravani Jambhulkar  
**Academic Background:** Fourth-Year B.Pharmacy Student  
**Project Area:** Pharmacovigilance, Drug Safety, Laboratory QC and Evidence Validation

---

# 1. Entry Point

This repository contains a research and mini-build project focused on:

- Pharmacovigilance fundamentals
- Drug-safety evidence
- Safety signal identification
- Laboratory Quality Control (QC)
- Evidence validation
- Data integrity
- Evidence provenance
- Batch/lot traceability
- Structured evidence tracking

The main entry point for the Python mini-build is:

```text
drug_safety_tracker.py
```

The sample evidence dataset is located at:

```text
sample_data/evidence_records.csv
```

The project can be started by running:

```bash
python drug_safety_tracker.py --file sample_data/evidence_records.csv --drug "Drug A"
```

The program loads the evidence records, searches for the selected drug/product, applies available filters, identifies validation status, flags records requiring human review, and produces structured JSON output.

---

# 2. Core Execution Flow

The overall project workflow is:

```text
Drug-Safety / QC Source
        ↓
Evidence Record
        ↓
Evidence Provenance
        ↓
Data Validation
        ↓
Validation Status
        ↓
Safety Observation Review
        ↓
Human Review Flag
        ↓
Structured JSON Output
        ↓
Future AI/DS Processing
```

The Python mini-build follows this simplified execution flow:

```text
Start Program
        ↓
Load CSV Evidence File
        ↓
Check File Exists
        ↓
Check Dataset and Required Data
        ↓
Search by Drug/Product
        ↓
Apply Evidence Type Filter (if selected)
        ↓
Apply Validation Status Filter (if selected)
        ↓
Display Safety Observations
        ↓
Display Evidence Provenance
        ↓
Identify Records Requiring Human Review
        ↓
Count Validation Status Categories
        ↓
Generate Structured JSON Output
        ↓
Display Safety Disclaimer
        ↓
End Program
```

---

# 3. Live/Sample Execution

The project uses a fictional/sample dataset.

No real patient-identifiable information is included.

Example command:

```bash
python drug_safety_tracker.py --file sample_data/evidence_records.csv --drug "Drug A"
```

Example structured output:

```json
{
  "drug_searched": "Drug A",
  "evidence_found": 5,
  "validated": 3,
  "needs_review": 2,
  "safety_signals": 2,
  "evidence_sources": [
    "FAERS",
    "PubMed",
    "Laboratory QC"
  ],
  "human_review_required": true
}
```

The exact numbers and sources depend on the sample dataset and selected filters.

The program clearly states that:

```text
A flagged record requires further human review.

It is not a clinical conclusion and does not prove
that a drug caused an observed event.
```

---

# 4. Repository Components

The repository contains the following major components:

## Research Documentation

```text
README.md
RESEARCH_REPORT.md
DATA_SOURCE_REGISTRY.md
QC_EVIDENCE_MAP.md
EVIDENCE_VALIDATION_MODEL.md
LEARNING_NOTES.md
REVIEW_PACKET.md
```

## Python Mini-Build

```text
drug_safety_tracker.py
```

## Sample Data

```text
sample_data/
    evidence_records.csv
```

## Testing

```text
tests/
    TEST_RESULTS.md
```

## Visual Evidence

```text
screenshots/
```

---

# 5. What Was Built

The following mini-build was developed as part of this project.

## Drug Safety Evidence Tracker

The Python program allows the user to:

1. Load a CSV evidence file.
2. Search by drug/product.
3. Filter by evidence type.
4. Filter by validation status.
5. Display safety observations.
6. Display evidence provenance.
7. Identify records requiring human review.
8. Produce structured JSON output.

The program is designed as a simple educational evidence-tracking tool.

It does not:

- Diagnose patients.
- Recommend treatment.
- Make clinical decisions.
- Establish causality.
- Replace pharmacovigilance professionals.
- Replace laboratory investigations.

---

# 6. What Changed During Development

The project was developed step by step.

The following components were created and integrated:

### Phase 1 — Learning

Learned and documented:

- Pharmacovigilance.
- Adverse event vs adverse drug reaction.
- Seriousness vs severity.
- Expected vs unexpected reactions.
- Safety signals.
- Signal detection.
- Signal validation.
- Basic causality assessment.
- Post-marketing surveillance.
- Medication-error reporting.
- Drug-quality complaints.
- QA vs QC.
- Laboratory QC principles.
- Batch/lot traceability.
- Data integrity.
- Evidence provenance.

### Phase 2 — Research

Created a structured registry of credible public drug-safety and pharmaceutical-quality sources.

Sources included examples such as:

- FDA FAERS.
- OpenFDA.
- DailyMed.
- FDA Drug Safety Communications.
- WHO pharmacovigilance resources.
- PubMed.
- ClinicalTrials.gov.
- EMA safety information.
- ICH guidelines.

Each source was assessed for:

- Purpose.
- Type of information.
- Accessibility.
- Evidence quality.
- Limitations.
- Important terminology.
- Potential project use.
- Suitability for AI/Data Science processing.

### Phase 3 — Evidence Map

Created a structured workflow:

```text
Observation
        ↓
Report
        ↓
Data Validation
        ↓
Signal Detection
        ↓
Evidence Review
        ↓
QC/Laboratory Evidence
        ↓
Scientific Assessment
        ↓
Human Review
        ↓
Documentation
        ↓
Follow-up
```

### Phase 4 — QC Component

Added laboratory QC evidence concepts including:

- Sample identification.
- Sample integrity.
- Instrument calibration.
- Reference standards.
- Controls.
- Replicates.
- Measurement uncertainty.
- OOS results.
- OOT results.
- Deviations.
- Equipment maintenance.
- Data integrity.
- Audit trails.
- Result review.
- Batch/lot traceability.

### Phase 5 — Evidence Validation Model

Created a model to classify records as:

- Validated.
- Needs Review.
- Incomplete.
- Unverified.
- Conflicting.

The model also includes a human-review flag.

### Phase 6 — Python Mini-Build

Developed the Drug Safety Evidence Tracker using:

- Python.
- CSV structured data.
- JSON output.
- Command-line input.

### Phase 7 — Testing

Tested the program with:

- Normal cases.
- Invalid-input cases.
- Evidence-validation edge cases.

---

# 7. Failure Cases Tested

The following failure cases were considered and tested.

## Missing Drug Name

### Expected Behaviour

The program should not silently perform an incorrect search.

It should provide a clear error or request valid input.

### Scientific Principle

A missing drug/product identifier makes evidence linking unreliable.

---

## Unknown Drug

### Expected Behaviour

The program should display:

```text
No evidence found for the selected drug/product.
```

It should not create a false safety conclusion.

---

## Missing CSV File

### Expected Behaviour

The program should clearly report that the file cannot be found.

Example:

```text
ERROR: CSV file not found.
```

This issue was encountered during development and corrected by checking the correct file location and path.

---

## Incomplete Evidence Record

### Expected Behaviour

Records with missing important information should be identified as:

```text
Incomplete
```

or:

```text
Needs Review
```

depending on the missing information and project logic.

---

## Invalid Validation Status

### Expected Behaviour

An invalid validation status should be flagged.

The accepted project categories are:

- Validated.
- Needs Review.
- Incomplete.
- Unverified.
- Conflicting.

---

## Duplicate Evidence ID

### Expected Behaviour

The system should identify the duplicate and flag it for review.

The program should not automatically delete evidence because records may require investigation before they are classified as true duplicates.

---

## Conflicting Evidence

### Expected Behaviour

Conflicting records should not be automatically resolved by the program.

They should be:

```text
Flagged
        ↓
Preserved
        ↓
Reviewed by a Human
```

---

## Empty Dataset

### Expected Behaviour

The program should display a clear message indicating that no evidence records are available.

It should not produce misleading summary statistics.

---

# 8. Test Evidence

Testing included the following categories.

## Normal Test Cases

1. Search for a valid drug/product.
2. Filter evidence by evidence type.
3. Filter evidence by validation status.
4. Display safety observations.
5. Generate structured JSON output.

## Invalid-Input Test Cases

1. Missing drug name.
2. Unknown drug.
3. Missing CSV file.
4. Invalid validation status.

## Evidence-Validation Edge Cases

1. Duplicate evidence ID.
2. Conflicting evidence.
3. Incomplete evidence record.
4. Empty dataset.

Detailed test information is documented in:

```text
tests/TEST_RESULTS.md
```

Screenshots of successful execution and testing are available in:

```text
screenshots/
```

---

# 9. Scientific Safeguards Used

The project was designed around the following mandatory distinctions:

```text
Reported Adverse Event
≠
Confirmed Adverse Drug Reaction
```

A reported event occurring after drug exposure does not automatically prove that the medicine caused the event.

---

```text
Safety Signal
≠
Proof of Causality
```

A safety signal is information that may indicate a possible association and requires further assessment.

---

```text
Laboratory/QC Finding
≠
Automatic Proof of Patient-Level Causality
```

A QC finding may provide important supporting evidence but requires scientific interpretation.

---

```text
Human Review Flag
≠
Clinical Conclusion
```

A flag only indicates that further review is required.

---

# 10. Known Limitations

This project is a research and educational foundation.

The current version has several limitations.

## Simplified Dataset

The sample evidence records are fictional and intended only to demonstrate the structure of an evidence-tracking system.

They are not real clinical or regulatory evidence.

---

## No Automatic Causality Assessment

The system does not determine whether a drug caused an adverse event.

Causality assessment requires appropriate scientific and professional evaluation.

---

## No Real-Time Data Integration

The current version does not automatically connect to live systems such as:

- FAERS.
- OpenFDA.
- DailyMed.
- PubMed.
- EMA databases.
- Laboratory Information Management Systems.

Future development could add carefully validated data integration.

---

## Simplified Validation Categories

The categories:

- Validated.
- Needs Review.
- Incomplete.
- Unverified.
- Conflicting.

are designed for this project.

A real-world regulated system may require more detailed procedures, controlled terminology, audit trails, permissions, and validation.

---

## Limited Duplicate Detection

The current project demonstrates duplicate-ID checking conceptually.

More advanced duplicate detection may compare:

- Drug/product.
- Observation.
- Date.
- Source.
- Batch/lot.
- Other relevant non-identifiable information.

---

## No Advanced Signal Detection Algorithm

The project does not perform advanced statistical signal detection.

Future AI/Data Science teams may add appropriate statistical methods while maintaining scientific and regulatory safeguards.

---

# 11. Next Recommended Work

Future work may include the following.

## 1. Standardized Terminology

Add standardized terminology and controlled vocabularies where appropriate.

For example:

```text
Medical Terminology
        ↓
Standardized Evidence Categories
        ↓
Improved Data Consistency
```

---

## 2. Improved Duplicate Detection

Develop methods to identify possible duplicate reports without incorrectly merging independent evidence.

---

## 3. Evidence Scoring

Develop a transparent evidence-quality model that considers:

- Source.
- Completeness.
- Documentation.
- Provenance.
- Limitations.

Any scoring model should remain explainable and should not replace human judgement.

---

## 4. Source Integration

Future versions may integrate selected public sources through approved access methods.

Possible workflow:

```text
Public Source
        ↓
Data Extraction
        ↓
Source Validation
        ↓
Standardization
        ↓
Evidence Record
        ↓
Human Review
```

---

## 5. Laboratory Data Integration

Future versions could connect structured laboratory information such as:

- Sample IDs.
- Batch/lot information.
- Test methods.
- Calibration status.
- QC results.
- Deviations.
- OOS/OOT investigations.

---

## 6. Improved User Interface

The command-line application could be developed into:

- Web application.
- Dashboard.
- Database application.
- Internal evidence-review system.

---

## 7. Audit Trail

Future systems should maintain appropriate audit information showing:

```text
Who changed a record?
What was changed?
When was it changed?
Why was it changed?
```

This would improve traceability and data integrity.

---

# 12. Handover Information

A future contributor should begin by reading:

```text
1. README.md
2. RESEARCH_REPORT.md
3. DATA_SOURCE_REGISTRY.md
4. QC_EVIDENCE_MAP.md
5. EVIDENCE_VALIDATION_MODEL.md
6. LEARNING_NOTES.md
7. REVIEW_PACKET.md
```

Then review:

```text
sample_data/evidence_records.csv
```

After understanding the data structure, review:

```text
drug_safety_tracker.py
```

Finally, review:

```text
tests/TEST_RESULTS.md
```

This order provides the scientific background before moving to the technical implementation.

---

# 13. Core Handover Model

The project can be understood through the following complete model:

```text
PHARMACY / DRUG-SAFETY KNOWLEDGE
                ↓
         CREDIBLE SOURCES
                ↓
         STRUCTURED EVIDENCE
                ↓
      PROVENANCE + TRACEABILITY
                ↓
        DATA QUALITY CHECKS
                ↓
         VALIDATION STATUS
                ↓
       SAFETY/QC OBSERVATION
                ↓
        HUMAN REVIEW FLAG
                ↓
       DOCUMENTATION + REVIEW
                ↓
       STRUCTURED JSON OUTPUT
                ↓
      FUTURE AI/DS/SOFTWARE USE
```

---

# 14. Final Project Summary

This project established a first-layer foundation for organizing drug-safety and pharmaceutical-quality evidence.

The completed work includes:

- Pharmacovigilance learning.
- Drug-safety research.
- Public source registry.
- Drug-safety evidence map.
- Laboratory QC evidence framework.
- Evidence-validation model.
- Hypothetical structured evidence records.
- Python-based Drug Safety Evidence Tracker.
- Sample CSV dataset.
- JSON output.
- Test cases and results.
- Screenshots.
- Documentation.
- Repository handover information.

The project is not intended to be a finished clinical or regulatory system.

Its purpose is to provide a reusable and structured foundation for future:

```text
Pharmacy Teams
        +
AI/Data Science Teams
        +
Software Teams
        +
Laboratory Teams
        +
QA/QC Teams
```

The final guiding principle of the project is:

```text
Observe
        ↓
Record
        ↓
Validate
        ↓
Trace
        ↓
Review
        ↓
Document
        ↓
Do Not Overinterpret
```

The system is designed to support trustworthy evidence handling while maintaining the most important scientific safeguards:

```text
Reported Event
≠
Confirmed Drug Causality
```

```text
Safety Signal
≠
Proof of Causality
```

```text
Flagged Record
≠
Clinical Conclusion
```

---

# 15. Final Reviewer Checklist

A reviewer can use the following checklist:

- [ ] README explains how to run the project.
- [ ] Research report explains the scientific background.
- [ ] Data source registry documents credible information sources.
- [ ] QC evidence map explains the laboratory QC component.
- [ ] Evidence validation model defines validation categories.
- [ ] Sample dataset contains fictional/non-identifiable records.
- [ ] Python tracker loads and processes the CSV file.
- [ ] Search functionality works.
- [ ] Evidence type filtering works.
- [ ] Validation status filtering works.
- [ ] Safety observations are displayed.
- [ ] Evidence provenance is displayed.
- [ ] Human-review records are flagged.
- [ ] Structured JSON output is generated.
- [ ] Normal test cases are documented.
- [ ] Invalid-input cases are documented.
- [ ] Edge cases are documented.
- [ ] Screenshots provide execution evidence.
- [ ] Known limitations are documented.
- [ ] Future recommended work is included.

---

# Conclusion

This review packet provides a summary of the completed Drug Safety & QC Evidence Mapping Foundation project, including its execution flow, mini-build, testing, failure handling, limitations, and future development possibilities.

The main achievement of this project is the creation of a structured evidence foundation that connects:

```text
Drug/Product
        ↓
Safety Observation
        ↓
Evidence
        ↓
QC/Provenance Information
        ↓
Validation Status
        ↓
Human Review
        ↓
Structured Output
```

The project demonstrates how pharmacy knowledge can be combined with research discipline, quality-control thinking, data integrity, evidence validation, and basic programming to create a foundation that future teams can continue to develop.