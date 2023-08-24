# mario2.py - Printing a Column of Bricks Using a Function with a Loop

def main():
    # Call the print_column function with a height of 3
    print_column(3)


def print_column(height):
    """
    Prints a column of bricks.

    Args:
        height (int): The height of the column (number of rows).
    """
    for _ in range(height):
        print("#")


main()



# Explanation:
# This code builds upon the previous example by introducing a function called print_column that takes the height
# of the column as an argument. The main function is used to initiate the printing process by calling print_column(3).

# The print_column function contains a loop that iterates height times, where each iteration prints a "#"
# character to form a vertical column of bricks. The use of functions enhances code organization and reusability.
