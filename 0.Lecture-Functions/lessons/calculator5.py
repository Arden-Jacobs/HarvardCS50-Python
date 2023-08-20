# calculator5.py - User Input, Floating-Point Addition, and Rounding

# This program demonstrates user input, type conversion to floating-point numbers,
# addition of floating-point numbers, and rounding of the result.

# The `float()` function is used to convert the user's input directly into floating-point numbers.
# The `input()` function is used to prompt the user for the value of `x` and convert it to a float, stored in the variable `x`.
x = float(input("What's x? "))

# Similarly, the `input()` function is used to prompt the user for the value of `y` and convert it to a float, stored in the variable `y`.
y = float(input("What's y? "))

# The variables `x` and `y` store float values obtained from user input.
# The float numbers are added using the `+` operator, and the result is stored in the variable `z`.
# The `round()` function is used to round the floating-point result to the nearest integer.
z = round(x + y)

# The `print()` function is used to display the rounded integer value of `z`.
print(z)



# In this section, we're continuing to work with user input, type conversion to floating-point numbers, a
# ddition of floating-point numbers, and rounding of the result. The float() function is used to directly 
# convert the user's input into floating-point numbers. The input() function is used twice to prompt the 
# user for values of x and y, and the resulting float values are used for calculations. The round() 
# function is then used to round the floating-point result to the nearest integer, which is 
# displayed using the print() function.
