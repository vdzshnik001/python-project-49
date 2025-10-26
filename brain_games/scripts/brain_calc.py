import operator
import random

import prompt

name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')


def welcome_user():
    print(f'Hello, {name}!')


def calc():
    print('What is the result of the expression?')
    count = 0
    operators = {
            operator.add: '+',
            operator.sub: '-',
            operator.mul: '*',
        }
    
    while count < 3:
        rand_num1, rand_num2 = random.randint(1, 100), random.randint(1, 100)
        rand_operator = random.choice(list(operators))
        symbol = operators[rand_operator]
        print(f'Question: {rand_num1} {symbol} {rand_num2}')
        correct_answer = rand_operator(rand_num1, rand_num2)
        user_answer = prompt.string('Your answer: ')
 
        if int(user_answer) == correct_answer:
            print('Correct!')
            count += 1
        else:
            return print(f"{user_answer} is wrong answer ;(. Correct answer was '{correct_answer}'\nLet's try again, {name}!")
        
    print(f'Congratulations, {name}!')


def main():
    welcome_user()
    calc()  