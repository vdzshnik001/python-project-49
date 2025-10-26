import random

import prompt

name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')


def welcome_user():
    print(f'Hello, {name}!')


def prime():
    count = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    
    while count < 3:
        rand_num = random.randint(0, 75)
        print(f'Question: {rand_num}')
        user_answer = prompt.string('Your answer: ')
        correct_answer = ''
        
        if rand_num in prime_numbers:
            correct_answer = 'yes'
        else: 
            correct_answer = 'no'
        
        if user_answer == correct_answer:
            print('Correct!')
            count += 1
        else:
            return print(f"{user_answer} is wrong answer ;(. Correct answer was {correct_answer}.\nLet`s try again, {name}!")
        
    print(f'Congratulations, {name}!')


def main():
    welcome_user()
    prime()