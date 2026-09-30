"""
Evidence Validation Module

Purpose:
Validate the structure and required fields of drug safety evidence records.

This module performs data-quality validation only.
It does not determine clinical causality, safety confirmation,
or regulatory decisions.
"""


# Accepted values for controlled fields
VALID_EVIDENCE_TYPES = {
    "ADVERSE_EVENT",
    "ADR",
    "QUALITY_COMPLAINT",
    "LITERATURE",
    "CLINICAL_TRIAL",
    "REGULATORY_SAFETY",
    "OTHER"
}

VALID_VALIDATION_STATUSES = {
    "VALID",
    "INVALID",
    "PENDING_REVIEW"
}


def validate_record(record):
    """
    Validate one evidence record.

    Returns a dictionary containing:
    - validation status
    - validation errors
    - human review requirement
    """

    errors = []

    # Required fields
    required_fields = [
        "evidence_id",
        "source",
        "drug_product",
        "observation"
    ]

    for field in required_fields:
        value = record.get(field)

        if value is None or str(value).strip() == "":
            errors.append(f"MISSING_REQUIRED_FIELD:{field}")

    # Evidence type validation
    evidence_type = record.get("evidence_type")

    if evidence_type:
        if str(evidence_type).strip().upper() not in VALID_EVIDENCE_TYPES:
            errors.append("INVALID_EVIDENCE_TYPE")

    # Validation status validation
    validation_status = record.get("validation_status")

    if validation_status:
        if str(validation_status).strip().upper() not in VALID_VALIDATION_STATUSES:
            errors.append("INVALID_VALIDATION_STATUS")

    # Provenance validation
    provenance = record.get("evidence_provenance")

    if provenance is None or str(provenance).strip() == "":
        errors.append("MISSING_PROVENANCE")

    # Final validation result
    if errors:
        validation_status_result = "INVALID"
        human_review_required = True
    else:
        validation_status_result = "VALID"
        human_review_required = False

    return {
        "evidence_id": record.get("evidence_id"),
        "validation_status": validation_status_result,
        "validation_errors": errors,
        "human_review_required": human_review_required
    }


def validate_records(records):
    """
    Validate a list of evidence records.
    """

    results = []

    for record in records:
        results.append(validate_record(record))

    return results


if __name__ == "__main__":

    test_record = {
        "evidence_id": "EV-001",
        "source": "FAERS",
        "drug_product": "Drug A",
        "observation": "Adverse event reported",
        "evidence_type": "ADVERSE_EVENT",
        "validation_status": "VALID",
        "evidence_provenance": "FDA FAERS dataset"
    }

    result = validate_record(test_record)

    print("Evidence Validation Result:")
    print(result)