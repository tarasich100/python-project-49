#!/usr/bin/env python3

from brain_games.games.game_engine import play_game
import random
import math


def start_gcd_game():
    def question_answer():
        num1, num2 = random.randint(1, 100), random.randint(1, 100)
        nums_pair = f'{num1} {num2}'
        gcd = math.gcd(num1, num2)
        return nums_pair, str(gcd)

    play_game('Find the greatest common divisor of given numbers.', question_answer)


if __name__ == "__main__":
    start_gcd_game()
