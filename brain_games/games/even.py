from random import randint


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    '''Сheck the number for parity.'''
    if (num % 2 == 0):
        return True


def get_question_answer():
    '''Generates task values and a question to the player.'''
    rnd_num = randint(0, 100)
    correct_answer = "yes" if is_even(rnd_num) else "no"
    question = f"Question: {rnd_num}"
    return question, correct_answer
