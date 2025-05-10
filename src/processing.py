from collections import Counter
from typing import List, Dict

def filter_operations_by_status(transactions: List[Dict], status: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует операции по указанному статусу.
    :param transactions: Список транзакций.
    :param status: Статус для фильтрации (по умолчанию 'EXECUTED').
    :return: Отфильтрованный список транзакций.
    """
    return [t for t in transactions if t.get("state", "").upper() == status.upper()]


def reorder_operations_by_date(transactions: List[Dict], descending: bool = True) -> List[Dict]:
    """
    Сортирует операции по дате.
    :param transactions: Список транзакций.
    :param descending: Порядок сортировки (по умолчанию убывание).
    :return: Отсортированный список транзакций.
    """
    return sorted(
        transactions,
        key=lambda t: t.get("date", ""),
        reverse=descending
    )


def count_transaction_categories(transactions: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций по заданным категориям.
    :param transactions: Список транзакций.
    :param categories: Список категорий для подсчета.
    :return: Словарь с количеством операций по категориям.
    """
    descriptions = [t.get("description", "") for t in transactions]
    counter = Counter(descriptions)
    return {category: counter[category] for category in categories}