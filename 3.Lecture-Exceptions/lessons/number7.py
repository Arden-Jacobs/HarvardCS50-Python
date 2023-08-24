# number7.py - Removes else

# Define the main function
def main():
    # Call the get_int function to obtain a valid integer
    x = get_int()
    # Print the obtained integer
    print(f"x is {x}")

# Define the get_int function to get a valid integer input from the user
def get_int():
    while True:
        try:
            return int(input("What's x? "))  # Prompt the user for input and return the integer
        except ValueError:
            print("x is not an integer")  # Handle the ValueError exception

# Call the main function to start the program
main()



# Explanation:
# This code snippet builds on the previous example and removes the "else" block from the get_int() function.

# The main() function remains the entry point of the program. It calls the get_int() function to obtain a valid
# integer input from the user and then prints the value of x.

# The get_int() function continues to use a "while True" loop to continuously prompt the user for input. Within the
# loop, it uses a "try" block to attempt to convert the user input into an integer. If successful, the "return"
# statement immediately returns the obtained integer to the caller, and the loop is terminated.

# If the user enters a value that cannot be converted to an integer, a ValueError exception is raised, and the
# "except" block is executed. The program prints a message indicating that the input is not an integer, but
# the loop continues to prompt the user for input until a valid integer is provided.

# By removing the "else" block, the get_int() function has a more streamlined structure, achieving the same goal of
# obtaining a valid integer input and handling potential errors.
