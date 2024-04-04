from brain_games.consts import EVEN_GAME_DESCRIPTION
from brain_games.engine import play_game
import random


def start_even_game():
    def question_answer():
        number = random.randint(1, 100)
        return str(number), 'yes' if number % 2 == 0 else 'no'

    play_game(EVEN_GAME_DESCRIPTION, question_answer)
