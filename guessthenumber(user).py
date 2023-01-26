import random

def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess!=random_number:
        guess=int(input(f"Guess a number between 1 and {x}: "))
        if guess<random_number:
            print("Sorry, your guess is too low. Guess again.")
        elif guess>random_number:
            print("Sorry, your guess is too high. Guess again.")
          
    print(f"Hurray! You guessed the right number {random_number}.")

number=int(input("From how many numbers would you like to guess? "))
guess(number)