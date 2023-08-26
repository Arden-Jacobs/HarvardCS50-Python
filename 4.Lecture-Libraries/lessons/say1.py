# say1.py - Demonstrates using a pip-installed package for a t-rex message

# Import the sys module for command-line arguments and the cowsay module
import sys
import cowsay

# Check if exactly one command-line argument is provided
if len(sys.argv) == 2:
    # Use the cowsay.trex() function to generate a message with a t-rex
    cowsay.trex("hello, " + sys.argv[1])

# Explanation:
# This code demonstrates how to use a pip-installed package (cowsay) to generate a message with a t-rex.

# The import statements "import sys" and "import cowsay" at the beginning of the script import the necessary
# modules. cowsay is a package that provides various ASCII art characters that say messages, and sys is
# used for handling command-line arguments.

# The if statement checks if exactly one command-line argument is provided. If there is exactly one argument,
# the cowsay.trex() function is used to generate a message with a t-rex saying "hello," followed by the provided
# command-line argument.
