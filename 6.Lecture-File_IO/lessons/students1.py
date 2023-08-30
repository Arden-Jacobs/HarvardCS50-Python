# students1.py - Reads and processes a CSV file containing student information using unpacking

# Open the "students0.csv" file in read mode using a context manager and loop through its lines
with open("students0.csv") as file:
    for line in file:
        # Unpack the line by splitting it into name and house using a comma as the delimiter
        name, house = line.rstrip().split(",")

        # Print a formatted message with the student's name and their location
        print(f"{name} is in {house}")

# Explanation:
# This script reads and processes a CSV (Comma-Separated Values) file named "students0.csv" containing student information.

# The script uses a context manager to open the "students0.csv" file in read mode. The context manager automatically
# takes care of opening and closing the file.

# The for loop directly iterates over the lines of the file using the file object itself. For each line, the loop
# performs the following steps:
# 1. rstrip(): Remove any trailing whitespace (including newline characters) from the line.
# 2. split(","): Split the line into a list of values using a comma as the delimiter. This creates a list with two elements,
#    where the first element corresponds to the student's name and the second element corresponds to their house.

# The script then uses unpacking to assign the values from the list to the variables "name" and "house". This allows for a more
# readable and intuitive way to access the individual components of the CSV data.

# Finally, the script uses f-strings to format and print a message for each student. The student's name (stored in "name") and
# their house (stored in "house") are used to create the message.

# The result is a series of formatted messages, each displaying a student's name and their house as read from the "students0.csv" file.
