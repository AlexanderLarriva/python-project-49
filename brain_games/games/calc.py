import random
import operator


TASK = 'What is the result of the expression?'


def get_result(first_rnd_num, second_rnd_num, sign):
    '''Finds the correct solution to the problem.'''
    if sign == '+':
        correct_answer = operator.add(first_rnd_num, second_rnd_num)
    elif sign == '-':
        correct_answer = operator.sub(first_rnd_num, second_rnd_num)
    else:
        correct_answer = operator.mul(first_rnd_num, second_rnd_num)
    return correct_answer


def get_question():
    '''Generates task values and a question to the player'''
    first_rnd_num = random.randint(0, 100)
    second_rnd_num = random.randint(0, 100)
    sign = random.choice('+-*')
    correct_answer = str(get_result(first_rnd_num, second_rnd_num, sign))
    question = f"Question: {first_rnd_num} {sign} {second_rnd_num}"
    return question, correct_answer
