import re
from typing import List, Dict


def search_transactions_by_description(
    transactions: List[Dict], search_string: str
) -> List[Dict]:
    """
    Ищет транзакции, содержащие строку в поле 'description'.
    :param transactions: Список словарей с транзакциями.
    :param search_string: Строка для поиска.
    :return: Список словарей с найденными транзакциями.
    """
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    return [
        transaction
        for transaction in transactions
        if pattern.search(transaction.get("description", ""))
    ]
