import random

def guess(num):
    random_number = random.randint(1,num)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {num}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, Guess again. Too High.')

    print(f'Congrats you guess the right number {random_number}')

def computer_guess(num):
    low = 1
    high = num
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L) , or correct (C)??').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    
    print(f'Yay! The computer guessed your number,{guess},correctly!')


computer_guess(10)