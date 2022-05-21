import random

secretNumber = random.randint(1,21)
print('I am thinking of a number between 1 and 20.')

for i in range(1, 11):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break

if guess == secretNumber:
    print(f'Good job! You guessed my number in {str(i)} guesses')
else:
    print(f'Nope, the number I was thinking of was {str(secretNumber)}')