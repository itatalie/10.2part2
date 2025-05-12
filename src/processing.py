import requests
from os import getenv
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()

def convert_transaction_currency(transaction: dict) -> float:
    """
    Конвертирует сумму транзакции в RUB, если валюта не RUB.
    :param transaction: Транзакция в виде словаря.
    :return: Сумма в рублях (RUB).
    """
    amount = float(transaction["operationAmount"]["amount"])
    currency_code = transaction["operationAmount"]["currency"]["code"]

    # Если валюта уже RUB, возвращаем сумму без изменений
    if currency_code == "RUB":
        return amount

    # Получаем API-ключ из переменных окружения
    api_key = getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY не найден в переменных окружения.")

    # URL для конвертации валют через API
    url = f"https://api.apilayer.com/exchangerates_data/convert"
    headers = {"apikey": api_key}
    params = {
        "from": currency_code,
        "to": "RUB",
        "amount": amount,
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get("result", amount)  # Возвращаем сконвертированную сумму
    except Exception as e:
        raise ValueError(f"Ошибка при конвертации валюты: {e}")