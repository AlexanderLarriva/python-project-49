import prompt


def greeting():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def is_win(score, name):
    if (score == 3):
        print(f"Congratulations, {name}!")
    else:
        print(f"Let's try again, {name}!")
