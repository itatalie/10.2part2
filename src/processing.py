import requests
from os import getenv
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()

def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
    """
    Конвертирует сумму из одной валюты в другую через внешнее API.
    :param amount: Сумма для конвертации.
    :param from_currency: Исходная валюта (например, 'USD').
    :param to_currency: Целевая валюта (например, 'RUB').
    :return: Сконвертированная сумма в целевой валюте.
    """
    if from_currency == to_currency:
        return amount

    api_key = getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY не найден в переменных окружения.")

    url = f"https://api.apilayer.com/exchangerates_data/convert"
    headers = {"apikey": api_key}
    params = {
        "from": from_currency,
        "to": to_currency,
        "amount": amount,
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get("result", amount)
    except Exception as e:
        raise ValueError(f"Ошибка при конвертации валюты: {e}")