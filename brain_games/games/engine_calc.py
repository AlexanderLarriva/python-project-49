import random
import prompt
import operator
import brain_games.ask


def run_play():
    name = brain_games.ask.greeting()
    print('What is the result of the expression?')
    SCORE = 0
    while (SCORE < 3):
        first_rnd_num = random.randint(0, 100)
        second_rnd_num = random.randint(0, 100)
        sign = random.choice('+-*')
        if sign == '+':
            result = operator.add(first_rnd_num, second_rnd_num)
        elif sign == '-':
            result = operator.sub(first_rnd_num, second_rnd_num)
        else:
            result = operator.mul(first_rnd_num, second_rnd_num)
        print(f'Question: {first_rnd_num} {sign} {second_rnd_num}')
        answer = int(prompt.integer('Your answer: '))
        if (result == answer):
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. \
Correct answer was '{result}'.")
            break
        SCORE += 1
    brain_games.ask.is_win(SCORE, name)
