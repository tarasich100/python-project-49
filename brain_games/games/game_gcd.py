from brain_games.consts import GCD_GAME_DESCRIPTION
from brain_games.engine import play_game
import random
import math


def generate_round():
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    nums_pair = f'{num1} {num2}'
    gcd = math.gcd(num1, num2)
    question = nums_pair
    answer = str(gcd)
    return [question, answer]


def start_gcd_game():
    play_game(GCD_GAME_DESCRIPTION, generate_round)
