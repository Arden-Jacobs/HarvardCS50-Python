# hogwarts5.py - Demonstrating Iterating Over a List of Dictionary Objects

# List of student dictionary objects
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

# Iterating over the list of dictionaries and printing student information
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")



# Explanation:
# This code demonstrates how to iterate over a list of dictionary objects and access the values of specific keys
# within each dictionary.

# List of Dictionaries:
# The students list contains multiple dictionary objects.
# Each dictionary object represents a student with information about their name, house, and patronus.

# Iterating Over the List:
# The for loop iterates over the students list.
# In each iteration, the variable student holds a dictionary object representing a student's information.

# Accessing Dictionary Values:
# Inside the loop, the code uses the student variable to access specific keys within the current dictionary.
# For example, student["name"] accesses the value associated with the "name" key in the dictionary.
# By iterating over the list of dictionary objects and accessing specific keys, the code prints each student's name, house, and patronus information.
