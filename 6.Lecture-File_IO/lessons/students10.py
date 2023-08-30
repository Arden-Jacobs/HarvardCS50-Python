# students10.py - Writes student information to a CSV file using csv.writer

# Import the "csv" module to work with CSV files
import csv

# Prompt the user for input: name and home
name = input("What's your name? ")
home = input("Where's your home? ")

# Open the "students2.csv" file in append mode using a context manager
with open("students2.csv", "a") as file:
    # Create a csv.writer object named "writer" using the open file
    writer = csv.writer(file)
    
    # Use the writerow method of the csv.writer object to write a row to the CSV file
    # The row is specified as a list of values [name, home]
    writer.writerow([name, home])

# Explanation:
# This script prompts the user for input to gather student information, specifically their name and home. The script then appends this information to a CSV file named "students2.csv" using the "csv.writer" object provided by the "csv" module.

# The script begins by importing the "csv" module.

# It uses the "input" function to prompt the user for their name and home and stores the entered values in the variables "name" and "home".

# Using a context manager, the script opens the "students2.csv" file in append mode. This allows the script to add new rows to the existing CSV file without overwriting its contents.

# Within the same context manager, the script creates a csv.writer object named "writer" using the open file. This object will be used to write rows to the CSV file.

# The script then uses the "writerow" method of the csv.writer object to write a row to the CSV file. The row is specified as a list containing the values [name, home]. The writerow method takes care of formatting the values and handling the writing process.

# After executing the script, the entered student information is added as a new row in the "students2.csv" file, following the existing rows.

# The result is an updated CSV file that contains the newly entered student information, stored as a row of values. The CSV file can be further processed or analyzed using other tools or scripts.
