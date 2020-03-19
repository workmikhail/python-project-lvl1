"""module contains functions of brain-even script."""
# coding: utf-8

from brain_games import cli, games


def main():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".')

    name = cli.welcome_user()
    game_result = games.brain_even()
    if game_result is False:
        message = '{0}{1}{2}'.format(
            "Let's try again, ",
            name,
            '!',
        )
        print(message)
    else:
        print('{0}{1}{2}'.format('Congratulations, ', name, '!'))


if __name__ == '__main__':
    main()
