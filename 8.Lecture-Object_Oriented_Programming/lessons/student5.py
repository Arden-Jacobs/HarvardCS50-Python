# File Name: student5.py

# Description: This script stores a student as a mutable list instead of an immutable tuple.
# It defines a 'get_student' function to collect a student's name and house and returns them as a list.
# The 'main' function calls 'get_student' to collect the information and modifies the list element to update the house.

# Define the main function.
def main():
    # Call the 'get_student' function to collect the student's name and house as a list.
    student = get_student()
    
    # Modify the list element to update the house if the student's name is "Padma."
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    
    # Display the student's name and house using indexed access to list elements and a formatted string.
    print(f"{student[0]} from {student[1]}")

# Define the 'get_student' function to collect the student's name and house and return them as a list.
def get_student():
    # Collect the student's name and house using the 'input' function.
    name = input("Name: ")
    house = input("House: ")
    
    # Return the name and house as a list.
    return [name, house]

# Check if the script is run as the main program.
if __name__ == "__main__":
    # If it is, call the 'main' function to collect input, potentially modify the list, and display the student's information.
    main()

# Explanation:

# Description: This script stores a student as a mutable list instead of an immutable tuple.
# It defines a 'get_student' function that collects a student's name and house, returning them as a list.
# The 'main' function calls 'get_student' to collect the information and modifies the list element to update the house if the
# student's name is "Padma."

# The script consists of the following components:

# - 'main': This function is the entry point of the script. It calls 'get_student' to collect the student's name and house as a list.
#   It then checks if the student's name is "Padma" and, if so, updates the list element (student[1]) to set the house to "Ravenclaw."
#   It then displays the student's name and house using indexed access to list elements and a formatted string.

# - 'get_student': This function collects the student's name and house using the 'input' function, prompting the user for input.
#   It returns the name and house as a list.

# The script also checks whether it is executed as the main program. If it is, it initiates the interactive process by calling the 'main'
# function, allowing the user to input the student's name and house and potentially updating the house if the student's name is "Padma."

# This script demonstrates the use of a mutable list to represent a student and how elements of a list can be modified.
