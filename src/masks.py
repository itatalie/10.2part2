import logging
from pathlib import Path
from typing import Union

# Создаем объект логгера для модуля masks
logger = logging.getLogger(__name__)

# Настройка папки для логов
log_dir = Path(__file__).parent.parent / "logs"
log_dir.mkdir(exist_ok=True)

# Настройка file_handler
log_file = log_dir / "masks.log"
file_handler = logging.FileHandler(log_file, mode="w")  # mode="w" для перезаписи файла при каждом запуске
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)

# Добавляем handler к логгеру
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)  # Устанавливаем уровень логирования


def obfuscate_card_number(card_num: str) -> Union[str, str]:
    """
    Маскирует номер карты.
    :param card_num: Номер карты.
    :return: Маскированный номер карты или сообщение об ошибке.
    """
    if not card_num.isdigit() or len(card_num) != 16:
        logger.error(f"Некорректный номер карты: {card_num}")
        return "Некорректный номер карты"
    logger.info(f"Успешно замаскирован номер карты: {card_num[:4]} **** **** {card_num[-4:]}")
    return f"{card_num[:4]} {card_num[4:6]}** **** {card_num[-4:]}"


def obfuscate_account_number(account_num: str) -> Union[str, str]:
    """
    Маскирует номер счета.
    :param account_num: Номер счета.
    :return: Маскированный номер счета или сообщение об ошибке.
    """
    if not account_num.isdigit():
        logger.error(f"Некорректный номер счета: {account_num}")
        return "Некорректный номер счета"
    if len(account_num) <= 4:
        logger.info(f"Успешно замаскирован короткий номер счета: **{account_num[-2:]}")
        return f"**{account_num[-2:]}"
    logger.info(f"Успешно замаскирован длинный номер счета: **{account_num[-4:]}")
    return f"**{account_num[-4:]}"