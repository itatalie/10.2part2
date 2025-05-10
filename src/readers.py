# src/readers.py
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
        # Преобразование типов данных
        df["id"] = df["id"].astype(str)
        df["amount"] = df["amount"].astype(float)
        # Преобразование DataFrame в список словарей
        transactions = df.to_dict(orient="records")
        return transactions
    except Exception as e:
        raise ValueError(f"Ошибка при чтении CSV-файла: {str(e)}")


def read_excel_transactions(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из XLSX-файла и возвращает их как список словарей.
    :param file_path: Путь к XLSX-файлу.
    :return: Список словарей с транзакциями.
    """
    try:
        # Чтение XLSX-файла
        df = pd.read_excel(file_path)
        # Преобразование типов данных
        df["id"] = df["id"].astype(str)
        df["amount"] = df["amount"].astype(float)
        # Преобразование DataFrame в список словарей
        transactions = df.to_dict(orient="records")
        return transactions
    except Exception as e:
        raise ValueError(f"Ошибка при чтении XLSX-файла: {str(e)}")


def read_json_transactions(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из JSON-файла и возвращает их как список словарей.
    :param file_path: Путь к JSON-файлу.
    :return: Список словарей с транзакциями.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            transactions = json.load(file)
        return transactions
    except Exception as e:
        raise ValueError(f"Ошибка при чтении JSON-файла: {str(e)}")