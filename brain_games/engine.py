from brain_games.consts import NUMBER_OF_ROUNDS


def play_game(game_description, get_question_and_answer):
    print('Welcome to the Brain Games!')
    user_name = input('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game_description)

    for _ in range(NUMBER_OF_ROUNDS):
        question, correct_answer = get_question_and_answer()
        print('Question:', question)
        user_answer = input('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')
