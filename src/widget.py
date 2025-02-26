from datetime import datetime
from typing import Union

def format_date(date_str: str) -> Union[str, str]:
    """
    Преобразует дату из ISO формата в читаемый вид.

    :param date_str: Дата в формате ISO.
    :return: Отформатированная дата или сообщение об ошибке.
    """
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        return "Неверный формат даты"