# parity3.py - Demonstrates Returning the Value of a Boolean Expression

def is_even(n):
    """
    Check if a number is even.

    Args:
        n (int): The number to be checked.

    Returns:
        bool: True if the number is even, False otherwise.
    """
    return n % 2 == 0

def main():
    """
    Prompt the user for a number and determine if it's even or odd.

    This function prompts the user to enter a number, checks whether the number is even
    using the `is_even` function with a returned boolean expression, and prints the result.
    """
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

main()



# In this section, the code demonstrates using the value of a boolean expression directly as the return value of
# the is_even function. Instead of using an if-else structure to return True or False based on the condition,
# the function directly returns the result of the boolean expression n % 2 == 0. 
# his approach simplifies the code and directly returns the boolean value.