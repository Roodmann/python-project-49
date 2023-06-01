import random


DESCRIPTION = 'What number is missing in the progression?'
NULL = 0
BEGIN_RANGE = 1
END_RANGE = 10


def ask_question_and_return_answer():
    """Задаем вопрос, получаем ответ"""
    question, correct_answer = get_progression()
    return question, correct_answer


def get_progression():
    """Получаем прогрессию"""
    num = []
    first_num = random.randint(BEGIN_RANGE, END_RANGE)
    num.append(str(first_num))
    step = random.randint(BEGIN_RANGE, END_RANGE)
    for _ in range(END_RANGE):
        temp = first_num + step
        num.append(str(temp))
        first_num = temp
    #  Длина индекса прогрессии
    skip_index = random.randint(NULL, len(num) - 1)
    answer = str(num[skip_index])
    num[skip_index] = '..'
    question = " ".join(num).strip()
    return question, answer
