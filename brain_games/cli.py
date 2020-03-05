# cli.py
import prompt
def welcome_user():
    name = prompt.string(prompt = 'May I have your name? ', empty = False)
    print('Hello, ' + name + '!')
