"""
Drug Safety Evidence Integration Module

Purpose:
Combine normalized evidence with validation, duplicate,
conflict, matching, and human-review information.

This module does not make clinical, causality, or regulatory decisions.
"""

import json
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from validation.validate_evidence import validate_record
from duplicates.detect_duplicates import detect_duplicates
from conflicts.detect_conflicts import detect_conflicts
from matching.drug_matcher import match_drug
from review.human_review import (
    review_for_validation,
    review_for_conflict,
    review_for_matching
)


def load_evidence(json_file):
    """Load normalized evidence JSON."""

    path = Path(json_file)

    if not path.exists():
        raise FileNotFoundError(
            f"Evidence file not found: {json_file}"
        )

    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    return data


def integrate_evidence(json_file, drug_query):
    """
    Run the evidence integration workflow.

    Workflow:
    1. Load evidence
    2. Validate records
    3. Detect duplicates
    4. Detect conflicts
    5. Match drug/product
    6. Create human-review requirements
    7. Produce structured output
    """

    data = load_evidence(json_file)

    records = data.get("records", [])
        # -----------------------------------------
    # Integration adapter
    # Maps canonical schema fields to the
    # existing validation/detection modules.
    # Original canonical records are preserved.
    # -----------------------------------------

    processing_records = []

    evidence_type_map = {
        "ADVERSE EVENT REPORT": "ADVERSE_EVENT",
        "LITERATURE": "LITERATURE",
        "PRODUCT LABEL": "REGULATORY_SAFETY",
        "CLINICAL TRIAL": "CLINICAL_TRIAL",
        "LABORATORY RESULT": "OTHER",
        "QUALITY COMPLAINT": "QUALITY_COMPLAINT",
        "MEDICATION ERROR": "OTHER"
    }

    validation_status_map = {
        "VALIDATED": "VALID",
        "NEEDS REVIEW": "PENDING_REVIEW",
        "INCOMPLETE": "PENDING_REVIEW",
        "UNVERIFIED": "PENDING_REVIEW",
        "CONFLICTING": "PENDING_REVIEW"
    }

    for record in records:

        processing_record = dict(record)

        processing_record["drug_product"] = (
            record.get("drug_product_identifier", "")
        )

        processing_record["source_identifier"] = (
            record.get("evidence_id", "")
        )

        evidence_type = str(
            record.get("evidence_type", "")
        ).strip().upper()

        processing_record["evidence_type"] = (
            evidence_type_map.get(
                evidence_type,
                "OTHER"
            )
        )

        validation_status = str(
            record.get("validation_status", "")
        ).strip().upper()

        processing_record["validation_status"] = (
            validation_status_map.get(
                validation_status,
                "PENDING_REVIEW"
            )
        )

        processing_records.append(
            processing_record
        )

    # -----------------------------
    # Validation
    # -----------------------------

    validation_results = []

    for record in processing_records:
        result = validate_record(record)

        validation_results.append(result)
    # -----------------------------
    # Duplicate detection
    # -----------------------------

    duplicate_results = detect_duplicates(
    processing_records
)
    # -----------------------------
    # Conflict detection
    # -----------------------------

    conflict_results = detect_conflicts(
    processing_records
)

    # -----------------------------
    # Drug/product matching
    # -----------------------------

    matching_result = match_drug(
    processing_records,
    drug_query
)

    # -----------------------------
    # Human review
    # -----------------------------

    review_results = []

    for result in validation_results:

        review = review_for_validation(
            result
        )

        if review["human_review_required"]:
            review_results.append(review)

    for conflict in conflict_results:

        review = review_for_conflict(
            conflict
        )

        if review["human_review_required"]:
            review_results.append(review)

    matching_review = review_for_matching(
        matching_result
    )

    if matching_review["human_review_required"]:
        review_results.append(matching_review)

            # Preserve human-review requirements already present
    # in the canonical source records.

    for record in records:

        if record.get("human_review_flag") is True:

            review_results.append({
                "human_review_required": True,
                "review_reason": "SOURCE_RECORD_REVIEW_FLAG",
                "evidence_ids": [
                    record.get("evidence_id")
                ],
                "source": record.get("source"),
                "safety_confirmed": False,
                "causality_confirmed": False
            })

    # -----------------------------
    # Final structured output
    # -----------------------------

    output = {
        "integration_name":
            "BHIV Drug Safety Evidence Integration",

        "integration_version":
            "1.0.0",

        "source_schema":
            data.get("schema_name"),

        "source_schema_version":
            data.get("schema_version"),

        "record_count":
            len(records),

        "query":
            drug_query,

        "matching":
            matching_result,

        "validation_results":
            validation_results,

        "duplicate_results":
            duplicate_results,

        "conflict_results":
            conflict_results,

        "human_review_results":
            review_results,

        "records":
            records
    }

    return output


def save_output(output, output_file):
    """Save structured integration output."""

    path = Path(output_file)

    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with path.open(
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            output,
            file,
            indent=4,
            ensure_ascii=False
        )


if __name__ == "__main__":

    input_file = (
        "normalized_data/"
        "normalized_evidence.json"
    )

    output_file = (
        "integration/"
        "integrated_evidence_output.json"
    )

    result = integrate_evidence(
        input_file,
        "Drug A"
    )

    save_output(
        result,
        output_file
    )

    print(
        "Evidence integration completed."
    )

    print(
        f"Records processed: "
        f"{result['record_count']}"
    )

    print(
        f"Duplicate relationships: "
        f"{len(result['duplicate_results'])}"
    )

    print(
        f"Conflict relationships: "
        f"{len(result['conflict_results'])}"
    )

    print(
        f"Human review items: "
        f"{len(result['human_review_results'])}"
    )

    print(
        f"Output saved to: "
        f"{output_file}"
    )