# mario3.py - Printing a Column of Bricks Using a Function with String Multiplication

def main():
    # Call the print_column function with a height of 3
    print_column(3)


def print_column(height):
    """
    Prints a column of bricks using string multiplication.

    Args:
        height (int): The height of the column (number of rows).
    """
    print("#\n" * height, end="")

main()



# Explanation:
# In this code, a function print_column is defined to print a column of bricks using string multiplication.
# The main function is used to initiate the printing process by calling print_column(3).

# The print_column function takes the height as an argument and prints a "#" character followed by a newline character,
# all multiplied by the height value. This results in a vertical column of bricks with the specified height.

# The end="" parameter in the print function ensures that the newline character at the end of each print statement
# is suppressed, so the bricks are printed vertically in a single line.
