# File Name: meows12.py
# Description: This script uses the argparse module to handle command-line arguments and control the number of times "meow" is printed.

import argparse

# Create an ArgumentParser object to handle command-line arguments.
parser = argparse.ArgumentParser()
# Add an argument '-n' to the parser, indicating the number of times to print "meow."
parser.add_argument("-n")
# Parse the command-line arguments.
args = parser.parse_args()

# Use a 'for' loop to iterate 'n' times (parsed from args.n) and print "meow" during each iteration.
for _ in range(int(args.n)):
    print("meow")
    
# Explanation:
# Description: This script uses the argparse module to handle command-line arguments and control the number of times "meow" is printed.
# The script contains the following components:
# - 'argparse.ArgumentParser()': It creates an ArgumentParser object to handle command-line arguments.
# - 'parser.add_argument("-n")': It adds an argument '-n' to the parser, indicating the number of times to print "meow."
# - 'parser.parse_args()': It parses the command-line arguments.
# - 'for' loop: It uses a 'for' loop to iterate 'n' times (parsed from args.n) and prints "meow" during each iteration.
# The script demonstrates how to use the argparse module for command-line argument parsing in Python.
