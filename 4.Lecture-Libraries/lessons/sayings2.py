# sayings2.py - Custom module with main function and __name__ check

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

# Check if the module is being run directly (not imported)
if __name__ == "__main__":
    # Call the main function to execute the code when the module is run directly
    main()

# Explanation:
# This custom module defines functions for generating greeting and goodbye messages, demonstrates the use
# of a main function, and includes a check using __name__ to ensure that code is executed only when the module is run directly.

# The function "main()" is defined to encapsulate the sequence of function calls. It calls the "hello" and "goodbye"
# functions to print greeting and goodbye messages for the name "world."

# The functions "hello(name)" and "goodbye(name)" are defined to print greeting and goodbye messages using f-strings.

# The if statement "__name__ == '__main__':" checks if the module is being run directly (not imported). If true, the
# "main()" function is called to execute the code contained within it when the module is run directly.
