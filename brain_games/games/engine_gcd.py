import random
# import math
import prompt
import brain_games.ask


def run_play():
    name = brain_games.ask.greeting()
    print('Find the greatest common divisor of given numbers.')
    SCORE = 0
    while (SCORE < 3):
        first_rnd_num = random.randint(0, 100)
        second_rnd_num = random.randint(0, 100)
        print(f"Question: {first_rnd_num} {second_rnd_num}")
        # print(math.gcd(a, b))
        while first_rnd_num != 0 and second_rnd_num != 0:
            if first_rnd_num > second_rnd_num:
                first_rnd_num = first_rnd_num % second_rnd_num
            else:
                second_rnd_num = second_rnd_num % first_rnd_num
        result = first_rnd_num + second_rnd_num
        answer = int(prompt.integer('Your answer: '))
        if (result == answer):
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. \
Correct answer was '{result}'.")
            break
        SCORE += 1
    brain_games.ask.is_win(SCORE, name)
