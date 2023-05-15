import random
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
    print('Find the greatest common divisor of given numbers.')


def ask_question_and_return_answer():
    """Задаем вопрос, получаем ответ"""
    first_num = random.randint(1, 100)
    second_num = random.randint(1, 100)
    correct_answer = get_gcd(first_num, second_num)
    question = f'{first_num} {second_num}'
    print(f'Question: {question}')
    return correct_answer


def get_gcd(first_num, second_num):
    """Нахождение НОД"""
    # Находим минимальное значение числа
    min_num = min(first_num, second_num)
    # Получаем min значение числа
    for i in range(1, min_num + 1):
        # Проверка остатка
        if ((first_num % i == 0) and (second_num % i == 0)):
            gcd = i
    return gcd


def user_answer():
    """Ответ Пользователя"""
    answer = input('Your answer: ')
    return answer


def cheсk_answer(user_answer, correct_answer, name):
    """Проверка ответа Пользователя"""
    if str(user_answer) == str(correct_answer):
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
