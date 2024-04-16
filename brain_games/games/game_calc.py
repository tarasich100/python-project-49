from brain_games.consts import CALC_GAME_DESCRIPTION
from brain_games.engine import play_game
import random
import operator


def generate_round():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    op, op_func = (
        random.choice(
            [(operator.add, '+'),
             (operator.sub, '-'),
             (operator.mul, '*')]
        )
    )
    question = f"{num1} {op_func} {num2}"
    answer = str(op(num1, num2))
    return [question, answer]


def start_calc_game():
    play_game(CALC_GAME_DESCRIPTION, generate_round)
