# coding: utf-8

"""Module contains functions of game calc."""

import operator
import random

DESCRIPTION = 'What is the result of the expression?'
MAX_NUMBER = 50
OPERATION_LIST = (
    (' + ', operator.add),
    (' - ', operator.sub),
    (' * ', operator.mul),
)


def generate():
    first_number = random.randint(1, MAX_NUMBER)
    second_number = random.randint(1, MAX_NUMBER)

    operation, function = random.choice(OPERATION_LIST)

    question = '{0}{1}{2}'.format(
        first_number,
        operation,
        second_number,
    )

    return question, str(function(first_number, second_number))
