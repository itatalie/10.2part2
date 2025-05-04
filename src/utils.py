from typing import List, Dict
from datetime import datetime


def filter_operations_by_status(
    operations_list: List[Dict], operation_status: str = "EXECUTED"
) -> List[Dict]:
    """
    Фильтрует операции по указанному статусу.
    :param operations_list: Список словарей с операциями.
    :param operation_status: Статус для фильтрации (по умолчанию 'EXECUTED').
    :return: Отфильтрованный список операций.
    """
    operation_status = operation_status.upper()
    return [
        op for op in operations_list if op.get("state", "").upper() == operation_status
    ]


def reorder_operations_by_date(
    operations_list: List[Dict], descending: bool = True
) -> List[Dict]:
    """
    Сортирует операции по дате.
    :param operations_list: Список словарей с операциями.
    :param descending: Порядок сортировки (по умолчанию убывание).
    :return: Отсортированный список операций.
    """
    return sorted(
        operations_list,
        key=lambda op: datetime.strptime(op["date"], "%Y-%m-%dT%H:%M:%S%z"),
        reverse=descending,
    )


def filter_rub_transactions(operations_list: List[Dict]) -> List[Dict]:
    """
    Фильтрует операции только в рублях.
    :param operations_list: Список словарей с операциями.
    :return: Отфильтрованный список операций.
    """
    return [
        op
        for op in operations_list
        if op.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"
    ]
