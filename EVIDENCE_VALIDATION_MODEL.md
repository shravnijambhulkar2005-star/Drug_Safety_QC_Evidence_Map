# Evidence Validation Model

## Drug Safety & QC Evidence Mapping Foundation

### Biotech Learnship – Test 1

**Prepared by:** Shravani Jambhulkar  
**Academic Background:** Fourth-Year B.Pharmacy Student  
**Project Area:** Pharmacovigilance, Drug Safety, Laboratory QC and Evidence Validation

---

# 1. Purpose of This Document

This document describes a proposed **Evidence Validation Model** for organizing and reviewing drug-safety, pharmacovigilance, laboratory QC, and pharmaceutical-quality evidence.

The purpose of this model is to help future pharmacy, AI/Data Science, software, laboratory, and QA/QC teams distinguish between:

- Validated evidence.
- Incomplete evidence.
- Unverified reports.
- Conflicting evidence.
- Evidence requiring human review.
- Potentially important safety signals.

The model is intended to organize evidence in a structured and traceable manner.

It does not diagnose patients, recommend treatment, make clinical decisions, or independently establish causality.

The main principle is:

```text
Evidence Record
        ↓
Source Verification
        ↓
Completeness Check
        ↓
Provenance Check
        ↓
Consistency Check
        ↓
Quality Review
        ↓
Validation Status
        ↓
Human Review if Required
```

---

# 2. Core Scientific Principles

The evidence-validation system must avoid making unsupported conclusions.

The following distinctions are mandatory:

```text
Reported Adverse Event
≠
Confirmed Adverse Drug Reaction
```

A reported adverse event means that an event occurred after or during drug exposure. It does not automatically prove that the drug caused the event.

Similarly:

```text
Safety Signal
≠
Proof of Causality
```

A safety signal is information that may suggest a possible association and requires further assessment.

Also:

```text
QC Finding
≠
Automatic Proof of Patient-Level Causality
```

A laboratory or product-quality finding may provide important supporting evidence, but it must be scientifically assessed with other available information.

Finally:

```text
Human Review Flag
≠
Clinical Conclusion
```

A record requiring human review simply indicates that further assessment is needed.

---

# 3. What Is an Evidence Record?

An evidence record is a structured representation of information relevant to a drug-safety, quality, or laboratory investigation.

A record may come from:

- Pharmacovigilance reports.
- Regulatory sources.
- Scientific literature.
- Clinical studies.
- Drug labeling.
- Laboratory QC records.
- Product-quality complaints.
- Safety communications.

Each record should preserve information about where the evidence came from and how it was assessed.

A basic evidence structure is:

```text
Evidence ID
        ↓
Source
        ↓
Evidence Type
        ↓
Drug/Product Identifier
        ↓
Observation
        ↓
Supporting Documentation
        ↓
Evidence Provenance
        ↓
Evidence Quality
        ↓
Validation Status
        ↓
Limitations
        ↓
Reviewer Action
```

---

# 4. Objectives of the Evidence Validation Model

The model aims to answer the following questions:

1. Is the evidence source identified?
2. Is the drug or product clearly identified?
3. Is the observation clearly recorded?
4. Is the evidence sufficiently complete?
5. Is supporting documentation available?
6. Can the evidence provenance be traced?
7. Are there missing or conflicting data?
8. Does the record require human review?
9. Can the record be used as validated supporting evidence?
10. What limitations must remain attached to the record?

The system should not automatically decide whether a drug caused an event.

Its purpose is:

```text
Organize
+
Check
+
Classify
+
Flag
+
Document
```

rather than:

```text
Diagnose
or
Prove Causality
```

---

# 5. Required Evidence Fields

Each evidence record should contain the following fields where applicable.

| Field | Purpose |
|---|---|
| Evidence ID | Unique identifier for the record |
| Source | Origin of the evidence |
| Source Organisation | Organisation responsible for the source |
| Evidence Type | Type of evidence |
| Drug/Product Identifier | Identifies the relevant product |
| Observation | Safety, QC, or other observation |
| Date | Date associated with the evidence |
| Population/Context | Relevant non-identifiable context |
| Measurement/Result | Structured result where applicable |
| Supporting Documentation | Related document or record |
| Evidence Provenance | Information about origin and traceability |
| Evidence Quality | General quality assessment |
| Validation Status | Current validation state |
| Limitations | Known weaknesses or missing information |
| Reviewer Action | Required next action |
| Human Review Flag | Indicates whether expert review is needed |

---

