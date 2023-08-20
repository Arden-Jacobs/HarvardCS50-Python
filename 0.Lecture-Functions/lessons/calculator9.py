# calculator9.py - Floating-Point Division, Rounding, and Formatting

# This program demonstrates floating-point division, rounding of the result, and formatting.

# The `float()` function is used to convert the user's input directly into floating-point numbers.
# The `input()` function is used to prompt the user for the value of `x` and convert it to a float, stored in the variable `x`.
x = float(input("What's x? "))

# Similarly, the `input()` function is used to prompt the user for the value of `y` and convert it to a float, stored in the variable `y`.
y = float(input("What's y? "))

# The variables `x` and `y` store float values obtained from user input.
# The float numbers are divided using the `/` operator, and the result is rounded to 2 decimal places and stored in the variable `z`.
z = round(x / y, 2)

# The `print()` function is used to display the result of the floating-point division,
# with the result rounded to 2 decimal places.
print(z)



# In this section, we're showcasing floating-point division, rounding of the result to two decimal places, and
# number formatting. The float() function is used to directly convert the user's input into floating-point
# numbers. The input() function is used twice to prompt the user for values of x and y, and the resulting 
# float values are used for calculations. The result of the division is rounded to two decimal places 
# and displayed using the print() function.