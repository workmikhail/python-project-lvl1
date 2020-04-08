"""module contains functions of game even"""
# coding: utf-8

from random import SystemRandom

Description = 'Answer "yes" if number even otherwise answer "no".'


def game():

    stop_int = 99
    random_number = SystemRandom().randint(1, stop_int)

    question = '{0}{1}'.format('Question: ', random_number)
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer