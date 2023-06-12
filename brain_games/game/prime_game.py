from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
BEGIN_RANGE = 2
END_RANGE = 100


def is_prime(number):
    """Проверка числа на простоту"""
    for i in range(2, (number // number) + 1):
        if number % i == 0:
            return False
    return True


def get_question_and_answer():
    """Получаем вопрос и ответ"""
    question = (randint(BEGIN_RANGE, END_RANGE))
    temp_answer = is_prime(question)
    if temp_answer:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
