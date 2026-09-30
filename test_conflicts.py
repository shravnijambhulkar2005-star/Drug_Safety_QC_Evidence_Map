from conflicts.detect_conflicts import detect_conflicts


def test_observation_conflict():
    records = [
        {
            "evidence_id": "EV-004",
            "source": "Source A",
            "drug_product": "Drug A",
            "observation": "Signal present"
        },
        {
            "evidence_id": "EV-017",
            "source": "Source B",
            "drug_product": "Drug A",
            "observation": "Signal not observed"
        }
    ]

    result = detect_conflicts(records)

    assert len(result) == 1

    conflict = result[0]

    assert conflict["conflict_type"] == "OBSERVATION_CONFLICT"
    assert conflict["evidence_ids"] == ["EV-004", "EV-017"]
    assert conflict["human_review_required"] is True