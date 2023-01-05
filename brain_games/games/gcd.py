import random


# Displaying the task on the screen
def say_task():
    print('Find the greatest common divisor of given numbers.')


def find_gcd(first_rnd_num, second_rnd_num):
    while first_rnd_num != 0 and second_rnd_num != 0:
        if first_rnd_num > second_rnd_num:
            first_rnd_num = first_rnd_num % second_rnd_num
        else:
            second_rnd_num = second_rnd_num % first_rnd_num
    return first_rnd_num + second_rnd_num


def run_game():
    first_rnd_num = random.randint(0, 100)
    second_rnd_num = random.randint(0, 100)
    return first_rnd_num, second_rnd_num
