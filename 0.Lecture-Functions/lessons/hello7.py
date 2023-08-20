# hello6.py - String Manipulation

# This program demonstrates string manipulation techniques, including stripping whitespace
# and capitalizing the first letter of each word using the `strip()` and `title()` methods.

# The `input()` function prompts the user for their name and stores it in the variable `name`.
# The `strip()` method is used to remove any leading or trailing whitespace from the input.
# The `title()` method capitalizes the first letter of each word in the input.
name = input("What's your name? ").strip().title()

# The `print()` function uses an f-string to create a personalized greeting.
# The value of the `name` variable, after string manipulation, is inserted into the string using curly braces.
print(f"hello, {name}")



# In this section, we're introducing string manipulation techniques. The user's name is obtained using the 
# input() function, and then the strip() method is applied to remove any leading or trailing whitespace. 
# Additionally, the title() method is used to capitalize the first letter of each word in the input. 
# The print() function then uses an f-string to create a personalized greeting with the manipulated name.