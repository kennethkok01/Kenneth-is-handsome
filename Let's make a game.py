#!/usr/bin/env python

import random

def main():

    """Start a number guessing game between 1-50."""
    print("Guess the number!")

    x = random.randrange(1,50)
    guess = None

    while x !=guess:

        guess=int(input("Pick a number between 1 to 50:"))

        if x == guess:
            print("Correct!")
            break
        else:
            print("Wrong")
def hello():
    print("Hello World")



main()