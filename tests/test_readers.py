import pytest
import pandas as pd  # Импортируем библиотеку pandas
from src.readers import read_csv_transactions, read_excel_transactions, read_json_transactions
from pathlib import Path


def test_read_csv_transactions(tmp_path):
    file = tmp_path / "test.csv"
    file.write_text("1;EXECUTED;2023-01-01T12:00:00Z;100.5;Ruble;RUB;;Счет 1234567890;Перевод организации\n")
    transactions = read_csv_transactions(file)
    assert len(transactions) == 1
    assert transactions[0]["id"] == "1"
    assert transactions[0]["amount"] == 100.5


def test_read_excel_transactions(tmp_path):
    file = tmp_path / "test.xlsx"
    df = pd.DataFrame({
        "id": ["1"],
        "state": ["EXECUTED"],
        "date": ["2023-01-01T12:00:00Z"],
        "amount": [100.5],
        "currency_name": ["Ruble"],
        "currency_code": ["RUB"],
        "from": [""],
        "to": ["Счет 1234567890"],
        "description": ["Перевод организации"]
    })
    df.to_excel(file, index=False)
    transactions = read_excel_transactions(file)
    assert len(transactions) == 1
    assert transactions[0]["id"] == "1"
    assert transactions[0]["amount"] == 100.5


def test_read_json_transactions(tmp_path):
    file = tmp_path / "test.json"
    file.write_text('[{"id": "1", "state": "EXECUTED", "date": "2023-01-01T12:00:00Z", "amount": 100.5}]')
    transactions = read_json_transactions(file)
    assert len(transactions) == 1
    assert transactions[0]["id"] == "1"
    assert transactions[0]["amount"] == 100.5