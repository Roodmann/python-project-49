import random


DESCRIPTION = 'Find the greatest common divisor of given numbers.'
BEGIN_RANGE = 1
END_RANGE = 100


def ask_question_and_return_answer():
    """Задаем вопрос, получаем ответ"""
    first_num = random.randint(BEGIN_RANGE, END_RANGE)
    second_num = random.randint(BEGIN_RANGE, END_RANGE)
    correct_answer = get_gcd(first_num, second_num)
    question = f'{first_num} {second_num}'
    return question, correct_answer


def get_gcd(first_num, second_num):
    """Нахождение НОД"""
    # Находим минимальное значение числа
    min_num = min(first_num, second_num)
    # Получаем min значение числа
    for i in range(BEGIN_RANGE, min_num + 1):
        # Проверка остатка
        if ((first_num % i == 0) and (second_num % i == 0)):
            gcd = i
    return gcd
