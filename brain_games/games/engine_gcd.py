import random
# import math
import prompt
import brain_games.ask


def run_play():
    name = brain_games.ask.action()
    print('Find the greatest common divisor of given numbers.')
    score = 0
    while (score < 3):
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        print(f"Question: {a} {b}")
        # print(math.gcd(a, b))
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        result = a + b
        score += 1
        answer = int(prompt.integer('Your answer: '))
        if (result == answer):
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. \
Correct answer was '{result}'.")
            break
    brain_games.ask.is_win(score, name)
