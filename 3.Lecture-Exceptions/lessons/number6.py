# number5.py - Adds functions, uses break and return

def main():
    # Call the get_int() function to obtain a valid integer
    x = get_int()
    # Print the value of x using an f-string
    print(f"x is {x}")

# Define the get_int() function to handle input and validation
def get_int():
    while True:
        try:
            # Attempt to get an integer input from the user and store it in variable x
            x = int(input("What's x? "))
        except ValueError:
            # If the input cannot be converted to an integer (ValueError), print an error message
            print("x is not an integer")
        else:
            # If no exception occurs, exit the loop and return the value of x
            return x

# Call the main() function to start the program
main()



# Explanation:
# This code snippet demonstrates the use of functions, "break", and "return" to organize and structure
# the code for better readability and maintainability.

# The main() function is defined to serve as the entry point of the program. It calls the get_int()
# function to obtain a valid integer input from the user. After receiving the input, it prints the value of x.

# The get_int() function is defined to handle the process of obtaining a valid integer input. It uses a
# "while True" loop to repeatedly prompt the user until a valid integer is entered. Inside the loop, it
# tries to convert the input to an integer using int(). If a ValueError exception is caught (indicating
# invalid input), an error message is printed. If no exception occurs, the loop is exited using "break",
# and the value of x is returned.

# By using functions, the code is divided into logical sections, making it easier to understand and maintain.
# The use of "return" in the get_int() function allows the valid integer to be returned to the caller, which
# is then assigned to the variable x in the main() function for printing.
