from random import randint
import brain_games.ask


def is_prime(n):
    if n == 1:
        return False
    # начинаем с 2, так как на 1 все делится; n не включается
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def run_play():
    NAME = brain_games.ask.greeting()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    SCORE = 0
    while (SCORE < 3):
        CHECK_NUM = randint(0, 100)
        print("Question:", CHECK_NUM)
        ANSWER = input("Your answer: ")
        if is_prime(CHECK_NUM) and ANSWER == "yes" or \
                not is_prime(CHECK_NUM) and ANSWER == "no":
            print("Correct!")
        if is_prime(CHECK_NUM) and (ANSWER != 'yes'):
            print(f"'{ANSWER}' is wrong answer ;(. Correct answer was 'yes'.")
            break
        elif not is_prime(CHECK_NUM) and (ANSWER != 'no'):
            print(f"'{ANSWER}' is wrong answer ;(. Correct answer was 'no'.")
            break
        SCORE += 1
    brain_games.ask.is_win(SCORE, NAME)
