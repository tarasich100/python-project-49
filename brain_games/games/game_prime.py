from brain_games.consts import PRIME_GAME_DESCRIPTION
from brain_games.engine import play_game
import random


def generate_round():
    number = random.randint(1, 100)
    question = str(number)
    answer = 'yes' if is_prime(number) else 'no'
    return [question, answer]


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def start_prime_game():
    play_game(PRIME_GAME_DESCRIPTION, generate_round)
