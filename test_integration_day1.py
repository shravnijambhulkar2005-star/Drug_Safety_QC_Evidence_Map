from duplicates.detect_duplicates import detect_duplicates
from conflicts.detect_conflicts import detect_conflicts


def test_day1_duplicate_and_conflict_detection():
    records = [
        {
            "evidence_id": "EV-001",
            "source": "Source A",
            "source_identifier": "SRC-100",
            "drug_product": "Drug A",
            "observation": "Signal present"
        },
        {
            "evidence_id": "EV-002",
            "source": "Source A",
            "source_identifier": "SRC-100",
            "drug_product": "Drug A",
            "observation": "Signal present"
        },
        {
            "evidence_id": "EV-003",
            "source": "Source B",
            "source_identifier": "SRC-200",
            "drug_product": "Drug A",
            "observation": "Signal not observed"
        }
    ]

    duplicates = detect_duplicates(records)
    conflicts = detect_conflicts(records)

    # Duplicate must be detected
    assert len(duplicates) >= 1

    # Conflict must be detected
    assert len(conflicts) >= 1

    # Human review must be required
    assert any(
        item["human_review_required"] is True
        for item in duplicates
    )

    assert any(
        item["human_review_required"] is True
        for item in conflicts
    )