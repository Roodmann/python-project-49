"""
Модуль для проведеня игры.
Правила для игрока:
Игроку задается на каждом этапе три вопроса.
Если в течении трех вопросах игрок ошибается - игра заканчивается,
после чего, игроку предлагается попробовать начать игру сначала.
Если игрок правильно ответил на три вопроса - игра заканчивается,
поздравление игрока с успешным прохождением игры.
"""


import prompt

NUMBER_OF_ROUNDS = 3


def welcome():
    """Приветствие"""
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ').capitalize()
    print(f'Hello, {name}!')
    return name


def user_answer():
    """Ответ Пользователя"""
    answer = input('Your answer: ')
    return answer


def cheсk_answer(user_answer, correct_answer, name):
    """Проверка ответа Пользователя"""
    if str(user_answer).lower() == str(correct_answer):
        print('Correct!')
        return True
    print(f'{user_answer} is wrong answer ;(.'
          f'Correct answer was {correct_answer}. \n'
          f"Let's try again, {name}!")
    return False


def run_game(DESCRIPTION, get_question_and_answer):
    name = welcome()
    # Печатаем задание
    print(DESCRIPTION)
    for _ in range(NUMBER_OF_ROUNDS):
        # Получаем вопрос и ответ
        question, answer = get_question_and_answer()
        # Печатаем вопрос
        print(f'Question: {question}')
        # Ответ пользователя
        u_answer = user_answer()
        # Сравниваем ответы
        result = cheсk_answer(u_answer, answer, name)
        if result is False:
            return  # Выход из игры, при не правльном ответе
    print(f'Congratulations, {name}!')
