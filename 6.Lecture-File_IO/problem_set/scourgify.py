# File: scourgify.py
# Description: Reads a CSV file, rearranges and writes it to another CSV file with specified columns.

# Import necessary modules: sys for command-line arguments, csv for handling CSV files, and tabulate for tabular formatting.
import sys
import csv
from tabulate import tabulate

# Check the number of command-line arguments.
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

# Get the first command-line argument (the input CSV filename).
arg = sys.argv[1]

# Check if the argument is a CSV file (contains ".csv" in the filename).
if ".csv" not in arg:
    sys.exit("Not a CSV file")

try:
    # Open the specified input CSV file.
    with open(arg) as main:
        # Create a CSV reader that interprets the first row as column headers.
        reader = csv.DictReader(main)
        # Open the specified output CSV file for writing.
        with open(sys.argv[2], 'w') as file:
            # Create a CSV writer with specified column names and write the header row.
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            # Iterate through each row in the input CSV file.
            for row in reader:
                # Split the 'name' field into first and last names.
                lname, f_name = row['name'].split(", ")
                house = row['house']
                # Write the rearranged data to the output CSV file.
                writer.writerow({"first": f_name, "last": lname, "house": house})

except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

# Explanation:

# This script reads a CSV file, rearranges its data, and writes it to another CSV file with specified columns.
# It uses the `sys` module to access command-line arguments, the `csv` module to handle CSV files,
# and the `tabulate` library for tabular formatting.

# It begins by checking the number of command-line arguments provided when running the script.
# If there are too few or too many arguments, it displays an error message and exits.

# Next, it extracts the first command-line argument, which should be the filename of the input CSV file.
# It checks if the argument contains ".csv" to ensure that it is indeed a CSV file. If not, it displays an error and exits.

# Then, the script opens the specified input CSV file and creates a CSV reader using `csv.DictReader`.
# This reader interprets the first row of the CSV file as column headers and treats each subsequent row as a dictionary.

# The script also opens the specified output CSV file for writing.

# It creates a CSV writer using `csv.DictWriter` and specifies the column names for the output CSV.
# It writes the header row to the output CSV file.

# The script then iterates through each row in the input CSV file using a for loop.
# For each row, it splits the 'name' field into first and last names and extracts the 'house' field.

# Finally, it writes the rearranged data to the output CSV file.

# If the specified input file does not exist, the script displays an error message and exits.

# In summary, this script provides a way to transform CSV data by rearranging and writing it to a new CSV file with specified columns.
