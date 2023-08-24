# number3.py - Demonstrates else in exception handling

try:
    # Attempt to get an integer input from the user and store it in variable x
    x = int(input("What's x? "))
except ValueError:
    # If the input cannot be converted to an integer (ValueError), print an error message
    print("x is not an integer")
else:
    # If no exception occurred, print the value of x using an f-string
    print(f"x is {x}")



# Explanation:
# This code snippet demonstrates the use of the "else" clause in exception handling, which
# executes a block of code when no exception occurs in the "try" block.

# Inside the "try" block, the input() function is used to prompt the user for input. If the user
# enters a non-integer value, a ValueError exception will be raised. If the input is a valid
# integer, it is stored in the variable x.

# If a ValueError exception occurs, the code inside the "except" block will be executed, and
# an error message "x is not an integer" will be printed.

# If no exception occurs in the "try" block, the code inside the "else" block will be executed.
# This block prints the value of x using an f-string, indicating that the value of x is an integer.

# The "else" clause provides a way to separate the code that handles exceptions from the code
# that executes when no exception occurs. It improves code readability by making it clear which
# part of the code is executed in which scenario.
