# students3.py - Reads and processes a CSV file containing student information into a list of dictionary objects

# Create an empty list to store student information as dictionary objects
students = []

# Open the "students0.csv" file in read mode using a context manager and loop through its lines
with open("students0.csv") as file:
    for line in file:
        # Unpack the line by splitting it into name and house using a comma as the delimiter
        name, house = line.rstrip().split(",")

        # Create an empty dictionary to store student data
        student = {}

        # Populate the dictionary with student name and house information
        student["name"] = name
        student["house"] = house

        # Append the dictionary to the "students" list
        students.append(student)

# Iterate through the list of dictionary objects and print each student's information
for student in students:
    print(f"{student['name']} is in {student['house']}")

# Explanation:
# This script reads and processes a CSV (Comma-Separated Values) file named "students0.csv" containing student information.

# The script starts by creating an empty list named "students" which will be used to store student information as dictionary objects.

# The script then uses a context manager to open the "students0.csv" file in read mode. The context manager automatically
# takes care of opening and closing the file.

# Inside the loop that iterates over the lines of the file, the line is unpacked using the split(",") operation. The student's
# name is assigned to the variable "name" and their house is assigned to the variable "house".

# A new empty dictionary named "student" is created to store the current student's information.

# The dictionary is populated with two key-value pairs using dictionary assignment:
# - The "name" key is assigned the value of the student's name.
# - The "house" key is assigned the value of the student's house.

# The populated dictionary is then appended to the "students" list.

# After processing all lines of the CSV file, the script iterates through the list of dictionary objects using a for loop.
# For each dictionary, the script uses f-strings to format and print the student's name and their house.

# The result is a series of formatted messages, each displaying a student's name and their house, as read from the "students0.csv" file,
# and stored as dictionary objects in the "students" list.
