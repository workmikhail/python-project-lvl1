"""module contains functions of brain games."""
# coding: utf-8

from random import randint
import prompt


def brain_even(name, step=0):
    random_number = randint(1, 99)

    print('{0}{1}'.format('Question: ', random_number))
    answer = prompt.string('Your answer: ')
    correct_answer = correct_answer_by_string(random_number)

    if answer == correct_answer:
        print('Correct!')
        step += 1
    else:
        print('{0}{1}{2}{3}'.format(answer, 'is wrong answer ;(. Correct answer was ', correct_answer, '.'))
        print('{0}{1}{2}'.format('Let\'s try again, ', name, '!'))

    if step < 3:
        brain_even(name, step)
    else:
        print('{0}{1}{2}'.format('Congratulations, ', name, '!'))


def correct_answer_by_string(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'
