import random
import operator


TASK = 'What is the result of the expression?'


def get_result(first_num, second_num, sign):
    '''Finds the correct solution to the problem.'''
    calculate = {"+": operator.add(first_num, second_num),
                 "-": operator.sub(first_num, second_num),
                 "*": operator.mul(first_num, second_num)}
    correct_answer = calculate.get(sign)
    return correct_answer


def get_question_answer():
    '''Generates task values and a question to the player.'''
    sign = random.choice('+-*')
    first_rnd_num = random.randint(0, 100)
    second_rnd_num = random.randint(0, 100)
    correct_answer = str(get_result(first_rnd_num, second_rnd_num, sign))
    question = f"Question: {first_rnd_num} {sign} {second_rnd_num}"
    return question, correct_answer
