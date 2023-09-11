# File Name: student6.py

# Description: This script stores a student as a dictionary (dict) instead of a list or tuple.
# It defines a 'get_student' function to collect a student's name and house and returns them as a dictionary.
# The 'main' function calls 'get_student' to collect the information and displays the student's name and house using dictionary keys.

# Define the main function.
def main():
    # Call the 'get_student' function to collect the student's name and house as a dictionary.
    student = get_student()
    
    # Display the student's name and house using dictionary keys and a formatted string.
    print(f"{student['name']} from {student['house']}")

# Define the 'get_student' function to collect the student's name and house and return them as a dictionary.
def get_student():
    # Create an empty dictionary to store the student's information.
    student = {}
    
    # Collect the student's name and house using the 'input' function and store them as dictionary keys.
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    
    # Return the student's information as a dictionary.
    return student

# Check if the script is run as the main program.
if __name__ == "__main__":
    # If it is, call the 'main' function to collect input and display the student's information.
    main()

# Explanation:

# Description: This script stores a student as a dictionary (dict) instead of a list or tuple.
# It defines a 'get_student' function that collects a student's name and house, returning them as a dictionary.
# The 'main' function calls 'get_student' to collect the information and displays the student's name and house using dictionary keys.

# The script consists of the following components:

# - 'main': This function is the entry point of the script. It calls 'get_student' to collect the student's name and house as a dictionary.
#   It then displays the student's name and house using dictionary keys and a formatted string.

# - 'get_student': This function creates an empty dictionary to store the student's information. It collects the student's name and house
#   using the 'input' function and stores them as dictionary keys. It then returns the student's information as a dictionary.

# The script also checks whether it is executed as the main program. If it is, it initiates the interactive process by calling the 'main'
# function, allowing the user to input the student's name and house and displaying the collected information.

# This script demonstrates the use of a dictionary to represent a student and how dictionary keys can be used to access and display information.
