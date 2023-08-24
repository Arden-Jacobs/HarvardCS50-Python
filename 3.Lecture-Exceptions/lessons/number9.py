# number9.py - Adds prompt

# Define the main function
def main():
    # Call the get_int function with a custom prompt to obtain a valid integer
    x = get_int("What's x? ")
    # Print the obtained integer
    print(f"x is {x}")

# Define the get_int function to get a valid integer input from the user
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))  # Prompt the user with the provided prompt and return the integer
        except ValueError:
            pass

# Call the main function to start the program
main()



# Explanation:
# This code snippet continues to build upon the previous example and introduces a custom prompt for the user input.

# The main() function and the get_int() function remain the same as in the previous example.

# Inside the main() function, the get_int() function is called with the custom prompt "What's x? ". This prompt is
# passed as an argument to the get_int() function.

# The get_int() function receives the custom prompt as a parameter named "prompt". When the input() function is used to
# prompt the user, the provided prompt argument is displayed to the user. This allows you to customize the prompt for
# different situations.

# The rest of the code within the get_int() function and the main() function remains unchanged.

# The overall behavior of the program remains the same: it repeatedly prompts the user with the custom prompt for input
# until a valid integer is provided, and then it prints the obtained integer.
