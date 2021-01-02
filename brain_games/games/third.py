import prompt
import brain_games.common as common
import random


def calc_game():
    prepare = common.prepare()
    games_counter = prepare["games_counter"]
    name = prepare["name"]
    right_answers = prepare["right_answers"]
    print("What is the result of the expression?")
    operator_seq = "+-*"
    while games_counter:
        operator_str = random.choice(operator_seq)
        first_operand = random.randint(0, 100)
        second_operand = random.randint(0, 100)
        question = f"{first_operand} {operator_str} {second_operand}"
        if operator_str == "+":
            right_answer = first_operand + second_operand
        if operator_str == "-":
            right_answer = first_operand - second_operand
        if operator_str == "*":
            right_answer = first_operand * second_operand
        print(f"Question: {question}")
        gamer_answer = prompt.integer("Your answer: ")
        result = common.result(
                gamer_answer,
                right_answer, games_counter,
                right_answers, name
                )
        games_counter = result["games_counter"]
        right_answers = result["right_answers"]
