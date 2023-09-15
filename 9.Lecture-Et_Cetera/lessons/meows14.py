# File Name: meows14.py
# Description: This script uses the argparse module to handle command-line arguments, providing a description, default value, and specifying the argument type, while controlling the number of times "meow" is printed.

import argparse

# Create an ArgumentParser object to handle command-line arguments, providing a description.
parser = argparse.ArgumentParser(description="Meow like a cat")
# Add an argument '-n' to the parser, indicating the number of times to print "meow," provide a help message, set a default value of 1, and specify the argument type as 'int'.
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
# Parse the command-line arguments.
args = parser.parse_args()

# Use a 'for' loop to iterate 'n' times (parsed from args.n) and print "meow" during each iteration.
for _ in range(args.n):
    print("meow")
    
# Explanation:
# Description: This script uses the argparse module to handle command-line arguments, providing a description, default value, and specifying the argument type, while controlling the number of times "meow" is printed.
# The script contains the following components:
# - 'argparse.ArgumentParser(description="Meow like a cat")': It creates an ArgumentParser object to handle command-line arguments, providing a description.
# - 'parser.add_argument("-n", default=1, help="number of times to meow", type=int)': It adds an argument '-n' to the parser, indicating the number of times to print "meow," provides a help message, sets a default value of 1, and specifies the argument type as 'int'.
# - 'parser.parse_args()': It parses the command-line arguments.
# - 'for' loop: It uses a 'for' loop to iterate 'n' times (parsed from args.n) and prints "meow" during each iteration.
# The script demonstrates how to use the argparse module to specify default values and argument types for command-line arguments in Python.
