import prompt
import brain_games.games.even


# Player's Greeting
def greeting():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


# Game Engine
def action(name):
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


# Determining the results of the game
def is_win(score, name):
    if (score == 3):
        print(f"Congratulations, {name}!")
    else:
        print(f"Let's try again, {name}!")
