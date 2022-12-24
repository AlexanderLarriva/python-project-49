from random import randint
import brain_games.ask


def run_play():
    name = brain_games.ask.action()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    score = 0
    while (score < 3):
        a = randint(0, 100)
        print("Question: ", a)
        answer = input("Your answer: ")
        if ((a % 2 == 0) and (answer == 'yes')) or \
                ((a % 2 != 0) and (answer == 'no')):
            print("Correct!")
        if (a % 2 == 0) and (answer != 'yes'):
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
            break
        elif (a % 2 != 0) and (answer != 'no'):
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
            break
        score += 1
    brain_games.ask.is_win(score, name)
