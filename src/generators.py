from typing import Iterator, List

def filter_by_currency(transactions: List[dict], currency_code: str) -> Iterator[dict]:
    """
    Возвращает итератор с транзакциями в указанной валюте.

    :param transactions: Список словарей с транзакциями.
    :param currency_code: Код валюты для фильтрации.
    :return: Итератор с транзакциями.
    """
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency_code:
            yield transaction

def generate_transaction_descriptions(transactions: List[dict]) -> Iterator[str]:
    """
    Генерирует описания операций из списка транзакций.

    :param transactions: Список словарей с транзакциями.
    :return: Описание каждой операции.
    """
    for transaction in transactions:
        yield transaction.get("description", "Описание отсутствует")

def generate_card_numbers(start: int, stop: int) -> Iterator[str]:
    """
    Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX.

    :param start: Начальное значение диапазона.
    :param stop: Конечное значение диапазона.
    :return: Номер карты в формате XXXX XXXX XXXX XXXX.
    """
    for number in range(start, stop + 1):
        formatted_number = f"{number:016}"
        formatted_number = ' '.join([formatted_number[i:i+4] for i in range(0, len(formatted_number), 4)])
        yield formatted_number
