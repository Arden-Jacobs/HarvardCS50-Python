# hello1.py - Demonstrates a function returning a string

# Main function to run the program
def main():
    # Prompt the user for input and store it in the variable "name"
    name = input("What's your name? ")
    # Call the "hello()" function and print the returned greeting message
    print(hello(name))

# Function to generate a greeting message and return it as a string
def hello(to="world"):
    # Generate and return the greeting message using an f-string
    return f"hello, {to}"

# Check if the script is run directly
if __name__ == "__main__":
    # Call the main function to start the program
    main()

# Explanation:
# This script demonstrates the use of a function that returns a string as a greeting message.

# The main function "main()" runs the program. It prompts the user for input and stores it in the variable "name".
# It then calls the "hello()" function with the provided name and prints the returned greeting message.

# The "hello(to="world")" function takes an optional parameter "to" with a default value of "world". It generates a
# greeting message using an f-string and returns the message as a string.

# The "__name__ == '__main__':" check at the end of the script ensures that the main function is executed only
# when the script is run directly, not when it's imported as a module.
