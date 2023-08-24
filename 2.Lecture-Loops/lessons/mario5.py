# mario5.py - Printing a Square of Bricks Using a Function with Nested Loops

def main():
    # Call the print_square function with a size of 3
    print_square(3)


def print_square(size):
    """
    Prints a square of bricks using nested loops.

    Args:
        size (int): The size of the square (number of rows and columns).
    """
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()


main()



# Explanation:
# In this code, a function print_square is defined to print a square of bricks using nested loops.
# The main function is used to initiate the printing process by calling print_square(3).

# The print_square function takes the size as an argument, which represents both the number of rows and columns
# in the square. It uses two nested loops to iterate through each row and column of the square.
# In the inner loop, the "#" character is printed without moving to the next line using the
# end="" parameter in the print function. After printing a row of bricks, the outer loop
# moves to the next line using the print() function.
