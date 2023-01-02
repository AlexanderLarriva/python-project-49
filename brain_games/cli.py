import prompt


def welcome_user():
    NAME = prompt.string('May I have your name? ')
    print(f'Hello, {NAME}!')
