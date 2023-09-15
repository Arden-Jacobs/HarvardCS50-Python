# File Name: meows11.py
# Description: This script uses command-line arguments to control the number of times "meow" is printed.

import sys

# Check the number of command-line arguments.
if len(sys.argv) == 1:
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    # Extract the value of 'n' from the command-line arguments.
    n = int(sys.argv[2])
    # Use a 'for' loop to iterate 'n' times and print "meow" during each iteration.
    for _ in range(n):
        print("meow")
else:
    print("usage: meows11.py [-n NUMBER]")

# Explanation:
# Description: This script uses command-line arguments to control the number of times "meow" is printed.
# The script contains the following components:
# - 'sys.argv': It is used to access the command-line arguments provided when running the script.
# - Command-line argument handling: The script checks the number of arguments and their values to determine the behavior:
#   - If no arguments are provided, it prints "meow" once.
#   - If two arguments are provided, where the first argument is "-n" and the second argument is an integer 'n', it prints "meow" 'n' times.
#   - Otherwise, it prints a usage message.
# The script demonstrates how to use command-line arguments for controlling program behavior in Python.
