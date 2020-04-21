"""module contains functions of game gcd."""
# coding: utf-8

import random

DESCRIPTION = 'Find the greatest common divisor of given numbers?'
MAX_NUMBER = 50


def generate():

    first_number = random.randint(2, MAX_NUMBER)
    second_number = random.randint(2, MAX_NUMBER)

    question = '{0} {1}'.format(
        first_number,
        second_number,
    )

    return question, get_gcd(first_number, second_number)


def get_gcd(first_number, second_number):

    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number %= second_number
        else:
            second_number %= first_number

    return first_number + second_number
