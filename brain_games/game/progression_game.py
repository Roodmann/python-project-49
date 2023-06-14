import random


DESCRIPTION = 'What number is missing in the progression?'
START_SKIP_INDEX = 0
BEGIN_RANGE = 1
END_RANGE = 10


def get_question_and_answer():
    """Получаем вопрос и ответ"""
    #  приняли прогрессию
    progression = get_progression()
    #  Длина индекса прогрессии
    skip_index = random.randint(START_SKIP_INDEX, len(progression) - 1)
    #  Далее получаем вопрос и ответ
    answer = str(progression[skip_index])
    progression[skip_index] = '..'
    question = " ".join(progression).strip()
    return question, answer


def get_progression():
    """Получаем прогрессию"""
    progression = []
    first_num = random.randint(BEGIN_RANGE, END_RANGE)
    step = random.randint(BEGIN_RANGE, END_RANGE)
    for _ in range(END_RANGE):
        temp = first_num + step
        progression.append(str(temp))
        first_num = temp
    return progression
