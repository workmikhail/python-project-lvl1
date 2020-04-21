# coding: utf-8

"""Module contains functions of game progression."""

import random

DESCRIPTION = 'What number is missing in the progression?'
MAX_NUMBER = 10


def generate():

    start_number = random.randint(1, MAX_NUMBER)
    progression_step = random.randint(1, MAX_NUMBER)
    position_in_progression = random.randint(1, MAX_NUMBER)

    progression_numbers = list(range(
        start_number,
        start_number + progression_step * 10,
        progression_step,
    ))

    progression = ''
    first_step = True
    counter = 1
    for elem in progression_numbers:
        if counter == position_in_progression:
            answer = str(elem)
            element = '...'
        else:
            element = str(elem)

        if first_step:
            progression = element
            first_step = False
        else:
            progression += ' ' + element

        counter += 1

    return progression, str(answer)
