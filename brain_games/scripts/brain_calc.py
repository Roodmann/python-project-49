from brain_games.game_engine import run_game
from brain_games.game.calc_game import quest_answer
from brain_games.game.calc_game import ask_question_and_return_answer


def main():
    run_game(quest_answer, ask_question_and_return_answer)


if __name__ == '__main__':
    main()
