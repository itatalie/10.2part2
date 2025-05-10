from src.readers import read_csv_transactions, read_excel_transactions, read_json_transactions
from src.processing import (
    filter_operations_by_status,
    reorder_operations_by_date,
    count_transaction_categories
)
import os

def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Введите номер пункта: ").strip()

    file_path = input("Введите путь к файлу: ").strip()

    # Проверяем, существует ли файл
    if not os.path.exists(file_path):
        print(f"Ошибка: Файл '{file_path}' не найден.")
        return

    try:
        if choice == "1":
            print("Для обработки выбран JSON-файл.")
            transactions = read_json_transactions(file_path)
        elif choice == "2":
            print("Для обработки выбран CSV-файл.")
            transactions = read_csv_transactions(file_path)
        elif choice == "3":
            print("Для обработки выбран XLSX-файл.")
            transactions = read_excel_transactions(file_path)
        else:
            print("Неверный выбор. Программа завершена.")
            return
    except Exception as e:
        print(f"Ошибка при чтении файла: {str(e)}")
        return

    # Фильтрация по статусу
    status = input("Введите статус (EXECUTED, CANCELED, PENDING): ").strip().upper()
    filtered_transactions = filter_operations_by_status(transactions, status)

    # Сортировка по дате
    sort_choice = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
    if sort_choice == "да":
        order = input("По возрастанию или по убыванию? (возрастание/убывание): ").strip().lower()
        descending = order != "возрастание"
        filtered_transactions = reorder_operations_by_date(filtered_transactions, descending)

    # Подсчет категорий
    categories = ["Перевод организации", "Открытие вклада"]
    category_counts = count_transaction_categories(filtered_transactions, categories)
    print("Количество операций по категориям:")
    for category, count in category_counts.items():
        print(f"{category}: {count}")

    # Вывод результата
    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
    else:
        print("Распечатываю итоговый список транзакций...")
        for transaction in filtered_transactions:
            print(f"{transaction.get('date', 'Дата отсутствует')} {transaction.get('description', 'Описание отсутствует')}")
            print(f"Сумма: {transaction.get('amount', 'Сумма отсутствует')} {transaction.get('currency_code', 'Валюта отсутствует')}")
            print()

if __name__ == "__main__":
    main()