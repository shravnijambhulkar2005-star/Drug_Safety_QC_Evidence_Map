"""
Duplicate Detection Module

Purpose:
Identify possible duplicate evidence records without deleting
or silently merging any records.

This module only identifies relationships.
It does not make clinical or causality decisions.
"""


def detect_duplicates(records):
    """
    Detect duplicate evidence records.

    Duplicate rules:
    1. Duplicate Evidence ID
    2. Same Source + Same Source Identifier
    3. Same Drug/Product + Same Observation

    Parameters:
        records (list): List of evidence dictionaries.

    Returns:
        list: Duplicate relationships.
    """

    duplicate_relationships = []

    # Rule 1: Duplicate Evidence IDs
    evidence_id_map = {}

    for record in records:
        evidence_id = record.get("evidence_id")

        if not evidence_id:
            continue

        if evidence_id in evidence_id_map:
            duplicate_relationships.append({
                "record_id": evidence_id,
                "duplicate_of": evidence_id_map[evidence_id],
                "duplicate_type": "DUPLICATE_EVIDENCE_ID",
                "human_review_required": True
            })
        else:
            evidence_id_map[evidence_id] = evidence_id

    # Rule 2: Same Source + Same Source Identifier
    source_identifier_map = {}

    for record in records:
        evidence_id = record.get("evidence_id")
        source = record.get("source")
        source_identifier = record.get("source_identifier")

        if not source or not source_identifier:
            continue

        key = (
            source.strip().lower(),
            source_identifier.strip().lower()
        )

        if key in source_identifier_map:
            duplicate_relationships.append({
                "record_id": evidence_id,
                "duplicate_of": source_identifier_map[key],
                "duplicate_type": "SOURCE_DUPLICATE",
                "human_review_required": True
            })
        else:
            source_identifier_map[key] = evidence_id

    # Rule 3: Same Drug/Product + Same Observation
    content_map = {}

    for record in records:
        evidence_id = record.get("evidence_id")
        drug = record.get("drug_product")
        observation = record.get("observation")

        if not drug or not observation:
            continue

        key = (
            drug.strip().lower(),
            observation.strip().lower()
        )

        if key in content_map:
            duplicate_relationships.append({
                "record_id": evidence_id,
                "duplicate_of": content_map[key],
                "duplicate_type": "CONTENT_DUPLICATE",
                "human_review_required": True
            })
        else:
            content_map[key] = evidence_id

    return duplicate_relationships


if __name__ == "__main__":
    # Small test dataset for this module
    test_records = [
        {
            "evidence_id": "EV-001",
            "source": "FAERS",
            "source_identifier": "FAERS-1001",
            "drug_product": "Drug A",
            "observation": "Adverse event reported"
        },
        {
            "evidence_id": "EV-002",
            "source": "FAERS",
            "source_identifier": "FAERS-1001",
            "drug_product": "Drug A",
            "observation": "Adverse event reported"
        },
        {
            "evidence_id": "EV-003",
            "source": "PubMed",
            "source_identifier": "PMID-12345",
            "drug_product": "Drug A",
            "observation": "Adverse event reported"
        }
    ]

    duplicates = detect_duplicates(test_records)

    print("Duplicate Detection Result:")
    print(duplicates)