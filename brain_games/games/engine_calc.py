import random
import prompt
import operator
import brain_games.ask


def run_play():
    name = brain_games.ask.action()
    print('What is the result of the expression?')
    score = 0
    while (score < 3):
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        sign = random.choice('+-*')
        if sign == '+':
            result = operator.add(a, b)
        elif sign == '-':
            result = operator.sub(a, b)
        else:
            result = operator.mul(a, b)
        print(f'Question: {a} {sign} {b}')
        answer = int(prompt.integer('Your answer: '))
        if (result == answer):
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. \
Correct answer was '{result}'.")
            break
        score += 1
    brain_games.ask.is_win(score, name)
