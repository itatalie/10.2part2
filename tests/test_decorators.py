import pytest
from src.decorators import log  # Импорт из src.decorators
from io import StringIO
import sys


@pytest.fixture
def capsys_wrapper(capsys):
    """
    Обертка для перехвата вывода в консоль.
    """

    def capture():
        captured = capsys.readouterr()
        return captured.out + captured.err  # Собираем вывод из stdout и stderr

    return capture


def test_log_to_console(capsys_wrapper):
    @log()
    def add(a: int, b: int) -> int:
        return a + b

    add(1, 2)
    output = capsys_wrapper()
    assert "Вызов функции add" in output
    assert "Функция add успешно завершена" in output
    assert "Результат: 3" in output


def test_log_to_file(tmp_path):
    log_file = tmp_path / "test_log.txt"

    @log(filename=str(log_file))
    def multiply(a: int, b: int) -> int:
        return a * b

    multiply(3, 4)
    with open(log_file, "r") as f:
        content = f.read()
    assert "multiply" in content
    assert "Результат: 12" in content


def test_log_error_handling(capsys_wrapper):
    @log()
    def divide(a: int, b: int) -> float:
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    output = capsys_wrapper()
    assert "Ошибка в функции divide" in output
    assert "ZeroDivisionError" in output
    assert "args=(1, 0)" in output