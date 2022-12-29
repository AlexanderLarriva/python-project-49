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
    name = brain_games.ask.action()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    score = 0
    while (score < 3):
        check_num = randint(0, 100)
        print("Question:", check_num)
        answer = input("Your answer: ")
        if is_prime(check_num) and answer == "yes" or \
                not is_prime(check_num) and answer == "no":
            print("Correct!")
        if is_prime(check_num) and (answer != 'yes'):
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
            break
        elif not is_prime(check_num) and (answer != 'no'):
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
            break
        score += 1
    brain_games.ask.is_win(score, name)
