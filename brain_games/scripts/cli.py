import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def win(name):
    print(f'Congratulations, {name}!')
    

def loose(name, answer, correct_answer):
    print(f"'{answer}' is wrong answer ;(. "
          f"Correct answer was '{correct_answer}'.")
    print(f"Let's try again, {name}!")