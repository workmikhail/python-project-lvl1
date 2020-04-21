# coding: utf-8

"""Module contains functions of brain games."""

from brain_games import cli


def run_game(game, number_of_rounds=3):

    print('Welcome to the Brain Games!')
    print(game.DESCRIPTION)
    name = cli.welcome_user()

    counter = 0
    while counter < number_of_rounds:
        question, correct_answer = game.generate()
        answer = cli.ask_question('Question: {0}'.format(question))
        if answer == correct_answer:
            print('Correct!')
            counter += 1
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(
                answer,
                correct_answer,
            ))
            print("Let's try again, {0}!".format(name))
            break

    if counter == 3:
        print('Congratulations, {0}!'.format(name))
