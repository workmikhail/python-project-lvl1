"""module contains functions of command line interface."""
# coding: utf-8

import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('')
    return name
