import random


def quest_answer():
    print('What number is missing in the progression?')


def ask_question_and_return_answer():
    """Задаем вопрос, получаем ответ"""
    question, correct_answer = get_progression()
    return question, correct_answer


def get_progression():
    """Получаем прогрессию"""
    num = []
    first_num = random.randint(1, 10)
    num.append(str(first_num))
    step = random.randint(1, 10)
    for _ in range(10):
        temp = first_num + step
        num.append(str(temp))
        first_num = temp
    temp_num = random.randint(1, 10)
    answer = str(num[temp_num])
    num[temp_num] = '..'
    question = " ".join(num).strip()
    return question, answer
