# names5.py - Reads names from a file and prints greeting messages

# Open the "names.txt" file in read mode using a context manager and read its lines into a list
with open("names.txt") as file:
    lines = file.readlines()

# Loop through the lines list and print greeting messages for each name
for line in lines:
    print("hello,", line.rstrip())

# Explanation:
# This script reads names from the "names.txt" file, where each name is stored on a separate line.

# The script uses a context manager to open the "names.txt" file in read mode. The context manager automatically
# takes care of opening and closing the file.

# The readlines() method is used to read the lines of the file and store them as a list of strings in the "lines" variable.
# Each element of the list corresponds to a line in the file.

# The script then loops through the "lines" list using a for loop. For each line, it prints a greeting message using the
# print() function. The rstrip() method is used to remove any trailing whitespace (including newline characters) from each line.

# The result is a series of greeting messages, each corresponding to a name read from the "names.txt" file.
