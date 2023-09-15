# File Name: bank3.py

# Description: This script defines a bank account using a class 'Account'. The class encapsulates the balance as a private attribute '_balance' and provides
# methods to interact with the balance, including 'deposit' and 'withdraw'. It also includes a 'balance' property to retrieve the current balance.

# Define the 'Account' class to represent a bank account.
class Account:
    def __init__(self):
        # Initialize the private attribute '_balance' with an initial value of 0.
        self._balance = 0

    # Define a 'balance' property to retrieve the current balance.
    @property
    def balance(self):
        return self._balance

    # Define the 'deposit' method to add the specified amount to the balance.
    def deposit(self, n):
        self._balance += n

    # Define the 'withdraw' method to subtract the specified amount from the balance.
    def withdraw(self, n):
        self._balance -= n

# Define the main function.
def main():
    # Create an 'Account' instance to represent the bank account.
    account = Account()
    
    # Print the current balance (0 at the beginning).
    print("Balance:", account.balance)
    
    # Deposit 100 into the account.
    account.deposit(100)
    
    # Withdraw 50 from the account.
    account.withdraw(50)
    
    # Print the updated balance (50 after deposit and withdrawal).
    print("Balance:", account.balance)

# Check if the script is run as the main program.
if __name__ == "__main__":
    # If it is, call the 'main' function to simulate transactions and display the balance.
    main()

# Explanation:

# Description: This script defines a bank account using a class 'Account'. The class encapsulates the balance as a private attribute '_balance' and provides
# methods to interact with the balance, including 'deposit' and 'withdraw'. It also includes a 'balance' property to retrieve the current balance.

# The script consists of the following components:

# - 'Account' class: This class is defined to represent a bank account. It has the following components:
#   - '__init__' method: The constructor initializes the private attribute '_balance' with an initial value of 0 when a new 'Account' instance is created.
#   - 'balance' property: This property uses the @property decorator to allow reading the current balance using the 'account.balance' syntax.
#   - 'deposit' method: This method adds the specified amount to the balance.
#   - 'withdraw' method: This method subtracts the specified amount from the balance.

# - 'main' function: This function serves as the entry point of the script. It demonstrates the usage of the 'Account' class by creating an 'Account' instance,
#   performing deposit and withdrawal transactions, and displaying the current balance using the 'account.balance' property.

# - Check for the script being run as the main program: The script checks whether it is executed as the main program and, if it is, calls the 'main' function
#   to initiate the banking simulation.

# By encapsulating the bank account functionality within a class, this script provides a cleaner and more organized way to manage the balance and transactions.
