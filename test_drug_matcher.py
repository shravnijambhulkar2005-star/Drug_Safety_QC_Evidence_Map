from matching.drug_matcher import match_drug


def test_exact_match_drug_a():
    records = [
        {
            "drug_product_identifier": "Drug A"
        },
        {
            "drug_product_identifier": "Drug B"
        }
    ]

    result = match_drug(records, "Drug A")

    assert result["match_status"] == "EXACT_MATCH"
    assert result["matched_products"] == ["drug a"]
    assert result["human_review_required"] is False


def test_drug_ab_does_not_match_drug_a():
    records = [
        {
            "drug_product_identifier": "Drug A"
        }
    ]

    result = match_drug(records, "Drug AB")

    assert result["match_status"] == "UNMATCHED"
    assert result["matched_products"] == []
    assert result["human_review_required"] is True


def test_partial_query_is_not_silently_matched():
    records = [
        {
            "drug_product_identifier": "Drug A"
        },
        {
            "drug_product_identifier": "Drug AB"
        }
    ]

    result = match_drug(records, "Drug")

    assert result["match_status"] == "UNMATCHED"
    assert result["matched_products"] == []
    assert result["human_review_required"] is True


def test_case_and_whitespace_normalization():
    records = [
        {
            "drug_product_identifier": "Drug A"
        }
    ]

    result = match_drug(records, "  DRUG   A  ")

    assert result["match_status"] == "EXACT_MATCH"
    assert result["matched_products"] == ["drug a"]
    assert result["human_review_required"] is False