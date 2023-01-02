from random import randint
import prompt
import brain_games.ask


def run_play():
    NAME = brain_games.ask.greeting()
    print('What number is missing in the progression?')
    SCORE = 0
    while (SCORE < 3):
        CREATE_LIST = [None] * randint(5, 12)
        CREATE_LIST[0] = randint(0, 100)
        STEP = randint(0, 10)
        for i in range(1, len(CREATE_LIST)):
            CREATE_LIST[i] = CREATE_LIST[i - 1] + STEP
        HIDDEN_NUM = randint(0, len(CREATE_LIST) - 1)
        CONVERT_CREATE_LIST_TXT = list(map(str, CREATE_LIST))
        CONVERT_CREATE_LIST_TXT[HIDDEN_NUM] = '..'
        print("Question:", *CONVERT_CREATE_LIST_TXT)
        ANSWER = int(prompt.integer('Your answer: '))
        # проверка типов данных
        # print('answer = ', type(answer))
        # print('target = ', type(pr_list[hidden_num]))
        if (ANSWER == CREATE_LIST[HIDDEN_NUM]):
            print("Correct!")
        else:
            print(f"'{ANSWER}' is wrong answer ;(. \
Correct answer was '{CREATE_LIST[HIDDEN_NUM]}'.")
            break
        SCORE += 1
    brain_games.ask.is_win(SCORE, NAME)
