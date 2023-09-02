# File: lines.py
# Description: Counts the number of non-empty and non-comment lines in a Python source code file.

# Import the sys module to access command-line arguments.
import sys

# Check the number of command-line arguments.
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

# Get the first command-line argument (the filename).
arg = sys.argv[1]

# Check if the argument is a Python file (ends with ".py").
if ".py" not in arg:
    sys.exit("Not a Python file")

# Initialize a variable to count non-empty and non-comment lines.
count = 0

try:
    # Open the Python file specified in the command-line argument.
    with open(arg) as file:
        # Iterate through each line in the file.
        for line in file:
            # Check if the line is either empty or starts with a comment (indicated by "# ").
            if line.strip() == "" or line.lstrip().startswith("# "):
                # If the line is empty or a comment, skip it.
                pass
            else:
                # If the line is not empty and not a comment, increment the count.
                count += 1
    # Print the final count of non-empty and non-comment lines.
    print(count)

except FileNotFoundError:
    sys.exit("File does not exist")

# Explanation:

# This script helps you count the number of lines that have actual code in a Python file. 
# It doesn't count blank lines or lines that contain comments.

# To use the script, you should run it from the command line with the name of a Python file as an argument. 
# For example, if you have a file named "my_program.py," you'd run the script like this:
# python lines.py my_program.py

# The script first checks if you provided the correct number of arguments when running it. 
# If you didn't provide the right number (either too few or too many), it will show an error message and exit.

# Then, it checks if the provided argument ends with ".py" to ensure it's a Python file. 
# If it's not, the script will also show an error message and exit.

# After these initial checks, the script opens the Python file you specified. 
# It goes through each line in the file one by one.

# For each line, it checks if the line is empty or if it starts with a "#" symbol. 
# In Python, "#" is used to mark comments. So, if a line is either empty or a comment, 
# it's skipped and not counted.

# If a line is not empty and doesn't start with "#" (meaning it contains actual code), 
# the script increases the count of non-empty, non-comment lines by one.

# After examining all lines in the file, the script prints out the final count, 
# which represents the number of lines with actual code.

# In summary, this script helps programmers quickly determine how much code is in a Python file 
# without counting comments or blank lines manually.
