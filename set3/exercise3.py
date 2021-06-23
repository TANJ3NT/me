"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    print("\nWelcome to the guessing game!")
    valid_input = False
    while valid_input == False:
        print("A number between 0 and _ ?")
        upperBound = input("Enter an upper bound: ")
        if isinstance(upperBound, int) == True:
            valid_input = True
        else:
            print("An exception occurred")

    print("OK then, a number between 0 and {} ?".format(upperBound))
    upperBound = int(upperBound)

    valid_input = False
    while valid_input == False:
        print("A number between _ and {} ?".format(upperBound))
        lowerBound = input("Enter an lower bound: ")
        if isinstance(lowerBound, int) == True:
            valid_input = True
        else:
            print("An exception occurred")

    print("OK then, a number between {} and {} ?".format(lowerBound, upperBound))
    lowerBound = int(lowerBound)

    if lowerBound > upperBound:
        temp = lowerBound
        lowerBound = upperBound
        upperBound = temp

    actualNumber = random.randint(lowerBound, upperBound)

    guessed = False
    valid_input = False

    while not guessed:
        while valid_input == False:
            guessedNumber = input("Guess a number: ")
            if isinstance(guessedNumber, int):
                valid_input = True
            else:
                print("An exception occurred")
        guessedNumber = int(guessedNumber)
        print("You guessed {},".format(guessedNumber))
        if guessedNumber == actualNumber:
            print("You got it!! It was {}".format(actualNumber))
            guessed = True
        elif guessedNumber < actualNumber:
            print("Too small, try again :'(")
            valid_input = False
        else:
            print("Too big, try again :'(")
            valid_input = False
    return "You got it!"

    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())

# test push
