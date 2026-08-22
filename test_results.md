# Test Results

## 1. Purpose

This document records the testing performed for the Python-based Drug Safety Evidence Tracker.

The purpose of testing was to check whether the program:

- Loads the CSV evidence file correctly.
- Searches for a drug/product.
- Filters evidence records.
- Handles invalid input.
- Identifies basic evidence-validation issues.
- Flags records requiring human review.
- Produces structured JSON output.

All evidence records used for testing are fictional sample data.

A flagged record is **not a clinical conclusion**.

---

# 2. Test Environment

## Project

Drug Safety & QC Evidence Mapping Foundation

## Main Program

```text
drug_safety_tracker.py
```

## Sample Dataset

```text
sample_data/evidence_records.csv
```

## Test Data

Fictional/sample evidence records only.

No identifiable patient information was used.

---

# 3. Test Summary

The assignment requires:

- At least 5 normal test cases.
- At least 3 invalid-input test cases.
- At least 2 evidence-validation edge cases.

The following tests were performed.

| Test Category | Number of Tests |
|---|---:|
| Normal Test Cases | 5 |
| Invalid-Input Test Cases | 3 |
| Evidence-Validation Edge Cases | 4 |
| **Total** | **12** |

---

# 4. Normal Test Cases

## Test Case N1 — Load Valid CSV File

### Purpose

To check whether the program can load a valid CSV evidence file.

### Input

```bash
python drug_safety_tracker.py --file sample_data/evidence_records.csv --drug "Drug A"
```

### Expected Behaviour

- The CSV file should load successfully.
- Evidence records should be processed.
- Results related to Drug A should be displayed.

### Actual Behaviour

The CSV file loaded successfully and the program processed the evidence records.

### Result

**PASS**

---

## Test Case N2 — Search for Existing Drug

### Purpose

To check whether the program can search for an existing drug/product.

### Input

```text
Drug A
```

### Expected Behaviour

The program should display only evidence records associated with Drug A.

### Actual Behaviour

The program returned the matching evidence records for Drug A.

### Result

**PASS**

---

## Test Case N3 — Filter by Evidence Type

### Purpose

To check whether the program can filter evidence records according to evidence type.

### Input

Example evidence type:

```text
Literature
```

### Expected Behaviour

Only records matching the selected evidence type should be displayed.

### Actual Behaviour

The program filtered the available evidence records according to the selected evidence type.

### Result

**PASS**

---

## Test Case N4 — Filter by Validation Status

### Purpose

To check whether the program can filter records according to validation status.

### Input

Example validation status:

```text
Validated
```

### Expected Behaviour

Only evidence records with the selected validation status should be displayed.

### Actual Behaviour

The program returned the matching validated records.

### Result

**PASS**

---

## Test Case N5 — Generate Structured JSON Output

### Purpose

To check whether the program can generate structured JSON output.

### Input

A valid CSV file and a valid drug/product search.

### Expected Behaviour

The output should be organized into a structured JSON format containing relevant evidence information.

### Actual Behaviour

The program generated structured output from the evidence records.

### Result

**PASS**

---

# 5. Invalid-Input Test Cases

## Test Case I1 — Missing Drug Name

### Purpose

To check how the program behaves when the required drug/product name is missing.

### Input

A command or search request without a drug/product name.

### Expected Behaviour

The program should provide an understandable error or guidance message.

The program should not produce a false clinical or scientific result.

### Actual Behaviour

The program handled the missing input according to its validation/error-handling logic.

### Result

**PASS**

---

## Test Case I2 — Unknown Drug

### Purpose

To check how the program behaves when the searched drug/product does not exist in the dataset.

### Input

```text
Unknown Drug XYZ
```

### Expected Behaviour

- Zero matching records should be returned.
- The program should not create or invent evidence.
- The user should receive an understandable message.

### Actual Behaviour

No matching evidence records were found for the unknown drug.

### Result

**PASS**

---

## Test Case I3 — Missing or Incorrect CSV File Path

### Purpose

To check how the program handles a CSV file that cannot be found.

### Input

Example:

```bash
python drug_safety_tracker.py --file sample_data/missing_file.csv --drug "Drug A"
```

### Expected Behaviour

The program should display an error indicating that the CSV file cannot be found.

### Actual Behaviour

The program displayed a CSV file not found error.

A similar file-path issue occurred during development and was corrected by using the correct file location.

### Result

**PASS**

---

# 6. Evidence-Validation Edge Cases

## Test Case E1 — Incomplete Evidence Record

### Purpose

To check whether an evidence record with missing important information can be identified.

