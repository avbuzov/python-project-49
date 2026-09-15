from ..games.calc import calc
from .cli import loose, welcome_user, win


def main():
    name = welcome_user()
    print('What is the result of the expression?')
    result, answer, correct_answer = calc()
    if result:
        win(name)
    else:
        loose(name, answer, correct_answer)
        

if __name__ == '__main__':
    main()