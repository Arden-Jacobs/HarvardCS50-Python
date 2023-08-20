# hello4.py - Customizing Print Output

# This program showcases how to customize the output of the `print()` function
# using the `end` parameter to modify the ending character.

# The `input()` function prompts the user for their name and stores it in the variable `name`.
name = input("What's your name? ")

# The `print()` function is used to output a personalized greeting.
# The `end` parameter is set to an empty string to prevent the default newline character.
# This allows the following `print()` statement to be displayed on the same line.
print("hello, ", end="")
print(name)



# In this section, we're customizing the output of the print() function using the end parameter.
# The user's name is obtained using the input() function and stored in the name variable. The 
# first print() statement outputs "hello, " and sets the end parameter to an empty string to 
# prevent a newline. This ensures that the following print() statement is displayed on the same line.