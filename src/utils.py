import json
from pathlib import Path
import logging

# Настройка логгера
logger = logging.getLogger(__name__)

log_dir = Path(__file__).parent.parent / "logs"
log_dir.mkdir(exist_ok=True)

# Настраиваем файловый обработчик
log_file = log_dir / "utils.log"
file_handler = logging.FileHandler(log_file)
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def read_json_file(file_path: str):
    """
    Читает JSON-файл и возвращает список словарей с данными о финансовых транзакциях.

    :param file_path: Путь к JSON-файлу.
    :return: Список словарей с данными о транзакциях или пустой список.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info("Успешно загружены данные из файла")
                return data
            logger.warning("Файл содержит не список")
            return []
    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}")
        return []
    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON в файле: {file_path}")
        return []