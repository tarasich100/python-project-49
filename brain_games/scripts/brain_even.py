import random


def is_even(num):
    return num % 2 == 0


def main():
    # приветствие
    print("Welcome to the Brain Games!")
    player_name = input("May I have your name? ")
    print(f"Hello, {player_name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0
    while correct_answers < 3:
        given_number = random.randint(1, 100)
        print(f"Question: {given_number}")
        player_answer = input("Your answer: ")
        # если правильный ответ
        if (is_even(given_number) and player_answer == 'yes') or \
                (not is_even(given_number) and player_answer == 'no'):
            print("Correct!")
            correct_answers += 1
        # если ответ неправильный
        else:
            correct_answer = 'yes' if is_even(given_number) else 'no'
            print(f"'{player_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {player_name}!")
            correct_answers = 0

    print(f"Congratulations, {player_name}!")


if __name__ == "__main__":
    main()
