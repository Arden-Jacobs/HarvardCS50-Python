# parity2.py - Demonstrates Conditional Expressions (Ternary Operators)

def is_even(n):
    """
    Check if a number is even.

    Args:
        n (int): The number to be checked.

    Returns:
        bool: True if the number is even, False otherwise.
    """
    return True if n % 2 == 0 else False

def main():
    """
    Prompt the user for a number and determine if it's even or odd.

    This function prompts the user to enter a number, checks whether the number is even
    using the `is_even` function with a ternary operator, and prints the result.
    """
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

main()



# In this section, the code uses a conditional expression (ternary operator) within the is_even function to
# determine if a given number is even. The is_even function now returns True if the condition n % 2 == 0 is
# true,and False otherwise, all in a single line using the ternary operator.

# The rest of the code structure remains similar to the previous examples, with docstrings and comments as
# required, and the main() function using the is_even function to determine and print whether the input
# number is even or odd.