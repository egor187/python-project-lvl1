import brain_games.common as common
import prompt
import random


def gcd_game():
    prepare = common.prepare()
    games_counter = prepare["games_counter"]
    name = prepare["name"]
    right_answers = prepare["right_answers"]
    print("Find the greatest common divisor of given numbers.")
    while games_counter:
        first_operand = random.randint(0, 100)
        second_operand = random.randint(0, 100)
        question = f"{first_operand} {second_operand}"
        right_answer = common.gcd(first_operand, second_operand)
        print(f"Question: {question}")
        gamer_answer = prompt.integer("Your answer: ")
        result = common.result(
                gamer_answer,
                right_answer,
                games_counter,
                right_answers,
                name
                )
        games_counter = result["games_counter"]
        right_answers = result["right_answers"]
