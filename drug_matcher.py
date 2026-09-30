import json
import argparse
from pathlib import Path


def normalize_name(name):
    """
    Normalize a drug/product name for deterministic comparison.

    Only whitespace and letter case are normalized.
    No fuzzy matching is performed.
    """

    if name is None:
        return ""

    return " ".join(
        name.strip().lower().split()
    )


def get_product_names(records):
    """Return unique normalized product names."""

    product_names = set()

    for record in records:

        product = record.get(
            "drug_product_identifier",
            ""
        )

        normalized = normalize_name(
            product
        )

        if normalized:
            product_names.add(
                normalized
            )

    return sorted(product_names)


def match_drug(records, query):
    """
    Deterministically match a drug/product.

    Possible results:

    EXACT_MATCH
    AMBIGUOUS_MATCH
    UNMATCHED
    """

    normalized_query = normalize_name(
        query
    )

    if not normalized_query:

        return {
            "query": query,
            "match_status": "UNMATCHED",
            "matched_products": [],
            "human_review_required": True,
            "reason": "Empty drug/product query"
        }

    products = get_product_names(
        records
    )

    exact_matches = [
        product
        for product in products
        if product == normalized_query
    ]

    if len(exact_matches) == 1:

        return {
            "query": query,
            "match_status": "EXACT_MATCH",
            "matched_products": exact_matches,
            "human_review_required": False,
            "reason": "Exactly one normalized product identity matched"
        }

    if len(exact_matches) > 1:

        return {
            "query": query,
            "match_status": "AMBIGUOUS_MATCH",
            "matched_products": exact_matches,
            "human_review_required": True,
            "reason": "Multiple exact product identities were found"
        }

    return {
        "query": query,
        "match_status": "UNMATCHED",
        "matched_products": [],
        "human_review_required": True,
        "reason": "No exact normalized product identity matched"
    }


def load_normalized_json(json_file):
    """Load canonical normalized evidence."""

    path = Path(json_file)

    if not path.exists():

        raise FileNotFoundError(
            f"JSON file not found: {json_file}"
        )

    with path.open(
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

    return data.get(
        "records",
        []
    )


def main():

    parser = argparse.ArgumentParser(
        description=
        "Deterministic drug/product matcher"
    )

    parser.add_argument(
        "--file",
        required=True,
        help=
        "Path to normalized evidence JSON"
    )

    parser.add_argument(
        "--drug",
        required=True,
        help=
        "Drug/product to match"
    )

    args = parser.parse_args()

    try:

        records = load_normalized_json(
            args.file
        )

        result = match_drug(
            records,
            args.drug
        )

        print(
            json.dumps(
                result,
                indent=4
            )
        )

    except FileNotFoundError as error:

        print(
            f"ERROR: {error}"
        )


if __name__ == "__main__":
    main()