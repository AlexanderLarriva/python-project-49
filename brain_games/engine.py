import prompt
import brain_games.games.even
import brain_games.games.calc
import brain_games.games.gcd
import brain_games.games.progression
import brain_games.games.prime


# Player's Greeting
def greeting():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


# Game Engine is_even
def even_check(name):
    brain_games.games.even.say_task()
    score = 0
    while (score < 3):
        rnd_num = brain_games.games.even.gen()
        check_even = brain_games.games.even.run_game(rnd_num)
        print("Question:", rnd_num)
        answer = input("Your answer: ")
        stop_while = is_correct(answer, check_even)
        if stop_while == 0:
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
        answer = prompt.integer('Your answer: ')
        result = brain_games.games.calc.math_action(first_rnd_num,
                                                    second_rnd_num, sign)
        stop_while = is_correct(answer, result)
        if stop_while == 0:
            break
        score += 1
    is_win(score, name)


# Game Engine gcd
def gcd(name):
    brain_games.games.gcd.say_task()
    score = 0
    while (score < 3):
        first_rnd_num, second_rnd_num = brain_games.games.gcd.run_game()
        print(f"Question: {first_rnd_num} {second_rnd_num}")
        result = brain_games.games.gcd.find_gcd(first_rnd_num, second_rnd_num)
        answer = prompt.integer('Your answer: ')
        stop_while = is_correct(answer, result)
        if stop_while == 0:
            break
        score += 1
    is_win(score, name)


# Game Engine progression
def progression(name):
    brain_games.games.progression.say_task()
    score = 0
    while (score < 3):
        mut_element, my_list_str = brain_games.games.progression.run_game()
        print("Question:", my_list_str)
        answer = prompt.integer('Your answer: ')
        stop_while = is_correct(answer, mut_element)
        if stop_while == 0:
            break
        score += 1
    is_win(score, name)


# Game Engine prime
def is_prime(name):
    brain_games.games.prime.say_task()
    score = 0
    while (score < 3):
        check_num = brain_games.games.prime.gen()
        check_prime = brain_games.games.prime.run_game(check_num)
        print("Question:", check_num)
        answer = input("Your answer: ")
        stop_while = is_correct(answer, check_prime)
        if stop_while == 0:
            break
#         if answer == check_prime:
#             print("Correct!")
#         else:
#             print(f"'{answer}' is wrong answer ;(.  \
# Correct answer was '{check_prime}'.")
#             break
        score += 1
    is_win(score, name)


# Determining the results of the game
def is_win(score, name):
    if (score == 3):
        print(f"Congratulations, {name}!")
    else:
        print(f"Let's try again, {name}!")


def is_correct(answer, check):
    if answer == check:
        print("Correct!")
    else:
        print(f"'{answer}' is wrong answer ;(.  \
Correct answer was '{check}'.")
        return 0
