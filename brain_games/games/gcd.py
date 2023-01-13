import random


TASK = 'Find the greatest common divisor of given numbers.'


def get_gcd(first_num, second_num):
    '''Finds the correct solution to the problem.'''
    while first_num != 0 and second_num != 0:
        if first_num > second_num:
            first_num = first_num % second_num
        else:
            second_num = second_num % first_num
    return first_num + second_num


def get_question_answer():
    '''Generates task values and a question to the player.'''
    first_rnd_num = random.randint(0, 100)
    second_rnd_num = random.randint(0, 100)
    correct_answer = str(get_gcd(first_rnd_num, second_rnd_num))
    question = f"Question: {first_rnd_num} {second_rnd_num}"
    return question, correct_answer
