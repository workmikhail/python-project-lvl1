# coding: utf-8

"""Module contains functions of game even."""

import random

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'
MAX_NUMBER = 99


def generate():
    random_number = random.randint(1, MAX_NUMBER)

    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return random_number, correct_answer
