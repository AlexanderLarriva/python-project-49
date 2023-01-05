import random
import operator


# Displaying the task on the screen
def say_task():
    print('What is the result of the expression?')


def math_action(first_rnd_num, second_rnd_num, sign):
    if sign == '+':
        result = operator.add(first_rnd_num, second_rnd_num)
    elif sign == '-':
        result = operator.sub(first_rnd_num, second_rnd_num)
    else:
        result = operator.mul(first_rnd_num, second_rnd_num)
    return result


def run_game():
    first_rnd_num = random.randint(0, 100)
    second_rnd_num = random.randint(0, 100)
    sign = random.choice('+-*')
    return first_rnd_num, second_rnd_num, sign
