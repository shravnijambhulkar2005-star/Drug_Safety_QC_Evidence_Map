# Learning Notes

## Drug Safety & QC Evidence Mapping Foundation

### Biotech Learnship – Test 1

**Prepared by:** Shravani Jambhulkar  
**Academic Background:** Fourth-Year B.Pharmacy Student  
**Project Area:** Pharmacovigilance, Drug Safety, Laboratory QC and Evidence Validation

---

# 1. Purpose of These Learning Notes

These notes summarize the important concepts I learned while completing the Drug Safety & QC Evidence Mapping Foundation project.

The purpose of this project was not only to collect information but also to understand how drug-safety and laboratory-quality evidence moves through a structured system.

Before this project, I understood basic pharmacy concepts such as adverse effects, quality control, laboratory testing, and drug safety. Through this project, I learned how these concepts can be connected with:

- Structured evidence.
- Data validation.
- Evidence provenance.
- Batch/lot traceability.
- Human review.
- Python-based data tracking.
- AI/Data Science workflows.

The most important learning from this project was that a large amount of information does not automatically mean that a scientific conclusion can be made.

Evidence must be checked, validated, documented, and interpreted carefully.

---

# 2. What I Learned About Pharmacovigilance

Pharmacovigilance is concerned with monitoring, identifying, assessing, understanding, and helping prevent adverse effects and other medicine-related problems.

I learned that pharmacovigilance continues even after a medicine is marketed.

This is important because some safety problems may only become visible when a drug is used by a large number of patients in real-world conditions.

A simple pharmacovigilance process can be represented as:

```text
Medicine Use
        ↓
Safety Observation
        ↓
Report
        ↓
Data Collection
        ↓
Signal Detection
        ↓
Evidence Review
        ↓
Further Assessment
        ↓
Human/Scientific Review
        ↓
Documentation and Follow-up
```

The important point is that pharmacovigilance is not simply collecting reports.

The reports must be assessed carefully.

---

# 3. Adverse Event and Adverse Drug Reaction

One of the most important things I learned was the difference between an adverse event and an adverse drug reaction.

## Adverse Event (AE)

An adverse event is an unwanted medical occurrence that happens after or during the use of a medicine.

However, the event does not automatically have to be caused by the medicine.

For example:

```text
Patient takes Drug A
        ↓
Patient experiences headache
```

This can be recorded as an adverse event.

However, the headache may also have other possible causes.

Therefore:

```text
Event After Drug Use
≠
Automatic Proof That the Drug Caused the Event
```

## Adverse Drug Reaction (ADR)

An adverse drug reaction refers to a harmful or unintended response in which there is a suspected or established relationship with the medicine, depending on the regulatory or scientific context being used.

A simple comparison is:

```text
AE = An event occurred during or after medicine use.

ADR = A harmful or unintended response with a suspected or established relationship to the medicine.
```

The important learning is:

```text
Reported AE
≠
Automatically Confirmed ADR
```

---

# 4. Seriousness and Severity

I learned that seriousness and severity are not the same.

## Severity

Severity describes the intensity of an event.

Examples:

- Mild headache.
- Moderate headache.
- Severe headache.

## Seriousness

Seriousness is based on the outcome or consequences of an event.

An event may be considered serious when it results in outcomes such as:

- Death.
- A life-threatening event.
- Hospitalization or prolonged hospitalization.
- Persistent or significant disability.
- Other medically important outcomes according to the applicable criteria.

Therefore:

```text
Severe
≠
Serious
```

A very severe headache may be extremely painful but may not meet the criteria for a serious event.

This distinction is important in pharmacovigilance.

---

# 5. Expected and Unexpected Reactions

An expected reaction is generally one that is already described in relevant product or reference safety information.

For example:

```text
Nausea is listed in the approved product information.
        ↓
A patient reports nausea after using the medicine.
        ↓
The reaction may be classified as expected,
depending on the applicable reference information.
```

An unexpected reaction is one that is not consistent with the available reference safety information.

However, I learned that:

```text
Unexpected
≠
Automatically Caused by the Drug
```

Unexpected information may require further assessment.

---

# 6. Safety Signals

A safety signal is information that suggests a possible relationship between a medicine and an event and requires further investigation or assessment.

For example:

```text
One report of headache
        ↓
May be an individual observation

Many similar reports
        ↓
Possible pattern

Possible pattern requiring investigation
        ↓
Potential safety signal
```

