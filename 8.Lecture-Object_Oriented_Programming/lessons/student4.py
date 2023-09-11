# File Name: student4.py

# Description: This script demonstrates the immutability of tuples by attempting to modify a tuple element.
# It defines a 'get_student' function to collect a student's name and house and returns them as an unpacked tuple.
# The 'main' function calls 'get_student' to collect the information and tries to modify the tuple element, which is not allowed.

# Define the main function.
def main():
    # Call the 'get_student' function to collect the student's name and house as an unpacked tuple.
    student = get_student()
    
    # Attempt to modify the tuple element, which will result in an error.
    if student[0] == "Padma":
        student[1] = "Ravenclaw"  # This line will raise an error
    
    # Display the student's name and house using indexed access to tuple elements and a formatted string.
    print(f"{student[0]} from {student[1]}")

# Define the 'get_student' function to collect the student's name and house and return them as an unpacked tuple.
def get_student():
    # Collect the student's name and house using the 'input' function.
    name = input("Name: ")
    house = input("House: ")
    
    # Return the name and house as an unpacked tuple.
    return name, house

# Check if the script is run as the main program.
if __name__ == "__main__":
    # If it is, call the 'main' function to collect input and display the student's information (with a potential error).
    main()

# Explanation:

# Description: This script demonstrates the immutability of tuples by attempting to modify a tuple element.
# It defines a 'get_student' function that collects a student's name and house, returning them as an unpacked tuple.
# The 'main' function calls 'get_student' to collect the information and tries to modify the tuple element, which is not allowed
# because tuples are immutable.

# The script consists of the following components:

# - 'main': This function is the entry point of the script. It calls 'get_student' to collect the student's name and house as an
#   unpacked tuple. It then attempts to modify the tuple element (student[1]), which will result in an error.

# - 'get_student': This function collects the student's name and house using the 'input' function, prompting the user for input.
#   It returns the name and house as an unpacked tuple.

# The script also checks whether it is executed as the main program. If it is, it initiates the interactive process by calling the 'main'
# function, allowing the user to input the student's name and house and potentially encountering an error when attempting to modify
# the tuple element.

# This script serves as an example of the immutability of tuples in Python.
