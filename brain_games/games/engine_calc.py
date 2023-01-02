import random
import prompt
import operator
import brain_games.ask


def run_play():
    NAME = brain_games.ask.greeting()
    print('What is the result of the expression?')
    SCORE = 0
    while (SCORE < 3):
        FIRST_RND_NUM = random.randint(0, 100)
        SECOND_RND_NUM = random.randint(0, 100)
        SIGN = random.choice('+-*')
        if SIGN == '+':
            RESULT = operator.add(FIRST_RND_NUM, SECOND_RND_NUM)
        elif SIGN == '-':
            RESULT = operator.sub(FIRST_RND_NUM, SECOND_RND_NUM)
        else:
            RESULT = operator.mul(FIRST_RND_NUM, SECOND_RND_NUM)
        print(f'Question: {FIRST_RND_NUM} {SIGN} {SECOND_RND_NUM}')
        ANSWER = int(prompt.integer('Your answer: '))
        if (RESULT == ANSWER):
            print("Correct!")
        else:
            print(f"'{ANSWER}' is wrong answer ;(. \
Correct answer was '{RESULT}'.")
            break
        SCORE += 1
    brain_games.ask.is_win(SCORE, NAME)
