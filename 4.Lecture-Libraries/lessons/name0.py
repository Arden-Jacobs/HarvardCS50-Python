# name0.py - Demonstrates sys.argv

# Import the sys module to access command-line arguments
import sys

# Print a message that includes the provided command-line argument
print("hello, my name is", sys.argv[1])

# Explanation:
# This code showcases the use of the sys.argv list to access command-line arguments passed to a Python script.

# The import statement "import sys" at the beginning of the script imports the sys module, which provides
# access to variables and functions related to the Python interpreter.

# The print() statement outputs a message using the provided command-line argument. The command-line arguments
# are stored in the sys.argv list. In this case, it prints a message that includes the second command-line
# argument, accessed using sys.argv[1].
