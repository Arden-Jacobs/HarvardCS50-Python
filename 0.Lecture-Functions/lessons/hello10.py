# hello10.py - Functions with Default Parameters

def hello(to="world"):
    """
    Prints a personalized greeting message using the provided name.
    
    :param to: The name of the person to greet. Default is "world".
    """
    print("hello,", to)

# Call the `hello()` function without passing any arguments.
hello()

# The `input()` function is used to prompt the user for their name and store it in the variable `name`.
name = input("What's your name? ")

# Call the `hello()` function, passing the value stored in the variable `name` as an argument.
hello(name)



# In this section, we're introducing functions with default parameters. The hello() function is defined to
# accept a parameter named to, with a default value of "world". The docstring explains the purpose of the
# function and the default parameter value. The function is called twice: first without passing any 
# arguments, which uses the default value, and then with the user's input stored in the variable 
# name as an argument.