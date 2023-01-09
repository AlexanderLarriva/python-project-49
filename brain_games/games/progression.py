from random import randint


TASK = 'What number is missing in the progression?'


def get_result(progression):
    '''Finds the correct solution to the problem.'''
    hidden_num = randint(0, len(progression) - 1)
    correct_answer = str(progression[hidden_num])
    progression_str = " ".join(map(str, progression))
    progression_str = progression_str.replace(str(correct_answer), '..')
    return correct_answer, progression_str


def get_question():
    '''Generates task values and a question to the player'''
    progression = list(range(0, randint(5, 12)))
    progression[0] = randint(0, 100)
    step = randint(1, 10)
    for i in range(1, len(progression)):
        progression[i] = progression[i - 1] + step
    correct_answer, progression_str = get_result(progression)
    question = f"Question: {progression_str}"
    return question, correct_answer
