# number5.py - Adds functions, uses break and return

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
            x = int(input("What's x? "))  # Prompt the user for input
        except ValueError:
            print("x is not an integer")  # Handle the ValueError exception
        else:
            break  # Exit the loop if valid input is obtained
    return x  # Return the obtained integer to the caller

# Call the main function to start the program
main()

# Explanation:
# This code snippet demonstrates the use of functions, the "break" statement, and the "return" statement to obtain
# and validate an integer input from the user.

# The main() function serves as the entry point of the program. It calls the get_int() function to obtain a valid
# integer input from the user and then prints the value of x.

# The get_int() function uses a "while True" loop to continuously prompt the user for input. Within the loop, it
# uses a "try" block to attempt to convert the user input into an integer. If successful, the loop is exited using
# the "break" statement, and the obtained integer is returned to the caller using the "return" statement.

# If the user enters a value that cannot be converted to an integer, a ValueError exception is raised, and the
# "except" block is executed. The program prints a message indicating that the input is not an integer, and the
# loop continues to prompt the user for input until a valid integer is provided.

# The use of functions and control statements like "break" and "return" enhances the code's readability, reusability,
# and error handling capabilities.
