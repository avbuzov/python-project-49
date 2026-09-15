from random import randint


def progression():    
    for _ in range(3):
        start = randint(1, 20)
        step = randint(2, 10)
        question = [str(start + i * step) for i in range(10)]
        result_index = randint(0, 9)
        correct_answer = int(question[result_index])
        question[result_index] = '..'
        print(f'Question: {' '.join(question)}')
        answer = input('Your answer: ')
        if answer.isdigit() and int(answer) == correct_answer:
            print('Correct!')
            continue
        else:
            return False, answer, correct_answer
    return True, answer, correct_answer