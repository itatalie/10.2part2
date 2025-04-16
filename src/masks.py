from typing import Union


def obfuscate_card_number(card_num: str) -> Union[str, str]:
    """
    Маскирует номер карты.

    :param card_num: Номер карты.
    :return: Маскированный номер карты или сообщение об ошибке.
    """
    if not card_num.isdigit() or len(card_num) != 16:
        return "Некорректный номер карты"
    return f"{card_num[:4]} {card_num[4:6]}** **** {card_num[-4:]}"


def obfuscate_account_number(account_num: str) -> Union[str, str]:
    """
    Маскирует номер счета.

    :param account_num: Номер счета.
    :return: Маскированный номер счета или сообщение об ошибке.
    """
    if not account_num.isdigit():
        return "Некорректный номер счета"
    if len(account_num) <= 4:
        return f"**{account_num[-2:]}"
    return f"**{account_num[-4:]}"
