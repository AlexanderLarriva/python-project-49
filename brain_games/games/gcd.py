import random
import prompt
import brain_games.engine


# Displaying the task on the screen
def say_task():
    print('Find the greatest common divisor of given numbers.')


def run_game():
    first_rnd_num = random.randint(0, 100)
    second_rnd_num = random.randint(0, 100)
    return first_rnd_num, second_rnd_num
        
