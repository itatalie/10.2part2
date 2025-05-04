from src.processing import (
    search_transactions_by_description,
    count_transaction_categories,
)


def test_search_transactions_by_description():
    transactions = [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Открытие вклада"},
    ]
    result = search_transactions_by_description(transactions, "организации")
    assert len(result) == 1
    assert result[0]["id"] == 1


def test_count_transaction_categories():
    transactions = [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Открытие вклада"},
        {"id": 3, "description": "Перевод организации"},
    ]
    categories = ["Перевод организации", "Открытие вклада"]
    result = count_transaction_categories(transactions, categories)
    assert result == {"Перевод организации": 2, "Открытие вклада": 1}
