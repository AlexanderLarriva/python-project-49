import prompt


def greeting():
    print("Welcome to the Brain Games!")
    NAME = prompt.string('May I have your name? ')
    print(f'Hello, {NAME}!')
    return NAME


def is_win(SCORE, NAME):
    if (SCORE == 3):
        print(f"Congratulations, {NAME}!")
    else:
        print(f"Let's try again, {NAME}!")
