from random import randint


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    '''Checking the number for simplicity.'''
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def get_question_answer():
    '''Generates task values and a question to the player.'''
    rnd_num = randint(1, 100)
    correct_answer = "yes" if is_prime(rnd_num) else "no"
    question = f"Question: {rnd_num}"
    return question, correct_answer
