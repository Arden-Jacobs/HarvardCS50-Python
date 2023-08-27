# calculator0.py - Demonstrates defining a function with a return value

# Main function to run the program
def main():
    # Prompt the user for input and store it in the variable x
    x = int(input("What's x? "))
    # Call the square function and print the result
    print("x squared is", square(x))

# Function to calculate the square of a number and return the result
def square(n):
    return n * n

# Call the main function to start the program
main()

# Explanation:
# This script demonstrates the use of a function with a return value to calculate the square of a number.

# The main function "main()" runs the program. It prompts the user for input and stores it in the variable "x".
# It then calls the "square()" function to calculate the square of "x" and prints the result.

# The "square(n)" function takes a parameter "n" and returns the square of the input number using the expression "n * n".

# The script concludes by calling the main function to start the program execution.
