from random import randint


# Displaying the task on the screen
def say_task():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def run_game(rnd_num):
    check_even = ""
    if (rnd_num % 2 == 0):
        check_even = "yes"
    else:
        check_even = "no"
    return check_even


def gen():
    return randint(0, 100)
