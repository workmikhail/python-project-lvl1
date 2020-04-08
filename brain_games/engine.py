"""module contains functions of brain games."""
# coding: utf-8

from brain_games import cli


def run_game(game):

    name = cli.welcome_user(game.Description)
    counter = 0
    number_of_rounds = 3
    while counter < number_of_rounds:
        question, correct_answer = game.game()
        answer = cli.get_answer(question)
        if not user_answer_is_correct(answer, correct_answer):
            break
        counter += 1

    endgame(counter == 3, name)


def user_answer_is_correct(answer, correct_answer):

    if answer == correct_answer:
        print('Correct!')
        return True

    print('{0}{1}{2}{3}{4}'.format(
        "'",
        answer,
        "' is wrong answer ;(. Correct answer was '",
        correct_answer,
        "'.",
    ))
    return False


def endgame(game_result, name):

    if game_result is False:
        message = '{0}{1}{2}'.format(
            "Let's try again, ",
            name,
            '!',
        )
        print(message)
    else:
        print('{0}{1}{2}'.format('Congratulations, ', name, '!'))
