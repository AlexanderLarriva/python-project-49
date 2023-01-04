import random


# Displaying the task on the screen
def say_task():
    print('What is the result of the expression?')


def run_game():
    first_rnd_num = random.randint(0, 100)
    second_rnd_num = random.randint(0, 100)
    sign = random.choice('+-*')
    return first_rnd_num, second_rnd_num, sign
