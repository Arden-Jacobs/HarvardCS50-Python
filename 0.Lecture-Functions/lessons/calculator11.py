# calculator11.py - Modular Approach with a Main Function

def main():
    """
    The main function that handles user input and calls the square function.
    """
    # The `input()` function is used to prompt the user for the value of `x` and convert it to an integer, stored in the variable `x`.
    x = int(input("What's x? "))
    
    # Call the `square()` function, passing the value stored in the variable `x` as an argument,
    # and print the result.
    print("x squared is", square(x))

def square(n):
    """
    Calculates the square of a given number.
    
    :param n: The number to be squared.
    :return: The square of the given number.
    """
    return n * n

# Call the `main()` function to start the program.
main()



# In this section, we're continuing the modular approach with a main function. The main() function is defined to
# handle user input, call the square() function, and print the result. The docstrings provide explanations for 
# both functions. The square() function calculates the square of a given number. The program starts by calling
# the main() function, which prompts the user for input, calls the square() function, and displays the result.