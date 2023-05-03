from random import randint
import prompt

NUMBER_OF_ROUNDS = 3


def welcome():
    """Приветствие"""
    print("Welcome to the Brain Games!")


def welcome_user():
    """Приветствие игрока"""
    name = prompt.string('May I have your name? ').capitalize()
    print(f'Hello, {name}!')
    return name


def quest_answer():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def is_even(number):
    """Выявляем True и Fals"""
    return number % 2 == 0


def ask_question_and_return_answer():
    """Задаем вопрос, получаем ответ"""
    question = (randint(1, 100))
    print(f'Question: {question}')
    temp_answer = is_even(question)
    if temp_answer:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer


def user_answer():
    """Ответ Пользователя"""
    answer = input('Your answer: ')
    return answer


def cheсk_answer(user_answer, correct_answer, name):
    """Проверка ответа Пользователя"""
    if user_answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f'{user_answer} is wrong answer ;(.'
              f'Correct answer was {correct_answer}. \n'
              f"Let's try again, {name}!")
        return False


def game_process(name):
    """Рабочий процесс игры"""
    for _ in range(NUMBER_OF_ROUNDS):
        correct_answer = ask_question_and_return_answer()
        user_answer = input('Your answer: ')
        result = cheсk_answer(user_answer, correct_answer, name)
        if not result:
            return
        print(f'Congratulations, {name}!')

# welcome()
# name = welcome_user()
# quest_answer()
# game_process(name)
