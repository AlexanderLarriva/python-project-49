import random
import prompt
import brain_games.engine


def run_game():
    name = brain_games.engine.greeting()
    print('Find the greatest common divisor of given numbers.')
    score = 0
    while (score < 3):
        first_rnd_num = random.randint(0, 100)
        second_rnd_num = random.randint(0, 100)
        print(f"Question: {first_rnd_num} {second_rnd_num}")
        while first_rnd_num != 0 and second_rnd_num != 0:
            if first_rnd_num > second_rnd_num:
                first_rnd_num = first_rnd_num % second_rnd_num
            else:
                second_rnd_num = second_rnd_num % first_rnd_num
        result = first_rnd_num + second_rnd_num
        answer = int(prompt.integer('Your answer: '))
        if (result == answer):
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. \
Correct answer was '{result}'.")
            break
        score += 1
    brain_games.engine.is_win(score, name)
