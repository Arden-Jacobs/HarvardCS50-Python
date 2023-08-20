# hello11.py - Modular Approach with a Main Function

def main():
    """
    The main function that handles user input and calling the hello function.
    """
    # The `input()` function is used to prompt the user for their name and store it in the variable `name`.
    name = input("What's your name? ")
    
    # Call the `hello()` function, passing the value stored in the variable `name` as an argument.
    hello(name)

def hello(to="world"):
    """
    Prints a personalized greeting message using the provided name.
    
    :param to: The name of the person to greet. Default is "world".
    """
    print("hello,", to)

# Call the `main()` function to start the program.
main()



# In this section, we're introducing a modular approach with a main function. The main() function is defined to
# handle user input and call the hello() function. The docstring explains the purpose of the main() function. 
# The hello() function remains the same, accepting a parameter with a default value. The program starts by
#  calling the main() function, which orchestrates the flow of the program by taking user input and 
#  calling the hello() function.