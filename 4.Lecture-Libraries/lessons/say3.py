# say3.py - Demonstrates using a custom module for generating a message

# Import the sys module for command-line arguments
import sys

# Import the "hello" function from the custom module "sayings1"
from sayings1 import hello

# Check if exactly one command-line argument is provided
if len(sys.argv) == 2:
    # Call the "hello" function from the custom module to generate a message
    hello(sys.argv[1])

# Explanation:
# This code demonstrates how to use a custom module "sayings1" to generate a message.

# The import statement "import sys" at the beginning of the script imports the sys module, which provides
# access to variables and functions related to the Python interpreter.

# The import statement "from sayings1 import hello" imports the "hello" function from the custom module "sayings1".
# This module likely contains functions to generate specific messages.

# The if statement checks if exactly one command-line argument is provided. If there is exactly one argument,
# the "hello" function from the "sayings1" module is called to generate a message using the provided argument.
