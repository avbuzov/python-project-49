from ..games.gcd import gcd
from .cli import loose, welcome_user, win


def main():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    result, answer, correct_answer = gcd()
    if result:
        win(name)
    else:
        loose(name, answer, correct_answer)
        

if __name__ == '__main__':
    main()