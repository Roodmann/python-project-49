import random
import prompt

NUMBER_OF_ROUNDS = 3
OPERATOR = ['+', '-', '*']


def welcome():
    """Приветствие"""
    print("Welcome to the Brain Games!")


def welcome_user():
    """Приветствие игрока"""
    name = prompt.string('May I have your name? ').capitalize()
    print(f'Hello, {name}!')
    return name


def quest_answer():
    print('What is the result of the expression?')


def ask_question_and_return_answer():
    """Задаем вопрос, получаем ответ"""
    first_num = random.randint(0, 100)
    second_num = random.randint(0, 100)
    symb_operator = random.choice(OPERATOR)
    correct_answer = count_answer(first_num, symb_operator, second_num)
    question = f'{first_num} {symb_operator} {second_num}'
    print(f'Question: {question}')
    return correct_answer


def count_answer(first_num, OPERATOR, second_num):
    """Проверка количество ответов"""
    if OPERATOR == '+':
        return first_num + second_num
    elif OPERATOR == '-':
        return first_num - second_num
    elif OPERATOR == '*':
        return first_num * second_num


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
