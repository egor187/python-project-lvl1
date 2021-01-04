import brain_games.common as common
import prompt
import random


def prime_game():
    prepare = common.prepare()
    games_counter = prepare["games_counter"]
    name = prepare["name"]
    right_answers = prepare["right_answers"]
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while games_counter:
        question = random.randint(0, 100)
        right_answer = "yes" if common.is_prime(question) else "no"
        print(f"Question: {question}")
        gamer_answer = prompt.string("Your answer: ")
        result = common.result(
                gamer_answer,
                right_answer,
                games_counter,
                right_answers,
                name
                )
        games_counter = result["games_counter"]
        right_answers = result["right_answers"]
