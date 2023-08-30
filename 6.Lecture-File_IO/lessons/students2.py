# students2.py - Reads and processes a CSV file containing student information, then sorts and prints the data

# Create an empty list to store formatted student information
students = []

# Open the "students0.csv" file in read mode using a context manager and loop through its lines
with open("students0.csv") as file:
    for line in file:
        # Unpack the line by splitting it into name and house using a comma as the delimiter
        name, house = line.rstrip().split(",")

        # Append a formatted string to the "students" list, combining the student's name and house
        students.append(f"{name} is in {house}")

# Sort the "students" list alphabetically
sorted_students = sorted(students)

# Iterate through the sorted list of students and print each student's information
for student in sorted_students:
    print(student)

# Explanation:
# This script reads and processes a CSV (Comma-Separated Values) file named "students0.csv" containing student information.

# The script starts by creating an empty list named "students" which will be used to store formatted student information.

# The script then uses a context manager to open the "students0.csv" file in read mode. The context manager automatically
# takes care of opening and closing the file.

# Inside the loop that iterates over the lines of the file, the line is unpacked using the split(",") operation. The student's
# name is assigned to the variable "name" and their house is assigned to the variable "house". A formatted string is then created
# using f-strings, combining the student's name and house information, and this formatted string is appended to the "students" list.

# After processing all lines of the CSV file, the script sorts the "students" list alphabetically using the sorted() function
# and assigns the result to the "sorted_students" variable.

# The script then iterates through the sorted list of students using a for loop and prints each student's information.

# The result is a series of formatted messages, each displaying a student's name and their house, sorted in alphabetical order,
# as read from the "students0.csv" file.
