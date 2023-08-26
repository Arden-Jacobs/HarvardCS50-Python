# sayings1.py - Custom module with main function

# Define the main function
def main():
    # Call the hello and goodbye functions within the main function
    hello("world")
    goodbye("world")

# Define a function to print a greeting message
def hello(name):
    print(f"hello, {name}")

# Define a function to print a goodbye message
def goodbye(name):
    print(f"goodbye, {name}")

# Call the main function to execute the code when the module is run
main()

# Explanation:
# This custom module defines functions for generating greeting and goodbye messages and demonstrates the use
# of a main function to organize the code and execute it.

# The function "main()" is defined to encapsulate the sequence of function calls. It calls the "hello" and "goodbye"
# functions to print greeting and goodbye messages for the name "world."

# The functions "hello(name)" and "goodbye(name)" are defined to print greeting and goodbye messages using f-strings.

# The "main()" function is called at the end of the module to execute the code contained within it when the module is run.