A safety signal does not prove causality.

The most important principle I learned is:

```text
Safety Signal
≠
Proof of Causality
```

A signal is the beginning of further investigation, not the final scientific conclusion.

---

# 7. Signal Detection

Signal detection is the process of identifying possible patterns in safety information.

I learned that possible approaches include:

- Review of individual cases.
- Statistical or data-based analysis.
- Review of published scientific literature.
- Review of regulatory information.
- Review of observed reporting patterns.

A simplified process is:

```text
Safety Reports
        ↓
Collect and Organize
        ↓
Look for Patterns
        ↓
Identify Unusual Information
        ↓
Possible Signal
        ↓
Further Review
```

Signal detection should not be confused with proving that a medicine caused an event.

---

# 8. Signal Validation

Signal validation involves checking whether the identified information is sufficiently reliable and relevant for further assessment.

Questions may include:

- Is the report complete?
- Is the medicine identified?
- Is the event clearly described?
- Is the source credible?
- Are there duplicate reports?
- Are there alternative explanations?
- Is supporting information available?

The process can be represented as:

```text
Possible Signal
        ↓
Check Data Quality
        ↓
Check Completeness
        ↓
Check Duplicates
        ↓
Check Supporting Evidence
        ↓
Assess Relevance
        ↓
Validated for Further Assessment
or
Needs Additional Information
```

Important:

```text
Signal Validation
≠
Final Proof of Causality
```

---

# 9. Basic Concept of Causality Assessment

I learned that causality assessment requires consideration of more than the timing of an event.

For example:

```text
Drug A Taken
        ↓
Rash Occurs
```

This does not automatically prove that Drug A caused the rash.

Other possible factors may include:

- Other medicines.
- Drug interactions.
- Existing diseases.
- Allergies.
- Food.
- Environmental exposure.
- Infection.
- Other health conditions.

Therefore, relevant information may include:

- Time relationship.
- Other medicines.
- Medical history.
- Disease condition.
- Dose information.
- Previous exposure.
- Dechallenge/rechallenge information where available and appropriate.
- Alternative explanations.

The key learning is:

```text
Temporal Association
≠
Proof of Causality
```

---

# 10. Post-Marketing Surveillance

Post-marketing surveillance refers to monitoring the safety of medicines after they become available for use in the general population.

Clinical trials may involve a limited number of selected participants.

After marketing:

```text
More Patients
+
Different Age Groups
+
Different Health Conditions
+
Concomitant Medicines
+
Longer-Term Use
        ↓
More Real-World Safety Information
```

Post-marketing surveillance can help identify rare, delayed, or unexpected safety concerns.

However, post-marketing reports still require evaluation and validation.

---

# 11. Medication-Error Reporting

A medication error is a preventable mistake that may lead to inappropriate medication use or patient harm.

Examples may include:

- Wrong medicine.
- Wrong dose or concentration.
- Wrong route of administration.
- Dispensing error.
- Administration error.
- Prescribing error.
- Handling or storage error.

Medication errors can occur at different stages:

```text
Prescribing
        ↓
Dispensing
        ↓
Preparation/Handling
        ↓
Administration
        ↓
Monitoring
```

I learned that medication-error information can be important during safety investigations because the observed problem may not always be caused by the medicine itself.

The cause may be related to how the medicine was prescribed, prepared, dispensed, or administered.

---

# 12. Drug-Quality Complaints

A drug-quality complaint is information suggesting a possible problem with the quality, identity, strength, purity, packaging, labeling, or performance of a pharmaceutical product.

Examples may include:

- Unusual tablet appearance.
- Broken tablets.
- Leaking packaging.
- Discoloration.
- Missing label information.
- Suspected contamination.
- Incorrect packaging.

A complaint can lead to an investigation.

The process may include:

```text
Complaint Received
        ↓
Product Identified
        ↓
Batch/Lot Identified
        ↓
Information Collected
        ↓
QC/Quality Investigation
        ↓
Evidence Review
        ↓
Documentation
        ↓
Follow-up
```

A complaint does not automatically prove that a manufacturing defect exists.

Similarly:

```text
Quality Complaint
≠
Confirmed Quality Defect
```

---

# 13. Quality Assurance and Quality Control

I learned the basic difference between QA and QC.

## Quality Assurance (QA)

QA is the broader quality system focused on ensuring that processes are properly planned, documented, controlled, and followed.

Examples include:

