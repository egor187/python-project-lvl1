import prompt
from random import randint


def even_greet():
    print('Welcome to the Brain Games!')


def even_welcome_user():
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def even_game():
    name = even_welcome_user()
    games_counter = 3
    right_answers = 0
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    print(rules)
    while games_counter:
        question = randint(0, 1000)
        print(f"Question: {question}")
        gamer_answer = prompt.string("You answer: ")
        right_answer = 'yes' if question % 2 == 0 else 'no'
        if gamer_answer == right_answer:
            print("Correct!")
            games_counter -= 1
            right_answers += 1
        else:
            print(
                    f"'{gamer_answer}' is wrong answer ;(. "
                    f"Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            games_counter = 0
        if right_answers == 3:
            print(f"Congratulations, {name}!")
