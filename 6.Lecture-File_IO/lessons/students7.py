# students7.py - Reads and sorts a CSV file containing student information into a list of dictionary objects using a lambda function

# Create an empty list to store student information as dictionary objects
students = []

# Open the "students0.csv" file in read mode using a context manager and loop through its lines
with open("students0.csv") as file:
    for line in file:
        # Unpack the line by splitting it into name and house using a comma as the delimiter
        name, house = line.rstrip().split(",")

        # Create a dictionary with student name and house information and directly append it to the "students" list
        students.append({"name": name, "house": house})

# Use a lambda function as the key argument to the sorted function
# The lambda function extracts the "name" value from each student dictionary for sorting
sorted_students = sorted(students, key=lambda student: student["name"])

# Iterate through the sorted list of dictionary objects and print each student's information
for student in sorted_students:
    print(f"{student['name']} is in {student['house']}")

# Explanation:
# This script is similar to the previous versions that read and process a CSV file named "students0.csv" containing student information.

# The script begins by creating an empty list named "students" to store student information as dictionary objects.

# Using a context manager, the script opens the "students0.csv" file in read mode. It then iterates through the lines of the file.

# For each line, the script unpacks the line into the "name" and "house" variables by splitting it using a comma as the delimiter.

# A dictionary object is created for each student using dictionary literal syntax, and the "name" and "house" keys are assigned
# the corresponding values obtained from the line.

# Each dictionary is directly appended to the "students" list within the same line of code.

# After processing all lines of the CSV file, the script uses the built-in "sorted" function to sort the list of dictionary objects.
# The "key" parameter is set to a lambda function that takes a student dictionary as an argument and returns the value associated with
# the "name" key.

# The sorted list of dictionary objects is stored in the variable "sorted_students".

# Finally, the script iterates through the sorted list of dictionary objects using a for loop. For each dictionary, the script uses f-strings
# to format and print the student's name and their house.

# The result is a series of formatted messages, each displaying a student's name and their house, as read from the "students0.csv" file,
# stored as dictionary objects in the "students" list, and sorted by the student's name using a lambda function.
