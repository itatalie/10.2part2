import re
from collections import Counter


def search_transactions_by_description(transactions: list, search_string: str) -> list:
    """
    Ищет транзакции по описанию с использованием регулярных выражений.
    :param transactions: Список словарей с транзакциями.
    :param search_string: Строка для поиска.
    :return: Список словарей с найденными транзакциями.
    """
    pattern = re.compile(search_string, re.IGNORECASE)
    return [
        transaction
        for transaction in transactions
        if pattern.search(transaction.get("description", ""))
    ]


def count_transaction_categories(transactions: list, categories: list) -> dict:
    """
    Подсчитывает количество операций по указанным категориям.
    :param transactions: Список словарей с операциями.
    :param categories: Список категорий для подсчета.
    :return: Словарь с количеством операций по категориям.
    """
    descriptions = [transaction.get("description") for transaction in transactions]
    counter = Counter(descriptions)
    return {category: counter[category] for category in categories}
