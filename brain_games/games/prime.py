from random import randint


def prime():    
    for _ in range(3):
        digit = randint(1, 300)
        if digit == 1:
            correct_answer = 'no'
        elif digit == 2:
            correct_answer = 'yes'
        else:
            for i in range(2, digit):
                if digit % i == 0:
                    correct_answer = 'no'
                    break
            else:
                correct_answer = 'yes'
        print(f'Question: {digit}')
        answer = input('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            continue
        else:
            return False, answer, correct_answer
    return True, answer, correct_answer