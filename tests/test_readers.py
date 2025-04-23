# tests/test_readers.py
import pytest
from unittest.mock import patch
import pandas as pd
from src.readers import read_csv_transactions, read_excel_transactions

@patch("pandas.read_csv")
def test_read_csv_transactions(mock_read_csv):
    # Мокируем DataFrame
    mock_data = pd.DataFrame({
        "id": [1, 2],
        "state": ["EXECUTED", "PENDING"],
        "date": ["2023-01-01", "2023-01-02"],
        "amount": [100, 200],
        "currency_name": ["USD", "EUR"],
        "currency_code": ["USD", "EUR"],
        "from": ["A", "B"],
        "to": ["C", "D"],
        "description": ["Test1", "Test2"]
    })
    mock_read_csv.return_value = mock_data

    # Вызов функции
    result = read_csv_transactions("dummy.csv")

    # Проверка результата
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["state"] == "PENDING"

@patch("pandas.read_excel")
def test_read_excel_transactions(mock_read_excel):
    # Мокируем DataFrame
    mock_data = pd.DataFrame({
        "id": [1, 2],
        "state": ["EXECUTED", "PENDING"],
        "date": ["2023-01-01", "2023-01-02"],
        "amount": [100, 200],
        "currency_name": ["USD", "EUR"],
        "currency_code": ["USD", "EUR"],
        "from": ["A", "B"],
        "to": ["C", "D"],
        "description": ["Test1", "Test2"]
    })
    mock_read_excel.return_value = mock_data

    # Вызов функции
    result = read_excel_transactions("dummy.xlsx")

    # Проверка результата
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["state"] == "PENDING"