# number2.py - Demonstrates a NameError

try:
    # Try to get an integer input from the user and store it in variable x
    x = int(input("What's x? "))
except ValueError:
    # If the input cannot be converted to an integer (ValueError), print an error message
    print("x is not an integer")

# Print the value of x using an f-string
print(f"x is {x}")



# Explanation:
# The code aims to demonstrate a NameError that occurs when attempting to access a variable
# that hasn't been defined in a particular scope.

# The try-except block is used to handle exceptions that might occur when attempting to get
# input from the user and convert it to an integer.

# Inside the try block, the input() function is used to prompt the user for input. If the user
# enters a non-integer value, a ValueError exception will be raised. If no exception is raised,
# the value entered by the user is stored in the variable x.

# If a ValueError occurs, the code inside the except block will be executed. In this case, a
# message "x is not an integer" is printed.

# After the try-except block, the code attempts to print the value of x using an f-string.
# However, if a ValueError occurred and x was not assigned a value, a NameError will be raised
# when trying to access x. This demonstrates the concept of a NameError, which occurs when
# attempting to use a variable that hasn't been defined or is not accessible in the current scope.

# To prevent a NameError, it's essential to ensure that a variable is defined and assigned a
# value before attempting to use it in the code.
