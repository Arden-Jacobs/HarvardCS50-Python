# File Name: student2.py

# Description: This script defines a 'get_student' function to collect a student's name and house and return them as a tuple.
# It then unpacks the tuple in the 'main' function to display the student's information.

# Define the main function.
def main():
    # Call the 'get_student' function to collect the student's name and house as a tuple, and unpack it.
    name, house = get_student()
    
    # Display the student's name and house using a formatted string.
    print(f"{name} from {house}")

# Define the 'get_student' function to collect the student's name and house and return them as a tuple.
def get_student():
    # Collect the student's name and house using the 'input' function.
    name = input("Name: ")
    house = input("House: ")
    
    # Return the name and house as a tuple.
    return name, house

# Check if the script is run as the main program.
if __name__ == "__main__":
    # If it is, call the 'main' function to collect input and display the student's information.
    main()

# Explanation:

# Description: This script defines a 'get_student' function that collects a student's name and house, returning them as a tuple.
# The 'main' function calls 'get_student' to collect the information and unpacks the tuple to display the student's details.

# The script consists of the following components:

# - 'main': This function is the entry point of the script. It calls 'get_student' to collect the student's name and house as a tuple.
#   Then, it unpacks the tuple into 'name' and 'house' variables and displays the student's information using a formatted string.

# - 'get_student': This function collects the student's name and house using the 'input' function, prompting the user for input.
#   It then returns the name and house as a tuple.

# The script also checks whether it is executed as the main program. If it is, it initiates the interactive process by calling the 'main'
# function, allowing the user to input the student's name and house and displaying the information.

# This script offers a streamlined way to capture and display information about a student, utilizing tuples for efficient data management.
