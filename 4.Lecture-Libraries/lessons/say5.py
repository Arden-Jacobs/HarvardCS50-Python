# say5.py - Demonstrates using a custom module for generating a message

# Import the sys module for command-line arguments
import sys

# Import the "goodbye" function from the custom module "sayings2"
from sayings2 import goodbye

# Check if exactly one command-line argument is provided
if len(sys.argv) == 2:
    # Call the "goodbye" function from the custom module to generate a message
    goodbye(sys.argv[1])

# Explanation:
# This code demonstrates how to use a custom module "sayings2" to generate a message.

# The import statement "import sys" at the beginning of the script imports the sys module, which provides
# access to variables and functions related to the Python interpreter.

# The import statement "from sayings2 import goodbye" imports the "goodbye" function from the custom module "sayings2".
# This module likely contains functions to generate specific messages.

# The if statement checks if exactly one command-line argument is provided. If there is exactly one argument,
# the "goodbye" function from the "sayings2" module is called to generate a message using the provided argument.
