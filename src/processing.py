from typing import List


def filter_operations_by_status(
    operations_list: List[dict], operation_status: str = "EXECUTED"
) -> List[dict]:
    """
    Фильтрует операции по указанному статусу.

    :param operations_list: Список словарей с операциями.
    :param operation_status: Статус для фильтрации (по умолчанию 'EXECUTED').
    :return: Отфильтрованный список операций.
    """
    return [op for op in operations_list if op.get("state") == operation_status]


def reorder_operations_by_date(
    operations_list: List[dict], descending: bool = True
) -> List[dict]:
    """
    Сортирует операции по дате.
    :param operations_list: Список словарей с операциями.
    :param descending: Порядок сортировки (по умолчанию убывание).
    :return: Отсортированный список операций.
    """
    return sorted(operations_list, key=lambda x: x.get("date", ""), reverse=descending)