from review.human_review import (
    create_review_flag,
    review_for_validation,
    review_for_conflict,
    review_for_matching
)


def test_conflict_requires_human_review():
    result = create_review_flag(
        reason="EVIDENCE_CONFLICT",
        evidence_ids=["EV-004", "EV-017"],
        source="Source A, Source B"
    )

    assert result["human_review_required"] is True
    assert result["review_reason"] == "EVIDENCE_CONFLICT"
    assert result["evidence_ids"] == ["EV-004", "EV-017"]


def test_validation_failure_requires_review():
    validation_result = {
        "evidence_id": "EV-100",
        "validation_status": "INVALID",
        "validation_errors": [
            "MISSING_REQUIRED_FIELD:source"
        ]
    }

    result = review_for_validation(
        validation_result
    )

    assert result["human_review_required"] is True
    assert result["review_reason"] == "VALIDATION_FAILURE"


def test_matching_failure_requires_review():
    match_result = {
        "query": "Unknown Drug",
        "match_status": "UNMATCHED",
        "matched_products": [],
        "human_review_required": True
    }

    result = review_for_matching(
        match_result
    )

    assert result["human_review_required"] is True
    assert result["review_reason"] == "DRUG_PRODUCT_MATCH_REVIEW"


def test_review_does_not_confirm_safety_or_causality():
    result = create_review_flag(
        reason="EVIDENCE_CONFLICT",
        evidence_ids=["EV-004", "EV-017"]
    )

    assert result["safety_confirmed"] is False
    assert result["causality_confirmed"] is False