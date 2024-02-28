"""Игра угадай число от 1 до 100
Компьютер угадывает число за минимальное количество попыток
"""


def predict_func(number: int = 1) -> int:
    """Функция угадывания числа

    Args:
        number (int): загаданное число

    Returns:
        int: число попыток
    """
    count = 0  # счетчик попыток
    predict_number = 50  # предполагаемое число
    current_gap = 50  # текущий шаг

    while number != predict_number:
        count += 1
        if current_gap > 1:
            current_gap = current_gap // 2
        if number > predict_number:
            predict_number += current_gap
        elif number < predict_number:
            predict_number -= current_gap
    return count  # выход из цикла если угадали
