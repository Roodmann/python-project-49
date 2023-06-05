from brain_games.game_engine import run_game
from brain_games.game.gcd_game import DESCRIPTION
from brain_games.game.gcd_game import get_question_and_answer


def main():
    run_game(DESCRIPTION, get_question_and_answer)


if __name__ == '__main__':
    main()
