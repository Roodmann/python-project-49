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
    print('What number is missing in the progression?')


def ask_question_and_return_answer():
    """Задаем вопрос, получаем ответ"""
    question, correct_answer = get_progression()
    print(f'Question: {question}')
    return correct_answer


def get_progression():
    """Получаем прогрессию"""
    num = []
    first_num = random.randint(1, 10)
    num.append(str(first_num))
    step = random.randint(1, 10)
    for _ in range(9):
        temp = first_num + step
        num.append(str(temp))
        first_num = temp
    temp_num = random.randint(1, 10)
    answer = str(num[temp_num])
    num[temp_num] = '..'
    question = " ".join(num).strip()
    return question, answer


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
