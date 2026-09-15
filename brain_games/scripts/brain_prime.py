from ..games.prime import prime
from .cli import loose, welcome_user, win


def main():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    result, answer, correct_answer = prime()
    if result:
        win(name)
    else:
        loose(name, answer, correct_answer)
        

if __name__ == '__main__':
    main()