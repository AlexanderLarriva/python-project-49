from random import randint
import brain_games.engine


def is_prime(n):
    if n == 1:
        return False
    # начинаем с 2, так как на 1 все делится; n не включается
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def run_game():
    name = brain_games.engine.greeting()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    score = 0
    while (score < 3):
        check_sum = randint(1, 100)
        print("Question:", check_sum)
        answer = input("Your answer: ")
        if is_prime(check_sum) and answer == "yes" or \
                not is_prime(check_sum) and answer == "no":
            print("Correct!")
        if is_prime(check_sum) and (answer != 'yes'):
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
            break
        elif not is_prime(check_sum) and (answer != 'no'):
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
            break
        score += 1
    brain_games.engine.is_win(score, name)