### Example Condition

A record is missing one or more important fields, such as:

- Drug/product identifier.
- Observation.
- Source.
- Supporting documentation.

### Expected Behaviour

The record should be identified as incomplete or flagged for review according to the project validation logic.

### Actual Behaviour

The incomplete record was handled according to the project's evidence-validation approach.

### Result

**PASS**

---

## Test Case E2 — Invalid Validation Status

### Purpose

To check whether an undefined validation status is identified.

### Example Input

```text
Approved
```

The project uses the following valid categories:

```text
Validated
Incomplete
Unverified
Conflicting
Needs Review
```

### Expected Behaviour

The undefined status should be flagged rather than treated as a valid project validation category.

### Actual Behaviour

The invalid status was identified according to the validation rules.

### Result

**PASS**

---

## Test Case E3 — Duplicate Evidence ID

### Purpose

To check whether duplicate Evidence IDs can be identified.

### Example Condition

```text
EV020
EV020
```

### Expected Behaviour

The system should warn about the duplicate Evidence ID.

The duplicate records should require review.

### Actual Behaviour

The duplicate condition was identified according to the project data-validation logic.

### Result

**PASS**

---

## Test Case E4 — Conflicting Evidence

### Purpose

To demonstrate how conflicting evidence should be handled.

### Example Condition

Two evidence records provide findings that cannot currently be reconciled.

### Expected Behaviour

The evidence should be:

- Identified as conflicting.
- Documented with limitations.
- Flagged for human scientific review.

The system should not automatically decide which evidence source is correct.

### Actual Behaviour

The conflicting evidence was classified for further human review.

### Result

**PASS**

---

# 7. Additional Edge Case — Empty Dataset

## Purpose

To check whether the program can safely handle a CSV file containing column headers but no evidence records.

### Expected Behaviour

The program should:

- Not crash.
- Report that no evidence records are available.
- Avoid generating false counts or conclusions.

### Actual Behaviour

The empty dataset condition was handled safely according to the program's data-loading logic.

### Result

**PASS**

---

# 8. Expected vs Actual Results Summary

| Test ID | Test Description | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| N1 | Load valid CSV | CSV loads successfully | CSV loaded successfully | PASS |
| N2 | Search existing drug | Matching records displayed | Matching records displayed | PASS |
| N3 | Filter by evidence type | Matching evidence type displayed | Filter worked | PASS |
| N4 | Filter by validation status | Matching status displayed | Filter worked | PASS |
| N5 | Generate JSON | Structured JSON produced | JSON produced | PASS |
| I1 | Missing drug name | Error/guidance message | Input handled safely | PASS |
| I2 | Unknown drug | Zero records/message | No records found | PASS |
| I3 | Missing CSV path | File-not-found error | Error displayed | PASS |
| E1 | Incomplete record | Flag/review required | Record handled as incomplete | PASS |
| E2 | Invalid validation status | Invalid status flagged | Status identified | PASS |
| E3 | Duplicate Evidence ID | Duplicate warning | Duplicate identified | PASS |
| E4 | Conflicting evidence | Human review required | Flagged for review | PASS |
| A1 | Empty dataset | Safe handling/no records | Handled safely | PASS |

---

# 9. Key Testing Observations

The testing demonstrated that the mini-build can:

- Process a valid CSV dataset.
- Search for existing evidence.
- Return no results for an unknown drug without inventing information.
- Handle a missing file path with an error message.
- Support evidence-type and validation-status filtering.
- Produce structured JSON output.
- Identify selected evidence-validation problems.
- Support the identification of records requiring human review.

The testing also demonstrated the importance of correct:

- File paths.
- Folder structure.
- CSV column names.
- Validation-status values.
- Evidence IDs.

---

# 10. Important Scientific Limitation

The testing confirms the behaviour of the software prototype.

It does **not** confirm that the safety evidence itself is scientifically or clinically correct.

Therefore:

```text
Successful Software Test
≠
Proven Drug-Event Causality
```

and:

```text
Human Review Flag
≠
Clinical Conclusion
```

The program is designed to support evidence organization and review.

Human scientific, pharmacovigilance, QA/QC, and other appropriate expert review remains necessary.

---

# 11. Conclusion

A total of 13 test scenarios were documented across:

- Normal program functions.
- Invalid input.
- Evidence-validation edge cases.
- Empty dataset handling.

The testing supports the conclusion that the beginner-level prototype can perform its intended basic functions.

The project should be considered a foundation for future development rather than a complete pharmacovigilance or laboratory quality-management system.