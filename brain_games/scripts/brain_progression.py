from ..games.progression import progression
from .cli import loose, welcome_user, win


def main():
    name = welcome_user()
    print('What number is missing in the progression?')
    result, answer, correct_answer = progression()
    if result:
        win(name)
    else:
        loose(name, answer, correct_answer)
        

if __name__ == '__main__':
    main()