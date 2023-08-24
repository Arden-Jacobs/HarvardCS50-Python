# number4.py - Adds a loop to repeatedly ask for valid input

while True:
    try:
        # Attempt to get an integer input from the user and store it in variable x
        x = int(input("What's x? "))
    except ValueError:
        # If the input cannot be converted to an integer (ValueError), print an error message
        print("x is not an integer")
    else:
        # If no exception occurs, exit the loop
        break

# After breaking out of the loop, print the value of x using an f-string
print(f"x is {x}")


# Explanation:
# This code snippet introduces a loop to repeatedly prompt the user for input until a valid integer
# is entered. It uses a combination of "try", "except", and "else" to handle exceptions and control
# the flow of the program.

# The while True: statement creates an infinite loop that keeps running until a "break" statement is
# encountered. Inside the loop, the code attempts to get an integer input from the user using input()
# and int(). If the input is not a valid integer, a ValueError exception is caught by the "except"
# block, and an error message is printed.

# If the input is a valid integer and no exception occurs, the "else" block is executed, and the "break"
# statement is encountered. This breaks out of the infinite loop, and the program proceeds to the next line.

# After breaking out of the loop, the value of x is printed using an f-string, indicating that the value
# of x is now a valid integer.

# This code ensures that the program continues to ask for input until a valid integer is provided,
# improving user experience and preventing crashes due to incorrect input.
