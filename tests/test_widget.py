import pytest
from src.widget import format_date

@pytest.mark.parametrize("date_str, expected", [
    ("2023-01-01T12:00:00.000000", "01.01.2023"),
    ("invalid-date", "Неверный формат даты")
])
def test_format_date(date_str, expected):
    result = format_date(date_str)
    assert result == expected