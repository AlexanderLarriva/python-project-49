from random import randint
import prompt
import brain_games.ask


def run_play():
    name = brain_games.ask.action()
    print('What number is missing in the progression?')
    score = 0
    while (score < 3):
        pr_list = [None] * randint(5, 12)
        pr_list[0] = randint(0, 100)
        step = randint(0, 10)
        for i in range(1, len(pr_list)):
            pr_list[i] = pr_list[i - 1] + step
        hidden_num = randint(0, len(pr_list) - 1)
        txt_pr_list = list(map(str, pr_list))
        txt_pr_list[hidden_num] = '..'
        print("Question: ", *txt_pr_list)
        answer = int(prompt.integer('Your answer: '))
        # проверка типов данных
        # print('answer = ', type(answer))
        # print('target = ', type(pr_list[hidden_num]))
        if (answer == pr_list[hidden_num]):
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. \
Correct answer was '{pr_list[hidden_num]}'.")
            break
        score += 1
    brain_games.ask.is_win(score, name)
