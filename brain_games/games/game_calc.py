#!/usr/bin/env python3

from brain_games.games.game_engine import play_game
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

    play_game('What is the result of the expression?', question_answer)
