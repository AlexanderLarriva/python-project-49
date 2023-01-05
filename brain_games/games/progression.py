from random import randint


# Displaying the task on the screen
def say_task():
    print('What number is missing in the progression?')


def run_game():
    progr_list = list(range(0, randint(5, 12)))
    progr_list[0] = randint(0, 100)
    step = randint(1, 10)
    for i in range(1, len(progr_list)):
        progr_list[i] = progr_list[i - 1] + step
    hidden_num = randint(0, len(progr_list) - 1)
    mut_element = progr_list[hidden_num]
    progr_list_str = " ".join(map(str, progr_list))
    progr_list_str = progr_list_str.replace(str(mut_element), '..')
    return mut_element, progr_list_str
