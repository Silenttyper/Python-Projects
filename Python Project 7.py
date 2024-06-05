#Number Guessing Game
import random

def guessthenumber(e):
    random_number=random.randint(1,e)
    guess=0
    while guess != random_number:
        guess=int(input(f"Guess a number between 1 and {e} "))
        if guess==e:
            print("You guessed it correct! ")
            quit()

guessthenumber(25)