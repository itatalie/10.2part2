import pytest
from unittest.mock import patch
from src.processing import convert_transaction_currency

def test_convert_transaction_currency_rub():
    """
    Тестирует конвертацию для транзакции в RUB.
    """
    transaction = {
        "id": 1,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "100.00",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    }
    result = convert_transaction_currency(transaction)
    assert result == 100.00


@patch("requests.get")
def test_convert_transaction_currency_usd(mock_get):
    """
    Тестирует конвертацию для транзакции в USD.
    """
    mock_response = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 100},
        "result": 9000.0,
    }
    mock_get.return_value.json.return_value = mock_response

    transaction = {
        "id": 1,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "100.00",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    }
    result = convert_transaction_currency(transaction)
    assert result == 9000.0