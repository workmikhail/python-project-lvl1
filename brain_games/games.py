"""module contains functions of brain games."""
# coding: utf-8

from random import SystemRandom

import prompt


def brain_even(step=0):
    stop_int = 99

    random_number = SystemRandom().randint(1, stop_int)

    print('{0}{1}'.format('Question: ', random_number))
    answer = prompt.string('Your answer: ')
    correct_answer = correct_answer_by_string(random_number)

    if answer == correct_answer:
        print('Correct!')
        step += 1
    else:
        print(
            '{0}{1}{2}{3}'.format(
                answer,
                ' is wrong answer ;(. Correct answer was ',
                correct_answer,
                '.',
            ),
        )
        return False

    if step < 3:
        brain_even(step)

    return True


def correct_answer_by_string(number):
    if number % 2 == 0:
        return 'yes'

    return 'no'
