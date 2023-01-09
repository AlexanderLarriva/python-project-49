import prompt


def get_name():
    '''Getting to know the player.'''
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def display_winner(score, name):
    '''Displays the result of the game.'''
    if (score == 3):
        print(f"Congratulations, {name}!")
    else:
        print(f"Let's try again, {name}!")


def get_result(answer, correct_answer):
    '''Check the correctness of the entered answer.'''
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"'{answer}' is wrong answer ;(.  \
Correct answer was '{correct_answer}'.")
        return 0


def run_game(engine):
    '''The game engine.'''
    name = get_name()
    print(engine.TASK)
    score = 0
    while (score < 3):
        question, correct_answer = engine.get_question()
        print(question)
        answer = prompt.string("Your answer: ")
        stop_while = get_result(answer, correct_answer)
        if stop_while == 0:
            break
        score += 1
    display_winner(score, name)
