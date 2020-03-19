"""module contains functions of brain-even script."""
# coding: utf-8

from brain_games import cli, games


def main():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".')
    name = cli.welcome_user()
    games.brain_even(name)


if __name__ == '__main__':
    main()
