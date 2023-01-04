import prompt
import operator
import brain_games.games.even
import brain_games.games.calc


# Player's Greeting
def greeting():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


# Game Engine is_even
def is_even(name):
    brain_games.games.even.say_task()
    score = 0
    while (score < 3):
        check_even, rnd_num = brain_games.games.even.run_game()
        print("Question:", rnd_num)
        answer = input("Your answer: ")
        if (check_even == answer):
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. \
                Correct answer was '{check_even}'.")
            break
        score += 1
    is_win(score, name)


# Game Engine calc
def calc(name):
    brain_games.games.calc.say_task()
    score = 0
    while (score < 3):
        first_rnd_num, second_rnd_num, sign = brain_games.games.calc.run_game()
        print(f'Question: {first_rnd_num} {sign} {second_rnd_num}')
        answer = int(prompt.integer('Your answer: '))
        if sign == '+':
            result = operator.add(first_rnd_num, second_rnd_num)
        elif sign == '-':
            result = operator.sub(first_rnd_num, second_rnd_num)
        else:
            result = operator.mul(first_rnd_num, second_rnd_num)
        if (result == answer):
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. \
Correct answer was '{result}'.")
            break
        score += 1
    is_win(score, name)


# Determining the results of the game
def is_win(score, name):
    if (score == 3):
        print(f"Congratulations, {name}!")
    else:
        print(f"Let's try again, {name}!")
