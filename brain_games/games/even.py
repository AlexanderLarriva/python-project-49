from random import randint


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_result(rnd_num):
    '''Finds the correct solution to the problem.'''
    correct_answer = ""
    if (rnd_num % 2 == 0):
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return correct_answer


def get_question():
    '''Generates task values and a question to the player'''
    rnd_num = randint(0, 100)
    correct_answer = get_result(rnd_num)
    question = f"Question: {rnd_num}"
    return question, correct_answer
