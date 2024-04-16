from brain_games.consts import (PROGRESSION_GAME_DESCRIPTION,
                                MIN_PROGRESSION_LENGTH,
                                MAX_PROGRESSION_LENGTH)
from brain_games.engine import play_game
import random


PROGRESSION_LENGTH_RANGE = (MIN_PROGRESSION_LENGTH, MAX_PROGRESSION_LENGTH)
START_RANGE = (0, 10)
STEP_RANGE = (1, 10)


def generate_progression(start, step, length):
    return [start + x * step for x in range(length)]


def generate_round():
    start = random.randint(*START_RANGE)
    step = random.randint(*STEP_RANGE)
    length = random.randint(*PROGRESSION_LENGTH_RANGE)
    progression = generate_progression(start, step, length)
    missing_position = random.randint(0, len(progression) - 1)
    answer = str(progression[missing_position])
    progression[missing_position] = '..'
    question = ' '.join(map(str, progression))
    return [question, answer]


def start_progression_game():
    play_game(PROGRESSION_GAME_DESCRIPTION, generate_round)
