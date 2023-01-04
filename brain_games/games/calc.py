import random
import prompt
import operator
import brain_games.engine


def run_game():
    name = brain_games.engine.greeting()
    print('What is the result of the expression?')
    score = 0
    while (score < 3):
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
        score += 1
    brain_games.engine.is_win(score, name)
