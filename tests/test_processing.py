from unittest.mock import patch
from src.processing import convert_currency
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()

@patch("requests.get")
def test_convert_currency(mock_get):
    """
    Тестирует функцию конвертации валюты с моком внешнего API.
    """
    # Мокаем ответ от API
    mock_response = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 100},
        "result": 9000.0,
    }
    mock_get.return_value.json.return_value = mock_response

    # Вызываем функцию конвертации
    result = convert_currency(100, "USD", "RUB")

    # Проверяем результат
    assert result == 9000.0

@patch("requests.get")
def test_convert_currency_same_currency(mock_get):
    """
    Тестирует функцию конвертации валюты, когда исходная и целевая валюты совпадают.
    """
    result = convert_currency(100, "RUB", "RUB")
    assert result == 100

@patch("requests.get")
def test_convert_currency_api_error(mock_get):
    """
    Тестирует обработку ошибок при вызове внешнего API.
    """
    mock_get.side_effect = Exception("API недоступно")
    try:
        convert_currency(100, "USD", "RUB")
    except ValueError as e:
        assert str(e) == "Ошибка при конвертации валюты: API недоступно"