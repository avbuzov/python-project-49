from random import randint


def calc():    
    for _ in range(3):
        digit1, digit2 = randint(1, 100), randint(1, 100)
        sign = ('+', '-', '*')[randint(0, 2)]
        print(f'Question: {digit1} {sign} {digit2}')
        correct_answer = eval(str(digit1) + sign + str(digit2))
        answer = input('Your answer: ')
        if answer.lstrip('-').isdigit() and int(answer) == correct_answer:
            print('Correct!')
            continue
        else:
            return False, answer, correct_answer
    return True, answer, correct_answer