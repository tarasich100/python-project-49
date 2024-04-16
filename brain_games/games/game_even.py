from brain_games.consts import EVEN_GAME_DESCRIPTION
from brain_games.engine import play_game
import random


def generate_round():
    number = random.randint(1, 100)
    question = str(number)
    answer = 'yes' if number % 2 == 0 else 'no'
    return [question, answer]


def start_even_game():
    play_game(EVEN_GAME_DESCRIPTION, generate_round)
