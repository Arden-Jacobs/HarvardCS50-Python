# game.py - Simple number guessing game

# Import the random module for generating random numbers
import random

# Loop to input a valid level
while True:
    try:
        # Prompt the user for the desired level
        lev = int(input("Level: "))
        # Check if the level is greater than 0
        if lev > 0:
            break
    except ValueError:
        lev = input("Level: ")

# Generate a random number within the specified level
num = random.randint(0, lev)

# Loop for the guessing game
while True:
    try:
        # Prompt the user for a guess
        guess = int(input("Guess: "))
        # Check if the guess is negative and prompt again
        if guess < 0:
            guess = int(input("Guess: "))
        # Compare the guess with the generated number
        if guess == num:
            print("Just right!")
            break
        if guess > num:
            print("Too large!")
        if guess < num:
            print("Too small!")
    except ValueError:
        pass

# Print the correct number
print(num)

# Explanation:
# This script is a simple number guessing game where the user is prompted to guess a number within a given level.

# The import statement "import random" at the beginning of the script imports the random module, which provides
# functions for generating random numbers.

# The first loop repeatedly prompts the user to input a valid level until a positive integer is entered.

# The random number to guess is generated using "num = random.randint(0, lev)", where "lev" is the specified level.

# The second loop runs the guessing game. The user is prompted to input their guess, and the script provides feedback
# based on whether the guess is too large, too small, or just right.

# The final "print(num)" statement prints the correct number that the user was trying to guess after the game is completed.
