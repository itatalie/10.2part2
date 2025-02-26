import pytest
from src.generators import (
    filter_by_currency,
    generate_transaction_descriptions,
    generate_card_numbers,
)


# Фикстура для создания примера транзакций
@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод со счета на счет",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод со счета на счет",
        },
    ]


# Тестирование функции filter_by_currency
@pytest.mark.parametrize(
    "currency, expected_count",
    [
        ("USD", 2),  # Две транзакции в USD
        ("RUB", 1),  # Одна транзакция в RUB
        ("EUR", 0),  # Нет транзакций в EUR
    ],
)
def test_filter_by_currency(sample_transactions, currency, expected_count):
    """
    Проверяет корректность фильтрации транзакций по валюте.
    """
    result = list(filter_by_currency(sample_transactions, currency))
    assert (
        len(result) == expected_count
    ), f"Неверное количество транзакций для валюты {currency}"
    for transaction in result:
        assert (
            transaction["operationAmount"]["currency"]["code"] == currency
        ), f"Транзакция не соответствует заданной валюте {currency}"


# Тестирование функции generate_transaction_descriptions
def test_generate_transaction_descriptions(sample_transactions):
    """
    Проверяет корректность генерации описаний операций.
    """
    descriptions = list(generate_transaction_descriptions(sample_transactions))
    assert len(descriptions) == len(
        sample_transactions
    ), "Количество описаний не совпадает с количеством транзакций"
    for desc in descriptions:
        assert isinstance(desc, str), "Описание должно быть строкой"
        assert len(desc.strip()) > 0, "Описание не должно быть пустым"


# Тестирование функции generate_card_numbers
@pytest.mark.parametrize(
    "start, stop, expected_numbers",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (10, 12, ["0000 0000 0000 0010", "0000 0000 0000 0011", "0000 0000 0000 0012"]),
    ],
)
def test_generate_card_numbers(start, stop, expected_numbers):
    """
    Проверяет корректность генерации номеров карт.
    """
    result = list(generate_card_numbers(start, stop))
    assert result == expected_numbers, "Номера карт сгенерированы некорректно"
    for card_number in result:
        assert isinstance(card_number, str), "Номер карты должен быть строкой"
        assert (
            len(card_number.replace(" ", "")) == 16
        ), "Номер карты должен содержать 16 цифр без пробелов"
