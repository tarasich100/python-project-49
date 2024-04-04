from brain_games.consts import GCD_GAME_DESCRIPTION
from brain_games.engine import play_game
import random
import math


def start_gcd_game():
    def question_answer():
        num1, num2 = random.randint(1, 100), random.randint(1, 100)
        nums_pair = f'{num1} {num2}'
        gcd = math.gcd(num1, num2)
        return nums_pair, str(gcd)

    play_game(GCD_GAME_DESCRIPTION, question_answer)
