from random import randint


def even():
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
            return False, answer, correct_answer
    return True, answer, correct_answer