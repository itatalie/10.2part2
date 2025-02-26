import pytest
from src.masks import obfuscate_card_number, obfuscate_account_number


@pytest.mark.parametrize(
    "card_num, expected",
    [
        ("9876543210987654", "9876 54** **** 7654"),
        ("1234", "Некорректный номер карты"),
        ("abcd1234efgh5678", "Некорректный номер карты"),
    ],
)
def test_obfuscate_card_number(card_num, expected):
    result = obfuscate_card_number(card_num)
    assert result == expected


@pytest.mark.parametrize(
    "account_num, expected",
    [
        ("98765432109876541234", "**1234"),
        ("98765432", "**5432"),
        ("1234", "**34"),
        ("abcd", "Некорректный номер счета"),
    ],
)
def test_obfuscate_account_number(account_num, expected):
    result = obfuscate_account_number(account_num)
    assert result == expected
