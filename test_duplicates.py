from duplicates.detect_duplicates import detect_duplicates


def test_duplicate_source_identifier():
    records = [
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
        }
    ]

    result = detect_duplicates(records)

    assert len(result) >= 1
    assert result[0]["record_id"] == "EV-002"
    assert result[0]["duplicate_of"] == "EV-001"
    assert result[0]["human_review_required"] is True