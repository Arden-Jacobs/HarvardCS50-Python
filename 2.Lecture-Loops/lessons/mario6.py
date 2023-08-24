# mario6.py - Printing a Square of Bricks Using a Function with a Loop and str Multiplication

def main():
    # Call the print_square function with a size of 3
    print_square(3)


def print_square(size):
    """
    Prints a square of bricks using a loop and str multiplication.

    Args:
        size (int): The size of the square (number of rows and columns).
    """
    for _ in range(size):
        print("#" * size)


main()



# Explanation:
# In this code, a function print_square is defined to print a square of bricks using a loop and string multiplication.
# The main function is used to initiate the printing process by calling print_square(3).

# The print_square function takes the size as an argument, which represents both the number of rows and columns in
# the square. It uses a loop to iterate through each row of the square. Inside the loop, the "#" character is
# multiplied by the size using the * operator, resulting in a row of bricks of the desired length.
# The print function is then used to print the row.
