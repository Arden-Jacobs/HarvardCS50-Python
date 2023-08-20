# compare2.py - Demonstrates Fewer Conditions

# Prompt the user for values of x and y, and convert them to integers.
x = int(input("What's x? "))
y = int(input("What's y? "))

# Compare x and y using fewer if-elif-else statements to determine the relationship between them.

# If x is less than y, print the corresponding message.
if x < y:
    print("x is less than y")

# If x is greater than y, print the corresponding message.
elif x > y:
    print("x is greater than y")

# If neither of the above conditions is met, it implies that x must be equal to y.
else:
    print("x is equal to y")



# In this section, the program continues to demonstrate comparison using if-elif-else statements. The process is
# the same as in the previous section. The input() function is used to prompt the user for values of x and y,
# which are converted to integers. The program uses if-elif-else statements to compare the values and print
# the corresponding message based on the comparison results. If neither the first if condition nor the elif
# condition is met, it implies that x must be equal to y, and the corresponding message is printed.