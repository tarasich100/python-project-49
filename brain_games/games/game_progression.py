from brain_games.consts import PROGRESSION_GAME_DESCRIPTION
from brain_games.engine import play_game
import random

MIN_PROGRESSION_LENGTH = 5
MAX_PROGRESSION_LENGTH = 10
PROGRESSION_LENGTH_RANGE = (MIN_PROGRESSION_LENGTH, MAX_PROGRESSION_LENGTH)
START_RANGE = (0, 10)
STEP_RANGE = (1, 10)



def generate_progression():
    length = random.randint(*PROGRESSION_LENGTH_RANGE)
    start = random.randint(*START_RANGE)
    step = random.randint(*STEP_RANGE)
    progr = []
    for i in range(length):
        progr.append(start + step * i)
    return progr


def start_progression_game():
    def question_answer():
        progression = generate_progression()
        missing_position = random.randint(0, len(progression) - 1)
        correct_answer = progression[missing_position]
        progression[missing_position] = '..'
        question = ' '.join(map(str, progression))
        return question, str(correct_answer)

    play_game(PROGRESSION_GAME_DESCRIPTION, question_answer)
