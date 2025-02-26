import pytest
from src.processing import filter_operations_by_status, reorder_operations_by_date


#
@pytest.fixture
def sample_operations():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01"},
        {"id": 2, "state": "PENDING", "date": "2023-01-02"},
        {"id": 3, "state": "EXECUTED", "date": "2023-01-03"},
    ]


@pytest.mark.parametrize(
    "status, expected_ids", [("EXECUTED", [1, 3]), ("PENDING", [2]), ("CANCELED", [])]
)
def test_filter_operations_by_status(sample_operations, status, expected_ids):
    result = filter_operations_by_status(sample_operations, status)
    ids = [op["id"] for op in result]
    assert ids == expected_ids


@pytest.mark.parametrize(
    "descending, expected_ids", [(True, [3, 2, 1]), (False, [1, 2, 3])]
)
def test_reorder_operations_by_date(sample_operations, descending, expected_ids):
    result = reorder_operations_by_date(sample_operations, descending)
    ids = [op["id"] for op in result]
    assert ids == expected_ids
