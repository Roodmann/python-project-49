from brain_games.game.gcd_game import (welcome, welcome_user,
                                       quest_answer, game_process
                                       )


def main():
    welcome()
    name = welcome_user()
    quest_answer()
    game_process(name)


if __name__ == '__main__':
    main()
