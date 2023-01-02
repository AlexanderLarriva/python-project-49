from random import randint
import prompt
import brain_games.ask


def run_play():
    name = brain_games.ask.greeting()
    print('What number is missing in the progression?')
    SCORE = 0
    while (SCORE < 3):
        my_list = [None] * randint(5, 12)
        my_list[0] = randint(0, 100)
        STEP = randint(0, 10)
        for i in range(1, len(my_list)):
            my_list[i] = my_list[i - 1] + STEP
        hidden_num = randint(0, len(my_list) - 1)
        my_list_in_txt = list(map(str, my_list))
        my_list_in_txt[hidden_num] = '..'
        print("Question:", *my_list_in_txt)
        answer = int(prompt.integer('Your answer: '))
        # проверка типов данных
        # print('answer = ', type(answer))
        # print('target = ', type(pr_list[hidden_num]))
        if (answer == my_list[hidden_num]):
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. \
Correct answer was '{my_list[hidden_num]}'.")
            break
        SCORE += 1
    brain_games.ask.is_win(SCORE, name)
