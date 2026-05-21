"""
data_quality_checker.py
------------------------
Validates rows of data before loading into a warehouse.
Checks for: missing fields, wrong data types, out-of-range values.

Author: Mounish
Date: 2026-05-21
"""

from typing import Any
SCHEMA : dict[str, type] = {
    "order_id":   int,
    "customer":   str,
    "amount":     float,
    "status":     str,
    "quantity":   int,
}

RANGE_RULES : dict[str, tuple] = {
    "amount":   (0.0, 1_000_000.0),
    "quantity": (1, 10_000),
}

def check_missing_fields(
        row : dict[str, Any],
        row_index : int
) -> list[str]:
    '''check if any fields are missing '''
    errors = []

    for field in SCHEMA:
        if field not in row:
            errors.append(f"Row {row_index} : missing required field '{field}'"
            )
    return errors

def check_data_types (
        row : dict[str, Any],
        row_index : int
) -> list[str]:
    """ check the data type of value's in each row  """
    errors = []
    for field, expected_type in SCHEMA.items():
        if field not in row:
            continue
        if not isinstance(row[field], expected_type) :
            errors.append(
            f"Row {row_index}: field '{field}' expected "
            f"{expected_type.__name__} but got "
            f"{type(row[field]).__name__} (value: {row[field]})"
        )
    return errors

def check_value_ranges(
        row : dict[str, Any],
        row_index : int
) -> list[str] :
    errors = []
    for field, (min_val, max_val) in RANGE_RULES.items():
        if field not in row:
            continue
        if not isinstance(row[field], (int, float)):
            continue
        if not (min_val <= row[field] <= max_val):
            errors.append(
                f"Row {row_index} : field {field} value {row[field]}"
                f"is out of range ({min_val}, {max_val})"
            )
    return errors

def validate(data : list[dict[str, Any]]) -> dict:
    "Returning all Validation checks on a list of rows. Returns a report"
    all_errors = []

    for index, row in enumerate(data):
        all_errors += check_missing_fields(row, index)
        all_errors += check_value_ranges(row, index)
        all_errors += check_data_types(row, index)
    
    total = len(data)
    failed = len(set(
        int(e.split("Row ")[1].split(":")[0])
        for e in all_errors
    ))

    return {
        "total_rows" : total,
        "passed" : total - failed,
        "failed" : failed,
        "errors" :  all_errors,
        "is_valid" :len(all_errors) == 0
    }

if __name__ == "__main__":
    test_data = [
        {"order_id": 1, "customer": "John", "amount": 49.99, "status": "paid", "quantity": 2},
        {"order_id": 2, "customer": "Sara", "amount": -100.0, "status": "pending", "quantity": 1},
        {"order_id": 3, "amount": "free", "status": "paid", "quantity": 5}
    ]

    report = validate(test_data)

    print(f"Total rows:  {report['total_rows']}")
    print(f"Passed:      {report['passed']}")
    print(f"Failed:      {report['failed']}")
    print(f"Is valid:    {report['is_valid']}")
    print("\nErrors found:")
    for error in report['errors']:
        print(f"  - {error}")