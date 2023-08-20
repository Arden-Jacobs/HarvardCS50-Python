# parity1.py - Demonstrates a Function That Returns a Boolean

# Define a function `is_even` that takes a number as a parameter and returns a boolean.

def is_even(n):
    """
    Check if a number is even.

    Args:
        n (int): The number to be checked.

    Returns:
        bool: True if the number is even, False otherwise.
    """
    if n % 2 == 0:
        return True
    else:
        return False

# Define the main function that prompts the user for a number,
# checks whether it's even using the `is_even` function,
# and prints "Even" or "Odd" accordingly.

def main():
    """
    Prompt the user for a number and determine if it's even or odd.

    This function prompts the user to enter a number, checks whether the number is even
    using the `is_even` function, and prints the result.
    """
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

# Call the main function to start the program execution.

main()



# In this section, the program demonstrates defining and using a function named is_even that returns a boolean
# value. The function takes a number as a parameter and uses the modulo operator to determine if the number is
# even or not.If the remainder of dividing the number by 2 is 0, the function returns True (indicating it's even),
# otherwise it returns False.

# The main function is defined to prompt the user for a number, call the is_even function to check if it's even,
# and then prints "Even" or "Odd" based on the result.The program execution starts by calling the main function.