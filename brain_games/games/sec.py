import prompt
import brain_games.common
from random import randint


def even_game():
    brain_games.common.greet()
    name = brain_games.common.welcome_user()
    games_counter = 3
    right_answers = 0
    rules = "Answer 'yes' if the number is even, otherwise answer 'no'."
    print(rules)
    while games_counter:
        question = randint(0, 1000)
        print(f"Question: {question}")
        gamer_answer = prompt.string("Your answer: ")
        right_answer = 'yes' if question % 2 == 0 else 'no'
        if gamer_answer == right_answer:
            print("Correct!")
            games_counter -= 1
            right_answers += 1
        else:
            brain_games.common.wrong_answer_message(right_answer, gamer_answer)
            brain_games.common.try_again_message(name)
            games_counter = 0
        if right_answers == 3:
            brain_games.common.congratulations(name)
