"""Example of Conditional (if-else) statements"""
"""Because the variable name is all caps it indicates that it is a constant"""
SECRET: int = 3

print("I'm thinking of a number between 1-5, what is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("You guessed correctly!!!")
    print("Congratulations, have a good day!")
else:
    print("Sorry, you guessed incorrectly :(")
    if guess > SECRET:
        print("You guessed too high!")
    else:
        print("You guessed too low!")

print("Game over.")