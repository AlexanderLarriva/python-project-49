import random


TASK = 'Find the greatest common divisor of given numbers.'


def get_result(first_rnd_num, second_rnd_num):
    '''Finds the correct solution to the problem.'''
    while first_rnd_num != 0 and second_rnd_num != 0:
        if first_rnd_num > second_rnd_num:
            first_rnd_num = first_rnd_num % second_rnd_num
        else:
            second_rnd_num = second_rnd_num % first_rnd_num
    return first_rnd_num + second_rnd_num


def get_question():
    '''Generates task values and a question to the player'''
    first_rnd_num = random.randint(0, 100)
    second_rnd_num = random.randint(0, 100)
    correct_answer = str(get_result(first_rnd_num, second_rnd_num))
    question = f"Question: {first_rnd_num} {second_rnd_num}"
    return question, correct_answer
