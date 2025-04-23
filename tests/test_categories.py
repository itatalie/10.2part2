from src.categories import count_transaction_categories


def test_count_transaction_categories():
    transactions = [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Открытие вклада"},
        {"id": 3, "description": "Перевод со счета на счет"},
        {"id": 4, "description": "Перевод организации"},
    ]
    result = count_transaction_categories(transactions)
    assert result["Перевод организации"] == 2
    assert result["Открытие вклада"] == 1
    assert result["Перевод со счета на счет"] == 1
