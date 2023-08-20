# parity0.py - Demonstrates Modulo Operator

# Prompt the user for a number and convert it to an integer.
x = int(input("What's x? "))

# Determine whether the number is even or odd using the modulo operator.

# If the remainder of dividing x by 2 is 0, the number is even.
if x % 2 == 0:
    print("Even")

# If the remainder of dividing x by 2 is not 0, the number is odd.
else:
    print("Odd")



# In this section, the program demonstrates determining whether a given number is even or odd using the modulo
# operator (%). The input() function is used to prompt the user for a number, which is converted to an integer.
# The program uses an if statement with the condition x % 2 == 0 to check whether the remainder of dividing
# x by 2 is 0. If this condition is true, it means that x is even, and the program prints "Even".
# Otherwise, if the condition is false, it implies that x is odd, and the program prints "Odd".