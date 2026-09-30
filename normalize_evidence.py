import csv
import json
import argparse
from pathlib import Path
from datetime import datetime, timezone


VALID_EVIDENCE_QUALITIES = {
    "High",
    "Moderate",
    "Low",
    "Unknown"
}


VALIDATION_STATUSES = {
    "Validated",
    "Incomplete",
    "Unverified",
    "Conflicting",
    "Needs Review"
}


SOURCE_ORGANISATIONS = {
    "FAERS/AEMS": "FDA",
    "PubMed": "National Library of Medicine",
    "DailyMed": "National Library of Medicine",
    "ClinicalTrials.gov": "U.S. National Library of Medicine",
    "Laboratory QC": "Source organisation not specified",
    "Drug Quality Complaint": "Source organisation not specified",
    "Medication Error Report": "Source organisation not specified"
}


def load_csv(csv_file):
    """Load the existing evidence CSV without modifying it."""

    path = Path(csv_file)

    if not path.exists():
        raise FileNotFoundError(
            f"CSV file not found: {csv_file}"
        )

    with path.open(
        "r",
        encoding="utf-8-sig",
        newline=""
    ) as file:

        reader = csv.DictReader(file)

        return list(reader)


def parse_human_review_flag(value):
    """Convert Yes/No CSV value into a boolean."""

    if value is None:
        return False

    return value.strip().lower() == "yes"


def normalize_date(value):
    """Preserve valid YYYY-MM-DD dates."""

    if not value:
        return ""

    try:
        datetime.strptime(
            value.strip(),
            "%Y-%m-%d"
        )

        return value.strip()

    except ValueError:
        return value.strip()


def get_source_organisation(source):
    """Map a known source to its organisation."""

    source = source.strip()

    return SOURCE_ORGANISATIONS.get(
        source,
        "Source organisation not specified"
    )


def normalize_record(record):
    """
    Convert one existing CSV record into the
    canonical Test 3 evidence structure.
    """

    evidence_id = record.get(
        "Evidence_ID",
        ""
    ).strip()

    source = record.get(
        "Source",
        ""
    ).strip()

    evidence_type = record.get(
        "Evidence_Type",
        ""
    ).strip()

    drug_product = record.get(
        "Drug_Product",
        ""
    ).strip()

    observation = record.get(
        "Observation",
        ""
    ).strip()

    date = normalize_date(
        record.get("Date", "")
    )

    population_context = record.get(
        "Population_Context",
        ""
    ).strip()

    measurement_result = record.get(
        "Measurement_Result",
        ""
    ).strip()

    supporting_documentation = record.get(
        "Supporting_Documentation",
        ""
    ).strip()

    evidence_quality = record.get(
        "Evidence_Quality",
        ""
    ).strip()

    validation_status = record.get(
        "Validation_Status",
        ""
    ).strip()

    limitations = record.get(
        "Limitations",
        ""
    ).strip()

    reviewer_action = record.get(
        "Reviewer_Action",
        ""
    ).strip()

    human_review_flag = parse_human_review_flag(
        record.get(
            "Human_Review_Required",
            ""
        )
    )

    normalized_record = {
        "evidence_id": evidence_id,

        "source": source,

        "source_organisation":
            get_source_organisation(source),

        "evidence_type":
            evidence_type,

        "drug_product_identifier":
            drug_product,

        "observation":
            observation,

        "date":
            date,

        "population_context":
            population_context,

        "measurement_result":
            measurement_result,

        "supporting_documentation":
            supporting_documentation,

        "evidence_provenance": {
            "original_source":
                source,

            "original_evidence_id":
                evidence_id,

            "ingestion_timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "source_version":
                "existing_test1_csv",

            "transformation_path": [
                "existing_csv",
                "field_mapping",
                "canonical_normalization"
            ]
        },

        "evidence_quality":
            evidence_quality
            if evidence_quality
            in VALID_EVIDENCE_QUALITIES
            else "Unknown",

        "validation_status":
            validation_status
            if validation_status
            in VALIDATION_STATUSES
            else "Unverified",

        "limitations":
            limitations,

        "reviewer_action":
            reviewer_action,

        "human_review_flag":
            human_review_flag,

        "interpretation":
            ""
    }

    return normalized_record


def normalize_records(records):
    """Normalize all evidence records."""

    return [
        normalize_record(record)
        for record in records
    ]


def save_json(records, output_file):
    """Save normalized records as JSON."""

    output_path = Path(output_file)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    output = {
        "schema_name":
            "BHIV_Drug_Safety_Evidence",

        "schema_version":
            "1.0.0",

        "record_count":
            len(records),

        "records":
            records
    }

    with output_path.open(
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            output,
            file,
            indent=4,
            ensure_ascii=False
        )


def main():

    parser = argparse.ArgumentParser(
        description=
        "Normalize existing Drug Safety evidence "
        "into the Test 3 canonical schema."
    )

    parser.add_argument(
        "--input",
        required=True,
        help=
        "Path to the existing evidence CSV."
    )

    parser.add_argument(
        "--output",
        required=True,
        help=
        "Path for the normalized JSON output."
    )

    args = parser.parse_args()

    try:

        records = load_csv(
            args.input
        )

        normalized_records = normalize_records(
            records
        )

        save_json(
            normalized_records,
            args.output
        )

        print(
            "Normalization completed successfully."
        )

        print(
            f"Input records: {len(records)}"
        )

        print(
            f"Normalized records: "
            f"{len(normalized_records)}"
        )

        print(
            f"Output file: {args.output}"
        )

    except FileNotFoundError as error:

        print(
            f"ERROR: {error}"
        )


if __name__ == "__main__":
    main()