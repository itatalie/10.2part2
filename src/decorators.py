import sys
from functools import wraps
from typing import Callable, Any


def log(filename: str = None) -> Callable:
    """
    Декоратор для логирования вызова функции, ее аргументов, результата или ошибки.

    :param filename: Имя файла для записи логов. Если не указано, логи выводятся в консоль.
    :return: Декорированный объект функции.
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            try:
                # Логирование начала выполнения
                log_message = f"Вызов функции {func.__name__} с аргументами: args={args}, kwargs={kwargs}\n"
                if filename:
                    with open(filename, "a") as f:
                        f.write(log_message)
                else:
                    print(log_message, end="", file=sys.stdout)

                # Выполнение функции
                result = func(*args, **kwargs)

                # Логирование успешного завершения
                log_message = f"Функция {func.__name__} успешно завершена. Результат: {result}\n"
                if filename:
                    with open(filename, "a") as f:
                        f.write(log_message)
                else:
                    print(log_message, end="", file=sys.stdout)

                return result
            except Exception as e:
                # Логирование ошибки
                error_message = f"Ошибка в функции {func.__name__}: {type(e).__name__}. Входные данные: args={args}, kwargs={kwargs}\n"
                if filename:
                    with open(filename, "a") as f:
                        f.write(error_message)
                else:
                    print(error_message, end="", file=sys.stderr)
                raise

        return wrapper

    return decorator