# 6. Proposed Validation Status Categories

The following categories are used in this project.

## 6.1 Validated

A record may be considered **Validated** when the required information has been checked and the evidence is sufficiently complete and traceable for its intended use.

This does not mean that the scientific observation is proven true in every respect.

It means:

```text
Record Validation
≠
Proof of Drug Causality
```

Example:

A QC record has a clear sample ID, batch number, method reference, supporting data, result review, and traceable documentation.

---

## 6.2 Needs Review

This status is used when the record contains potentially important information but requires further human assessment.

Reasons may include:

- Missing supporting information.
- Possible inconsistency.
- Unusual observation.
- Important safety pattern.
- Need for scientific interpretation.

A **Needs Review** status should generate a human-review flag.

---

## 6.3 Incomplete

This status is used when important required information is missing.

Examples:

- Drug/product not clearly identified.
- Missing source.
- Missing observation.
- Missing date where required.
- No supporting documentation.
- Missing batch information for a QC investigation.

An incomplete record should not automatically be treated as reliable evidence.

---

## 6.4 Unverified

This status is used when information has been received or recorded but has not yet been sufficiently checked.

Example:

A public safety report may be recorded as unverified until appropriate review is completed.

---

## 6.5 Conflicting

This status is used when important evidence records appear to provide inconsistent information.

Examples:

- Two records with the same identifier contain different observations.
- A QC result conflicts with another documented result.
- Different sources provide incompatible information about the same evidence item.

Conflicting evidence should not be automatically resolved by the system.

It should be flagged for human review.

---

# 7. Evidence Validation Workflow

The proposed validation workflow is:

```text
Step 1
Evidence Received
        ↓
Step 2
Assign/Check Evidence ID
        ↓
Step 3
Identify Source
        ↓
Step 4
Classify Evidence Type
        ↓
Step 5
Verify Drug/Product Identifier
        ↓
Step 6
Check Observation and Context
        ↓
Step 7
Check Supporting Documentation
        ↓
Step 8
Check Evidence Provenance
        ↓
Step 9
Check Completeness
        ↓
Step 10
Check for Duplicate or Conflicting Records
        ↓
Step 11
Assess Evidence Quality
        ↓
Step 12
Assign Validation Status
        ↓
Step 13
Flag for Human Review if Required
        ↓
Step 14
Document Reviewer Action
        ↓
Step 15
Store Structured Evidence Output
```

---

# 8. Evidence Validation Checks

## 8.1 Source Check

Questions:

- Is the source identified?
- Is the source credible for the type of evidence?
- Is the responsible organisation known?
- Is the source date available where relevant?

Possible failure:

```text
Unknown Source
        ↓
Reduced Traceability
        ↓
Needs Further Review
```

---

## 8.2 Drug/Product Identification Check

Questions:

- Is the product clearly identified?
- Is the product name recorded correctly?
- Is the batch/lot number available when relevant?
- Is there enough information to distinguish the product from another product?

Possible failure:

```text
Unknown Drug/Product
        ↓
Evidence Cannot Be Reliably Linked
```

---

## 8.3 Completeness Check

The record should contain sufficient information for its intended purpose.

The system may check for missing fields such as:

- Evidence ID.
- Source.
- Evidence type.
- Drug/product.
- Observation.
- Validation status.

Depending on the evidence type, additional fields may be required.

For example, QC evidence may require:

- Sample ID.
- Batch/lot information.
- Method information.
- Result documentation.

---

## 8.4 Supporting Documentation Check

The system should identify whether supporting documentation is available.

Examples include:

- Published article.
- Regulatory document.
- Laboratory record.
- Product label.
- Clinical study record.
- Investigation report.

If documentation is unavailable, the record may remain:

```text
Unverified
or
Needs Review
```

depending on the context.

---

## 8.5 Evidence Provenance Check

Evidence provenance answers:

```text
Where did this evidence come from?
```

A strong evidence record should preserve:

- Original source.
- Organisation.
- Source date.
- Access date where relevant.
- Document or record identifier.
- Relevant batch/sample identifiers.
- Evidence extraction method where applicable.

Loss of provenance reduces the ability to verify the evidence.

---

## 8.6 Duplicate Check

Duplicate records can create false impressions about the amount of evidence.

For example:

```text
One Event Reported Multiple Times
≠
Multiple Independent Events
```

Therefore, duplicate evidence IDs or highly similar records should be flagged.

Possible actions include:

- Review.
- Merge after verification.
- Preserve linked records.
- Prevent double counting.

