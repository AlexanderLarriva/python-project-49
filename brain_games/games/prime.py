from random import randint


# Displaying the task on the screen
def say_task():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def run_game(check_num):
    check_prime = ''
    if check_num == 1:
        check_prime = 'no'
        return check_prime
    # начинаем с 2, так как на 1 все делится; n не включается
    for i in range(2, check_num):
        if check_num % i == 0:
            check_prime = 'no'
            return check_prime
    check_prime = 'yes'
    return check_prime


def gen():
    return randint(1, 100)
