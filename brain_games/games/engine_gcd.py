import random
# import math
import prompt
import brain_games.ask


def run_play():
    NAME = brain_games.ask.greeting()
    print('Find the greatest common divisor of given numbers.')
    SCORE = 0
    while (SCORE < 3):
        FIRST_RND_NUM = random.randint(0, 100)
        SECOND_RND_NUM = random.randint(0, 100)
        print(f"Question: {FIRST_RND_NUM} {SECOND_RND_NUM}")
        # print(math.gcd(a, b))
        while FIRST_RND_NUM != 0 and SECOND_RND_NUM != 0:
            if FIRST_RND_NUM > SECOND_RND_NUM:
                FIRST_RND_NUM = FIRST_RND_NUM % SECOND_RND_NUM
            else:
                SECOND_RND_NUM = SECOND_RND_NUM % FIRST_RND_NUM
        RESULT = FIRST_RND_NUM + SECOND_RND_NUM
        ANSWER = int(prompt.integer('Your answer: '))
        if (RESULT == ANSWER):
            print("Correct!")
        else:
            print(f"'{ANSWER}' is wrong answer ;(. \
Correct answer was '{RESULT}'.")
            break
        SCORE += 1
    brain_games.ask.is_win(SCORE, NAME)
