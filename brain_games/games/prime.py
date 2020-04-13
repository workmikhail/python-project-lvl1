"""module contains functions of game even."""
# coding: utf-8

from operator import mod
from random import SystemRandom

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def game():

    stop_int = 99
    dividend = SystemRandom().randint(1, stop_int)
    divider = 2
    while divider * divider <= dividend and mod(dividend, divider) != 0:
        divider += 1

    question = '{0}{1}'.format('Question: ', dividend)

    if divider * divider > dividend:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer
