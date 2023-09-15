# File Name: bank0.py

# Description: This script implements a basic bank account by defining a 'balance' variable and a 'main' function to display the balance.
# The balance is initialized to zero and displayed when the script is run as the main program.

# Initialize the 'balance' variable to zero.
balance = 0

# Define the main function.
def main():
    # Print the current balance.
    print("Balance:", balance)

# Check if the script is run as the main program.
if __name__ == "__main__":
    # If it is, call the 'main' function to display the balance, which is initially set to zero.
    main()

# Explanation:

# Description: This script implements a basic bank account by defining a 'balance' variable and a 'main' function to display the balance.
# The balance is initialized to zero and displayed when the script is run as the main program.

# The script consists of the following components:

# - 'balance' variable: This variable is initialized to zero, representing the initial balance of the bank account.

# - 'main' function: This function is the entry point of the script. It simply prints the current balance by using the 'print' function with the message "Balance:"
#   followed by the value of the 'balance' variable.

# - Check for the script being run as the main program: The script checks whether it is executed as the main program using the '__name__' attribute.
#   If it is the main program (i.e., '__name__' is equal to "__main__"), it calls the 'main' function to display the balance, which is initially set to zero.
