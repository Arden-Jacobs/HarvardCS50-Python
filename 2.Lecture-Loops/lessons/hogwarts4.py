# hogwarts4.py - Demonstrating Iterating Over and Indexing into a Dictionary

# Dictionary of students' houses
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

# Iterating over the dictionary and printing student names and their houses
for student in students:
    print(student, students[student], sep=", ")



# Explanation:
# This code demonstrates how to iterate over a dictionary, accessing both keys and their corresponding values.

# Dictionary Definition:
# The students dictionary is defined with student names as keys and their corresponding houses as values.
# Each key-value pair represents a student's name and their assigned house in Hogwarts.

# Iterating Over the Dictionary:
# The for loop iterates over the students dictionary.
# In each iteration, the variable student takes the value of a key (student's name) from the dictionary.

# Indexing into the Dictionary:
# Inside the loop, the code uses the student variable as a key to access the corresponding house from the dictionary.
# The students[student] expression retrieves the value associated with the current key (student's name).
# By iterating over the dictionary and indexing into it, the code prints the names of students along with their assigned houses.
