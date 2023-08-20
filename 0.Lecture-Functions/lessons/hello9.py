# hello9.py - Functions with Parameters

def hello(to):
    """
    Prints a personalized greeting message using the provided name.
    
    :param to: The name of the person to greet.
    """
    print("hello,", to)

# The `input()` function is used to prompt the user for their name and store it in the variable `name`.
name = input("What's your name? ")

# Call the `hello()` function, passing the value stored in the variable `name` as an argument.
hello(name)



# In this section, we're introducing functions with parameters. The hello() function is defined to accept
# a parameter named to, which represents the name of the person to greet. The docstring explains the 
# purpose and parameter of the function. The input() function is used to prompt the user for their
# name, and the value is stored in the variable name. The hello() function is then called, 
# passing the value stored in the variable name as an argument.

