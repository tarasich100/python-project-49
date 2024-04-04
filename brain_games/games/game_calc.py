from brain_games.consts import CALC_GAME_DESCRIPTION
from brain_games.engine import play_game
import random
import operator


def start_calc_game():
    def question_answer():
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        op, op_func = (
            random.choice(
                [(operator.add, '+'),
                 (operator.sub, '-'),
                 (operator.mul, '*')]
            )
        )
        return f"{num1} {op_func} {num2}", str(op(num1, num2))

    play_game(CALC_GAME_DESCRIPTION, question_answer)
