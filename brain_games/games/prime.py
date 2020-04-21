# coding: utf-8

"""Module contains functions of game even."""

import operator
import random
from math import sqrt

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'
MAX_NUMBER = 99


def generate():

    dividend = random.randint(1, MAX_NUMBER)

    if is_prime(dividend):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return str(dividend), correct_answer


def is_prime(dividend):

    if dividend == 2:
        return True

    divider = 2
    while divider <= sqrt(dividend):
        if operator.mod(dividend, divider) == 0:
            return False

        divider += 1

    return True
