import random

def computer_guess(x):
    low=0
    high=x
    feedback=''
    while feedback != 'C':
        if low != high:
           guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f"Is {guess} too high(H), too low(L) or correct(C)? ")
        if feedback=="H":
            high=guess-1
        elif feedback=="L":
            low=guess+1
    print(f"Yay! Computer guessed your number, {guess}, correctly.")

x=int(input("From how many numbers would you like to guess? "))
computer_guess(x)
