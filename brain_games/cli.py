"""module contains functions of command line interface."""
# coding: utf-8

import prompt


def welcome_user():

    name = prompt.string('May I have your name? ')
    print('{0}{1}{2}'.format('Hello, ', name, '!'))
    print('')
    return name


def get_answer(question):
    print(question)
    return prompt.string('Your answer: ')
