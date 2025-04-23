import pandas as pd
from typing import List, Dict


def read_csv_transactions(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из CSV-файла и возвращает их как список словарей.
    :param file_path: Путь к CSV-файлу.
    :return: Список словарей с транзакциями.
    """
    try:
        # Чтение CSV-файла
        df = pd.read_csv(file_path, sep=";", header=None)

        # Присвоение названий столбцам
        df.columns = [
            "id", "state", "date", "amount", "currency_name",
            "currency_code", "from", "to", "description"
        ]

        # Преобразование DataFrame в список словарей
        transactions = df.to_dict(orient="records")
        return transactions
    except Exception as e:
        raise ValueError(f"Ошибка при чтении CSV-файла: {str(e)}")


def read_excel_transactions(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из Excel-файла и возвращает их как список словарей.
    :param file_path: Путь к Excel-файлу.
    :return: Список словарей с транзакциями.
    """
    try:
        # Чтение Excel-файла
        df = pd.read_excel(file_path)

        # Преобразование DataFrame в список словарей
        transactions = df.to_dict(orient="records")
        return transactions
    except Exception as e:
        raise ValueError(f"Ошибка при чтении Excel-файла: {str(e)}")