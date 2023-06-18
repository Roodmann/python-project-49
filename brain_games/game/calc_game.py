import random


DESCRIPTION = 'What is the result of the expression?'
OPERATORS = ('+', '-', '*')
BEGIN_RANGE = 0
END_RANGE = 100


def get_question_and_answer():
    """Получаем вопрос и ответ"""
    first_num = random.randint(BEGIN_RANGE, END_RANGE)
    second_num = random.randint(BEGIN_RANGE, END_RANGE)
    symb_operator = random.choice(OPERATORS)
    correct_answer = calc_answer(first_num, symb_operator, second_num)
    question = f'{first_num} {symb_operator} {second_num}'
    return question, correct_answer


def calc_answer(first_num, operator, second_num):
    """Вычисляем значение по оператору"""
    if operator == '+':
        return first_num + second_num
    elif operator == '-':
        return first_num - second_num
    elif operator == '*':
        return first_num * second_num
