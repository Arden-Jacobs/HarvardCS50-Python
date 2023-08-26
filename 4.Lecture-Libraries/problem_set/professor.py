# professor.py - Simple math quiz game

# Import the random module for generating random numbers
import random

# Main function to run the math quiz game
def main():
    # Get the user-selected level
    level = get_level()
    # Generate lists of random integers for x and y based on the level
    x, y = generate_integer(level)
    # Initialize the score
    score = 0
    # Iterate through 10 math problems
    for i in range(10):
        # Calculate the correct answer
        mat = x[i] + y[i]
        # Initialize the attempts counter
        attempts = 0
        # Loop for up to 3 attempts
        while attempts < 3:
            ans = input("{} + {} = ".format(x[i], y[i]))
            try:
                # Check if the answer is correct
                if int(ans) == mat:
                    score += 1
                    break
                else:
                    print("EEE")
                    attempts += 1
            except ValueError:
                print("EEE")
                attempts += 1
        # If all attempts are used, display the correct answer
        if attempts == 3:
            print("{} + {} = {}".format(x[i], y[i], mat))
    # Print the final score
    print(f"{score}")


# Function to get the user-selected level
def get_level():
    levels = [1, 2, 3]
    while True:
        try:
            level = int(input("Level: "))
            if level in levels:
                return level
                break
        except ValueError:
            level = input("Level: ")


# Function to generate lists of random integers based on the selected level
def generate_integer(level):
    x_num = []
    y_num = []
    if level == 1:
        ran_num1 = 0
        ran_num2 = 9
    elif level == 2:
        ran_num1 = 10
        ran_num2 = 99
    else:
        ran_num1 = 100
        ran_num2 = 999
    for i in range(10):
        x = random.randint(ran_num1, ran_num2)
        y = random.randint(ran_num1, ran_num2)
        x_num.append(int(x))
        y_num.append(int(y))
    return (x_num, y_num)


# Run the main function when the script is executed
if __name__ == "__main__":
    main()

# Explanation:
# This script is a simple math quiz game that generates addition problems based on user-selected levels.

# The import statement "import random" at the beginning of the script imports the random module, which provides
# functions for generating random numbers.

# The main function "main()" runs the math quiz game. It gets the user-selected level using the "get_level()" function,
# generates lists of random integers for x and y using the "generate_integer()" function, and then iterates through
# 10 math problems. Users can attempt to answer each problem up to 3 times.

# The "get_level()" function prompts the user for the level of difficulty and ensures a valid input.

# The "generate_integer(level)" function generates lists of random integers for x and y based on the selected level.

# The "__name__ == '__main__':" check at the end of the script ensures that the "main()" function is executed only
# when the script is run directly, not when it's imported as a module.