- SOPs.
- Training.
- Audits.
- Documentation.
- Change control.
- Deviation management.

QA is mainly focused on building systems that help prevent problems.

## Quality Control (QC)

QC focuses more directly on testing and checking materials, samples, and products.

Examples include:

- Laboratory testing.
- Instrument checks.
- Calibration.
- Reference standards.
- Controls.
- Result review.

A simple way to remember the difference is:

```text
QA = Quality System and Prevention

QC = Testing and Checking
```

Both QA and QC are important for reliable pharmaceutical evidence.

---

# 14. Batch/Lot Traceability

Batch or lot traceability is the ability to connect a specific product batch with relevant manufacturing, quality, distribution, and investigation records.

For example:

```text
Safety Report
        ↓
Product Identified
        ↓
Batch/Lot Number Identified
        ↓
Manufacturing Records
        ↓
QC Records
        ↓
Quality Complaints
        ↓
Investigation
```

I learned that batch traceability can help investigate whether several observations are connected with the same batch.

For example, if several complaints involve the same batch, this may provide a reason for further investigation.

However:

```text
Same Batch
+
Multiple Reports
≠
Automatic Proof That the Batch Caused the Events
```

Further scientific and quality investigation is required.

---

# 15. Data Integrity

Data integrity means ensuring that data is accurate, complete, reliable, and traceable throughout its lifecycle.

For pharmaceutical and laboratory evidence, data should not be manipulated or changed without appropriate documentation.

Important principles include making sure data is:

- Attributable.
- Legible/readable.
- Recorded appropriately.
- Accurate.
- Complete.
- Consistent.
- Enduring.
- Available when needed.

Poor data integrity can include:

- Missing records.
- Incorrect transcription.
- Unexplained changes.
- Missing raw data.
- Duplicate records.
- Loss of traceability.

A simple concept is:

```text
Reliable Evidence
Requires
Reliable Data
```

---

# 16. Evidence Provenance

Evidence provenance means keeping track of where evidence came from and how it can be traced.

For each evidence record, it is useful to know:

- Source.
- Organisation.
- Date.
- Document or record ID.
- Access method.
- Supporting documentation.
- Relevant product, batch, or sample identifiers.

For example:

```text
Evidence Record
        ↓
Where Did It Come From?
        ↓
Who Produced It?
        ↓
When Was It Recorded?
        ↓
What Document Supports It?
        ↓
Can Another Researcher Trace It?
```

I learned that evidence without provenance is difficult to validate.

The basic principle is:

```text
No Clear Provenance
        ↓
Reduced Confidence
        ↓
More Review Required
```

---

# 17. Reference Standards and Controls

Reference standards are materials with known and appropriate characteristics that can be used as a comparison during testing.

Controls help determine whether a test or analytical system is performing as expected.

They can help answer:

```text
Is the analytical system working correctly?
```

Before accepting a laboratory result, relevant standards and controls should be checked according to the applicable method or procedure.

---

# 18. Instrument Calibration

Calibration helps establish and maintain confidence that an instrument is performing appropriately for its intended measurement.

Before relying on laboratory results, relevant information may include:

- Calibration status.
- Maintenance status.
- Performance checks.
- Instrument records.

I learned that:

```text
Laboratory Result
+
Instrument Problem
        ↓
Requires Investigation
```

However:

```text
Instrument Problem
≠
Automatic Proof That Every Result Is Invalid
```

The impact must be assessed.

---

# 19. Sample Identification and Sample Integrity

A laboratory sample must be clearly identified so that results can be linked to the correct material.

Important sample information may include:

- Sample ID.
- Product name.
- Batch/lot number.
- Date received.
- Source of sample.

Sample integrity means checking whether the sample is suitable for testing.

Potential problems may include:

- Damage.
- Contamination.
- Incorrect storage.
- Degradation.
- Missing identification.

If sample integrity is uncertain, the reliability of the test result may also be affected.

---

# 20. Replicates and Measurement Uncertainty

Replicate measurements can help determine whether results are consistent.

Unexpected variation between measurements may require further review.

Measurement uncertainty recognizes that laboratory measurements are not always perfectly exact.

Factors may include:

- Instrument variability.
- Sample preparation.
- Analytical method.
- Reference materials.
- Environmental conditions.

I learned that the applicable validated method or laboratory procedure should define how uncertainty is handled.

I should not invent acceptance limits or scientific thresholds.

---

# 21. OOS and OOT Results

