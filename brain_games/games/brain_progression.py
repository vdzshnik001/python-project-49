import random

import prompt

from brain_games.cli import welcome_user

name = welcome_user()


def progression():
    count = 0
    print('What number is missing in the progression?')

    while count < 3:
        start = random.randint(1, 10)
        end = random.randint(40, 50)
        step = random.randint(2, 10)
        numbers = []

        for current in range(start, end, step):
            numbers.append(current)
    
        numbers.sort()
        index_to_hide = random.randint(0, len(numbers) - 1)
        correct_answer = numbers[index_to_hide]
        numbers[index_to_hide] = ".."
        string = " ".join(map(str, numbers))
        print(f'Question: {string}')
        user_answer = prompt.string('Your answer: ')

        if int(user_answer) == int(correct_answer):
            print('Correct!')
            count += 1
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer is {correct_answer}.")
            return print(f"Let's try again, {name}!")
    print(f'Congratulations, {name}!')


def main():
    progression()
