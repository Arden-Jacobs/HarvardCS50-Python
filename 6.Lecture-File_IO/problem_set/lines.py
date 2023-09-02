# File Name: lines.py
# Description: Count non-empty lines of code in a Python file

import sys

# Check the number of command-line arguments
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

arg = sys.argv[1]

# Check if the argument is a Python file
if ".py" not in arg:
    sys.exit("Not a Python file")

count = 0

try:
    with open(arg) as file:
        for line in file:
            # Check if the line is empty or a comment line (starts with "#")
            if line.strip() == "" or line.lstrip().startswith("# "):
                pass
            else:
                count += 1
    print(count)

except FileNotFoundError:
    sys.exit("File does not exist")

# Explanation:
# This script counts non-empty lines of code in a Python file.
# It takes a Python file as a command-line argument and checks if the argument is a valid Python file.

# The script uses a try-except block to handle possible errors, such as a non-existing file.
# It opens the specified Python file using a with statement and iterates through each line in the file.

# For each line, it checks if the line is either empty (whitespace characters removed) or a comment line
# (starts with "# "). If the line is neither empty nor a comment, it increments the count variable.

# After processing all lines in the file, the script prints the count of non-empty lines of code.
