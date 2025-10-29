import random

import prompt

from brain_games.cli import welcome_user

name = welcome_user()


def prime():
    count = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    
    while count < 3:
        rand_num = random.randint(0, 75)
        print(f'Question: {rand_num}')
        user_answer = prompt.string('Your answer: ')
        correct_answer = ''
        cor_str = 'Correct answer was '
        
        if rand_num in prime_numbers:
            correct_answer = 'yes'
        else: 
            correct_answer = 'no'
        
        if user_answer == correct_answer:
            print('Correct!')
            count += 1
        else:
            print(f"{user_answer} is wrong answer ;(. {cor_str}{correct_answer}.")
            return print(f"Let's try again, {name}!")
        
    print(f'Congratulations, {name}!')


def main():
    prime()