## Out-of-Specification (OOS)

An OOS result is a result that does not meet the applicable approved specification or acceptance criteria.

A result should be investigated according to the applicable quality procedure.

Important:

```text
OOS Result
≠
Automatic Proof of Manufacturing Failure
```

The data, calculations, sample, method, and instrument may need to be reviewed.

## Out-of-Trend (OOT)

An OOT result is a result that appears unusual compared with relevant historical or expected trends.

An OOT result may require investigation even when it remains within specification.

Important:

```text
OOT Result
≠
Automatic Product Failure
```

---

# 22. Deviations

A deviation is a departure from an approved procedure or expected process.

Examples may include:

- Incorrect procedure followed.
- Equipment problem.
- Sample-handling issue.
- Documentation error.
- Unexpected delay.

A deviation should be:

```text
Identified
        ↓
Documented
        ↓
Investigated
        ↓
Impact Assessed
        ↓
Reviewed
```

I learned that a deviation should not simply be ignored because it may affect the reliability of evidence.

---

# 23. Evidence Validation

One of the most important concepts in this project was evidence validation.

Evidence validation means checking whether information is sufficiently complete, traceable, and reliable for its intended use.

I learned to classify evidence into categories such as:

- Validated.
- Needs Review.
- Incomplete.
- Unverified.
- Conflicting.

A simplified workflow is:

```text
Evidence Received
        ↓
Source Check
        ↓
Drug/Product Check
        ↓
Observation Check
        ↓
Completeness Check
        ↓
Supporting Document Check
        ↓
Provenance Check
        ↓
Duplicate/Conflict Check
        ↓
Validation Status
        ↓
Human Review if Required
```

The important distinction is:

```text
Validated Record
≠
Scientifically Proven Causality
```

Validation refers to the quality and usability of the evidence record.

---

# 24. Duplicate and Conflicting Evidence

Duplicate evidence can create a false impression that there is more evidence than actually exists.

For example:

```text
One Event Reported Three Times
≠
Three Independent Events
```

Therefore, duplicate evidence IDs or highly similar records should be reviewed.

Conflicting evidence means that records provide inconsistent information.

For example:

```text
Record A:
No Quality Problem Identified

Record B:
Possible Quality Problem Identified
```

The system should not automatically decide which record is correct.

Instead:

```text
Conflicting Evidence
        ↓
Preserve Records
        ↓
Document Conflict
        ↓
Human Review Required
```

---

# 25. Public Drug-Safety Sources

During this project, I learned about important sources of drug-safety and pharmaceutical information.

Examples include:

- FDA FAERS.
- OpenFDA.
- DailyMed.
- FDA Drug Safety Communications.
- WHO pharmacovigilance resources.
- PubMed.
- ClinicalTrials.gov.
- EMA safety information.
- ICH guidelines.

I learned that these sources should not all be treated equally.

Different sources provide different types of evidence.

For example:

```text
FAERS
→ Post-Marketing Safety Reports

PubMed
→ Scientific Literature

DailyMed
→ Product Label Information

ClinicalTrials.gov
→ Clinical Study Information

ICH
→ Quality and Regulatory Guidelines
```

The important principle is:

```text
Public Source
≠
Automatic Proof
```

The evidence type and limitations must always be considered.

---

# 26. Learning About AI and Data Science

Before this project, I had no practical experience using Python or building a data-processing system.

Through this project, I learned the basic idea of how pharmacy evidence can be converted into structured data.

For example:

```text
Source
        ↓
Evidence Record
        ↓
Validation Status
        ↓
Evidence Provenance
        ↓
Human Review Flag
        ↓
Structured Output
```

I learned that AI/Data Science systems can help with:

- Searching evidence.
- Filtering records.
- Organizing data.
- Detecting duplicates.
- Identifying missing information.
- Flagging records for human review.
- Producing structured output.

However:

```text
AI Assistance
≠
Replacement for Scientific Judgement
```

Human review remains important.

---

# 27. Learning Python

As part of this project, I learned the basic structure of a Python program.

The Drug Safety Evidence Tracker can:

1. Load a CSV evidence file.
2. Search by drug/product.
3. Filter by evidence type.
4. Filter by validation status.
5. Display safety observations.
6. Display evidence provenance.
7. Flag records requiring human review.
8. Produce structured JSON output.

The basic program workflow is:

