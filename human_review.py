"""
Human Review Layer

Purpose:
Convert validation, duplicate, conflict, and matching conditions
into explicit human-review requirements.

This module does not make clinical decisions.
It does not confirm safety or causality.
"""


def create_review_flag(
    reason,
    evidence_ids=None,
    source=None
):
    """
    Create a structured human-review flag.
    """

    if evidence_ids is None:
        evidence_ids = []

    return {
        "human_review_required": True,
        "review_reason": reason,
        "evidence_ids": evidence_ids,
        "source": source,
        "safety_confirmed": False,
        "causality_confirmed": False
    }


def review_for_validation(validation_result):
    """
    Create a review flag when validation fails.
    """

    if validation_result.get("validation_status") == "INVALID":

        return create_review_flag(
            reason="VALIDATION_FAILURE",
            evidence_ids=[
                validation_result.get("evidence_id")
            ]
        )

    return {
        "human_review_required": False,
        "review_reason": None,
        "evidence_ids": [],
        "source": None,
        "safety_confirmed": False,
        "causality_confirmed": False
    }


def review_for_conflict(conflict_result):
    """
    Create a review flag for a detected conflict.
    """

    if conflict_result.get("human_review_required"):

        return create_review_flag(
            reason="EVIDENCE_CONFLICT",
            evidence_ids=conflict_result.get(
                "evidence_ids",
                []
            ),
            source=", ".join(
                conflict_result.get(
                    "sources",
                    []
                )
            )
        )

    return {
        "human_review_required": False,
        "review_reason": None,
        "evidence_ids": [],
        "source": None,
        "safety_confirmed": False,
        "causality_confirmed": False
    }


def review_for_matching(match_result):
    """
    Create a review flag when product matching is ambiguous
    or unmatched.
    """

    if match_result.get("human_review_required"):

        return create_review_flag(
            reason="DRUG_PRODUCT_MATCH_REVIEW"
        )

    return {
        "human_review_required": False,
        "review_reason": None,
        "evidence_ids": [],
        "source": None,
        "safety_confirmed": False,
        "causality_confirmed": False
    }


if __name__ == "__main__":

    example = create_review_flag(
        reason="EVIDENCE_CONFLICT",
        evidence_ids=[
            "EV-004",
            "EV-017"
        ],
        source="Source A, Source B"
    )

    print("Human Review Result:")
    print(example)