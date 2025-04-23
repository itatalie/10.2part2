from collections import Counter
from typing import List, Dict


def count_transaction_categories(transactions: List[Dict]) -> Dict[str, int]:
    """
    Подсчитывает количество операций каждой категории.
    :param transactions: Список словарей с транзакциями.
    :return: Словарь, где ключи — категории, а значения — количество операций.
    """
    categories = [
        transaction.get("description", "No Description") for transaction in transactions
    ]
    return dict(Counter(categories))