```text
CSV File
        ↓
Python Program
        ↓
Read Evidence Records
        ↓
Check Data
        ↓
Search/Filter
        ↓
Identify Validation Status
        ↓
Flag Human Review Records
        ↓
Generate Structured Output
```

I learned that code can support pharmacy research by making evidence easier to organize and review.

---

# 28. Learning About CSV and JSON

## CSV

CSV stands for Comma-Separated Values.

It is a simple format used to store structured information in rows and columns.

For this project:

```text
Evidence ID | Source | Drug | Observation | Validation Status
```

Each row represents an evidence record.

## JSON

JSON stands for JavaScript Object Notation.

It is a structured format that can be easily read by software systems.

For example:

```text
{
  "drug": "Drug A",
  "evidence_found": 5,
  "validated": 3,
  "needs_review": 2
}
```

I learned that JSON can help future AI/Data Science or software systems use structured evidence.

---

# 29. Importance of Testing

Testing was an important part of the Python mini-build.

I learned that a program should not only be tested with correct input.

It should also be tested with incorrect and unusual situations.

Examples include:

## Normal Test Cases

- Valid drug search.
- Evidence type filter.
- Validation status filter.
- Human review flag.
- JSON output.

## Invalid Input Cases

- Missing drug name.
- Unknown drug.
- Invalid validation status.
- Missing file.

## Evidence Validation Edge Cases

- Duplicate evidence ID.
- Conflicting evidence.
- Incomplete evidence record.
- Empty dataset.

The important learning is:

```text
Program Runs Successfully
≠
Program Has Been Fully Tested
```

Testing helps identify failures before submission or future use.

---

# 30. Important Mistake I Learned to Avoid

One of the most important things I learned during this project was to avoid overinterpreting evidence.

I should not assume:

```text
Event After Drug
= Drug Caused Event
```

I should not assume:

```text
Many Reports
= Proven Drug Causality
```

I should not assume:

```text
QC Result
= Patient-Level Causality
```

I should not assume:

```text
Flagged Record
= Clinical Conclusion
```

Instead, I learned to think:

```text
Observation
        ↓
Evidence
        ↓
Validation
        ↓
Limitations
        ↓
Further Assessment
        ↓
Human Review
```

---

# 31. Overall Project Learning

The complete learning model from this project can be represented as:

```text
Drug/Product
        ↓
Safety Observation
        ↓
Evidence Report
        ↓
Data Validation
        ↓
Possible Signal
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

I learned that each stage requires careful documentation and scientific caution.

The purpose of a structured evidence system is not to replace professionals.

Its purpose is to help organize information so that qualified people can review it more effectively.

---

# 32. Key Takeaways

The most important things I learned are:

1. An adverse event does not automatically mean that a drug caused the event.

2. A safety signal is not proof of causality.

3. Seriousness and severity are different concepts.

4. Unexpected reactions require further assessment but are not automatically proven to be caused by a drug.

5. Causality assessment requires consideration of alternative explanations.

6. Post-marketing surveillance is important because real-world drug use provides additional safety information.

7. Medication errors and drug-quality complaints can be important evidence during investigations.

8. QA and QC have different but connected roles.

9. Batch/lot traceability helps connect product information with quality and safety investigations.

10. Data integrity is essential for trustworthy evidence.

11. Evidence provenance allows another researcher to trace where information came from.

12. OOS and OOT results require investigation and should not be overinterpreted.

13. Evidence must be checked for completeness, duplicates, and conflicts.

14. A validated evidence record does not automatically establish drug causality.

15. AI and Python can help organize evidence, but human scientific review remains essential.

---

# 33. Final Reflection

As a fourth-year B.Pharmacy student, this project helped me connect my pharmacy knowledge with structured research, quality-control thinking, data organization, and basic programming.

I learned that pharmacovigilance and QC are not separate activities.

They can be connected through a structured evidence system.

The final model I developed is:

```text
Credible Source
        ↓
Evidence Record
        ↓
Evidence Provenance
        ↓
Data and Quality Checks
        ↓
Validation Status
        ↓
Human Review Flag
        ↓
Structured Output
        ↓
Future AI/Data Science Use
```

The most important principle I will carry forward is:

```text
Good research is not only about collecting information.

Good research is about knowing:

Where the information came from,
What it actually means,
What its limitations are,
What cannot yet be concluded,
and when human review is necessary.
```

This project gave me a foundation in pharmacovigilance, drug safety, pharmaceutical QC, evidence validation, data integrity, and basic Python-based evidence tracking.