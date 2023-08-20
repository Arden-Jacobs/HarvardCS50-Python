# interpreter.py - Prompt User for an Arithmetic Expression and Perform Calculation

# Prompt the user for an arithmetic expression.
expression = input("Enter an expression: ")

# Extract individual elements from the expression.
x = expression[0]
y = expression[2]
z = expression[-1]

# Convert elements to float for calculation.
x = float(x)
z = float(z)

# Check if the expression has a length of 6 characters.
if len(expression) == 6:
    # If true, extract the second element and perform calculations.
    x = expression[0] + expression[1]
    x = float(x)
    y = expression[3]

# Perform calculations based on the operator.
if y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "*":
    print(x * z)
elif y == "/":
    print(x / z)



# In this section, the code prompts the user for an arithmetic expression and performs calculations based on the
# provided expression. The expression is assumed to be in the format "x y z" where x and z are numbers,
# and y is an arithmetic operator.

# The code extracts the individual elements (x, y, and z) from the expression and converts them to floats for
# calculation. It then checks if the length of the expression is 6 characters. If it is, the code extracts
# the second element from the expression and performs calculations.

# Based on the operator y, the code performs addition, subtraction, multiplication, or division calculations
# and prints the result.