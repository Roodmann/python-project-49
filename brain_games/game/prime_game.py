from random import randint


def quest_answer():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def is_prime(number):
    """Выявляем True и Fals"""
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return False
    return True


def ask_question_and_return_answer():
    """Задаем вопрос, получаем ответ"""
    question = (randint(2, 100))
    temp_answer = is_prime(question)
    if temp_answer:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
