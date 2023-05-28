import random


OPERATORS = ('+', '-', '*')


def quest_answer():
    print('What is the result of the expression?')


def ask_question_and_return_answer():
    """Задаем вопрос, получаем ответ"""
    first_num = random.randint(0, 100)
    second_num = random.randint(0, 100)
    symb_operator = random.choice(OPERATORS)
    correct_answer = count_answer(first_num, symb_operator, second_num)
    question = f'{first_num} {symb_operator} {second_num}'
    return question, correct_answer


def count_answer(first_num, OPERATORS, second_num):
    """Проверка количество ответов"""
    if OPERATORS == '+':
        return first_num + second_num
    elif OPERATORS == '-':
        return first_num - second_num
    elif OPERATORS == '*':
        return first_num * second_num
