from src.readers import read_csv_transactions, read_excel_transactions
from src.processing import filter_operations_by_status, reorder_operations_by_date, filter_rub_transactions
from src.search import search_transactions_by_description
from src.categories import count_transaction_categories
from typing import Dict


def print_transaction(transaction: Dict):
    date = transaction.get("date", "Дата не указана")
    description = transaction.get("description", "Описание отсутствует")
    amount = transaction.get("operationAmount", {}).get("amount", "Сумма не указана")
    currency = transaction.get("operationAmount", {}).get("currency", {}).get("name", "Валюта не указана")
    from_account = transaction.get("from", "Источник не указан")
    to_account = transaction.get("to", "Получатель не указан")

    print(f"{date} {description}")
    print(f"{from_account} -> {to_account}")
    print(f"Сумма: {amount} {currency}\n")


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    # Выбор источника данных
    file_type = input("Выберите источник данных (1 - JSON, 2 - CSV, 3 - XLSX): ")
    if file_type == "2":
        file_path = input("Введите путь к CSV-файлу: ")
        transactions = read_csv_transactions(file_path)
    elif file_type == "3":
        file_path = input("Введите путь к XLSX-файлу: ")
        transactions = read_excel_transactions(file_path)
    else:
        print("Неверный выбор. Завершение программы.")
        return

    # Фильтрация по статусу
    valid_statuses = {"EXECUTED", "CANCELED", "PENDING"}
    while True:
        status = input("Введите статус (EXECUTED, CANCELED, PENDING): ").upper()
        if status in valid_statuses:
            break
        print(f"Статус операции '{status}' недоступен.")
    filtered_transactions = filter_operations_by_status(transactions, status)

    # Сортировка по дате
    sort_choice = input("Отсортировать операции по дате? (да/нет): ").lower()
    if sort_choice == "да":
        order = input("По возрастанию или по убыванию? (возрастание/убывание): ").lower()
        descending = order == "убывание"
        filtered_transactions = reorder_operations_by_date(filtered_transactions, descending=descending)

    # Фильтрация рублевых транзакций
    rub_only = input("Выводить только рублевые транзакции? (да/нет): ").lower()
    if rub_only == "да":
        filtered_transactions = filter_rub_transactions(filtered_transactions)

    # Поиск по описанию
    search_choice = input("Фильтровать список транзакций по определенному слову в описании? (да/нет): ").lower()
    if search_choice == "да":
        search_string = input("Введите слово для поиска: ")
        filtered_transactions = search_transactions_by_description(filtered_transactions, search_string)

    # Подсчет категорий
    category_counts = count_transaction_categories(filtered_transactions)

    # Вывод результатов
    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
    else:
        print("\nРаспечатываю итоговый список транзакций...")
        for transaction in filtered_transactions:
            print_transaction(transaction)
        print(f"\nВсего банковских операций в выборке: {len(filtered_transactions)}")
        print("Количество операций по категориям:")
        for category, count in category_counts.items():
            print(f"{category}: {count}")