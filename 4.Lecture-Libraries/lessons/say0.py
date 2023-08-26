# say0.py - Demonstrates using a pip-installed package

# Import the cowsay module and the sys module for command-line arguments
import sys
import cowsay

# Check if exactly one command-line argument is provided
if len(sys.argv) == 2:
    # Use the cowsay.cow() function to generate a message with a cow
    cowsay.cow("hello, " + sys.argv[1])

# Explanation:
# This code demonstrates how to use a pip-installed package (cowsay) to generate a fun message.

# The import statements "import cowsay" and "import sys" at the beginning of the script import the
# necessary modules. cowsay is a package that provides various ASCII art characters that say messages,
# and sys is used for handling command-line arguments.

# The if statement checks if exactly one command-line argument is provided. If there is exactly one
# argument, the cowsay.cow() function is used to generate a message with a cow saying "hello," followed
# by the provided command-line argument.
