# File Name: meows8.py
# Description: This script demonstrates a successful function with proper type annotations and returns a string containing "meow" repeated 'n' times.

# Define the 'meow' function, which takes an integer 'n' as an argument, returns a string containing "meow" repeated 'n' times, and is annotated with a return type of 'str'.
def meow(n: int) -> str:
    return "meow\n" * n

# Prompt the user for input, convert it to an integer, and store it in the 'number' variable with a type hint of 'int'.
number: int = int(input("Number: "))

# Call the 'meow' function with the 'number' input, which successfully returns a string, and assign it to 'meows'.
meows: str = meow(number)

# Print 'meows' without adding an extra newline character.
print(meows, end="")

# Explanation:
# Description: This script showcases a successful function with proper type annotations. The 'meow' function takes an integer 'n' as an argument, returns a string containing "meow" repeated 'n' times, and is annotated with a return type of 'str'.
# The script contains the following components:
# - 'meow' function: It is defined to expect an integer 'n' as an argument, return a string containing "meow" repeated 'n' times, and is annotated with a return type of 'str'.
# - Input prompt: The user is prompted to enter a number, and the input is converted to an integer using 'int()' and then assigned to the 'number' variable with a type hint of 'int'.
# - Function call: The 'meow' function is called with the 'number' input, which successfully returns a string, and the result is assigned to 'meows'.
# - Print statement: The 'meows' variable is printed without adding an extra newline character to the end.
# The script demonstrates proper function annotations and return values in Python.
