from random import randint
import brain_games.ask


def run_play():
    name = brain_games.ask.greeting()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    SCORE = 0
    while (SCORE < 3):
        rnd_num = randint(0, 100)
        print("Question:", rnd_num)
        answer = input("Your answer: ")
        if ((rnd_num % 2 == 0) and (answer == 'yes')) or \
                ((rnd_num % 2 != 0) and (answer == 'no')):
            print("Correct!")
        if (rnd_num % 2 == 0) and (answer != 'yes'):
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
            break
        elif (rnd_num % 2 != 0) and (answer != 'no'):
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
            break
        SCORE += 1
    brain_games.ask.is_win(SCORE, name)
