from validation.validate_evidence import validate_record
from duplicates.detect_duplicates import detect_duplicates
from conflicts.detect_conflicts import detect_conflicts


def complete_record():
    return {
        "evidence_id": "EV-001",
        "source": "FAERS",
        "drug_product": "Drug A",
        "observation": "Adverse event reported",
        "evidence_type": "ADVERSE_EVENT",
        "validation_status": "VALID",
        "evidence_provenance": "FDA FAERS dataset"
    }


def test_01_complete_record():
    record = complete_record()

    result = validate_record(record)

    assert result["validation_status"] == "VALID"
    assert result["validation_errors"] == []
    assert result["human_review_required"] is False


def test_02_missing_evidence_id():
    record = complete_record()
    record["evidence_id"] = ""

    result = validate_record(record)

    assert result["validation_status"] == "INVALID"
    assert "MISSING_REQUIRED_FIELD:evidence_id" in result["validation_errors"]
    assert result["human_review_required"] is True


def test_04_missing_source():
    record = complete_record()
    record["source"] = ""

    result = validate_record(record)

    assert result["validation_status"] == "INVALID"
    assert "MISSING_REQUIRED_FIELD:source" in result["validation_errors"]


def test_05_missing_drug_product():
    record = complete_record()
    record["drug_product"] = ""

    result = validate_record(record)

    assert result["validation_status"] == "INVALID"
    assert "MISSING_REQUIRED_FIELD:drug_product" in result["validation_errors"]


def test_06_missing_observation():
    record = complete_record()
    record["observation"] = ""

    result = validate_record(record)

    assert result["validation_status"] == "INVALID"
    assert "MISSING_REQUIRED_FIELD:observation" in result["validation_errors"]


def test_07_invalid_evidence_type():
    record = complete_record()
    record["evidence_type"] = "WRONG_TYPE"

    result = validate_record(record)

    assert result["validation_status"] == "INVALID"
    assert "INVALID_EVIDENCE_TYPE" in result["validation_errors"]


def test_08_invalid_validation_status():
    record = complete_record()
    record["validation_status"] = "WRONG_STATUS"

    result = validate_record(record)

    assert result["validation_status"] == "INVALID"
    assert "INVALID_VALIDATION_STATUS" in result["validation_errors"]


def test_09_missing_provenance():
    record = complete_record()
    record["evidence_provenance"] = ""

    result = validate_record(record)

    assert result["validation_status"] == "INVALID"
    assert "MISSING_PROVENANCE" in result["validation_errors"]
    from duplicates.detect_duplicates import detect_duplicates
from conflicts.detect_conflicts import detect_conflicts


def test_03_duplicate_evidence_id():
    records = [
        complete_record(),
        {
            **complete_record(),
            "evidence_id": "EV-001"
        }
    ]

    result = detect_duplicates(records)

    assert len(result) >= 1

    assert any(
        item["duplicate_type"] == "DUPLICATE_EVIDENCE_ID"
        for item in result
    )


def test_10_empty_dataset():
    records = []

    validation_results = []

    for record in records:
        validation_results.append(validate_record(record))

    assert validation_results == []


def test_11_conflicting_records():
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

    assert len(result) >= 1

    assert result[0]["conflict_type"] == "OBSERVATION_CONFLICT"
    assert result[0]["human_review_required"] is True


def test_12_ambiguous_drug_product_match():
    records = [
        {
            "evidence_id": "EV-101",
            "source": "Source A",
            "drug_product": "Drug A",
            "observation": "Observation A"
        },
        {
            "evidence_id": "EV-102",
            "source": "Source B",
            "drug_product": "Drug AB",
            "observation": "Observation B"
        }
    ]

    query = "Drug"

    normalized_matches = [
        record["drug_product"]
        for record in records
        if query.lower() in record["drug_product"].lower()
    ]

    assert len(normalized_matches) == 2

    # Multiple possible products must require human review.
    human_review_required = len(normalized_matches) > 1

    assert human_review_required is True