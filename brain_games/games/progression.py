"""module contains functions of game progression."""
# coding: utf-8

from random import SystemRandom

Description = 'What number is missing in the progression?'


def game():

    start_number = SystemRandom().randint(1, 10)
    progression_step = SystemRandom().randint(1, 10)
    position_in_progression = SystemRandom().randint(1, 10)

    progression_list = list(range(
        start_number,
        start_number + progression_step * 10,
        progression_step,
    ))
    answer = progression_list[position_in_progression - 1]
    progression_list[position_in_progression - 1] = '...'

    question = get_question(progression_list)
    return question, str(answer)


def get_question(list_of_progression):

    progression = ''
    space = ''
    max_step = len(list_of_progression)
    for counter in range(0, max_step, 1):
        if counter > 0:
            space = ' '

        progression = '{0}{1}{2}'.format(
            progression,
            space,
            list_of_progression[counter],
        )

    return '{0}{1}'.format('Question: ', progression)
