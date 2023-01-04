from random import randint


# Displaying the task on the screen
def say_task():
    print('Answer "yes" if the number is even, otherwise answer "no".')


# Random number generator and parity check
def run_game():
    rnd_num = randint(0, 100)
    check_even = ""
    if (rnd_num % 2 == 0):
        check_even = "yes"
    else:
        check_even = "no"
    return check_even, rnd_num
