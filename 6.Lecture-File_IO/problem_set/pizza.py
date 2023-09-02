# File Name: pizza.py
# Description: Read and display data from a CSV file using the 'tabulate' library

import sys
import csv
from tabulate import tabulate

# Check the number of command-line arguments
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

arg = sys.argv[1]

# Check if the argument is a CSV file
if ".csv" not in arg:
    sys.exit("Not a CSV file")

try:
    table = []

    with open(arg) as file:
        reader = csv.DictReader(file)
        for row in reader:
            table.append(row)

        # Use the 'tabulate' library to display the data in a grid format
        print(tabulate(table, headers="keys", tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File does not exist")

# Explanation:
# This script reads and displays data from a CSV file using the 'tabulate' library.
# It takes a CSV file as a command-line argument and checks if the argument is a valid CSV file.

# The script uses a try-except block to handle possible errors, such as a non-existing file.
# It reads the data from the CSV file using the 'csv.DictReader' class, which treats the first row as headers.

# The data is stored in a list of dictionaries ('table') where each dictionary represents a row of data.

# After reading the data, the script uses the 'tabulate' library to format and display the data in a grid format.
# The 'headers="keys"' argument specifies that the dictionary keys (column names) should be used as headers.

# Finally, the script prints the formatted table to the console.
