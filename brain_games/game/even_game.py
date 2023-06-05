from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
BEGIN_RANGE = 1
END_RANGE = 100


def is_even(number):
    """Выявляем True и Fals"""
    return number % 2 == 0


def get_question_and_answer():
    """Получаем вопрос и ответ"""
    question = (randint(BEGIN_RANGE, END_RANGE))
    temp_answer = is_even(question)
    if temp_answer:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
