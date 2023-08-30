# names6.py - Reads names from a file, one line at a time, and prints greeting messages

# Open the "names.txt" file in read mode using a context manager and loop through its lines
with open("names.txt") as file:
    for line in file:
        print("hello,", line.rstrip())

# Explanation:
# This script reads names from the "names.txt" file, where each name is stored on a separate line.

# The script uses a context manager to open the "names.txt" file in read mode. The context manager automatically
# takes care of opening and closing the file.

# The for loop directly iterates over the lines of the file using the file object itself. For each iteration, the loop
# assigns the current line to the "line" variable. This allows the script to process one line at a time.

# Within the loop, the print() function is used to display a greeting message for each name. The rstrip() method is
# used to remove any trailing whitespace (including newline characters) from each line.

# The result is a series of greeting messages, each corresponding to a name read from the "names.txt" file.
