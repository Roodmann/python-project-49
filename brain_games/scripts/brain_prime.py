from brain_games.game_engine import run_game
from brain_games.game.prime_game import DESCRIPTION
from brain_games.game.prime_game import ask_question_and_return_answer


def main():
    run_game(DESCRIPTION, ask_question_and_return_answer)


if __name__ == '__main__':
    main()
