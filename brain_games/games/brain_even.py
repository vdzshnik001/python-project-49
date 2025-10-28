from brain_games.cli import welcome_user
import random
import prompt

name = welcome_user()

def even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    
    while count < 3:
        rand_num = random.randint(1, 100)
        rand_to_string = str(rand_num)
        print(f'Question: {rand_to_string}')
        user_answer = prompt.string('Your answer: ')
 
        if rand_num % 2 == 0 and user_answer == 'yes':
            print('Correct!')
            count += 1
        elif rand_num % 2 != 0 and user_answer == 'no':
            print('Correct!')
            count += 1
        elif rand_num % 2 == 0 and user_answer == 'no':
            return print(f"'no' is wrong answer ;(. Correct answer was 'yes'.\nLet`s try again, {name}!")
        elif rand_num % 2 != 0 and user_answer == 'yes':
            return print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet`s try again, {name}!")
        else:
            return print(f"{user_answer} is wrong answer ;(.\nLet's try again, {name}!")
        
    print(f'Congratulations, {name}!')


def main():
    even()  