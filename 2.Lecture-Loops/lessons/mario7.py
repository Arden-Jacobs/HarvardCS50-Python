# mario7.py - Printing a Square of Bricks Using Functions with Loops and str Multiplication

def main():
    # Call the print_square function with a size of 3
    print_square(3)


def print_square(size):
    """
    Prints a square of bricks using a function with loops and str multiplication.

    Args:
        size (int): The size of the square (number of rows and columns).
    """
    for _ in range(size):
        print_row(size)


def print_row(width):
    """
    Prints a row of bricks using str multiplication.

    Args:
        width (int): The width of the row (number of bricks).
    """
    print("#" * width)


main()

# Explanation:
# In this code, two functions are defined: print_square and print_row, both of which contribute to printing a square of bricks.

# The main function initiates the printing process by calling print_square(3).

# The print_square function takes the size as an argument, representing the number of rows and columns in the square.
# It uses a loop to iterate through each row of the square, and within each row, it calls the print_row
# function to print a row of bricks.

# The print_row function takes the width as an argument, representing the number of bricks in the row. It uses
# string multiplication to print a row of bricks of the desired width.
