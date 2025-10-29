import math
import random

import prompt

from brain_games.cli import welcome_user

name = welcome_user()


def gcd():
    print('Find the greatest common divisor of given numbers.')
    count = 0

    while count < 3:
        rand_num1, rand_num2 = random.randint(1, 100), random.randint(1, 100)
        print(f'Question: {rand_num1} {rand_num2}')
        user_answer = prompt.string('Your answer: ')
        correct_answer = math.gcd(rand_num1, rand_num2) 
        
        if user_answer == str(correct_answer):
            print('Correct!')
            count += 1
        else:
            return print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet`s try again, {name}!")
    
    print(f'Congratulations, {name}!')


def main():
    gcd()