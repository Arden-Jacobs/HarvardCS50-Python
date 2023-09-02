# File: pizza.py
# Description: Reads a CSV file, converts it to a table, and prints it using the tabulate library.

# Import necessary modules: sys for command-line arguments, csv for handling CSV files, and tabulate for tabular formatting.
import sys
import csv
from tabulate import tabulate

# Check the number of command-line arguments.
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

# Get the first command-line argument (the filename).
arg = sys.argv[1]

# Check if the argument is a CSV file (contains ".csv" in the filename).
if ".csv" not in arg:
    sys.exit("Not a CSV file")

# Initialize an empty list to store table data.
table = []

try:
    # Open the specified CSV file.
    with open(arg) as file:
        # Create a CSV reader that interprets the first row as column headers.
        reader = csv.DictReader(file)
        # Iterate through each row in the CSV file.
        for row in reader:
            # Append each row (represented as a dictionary) to the table list.
            table.append(row)
        # Use the tabulate library to print the table in a grid format with headers.
        print(tabulate(table, headers="keys", tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File does not exist")

# Explanation:

# This script reads a CSV file, converts its content into a table, and then prints the table in a grid format. 
# It uses the `sys` module to access command-line arguments, the `csv` module to handle CSV files, and the `tabulate` library for formatting the table.

# It begins by checking the number of command-line arguments provided when running the script. 
# If there are too few or too many arguments, it displays an error message and exits.

# Next, it extracts the first command-line argument, which should be the filename of a CSV file. 
# It checks if the argument contains ".csv" to ensure that it is indeed a CSV file. If not, it displays an error and exits.

# Then, the script initializes an empty list named `table` to store the data from the CSV file.

# It opens the specified CSV file and creates a CSV reader using `csv.DictReader`. 
# This reader interprets the first row of the CSV file as column headers and treats each subsequent row as a dictionary.

# The script then iterates through each row in the CSV file using a for loop. 
# For each row, it appends the row (represented as a dictionary) to the `table` list.

# Finally, it uses the `tabulate` library to print the table. 
# It specifies "keys" for the headers parameter to use the dictionary keys (column names) as table headers. 
# The `tablefmt` parameter is set to "grid" to format the table in a grid format.

# If the specified file does not exist, the script displays an error message and exits.

# In summary, this script provides an easy way to read and display the contents of a CSV file as a well-formatted table.