The system should not automatically assume that every similar record is a duplicate.

---

## 8.7 Conflict Check

A conflict may occur when two records contain inconsistent information.

Example:

```text
Evidence Record A
Result: No Quality Issue Found

Evidence Record B
Result: Quality Issue Reported
```

The system should record the conflict.

It should not automatically decide which record is correct.

The correct action is:

```text
Conflicting Evidence
        ↓
Human Review Required
```

---

# 9. Evidence Quality Categories

For this project, evidence quality may be recorded using simple categories.

## High

Generally complete, traceable, and supported by credible documentation.

## Medium

Useful evidence but with some limitations or incomplete contextual information.

## Low

Limited information, uncertain provenance, or important missing data.

## Unknown

Evidence quality cannot yet be assessed.

Important principle:

```text
Evidence Quality Category
=
Organizational Assessment

NOT

Automatic Clinical Proof
```

---

# 10. Human Review Rules

The following situations should trigger a human-review flag:

- Important information is missing.
- Validation status is invalid or unknown.
- Evidence is conflicting.
- Duplicate evidence ID is detected.
- A potentially important safety pattern is identified.
- A QC result is unusual.
- An OOS or OOT investigation is relevant.
- Source provenance is unclear.
- Scientific interpretation is required.

The system output should clearly state:

```text
FLAGGED FOR HUMAN REVIEW

This flag indicates that further assessment is required.
It is not a clinical conclusion and does not establish drug causality.
```

---

# 11. Evidence Validation Decision Model

A simplified decision model is:

```text
Evidence Received
        ↓
Is Evidence ID Present?
        ↓
No → Incomplete / Human Review
Yes
        ↓
Is Source Identified?
        ↓
No → Unverified / Human Review
Yes
        ↓
Is Drug/Product Identified?
        ↓
No → Incomplete / Human Review
Yes
        ↓
Is Observation Recorded?
        ↓
No → Incomplete / Human Review
Yes
        ↓
Is Supporting Documentation Available?
        ↓
No → Needs Review
Yes
        ↓
Is Provenance Traceable?
        ↓
No → Needs Review
Yes
        ↓
Is There Duplicate/Conflicting Evidence?
        ↓
Yes → Conflicting / Human Review
No
        ↓
Evidence Quality Assessment
        ↓
Validation Status Assigned
        ↓
Structured Output
```

---

# 12. Hypothetical Evidence Validation Matrix

The following records are fictional and contain no identifiable patient information.

| Evidence ID | Source | Evidence Type | Drug/Product | Observation | Date | Population/Context | Measurement/Result | Supporting Documentation | Evidence Quality | Validation Status | Limitations | Reviewer Action |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| EV-001 | FAERS | Adverse Event Report | Drug A | Repeated reports of nausea | 2026-01-10 | Post-marketing reports | No causal conclusion | Report record | Medium | Needs Review | Reporting bias and incomplete context possible | Review for pattern |
| EV-002 | PubMed | Published Study | Drug A | Nausea reported during study | 2025-11-15 | Adult study population | Reported study finding | Journal article | High | Validated | Limited population size | Compare with other evidence |
| EV-003 | DailyMed | Product Label | Drug A | Nausea listed as an adverse reaction | 2026-02-01 | Product labeling | Listed reaction | Official label | High | Validated | Label may not include every possible reaction | Use as supporting reference |
| EV-004 | Laboratory QC | QC Test Result | Drug A | Product sample tested | 2026-02-05 | Sample from LOT-EXAMPLE-001 | Result documented | QC test record | High | Validated | Hypothetical sample data | Retain as supporting QC evidence |
| EV-005 | Product Complaint | Quality Complaint | Drug A | Tablet appearance reported as unusual | 2026-02-08 | Product complaint | Investigation pending | Complaint record | Low | Unverified | Batch information incomplete | Request additional information |
| EV-006 | FDA Safety Communication | Regulatory Safety Information | Drug B | Regulatory safety concern communicated | 2026-01-20 | Public safety information | Regulatory review information | Official communication | High | Validated | Issue-specific information | Link to relevant evidence |
| EV-007 | ClinicalTrials.gov | Clinical Study Record | Drug B | Study contains adverse-event information | 2025-12-10 | Registered study population | Results available for review | Study record | Medium | Needs Review | Requires study-context assessment | Review study design |
| EV-008 | Laboratory QC | QC Investigation | Drug C | Unusual analytical result observed | 2026-02-12 | Investigation sample | Further investigation required | QC investigation record | Medium | Needs Review | Root cause not established | Human QC review |
| EV-009 | Public Report | Unverified Safety Observation | Drug C | Rash reported after exposure | 2026-02-14 | Limited context | No causality established | Initial report | Low | Unverified | Concomitant medicines unknown | Request more information |
| EV-010 | Internal Sample Record | QC Evidence | Drug D | Record contains incomplete test information | 2026-02-16 | Sample context incomplete | Result field missing | Partial record | Low | Incomplete | Missing result and method details | Complete or reject record |
| EV-011 | PubMed | Published Study | Drug E | Safety finding differs from another source | 2026-02-18 | Research population | Conflicting interpretation | Published article | Medium | Conflicting | Different study design and context | Human scientific review |
| EV-012 | OpenFDA | Structured Safety Data | Drug A | Similar event reports identified | 2026-02-20 | Public structured reports | Pattern requires assessment | Source dataset | Medium | Needs Review | Duplicate reports may be present | Duplicate and signal review |

