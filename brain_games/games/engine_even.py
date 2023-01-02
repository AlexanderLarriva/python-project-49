from random import randint
import brain_games.ask


def run_play():
    NAME = brain_games.ask.greeting()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    SCORE = 0
    while (SCORE < 3):
        RND_NUM = randint(0, 100)
        print("Question:", RND_NUM)
        ANSWER = input("Your answer: ")
        if ((RND_NUM % 2 == 0) and (ANSWER == 'yes')) or \
                ((RND_NUM % 2 != 0) and (ANSWER == 'no')):
            print("Correct!")
        if (RND_NUM % 2 == 0) and (ANSWER != 'yes'):
            print(f"'{ANSWER}' is wrong answer ;(. Correct answer was 'yes'.")
            break
        elif (RND_NUM % 2 != 0) and (ANSWER != 'no'):
            print(f"'{ANSWER}' is wrong answer ;(. Correct answer was 'no'.")
            break
        SCORE += 1
    brain_games.ask.is_win(SCORE, NAME)
