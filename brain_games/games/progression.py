from random import randint


TASK = 'What number is missing in the progression?'
MIN_LENGTH_PROGRESSION = 5
MAX_LENFTH_PROGRESSION = 10
RANGE_LIMIT = 1000000


def get_result(progression):
    '''Finds the correct solution to the problem.'''
    hidden_num = randint(0, len(progression) - 1)
    correct_answer = str(progression[hidden_num])
    progression = list(map(str, progression))
    progression[hidden_num] = '..'
    progression_str = " ".join(progression)
    return correct_answer, progression_str


def get_question_answer():
    '''Generates task values and a question to the player.'''
    length_progression = randint(MIN_LENGTH_PROGRESSION, MAX_LENFTH_PROGRESSION)
    start = randint(0, 100)
    step = randint(1, 10)
    progression = list(range(start, RANGE_LIMIT, step)[:length_progression])
    correct_answer, progression_str = get_result(progression)
    question = f"Question: {progression_str}"
    return question, correct_answer
