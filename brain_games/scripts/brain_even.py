from random import randint

from .cli import welcome_user


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    result = True
    for _ in range(3):
        digit = randint(1, 100)
        print(f'Question: {digit}')
        if digit % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        answer = input('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            continue
        else:
            result = False
            break
    if result:
        print(f'Congratulations, {name}!')
    else:
        print(f"'{answer}' is wrong answer ;(. "
              f"Correct answer was'{correct_answer}'.")
        print(f"Let's try again, {name}!")
        

if __name__ == '__main__':
    main()