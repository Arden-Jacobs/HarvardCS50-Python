# mario4.py - Printing a Row of Coins Using a Function with String Multiplication

def main():
    # Call the print_row function with a width of 4
    print_row(4)


def print_row(width):
    """
    Prints a row of coins using string multiplication.

    Args:
        width (int): The width of the row (number of coins).
    """
    print("?" * width)

main()



# Explanation:
# In this code, a function print_row is defined to print a row of coins using string multiplication.
# The main function is used to initiate the printing process by calling print_row(4).

# The print_row function takes the width as an argument and prints the "?" character multiplied by the width
# value. This results in a horizontal row of coins with the specified width.
