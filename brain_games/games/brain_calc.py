import random

import prompt

from brain_games.cli import welcome_user

name = welcome_user()


def calc():
    print('What is the result of the expression?')
    count = 0

    def add(num1, num2):
        return num1 + num2
    
    def sub(num1, num2):
        return num1 - num2
    
    def mul(num1, num2):
        return num1 * num2
    
    operators = {
        '+': add,
        '-': sub,
        '*': mul,
    }
    
    while count < 3:
        num1, num2 = random.randint(1, 100), random.randint(1, 100)
        rand_operator = random.choice(list(operators))
        symbol = operators[rand_operator]
        print(f'Question: {num1} {rand_operator} {num2}')
        cor_ans = symbol(num1, num2)
        cor_str = 'Correct answer was '
        user_answer = prompt.string('Your answer: ')
 
        if int(user_answer) == cor_ans:
            print('Correct!')
            count += 1
        else:
            print(f"{user_answer} is wrong answer ;(. {cor_str}'{cor_ans}'.")
            return print(f"Let's try again, {name}!")
        
    print(f'Congratulations, {name}!')


def main():
    calc()  