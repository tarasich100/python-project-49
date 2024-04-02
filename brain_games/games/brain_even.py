#!/usr/bin/env python3

from brain_games.games.game_engine import play_game
import random


def even_game():
    def question_answer():
        number = random.randint(1, 100)
        return str(number), 'yes' if number % 2 == 0 else 'no'

    play_game('Answer "yes" if the number is even, '
              'otherwise answer "no".', question_answer)


if __name__ == "__main__":
    even_game()
