# File Name: bank1.py

# Description: This script defines a simple bank account with a 'balance' variable and two functions, 'deposit' and 'withdraw', to modify the balance.
# However, it encounters an UnboundLocalError due to the variable scope issue.

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
    
    # Print the updated balance, which should be 50. However, it will result in an UnboundLocalError.
    print("Balance:", balance)

# Define the 'deposit' function to add the specified amount to the balance.
def deposit(n):
    # Attempt to modify the 'balance' variable without declaring it as global.
    # This will lead to an UnboundLocalError since Python treats 'balance' as a local variable in this scope.
    balance += n

# Define the 'withdraw' function to subtract the specified amount from the balance.
def withdraw(n):
    # Attempt to modify the 'balance' variable without declaring it as global.
    # This will also lead to an UnboundLocalError.
    balance -= n

# Check if the script is run as the main program.
if __name__ == "__main__":
    # If it is, call the 'main' function to simulate transactions and display the balance.
    main()

# Explanation:

# Description: This script defines a simple bank account with a 'balance' variable and two functions, 'deposit' and 'withdraw', to modify the balance.
# However, it encounters an UnboundLocalError due to the variable scope issue.

# The script consists of the following components:

# - 'balance' variable: This variable is initialized with an initial value of 0 and represents the bank account balance.

# - 'main' function: This function is the entry point of the script. It prints the current balance, calls the 'deposit' and 'withdraw' functions to simulate
#   transactions, and attempts to print the updated balance. However, this attempt results in an UnboundLocalError due to the variable scope issue.

# - 'deposit' function: This function is defined to add the specified amount to the balance. However, it attempts to modify the 'balance' variable without
#   declaring it as global, which leads to an UnboundLocalError. The corrected code should use the 'global' keyword to indicate that it's modifying the
#   global 'balance' variable.

# - 'withdraw' function: This function is defined to subtract the specified amount from the balance. Similar to the 'deposit' function, it also attempts
#   to modify the 'balance' variable without declaring it as global, resulting in an UnboundLocalError.

# - Check for the script being run as the main program: The script checks whether it is executed as the main program and, if it is, calls the 'main' function
#   to initiate the banking simulation.

# To fix the UnboundLocalError issue, you should modify the 'deposit' and 'withdraw' functions by adding the 'global' keyword before 'balance', indicating
# that you intend to modify the global variable 'balance'. Here's the corrected code:

# def deposit(n):
#     global balance
#     balance += n

# def withdraw(n):
#     global balance
#     balance -= n
