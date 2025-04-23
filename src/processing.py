from typing import List, Dict

def filter_operations_by_status(operations: List[Dict], status: str) -> List[Dict]:
    """
    Фильтрует операции по статусу.
    :param operations: Список операций.
    :param status: Статус для фильтрации.
    :return: Отфильтрованный список операций.
    """
    return [
        op for op in operations
        if isinstance(op.get("state"), str) and op.get("state", "").upper() == status.upper()
    ]

def reorder_operations_by_date(operations: List[Dict], descending: bool = False) -> List[Dict]:
    """
    Сортирует операции по дате.
    :param operations: Список операций.
    :param descending: True, если сортировка по убыванию.
    :return: Отсортированный список операций.
    """
    return sorted(
        operations,
        key=lambda x: x.get("date", ""),
        reverse=descending
    )

def filter_rub_transactions(operations: List[Dict]) -> List[Dict]:
    """
    Фильтрует операции, в которых валюта — рубли (RUB).
    :param operations: Список операций.
    :return: Отфильтрованный список операций.
    """
    return [
        op for op in operations
        if op.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"
    ]