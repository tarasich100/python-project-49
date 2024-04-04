#!/usr/bin/env python3

def play_game(game_description, get_question_and_answer):
    welcome_user()
    user_name = get_user_name()
    print(game_description)
    game_is_finished = False
    while not game_is_finished:
        for _ in range(3):
            if not play_round(get_question_and_answer, user_name):
                break
        else:
            print(f'Congratulations, {user_name}!')
            game_is_finished = True


def welcome_user():
    print('Welcome to the Brain Games!')


def get_user_name():
    user_name = input('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def play_round(get_question_and_answer, user_name):
    question, correct_answer = get_question_and_answer()
    print('Question:', question)
    user_answer = input('Your answer: ')
    if user_answer == correct_answer:
        print('Correct!')
        return True
    else:
        return print_incorrect_message(user_answer, user_name, correct_answer)


def print_incorrect_message(user_answer, user_name, correct_answer):
    print(f"'{user_answer}' is wrong answer ;(. "
          f"Correct answer was '{correct_answer}'.")
    print(f"Let's try again, {user_name}!")
    return False
