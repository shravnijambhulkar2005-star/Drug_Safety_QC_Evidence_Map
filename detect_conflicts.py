"""
Conflict Detection Module

Purpose:
Identify potential conflicts between comparable evidence records.

Important:
Different observations are not automatically conflicts.

A potential conflict is identified only when records:
- refer to the same normalized drug/product
- describe comparable evidence types
- contain explicitly opposing observations

This module does not determine which evidence is correct.
It only identifies potential conflicts and requests human review.
"""


def normalize_text(value):
    """Normalize text for deterministic comparison."""

    if value is None:
        return ""

    return " ".join(
        str(value).strip().lower().split()
    )


def observations_are_opposite(observation_a, observation_b):
    """
    Identify explicitly opposing observations.

    This is intentionally conservative.
    It does not use scientific inference.
    """

    a = normalize_text(observation_a)
    b = normalize_text(observation_b)

    opposing_pairs = [
        (
            "signal present",
            "signal not observed"
        ),
        (
            "association observed",
            "no association observed"
        ),
        (
            "associated",
            "not associated"
        ),
        (
            "positive",
            "negative"
        )
    ]

    for first, second in opposing_pairs:

        if (
            first in a
            and second in b
        ):
            return True

        if (
            first in b
            and second in a
        ):
            return True

    return False


def are_comparable(record_a, record_b):
    """
    Determine whether two records are comparable
    for the simple deterministic conflict rules.

    Only records with the same evidence type are compared.

    This avoids treating unrelated evidence types such as:
    laboratory results and medication-error reports
    as direct conflicts.
    """

    type_a = normalize_text(
        record_a.get("evidence_type")
    )

    type_b = normalize_text(
        record_b.get("evidence_type")
    )

    return type_a == type_b


def detect_conflicts(records):
    """
    Detect potential conflicts between comparable evidence records.

    Original records are never modified or deleted.
    """

    conflicts = []

    drug_groups = {}

    # Group records by normalized drug/product
    for record in records:

        evidence_id = record.get(
            "evidence_id"
        )

        drug = normalize_text(
            record.get("drug_product")
        )

        observation = normalize_text(
            record.get("observation")
        )

        if (
            not evidence_id
            or not drug
            or not observation
        ):
            continue

        if drug not in drug_groups:
            drug_groups[drug] = []

        drug_groups[drug].append(
            record
        )

    # Compare records within each drug/product group
    for drug, group in drug_groups.items():

        for i in range(len(group)):

            for j in range(i + 1, len(group)):

                record_a = group[i]
                record_b = group[j]

                # Only compare comparable evidence types
                if not are_comparable(
                    record_a,
                    record_b
                ):
                    continue

                if observations_are_opposite(
                    record_a.get("observation"),
                    record_b.get("observation")
                ):

                    conflicts.append({
                        "conflict_type":
                            "OBSERVATION_CONFLICT",

                        "evidence_ids": [
                            record_a.get(
                                "evidence_id"
                            ),
                            record_b.get(
                                "evidence_id"
                            )
                        ],

                        "drug_product":
                            drug,

                        "observations": [
                            record_a.get(
                                "observation"
                            ),
                            record_b.get(
                                "observation"
                            )
                        ],

                        "sources": [
                            record_a.get(
                                "source"
                            ),
                            record_b.get(
                                "source"
                            )
                        ],

                        "human_review_required":
                            True
                    })

    return conflicts


if __name__ == "__main__":

    test_records = [
        {
            "evidence_id": "EV-004",
            "source": "Source A",
            "drug_product": "Drug A",
            "evidence_type": "LITERATURE",
            "observation": "Signal present"
        },
        {
            "evidence_id": "EV-017",
            "source": "Source B",
            "drug_product": "Drug A",
            "evidence_type": "LITERATURE",
            "observation": "Signal not observed"
        }
    ]

    conflicts = detect_conflicts(
        test_records
    )

    print(
        "Conflict Detection Result:"
    )

    print(conflicts)