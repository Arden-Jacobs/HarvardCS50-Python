# calculator10.py - Integer Division, Formatting

# This program demonstrates integer division, result formatting with two decimal places.

# The `int()` function is used to convert the user's input directly into integers.
# The `input()` function is used to prompt the user for the value of `x` and convert it to an integer, stored in the variable `x`.
x = int(input("What's x? "))

# Similarly, the `input()` function is used to prompt the user for the value of `y` and convert it to an integer, stored in the variable `y`.
y = int(input("What's y? "))

# The variables `x` and `y` store integer values obtained from user input.
# The integers are divided using the `/` operator, and the result is stored in the variable `z`.
z = x / y

# The `print()` function uses an f-string to display the result of the integer division,
# formatted with two decimal places.
print(f"{z:.2f}")



# In this section, we're demonstrating integer division, result formatting with two decimal places, and number 
# formatting using an f-string. The int() function is used to directly convert the user's input into integers.
# The input() function is used twice to prompt the user for values of x and y, and the resulting integer 
# values are used for calculations. The result of the division is displayed with two decimal places 
# using an f-string.