from src.processing import (
    search_transactions_by_description,
    count_transaction_categories,
)
from src.utils import (
    filter_operations_by_status,
    reorder_operations_by_date,
    filter_rub_transactions,
)


def main():
    # Пример данных
    transactions = [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод организации",
        },
        {
            "id": 2,
            "state": "CANCELED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод со счета на счет",
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Открытие вклада",
        },
    ]

    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Введите номер пункта: ")

    if choice == "1":
        print("Для обработки выбран JSON-файл.")
    else:
        print("Обработка других форматов временно недоступна.")
        return

    # Фильтрация по статусу
    while True:
        status = input("Введите статус (EXECUTED, CANCELED, PENDING): ").strip().upper()
        if status in ["EXECUTED", "CANCELED", "PENDING"]:
            filtered_transactions = filter_operations_by_status(transactions, status)
            print(f"Операции отфильтрованы по статусу '{status}'.")
            break
        else:
            print("Статус операции недоступен. Попробуйте снова.")

    # Сортировка по дате
    sort_choice = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
    if sort_choice == "да":
        order = (
            input("По возрастанию или по убыванию? (возрастание/убывание): ")
            .strip()
            .lower()
        )
        descending = order != "возрастание"
        filtered_transactions = reorder_operations_by_date(
            filtered_transactions, descending
        )

    # Фильтрация рублевых транзакций
    rub_choice = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
    if rub_choice == "да":
        filtered_transactions = filter_rub_transactions(filtered_transactions)

    # Поиск по описанию
    search_choice = (
        input(
            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет: "
        )
        .strip()
        .lower()
    )
    if search_choice == "да":
        search_string = input("Введите слово для поиска: ").strip()
        filtered_transactions = search_transactions_by_description(
            filtered_transactions, search_string
        )

    # Вывод результата
    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
    else:
        print("Распечатываю итоговый список транзакций...")
        for transaction in filtered_transactions:
            print(f"{transaction['date']} {transaction['description']}")
            print(
                f"Сумма: {transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']['code']}"
            )
            print()

    # Подсчет категорий
    categories = ["Перевод организации", "Открытие вклада"]
    category_counts = count_transaction_categories(filtered_transactions, categories)
    print("Количество операций по категориям:")
    for category, count in category_counts.items():
        print(f"{category}: {count}")


if __name__ == "__main__":
    main()
