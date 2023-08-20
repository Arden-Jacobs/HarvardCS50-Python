# calculator7.py - User Input, Floating-Point Addition, Rounding, and Formatting

# This program demonstrates user input, type conversion to floating-point numbers,
# addition of floating-point numbers, rounding of the result, and number formatting.

# The `float()` function is used to convert the user's input directly into floating-point numbers.
# The `input()` function is used to prompt the user for the value of `x` and convert it to a float, stored in the variable `x`.
x = float(input("What's x? "))

# Similarly, the `input()` function is used to prompt the user for the value of `y` and convert it to a float, stored in the variable `y`.
y = float(input("What's y? "))

# The variables `x` and `y` store float values obtained from user input.
# The float numbers are added using the `+` operator, and the result is stored in the variable `z`.
# The `round()` function is used to round the floating-point result to the nearest integer.
z = round(x + y)

# The `print()` function uses an f-string to display the rounded integer value of `z`,
# formatted with commas to improve readability.
print(f"{z:,}")



# In this section, we're continuing to explore user input, type conversion to floating-point numbers,
# addition of floating-point numbers, rounding of the result, and number formatting. The float() 
# function is used to directly convert the user's input into floating-point numbers. The input()
# function is used twice to prompt the user for values of x and y, and the resulting float values
#  are used for calculations. The result of the addition is rounded and displayed using an 
# f-string with formatting to include commas for better readability.