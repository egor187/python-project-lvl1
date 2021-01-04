import prompt


def greet():
    print("Welcome to the Brain Games!")


def welcome_user():
    name = prompt.string("May I have your name?: ")
    print(f"Hello, {name}!")
    return name


def congratulations(name):
    print(f"Congratulations, {name}")


def wrong_answer_message(right_answer, gamer_answer):
    print(
            f"'{gamer_answer}' is wrong answer ;(."
            f"Correct answer was '{right_answer}'"
            )


def try_again_message(name):
    print(f"Let's try again, {name}!")


def prepare(games_counter=3, right_answers=0):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return {
            "games_counter": games_counter,
            "right_answers": right_answers,
            "name": name
            }


def result(gamer_answer, right_answer, games_counter, right_answers, name):
    if gamer_answer == right_answer:
        print("Correct!")
        games_counter -= 1
        right_answers += 1
        if right_answers == 3:
            print(f"Congratulations, {name}!")
        return {
                "games_counter": games_counter,
                "right_answers": right_answers
                }
    else:
        print(
                f"'{gamer_answer}' is wrong answer ;(."
                f"Correct answer is '{right_answer}'"
                )
        print(f"Let's try again, {name}!")
        games_counter = 0
        return {
                "games_counter": games_counter,
                "right_answers": right_answers
                }


def gcd(first_operand: int, second_operand: int):
    while second_operand:
        first_operand, second_operand = \
                second_operand, first_operand % second_operand
    return abs(first_operand)


def is_prime(integer: int):
    i = 2
    while i <= integer ** 0.5:
        if integer % i == 0:
            return False
        i += 1
    return True
