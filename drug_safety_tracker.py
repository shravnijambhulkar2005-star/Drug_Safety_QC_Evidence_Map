import csv
import json
import argparse
from pathlib import Path


VALIDATION_STATUSES = {
    "Validated",
    "Incomplete",
    "Unverified",
    "Conflicting",
    "Needs Review"
}


def load_evidence(csv_file):
    """Load evidence records from a CSV file."""
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
        records = list(reader)

    return records


def search_by_drug(records, drug_name):
    """Search records by drug/product."""
    
    if not drug_name.strip():
        return []

    return [
        record
        for record in records
        if drug_name.lower()
        in record["Drug_Product"].lower()
    ]


def filter_by_evidence_type(records, evidence_type):
    """Filter records by evidence type."""

    if not evidence_type:
        return records

    return [
        record
        for record in records
        if record["Evidence_Type"].lower()
        == evidence_type.lower()
    ]


def filter_by_validation_status(records, status):
    """Filter records by validation status."""

    if not status:
        return records

    return [
        record
        for record in records
        if record["Validation_Status"].lower()
        == status.lower()
    ]


def get_summary(records):
    """Create a summary of selected evidence."""

    validated = sum(
        r["Validation_Status"].lower()
        == "validated"
        for r in records
    )

    needs_review = sum(
        r["Human_Review_Required"].lower()
        == "yes"
        for r in records
    )

    sources = sorted(
        set(r["Source"] for r in records)
    )

    return {
        "evidence_found": len(records),
        "validated": validated,
        "needs_human_review": needs_review,
        "evidence_sources": sources
    }


def display_records(records):
    """Display safety observations and provenance."""

    if not records:
        print("\nNo evidence records found.")
        return

    print("\n--- SAFETY OBSERVATIONS ---")

    for record in records:

        print("\nEvidence ID:",
              record["Evidence_ID"])

        print("Drug/Product:",
              record["Drug_Product"])

        print("Observation:",
              record["Observation"])

        print("Evidence Type:",
              record["Evidence_Type"])

        print("Source:",
              record["Source"])

        print("Validation Status:",
              record["Validation_Status"])

        print("Supporting Documentation:",
              record["Supporting_Documentation"])

        print("Limitations:",
              record["Limitations"])

        if record["Human_Review_Required"].lower() == "yes":

            print(
                "⚠ HUMAN REVIEW REQUIRED"
            )

    print(
        "\nIMPORTANT: A human-review flag is "
        "not a clinical conclusion and does "
        "not establish drug-event causality."
    )


def create_json_output(records, drug_name):

    output = {

        "drug_searched": drug_name,

        "summary": get_summary(records),

        "records": records,

        "interpretation_note":
            "Flagged records require human review. "
            "A flag is not a clinical conclusion "
            "and does not establish causality."
    }

    return json.dumps(
        output,
        indent=4
    )


def main():

    parser = argparse.ArgumentParser(
        description=
        "Drug Safety Evidence Tracker"
    )

    parser.add_argument(
        "--file",
        required=True,
        help=
        "Path to evidence CSV file"
    )

    parser.add_argument(
        "--drug",
        help=
        "Search by drug/product"
    )

    parser.add_argument(
        "--evidence-type",
        help=
        "Filter by evidence type"
    )

    parser.add_argument(
        "--status",
        help=
        "Filter by validation status"
    )

    parser.add_argument(
        "--json",
        action="store_true",
        help=
        "Produce structured JSON output"
    )

    args = parser.parse_args()

    try:

        records = load_evidence(
            args.file
        )

    except FileNotFoundError as error:

        print(
            f"ERROR: {error}"
        )

        return

    filtered_records = records

    if args.drug:

        filtered_records = search_by_drug(
            filtered_records,
            args.drug
        )

    if args.evidence_type:

        filtered_records = filter_by_evidence_type(
            filtered_records,
            args.evidence_type
        )

    if args.status:

        filtered_records = filter_by_validation_status(
            filtered_records,
            args.status
        )

    if args.json:

        print(
            create_json_output(
                filtered_records,
                args.drug
            )
        )

        return

    print("\n======================================")
    print("   DRUG SAFETY EVIDENCE TRACKER")
    print("======================================")

    if args.drug:

        print(
            f"Drug searched: {args.drug}"
        )

    summary = get_summary(
        filtered_records
    )

    print(
        f"Evidence found: "
        f"{summary['evidence_found']}"
    )

    print(
        f"Validated: "
        f"{summary['validated']}"
    )

    print(
        f"Needs human review: "
        f"{summary['needs_human_review']}"
    )

    print(
        "Evidence sources: "
        + ", ".join(
            summary["evidence_sources"]
        )
    )

    display_records(
        filtered_records
    )


if __name__ == "__main__":
    main()