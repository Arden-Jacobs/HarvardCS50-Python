# File Name: bank2.py

# Description: This script defines a simple bank account with a 'balance' variable and two functions, 'deposit' and 'withdraw', to modify the balance.
# It correctly uses the 'global' keyword to indicate that it's modifying the global 'balance' variable.

# Initialize the 'balance' variable with an initial value of 0.
balance = 0

# Define the main function.
def main():
    # Print the current balance.
    print("Balance:", balance)
    
    # Call the 'deposit' function to add 100 to the balance.
    deposit(100)
    
    # Call the 'withdraw' function to subtract 50 from the balance.
    withdraw(50)
    
    # Print the updated balance, which should be 50.
    print("Balance:", balance)

# Define the 'deposit' function to add the specified amount to the balance.
def deposit(n):
    # Use the 'global' keyword to indicate that we're modifying the global 'balance' variable.
    global balance
    balance += n

# Define the 'withdraw' function to subtract the specified amount from the balance.
def withdraw(n):
    # Use the 'global' keyword to indicate that we're modifying the global 'balance' variable.
    global balance
    balance -= n

# Check if the script is run as the main program.
if __name__ == "__main__":
    # If it is, call the 'main' function to simulate transactions and display the balance.
    main()

# Explanation:

# Description: This script defines a simple bank account with a 'balance' variable and two functions, 'deposit' and 'withdraw', to modify the balance.
# It correctly uses the 'global' keyword to indicate that it's modifying the global 'balance' variable.

# The script consists of the following components:

# - 'balance' variable: This variable is initialized with an initial value of 0 and represents the bank account balance.

# - 'main' function: This function is the entry point of the script. It prints the current balance, calls the 'deposit' and 'withdraw' functions to simulate
#   transactions, and prints the updated balance. The usage of the 'global' keyword ensures that the 'balance' variable is modified globally.

# - 'deposit' function: This function is defined to add the specified amount to the balance. It uses the 'global' keyword to indicate that it's modifying
#   the global 'balance' variable, ensuring that the modification is applied globally.

# - 'withdraw' function: This function is defined to subtract the specified amount from the balance. Similar to the 'deposit' function, it uses the 'global'
#   keyword to indicate that it's modifying the global 'balance' variable, ensuring that the modification is applied globally.

# - Check for the script being run as the main program: The script checks whether it is executed as the main program and, if it is, calls the 'main' function
#   to initiate the banking simulation.

# By using the 'global' keyword in the 'deposit' and 'withdraw' functions, this script correctly updates the global 'balance' variable and avoids
# the UnboundLocalError issue encountered in the previous version of the script (bank1.py).