---

# 13. How the Model Distinguishes Evidence Types

## Validated Evidence

Example:

```text
Source identified
+
Supporting documentation available
+
Provenance traceable
+
Required information complete
+
Appropriate review performed
```

Result:

```text
Validated
```

This means the record has passed the required validation checks for its intended use.

It does not prove clinical causality.

---

## Incomplete Evidence

Example:

```text
Missing Drug Identifier
or
Missing Result
or
Missing Supporting Information
```

Result:

```text
Incomplete
```

Action:

```text
Request Additional Information
or
Human Review
```

---

## Unverified Evidence

Example:

```text
Initial report received
but
not yet sufficiently checked
```

Result:

```text
Unverified
```

Action:

```text
Validate Source and Supporting Information
```

---

## Conflicting Evidence

Example:

```text
Record A → Suggests Quality Issue

Record B → Does Not Support Quality Issue
```

Result:

```text
Conflicting
```

Action:

```text
Do Not Automatically Choose One
        ↓
Human Review Required
```

---

## Potentially Important Safety Evidence

Example:

```text
Repeated Similar Reports
        ↓
Possible Pattern Identified
        ↓
Potential Safety Signal
        ↓
Further Assessment Required
```

Important:

```text
Potential Signal
≠
Confirmed Causality
```

---

# 14. Relationship Between Validation Status and Human Review

| Validation Status | Human Review Requirement |
|---|---|
| Validated | Usually not automatically required, unless new concerns appear |
| Needs Review | Yes |
| Incomplete | Yes or additional information required |
| Unverified | Yes |
| Conflicting | Yes |

A human-review flag should remain visible in the structured output.

---

# 15. Proposed Structured Data Model

A future AI/Data Science system may represent a record as:

```text
Evidence Record
│
├── Evidence ID
├── Source
├── Source Organisation
├── Evidence Type
├── Drug/Product
├── Observation
├── Date
├── Population/Context
├── Measurement/Result
├── Supporting Documentation
├── Evidence Provenance
├── Evidence Quality
├── Validation Status
├── Limitations
├── Reviewer Action
└── Human Review Flag
```

Example:

```text
Evidence ID: EV-001
Source: FAERS
Evidence Type: Adverse Event Report
Drug/Product: Drug A
Observation: Repeated reports of nausea
Evidence Quality: Medium
Validation Status: Needs Review
Human Review Flag: Yes
```

This structure is designed for future:

- CSV datasets.
- JSON output.
- Python programs.
- Data analysis.
- AI/Data Science workflows.
- Human evidence review.

---

# 16. Validation Logic for the Python Mini-Build

The Python Drug Safety Evidence Tracker can use this model to:

1. Load evidence records.
2. Search by drug/product.
3. Filter by evidence type.
4. Filter by validation status.
5. Display observations.
6. Display evidence provenance.
7. Identify records needing human review.
8. Detect potential duplicate evidence IDs.
9. Highlight conflicting evidence where recorded.
10. Produce structured JSON output.

A simplified logic model is:

```text
Load CSV
        ↓
Check Dataset Exists
        ↓
Check Required Columns
        ↓
Check for Empty Dataset
        ↓
Check Evidence IDs
        ↓
Check Duplicate IDs
        ↓
Check Validation Status Values
        ↓
Search/Filter Records
        ↓
Identify Needs Review / Human Review
        ↓
Display Evidence and Provenance
        ↓
Generate JSON Output
```

The program should clearly state:

