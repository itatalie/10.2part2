import pytest
from src.processing import (
    filter_operations_by_status,
    reorder_operations_by_date,
    count_transaction_categories
)

@pytest.fixture
def sample_transactions():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01", "description": "Перевод организации"},
        {"id": 2, "state": "CANCELED", "date": "2023-01-02", "description": "Открытие вклада"},
        {"id": 3, "state": "EXECUTED", "date": "2023-01-03", "description": "Перевод со счета на счет"},
    ]


def test_filter_operations_by_status(sample_transactions):
    result = filter_operations_by_status(sample_transactions, "EXECUTED")
    assert len(result) == 2
    assert all(t["state"] == "EXECUTED" for t in result)


def test_reorder_operations_by_date(sample_transactions):
    result = reorder_operations_by_date(sample_transactions, descending=True)
    dates = [t["date"] for t in result]
    assert dates == ["2023-01-03", "2023-01-02", "2023-01-01"]


def test_count_transaction_categories(sample_transactions):
    categories = ["Перевод организации", "Открытие вклада"]
    result = count_transaction_categories(sample_transactions, categories)
    assert result == {"Перевод организации": 1, "Открытие вклада": 1}