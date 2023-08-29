# name1.py - Stores names in a list, sorts them, and prints greeting messages

# Create an empty list to store names
names = []

# Loop to input names and append them to the "names" list
for _ in range(3):
    names.append(input("What's your name? "))

# Loop to iterate through sorted names and print greeting messages
for name in sorted(names):
    print(f"hello, {name}")

# Explanation:
# This script demonstrates how to store names in a list, sort the list, and print greeting messages for each name.

# The script starts by creating an empty list called "names" to store the input names.

# The first loop runs three times (for _ in range(3)) and prompts the user to input their name using the input() function.
# Each input name is appended to the "names" list using the append() method.

# After all names are collected in the list, the second loop iterates through the sorted "names" list using the sorted() function.
# It then prints a greeting message for each sorted name using an f-string. The message "hello, {name}" is printed to the console,
# where {name} is replaced with each name from the sorted list.

# The result is a series of greeting messages, each corresponding to a name that has been sorted in alphabetical order.
