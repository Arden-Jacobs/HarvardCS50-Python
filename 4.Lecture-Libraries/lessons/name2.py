# name2.py - Adds error checking for command-line arguments

# Import the sys module to access command-line arguments
import sys

# Check the number of command-line arguments and handle different cases
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    # Print a message that includes the provided command-line argument
    print("hello, my name is", sys.argv[1])

# Explanation:
# This code demonstrates how to perform error checking for the number of command-line arguments using sys.argv.

# The import statement "import sys" at the beginning of the script imports the sys module, which provides
# access to variables and functions related to the Python interpreter.

# The if-elif-else structure is used to check the number of command-line arguments provided:
# - If there are fewer than 2 arguments, the script prints "Too few arguments."
# - If there are more than 2 arguments, the script prints "Too many arguments."
# - If there are exactly 2 arguments, the script prints a message that includes the second command-line
#   argument, accessed using sys.argv[1].
