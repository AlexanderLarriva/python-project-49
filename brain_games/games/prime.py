from random import randint


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_result(rnd_num):
    '''Finds the correct solution to the problem.'''
    correct_answer = ''
    if rnd_num == 1:
        correct_answer = 'no'
        return correct_answer
    for i in range(2, rnd_num):
        if rnd_num % i == 0:
            correct_answer = 'no'
            return correct_answer
    correct_answer = 'yes'
    return correct_answer


def get_question():
    '''Generates task values and a question to the player'''
    rnd_num = randint(1, 100)
    correct_answer = get_result(rnd_num)
    question = f"Question: {rnd_num}"
    return question, correct_answer
