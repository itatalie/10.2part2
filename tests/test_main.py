import pytest
from unittest.mock import patch
from src.main import main


@patch(
    "builtins.input",
    side_effect=["2", "data/transactions.csv", "EXECUTED", "нет", "нет", "нет"],
)
@patch("src.readers.read_csv_transactions")
def test_main(mock_read_csv, mock_input):
    mock_read_csv.return_value = [
        {"id": 1, "state": "EXECUTED", "description": "Перевод организации"},
        {"id": 2, "state": "PENDING", "description": "Перевод со счета на счет"},
    ]
    main()


