from random import randint
import prompt


def run_play():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    score = 0
    while (score < 3):
        a = randint(0, 100)
        print("Question: ", a)
        answer = input("Your answer: ")
        # слишком длинная строка
        if ((a % 2 == 0) and (answer == 'yes')) or ((a % 2 != 0) and (answer == 'no')):
            print("Correct!")
        if (a % 2 == 0) and (answer != 'yes'):
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
            break
        elif (a % 2 != 0) and (answer != 'no'):
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
            break
        score += 1
    if (score == 3):
        print(f"Congratulations, {name}!")