```text
A flagged record requires further human review.

It is not a clinical conclusion and does not prove
that a drug caused an observed event.
```

---

# 17. Failure Handling

The evidence-validation model should handle common failure situations.

## Missing Drug Name

```text
Input:
Drug field is empty

Expected Action:
Reject or flag incomplete record.
```

---

## Unknown Drug

```text
Input:
Search returns no matching records.

Expected Action:
Display a clear "No evidence found" message.
Do not generate a false safety conclusion.
```

---

## Incomplete Evidence Record

```text
Input:
Required fields are missing.

Expected Action:
Assign "Incomplete" or "Needs Review" as appropriate.
```

---

## Invalid Validation Status

Example:

```text
Validation Status: Approved Forever
```

If this is not one of the accepted categories, the system should flag it as invalid.

Accepted categories for this project are:

- Validated.
- Needs Review.
- Incomplete.
- Unverified.
- Conflicting.

Expected action:

```text
Invalid Status
        ↓
Flag Record
        ↓
Require Correction or Human Review
```

---

## Duplicate Evidence ID

Example:

```text
EV-005 appears twice
```

Expected action:

```text
Duplicate ID Detected
        ↓
Do Not Automatically Delete Evidence
        ↓
Flag for Review
```

---

## Conflicting Evidence

Expected action:

```text
Conflict Detected
        ↓
Preserve Both Records
        ↓
Document Conflict
        ↓
Flag for Human Review
```

---

## Empty Dataset

Expected action:

```text
No Evidence Records Available

Display Clear Message
Do Not Generate Summary Statistics
```

---

# 18. Known Limitations of This Model

This evidence-validation model is a simplified educational and research framework.

It does not:

- Diagnose patients.
- Recommend treatments.
- Establish clinical causality.
- Replace formal pharmacovigilance assessment.
- Replace regulatory reporting systems.
- Replace professional laboratory investigations.
- Replace GMP or GCP requirements.
- Create medical thresholds.
- Independently resolve scientific conflicts.

The model is designed to support:

```text
Evidence Organization
+
Traceability
+
Validation
+
Documentation
+
Human Review
```

---

# 19. Future Improvements

Future teams may improve this model by adding:

- Standardized medical terminology.
- MedDRA mapping where appropriately licensed and available.
- Automated duplicate detection.
- Evidence version control.
- Source reliability scoring.
- Date/version checking.
- Conflict-detection algorithms.
- Role-based reviewer approval.
- Audit trails.
- Batch/lot linkage.
- Laboratory information system integration.
- Advanced data visualization.
- AI-assisted evidence classification.

Any future AI system should preserve the requirement for appropriate human scientific review.

---

# 20. Final Evidence Validation Framework

The final proposed framework is:

```text
Evidence Received
        ↓
Source Identified
        ↓
Evidence Classified
        ↓
Drug/Product Identified
        ↓
Completeness Checked
        ↓
Supporting Documentation Checked
        ↓
Provenance Preserved
        ↓
Duplicate Check
        ↓
Conflict Check
        ↓
Evidence Quality Assessed
        ↓
Validation Status Assigned
        ↓
Human Review Flag Applied if Needed
        ↓
Structured Output Generated
```

The most important principle is:

```text
The purpose of evidence validation is not to make
a clinical conclusion.

The purpose is to ensure that evidence is:

Traceable
+
Structured
+
Checked
+
Limited appropriately
+
Documented
+
Ready for responsible human review
```

---

# 21. Conclusion

This Evidence Validation Model provides a structured foundation for organizing drug-safety, pharmacovigilance, laboratory QC, and pharmaceutical-quality evidence.

It allows future teams to distinguish between:

- Validated evidence.
- Incomplete evidence.
- Unverified evidence.
- Conflicting evidence.
- Records needing human review.

The model preserves the relationship:

```text
Source
        ↓
Evidence
        ↓
Provenance
        ↓
Validation
        ↓
Limitations
        ↓
Human Review
        ↓
Structured Output
```

The central scientific safeguards are:

```text
Reported Adverse Event
≠
Confirmed Adverse Drug Reaction
```

```text
Safety Signal
≠
Proof of Causality
```

```text
Laboratory Finding
≠
Automatic Proof of Patient-Level Causality
```

```text
Human Review Flag
≠
Clinical Conclusion
```

This model therefore provides a reusable foundation for future pharmacy, AI/Data Science, software, laboratory, and QA/QC teams to organize evidence while maintaining traceability, scientific caution, data integrity, and appropriate human oversight.