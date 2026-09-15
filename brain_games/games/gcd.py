from random import randint


def gcd():    
    for _ in range(3):
        digit1, digit2 = randint(1, 100), randint(1, 100)
        print(f'Question: {digit1} {digit2}')
        while digit2 != 0:
            digit1, digit2 = digit2, digit1 % digit2
        correct_answer = digit1
        answer = input('Your answer: ')
        if answer.isdigit() and int(answer) == correct_answer:
            print('Correct!')
            continue
        else:
            return False, answer, correct_answer
    return True, answer, correct_answer