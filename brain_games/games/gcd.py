"""module contains functions of game gcd."""
# coding: utf-8

from random import SystemRandom

DESCRIPTION = 'Find the greatest common divisor of given numbers?'


def game():

    stop_int = 50
    first_number = SystemRandom().randint(2, stop_int)
    second_number = SystemRandom().randint(2, stop_int)

    question = '{0}{1}{2}{3}'.format(
        'Question: ',
        first_number,
        ' ',
        second_number,
    )

    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number %= second_number
        else:
            second_number %= first_number

    gcd = first_number + second_number

    return question, str(gcd)
