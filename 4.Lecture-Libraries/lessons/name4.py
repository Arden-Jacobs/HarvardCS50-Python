# name4.py - Demonstrates list slicing with sys.argv

# Import the sys module to access command-line arguments
import sys

# Check if at least one command-line argument is provided
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

# Iterate over command-line arguments starting from the second one and print a message for each
for arg in sys.argv[1:]:
    print("hello, my name is", arg)

# Explanation:
# This code demonstrates how to use list slicing with sys.argv to iterate over and process multiple command-line arguments.

# The import statement "import sys" at the beginning of the script imports the sys module, which provides
# access to variables and functions related to the Python interpreter.

# The if statement checks if there is at least one command-line argument (excluding the script name itself).
# If there aren't enough arguments, the sys.exit() function is used to exit the script with an error message.

# The for loop iterates over the command-line arguments starting from the second one (sys.argv[1:]).
# Inside the loop, the script prints a message for each argument using the value of "arg".
