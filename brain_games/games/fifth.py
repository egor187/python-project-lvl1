import brain_games.common as common
import prompt
import random


def progression_game():
    prepare = common.prepare()
    games_counter = prepare["games_counter"]
    name = prepare["name"]
    right_answers = prepare["right_answers"]
    print("What number is missing in the progression?")
    while games_counter:
        progression = [i for i in range(0, 50, random.randint(2, 10))]
        index = random.randint(0, len(progression)-1)
        right_answer = progression[index]
        progression[index] = ".."
        print("Question: ", *progression)
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
