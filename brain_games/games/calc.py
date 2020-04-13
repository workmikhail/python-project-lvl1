"""module contains functions of game calc."""
# coding: utf-8

from operator import add, mul, sub
from random import SystemRandom

DESCRIPTION = 'What is the result of the expression?'


def game():

    stop_int = 50

    first_number = SystemRandom().randint(1, stop_int)
    second_number = SystemRandom().randint(1, stop_int)
    operation_number = SystemRandom().randint(1, 3) - 1

    operation_list = [(' + ', add), (' - ', sub), (' * ', mul)]

    operation, function = operation_list[operation_number]

    question = '{0}{1}{2}{3}'.format(
        'Question: ',
        first_number,
        operation,
        second_number,
    )

    return question, str(function(first_number, second_number))
