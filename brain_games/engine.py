import prompt


NUMBER_ROUNDS = 3


def get_name():
    '''Getting to know the player.'''
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def display_winner(score, name):
    '''Displays the result of the game.'''
    if (score == NUMBER_ROUNDS):
        print(f"Congratulations, {name}!")
    else:
        print(f"Let's try again, {name}!")


def run_game(game):
    '''The game engine.'''
    name = get_name()
    print(game.TASK)
    score = 0
    while (score < NUMBER_ROUNDS):
        question, correct_answer = game.get_question_answer()
        print(question)
        answer = prompt.string("Your answer: ")
        if answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            break
        score += 1
    display_winner(score, name)
