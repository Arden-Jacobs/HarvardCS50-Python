# File Name: student1.py

# Description: This script modularizes the process of getting a student's name and house.
# It defines functions 'get_name' and 'get_house' to collect input and a 'main' function to call these functions and display the information.

# Define the main function.
def main():
    # Call the 'get_name' and 'get_house' functions to collect the student's name and house.
    name = get_name()
    house = get_house()
    
    # Display the student's name and house using a formatted string.
    print(f"{name} from {house}")

# Define the 'get_name' function to collect the student's name and return it.
def get_name():
    return input("Name: ")

# Define the 'get_house' function to collect the student's house and return it.
def get_house():
    return input("House: ")

# Check if the script is run as the main program.
if __name__ == "__main__":
    # If it is, call the 'main' function to collect input and display the student's information.
    main()

# Explanation:

# Description: This script modularizes the process of getting a student's name and house by defining functions for these tasks.
# It defines three functions: 'main', 'get_name', and 'get_house.'

# - 'main': This function is the entry point of the script. It calls 'get_name' and 'get_house' to collect the student's name and house.
#   Then, it displays the student's information using a formatted string.

# - 'get_name': This function collects the student's name by using the 'input' function to prompt the user for input. It returns the input as
#   the student's name.

# - 'get_house': This function collects the student's house by using the 'input' function to prompt the user for input. It returns the input
#   as the student's house.

# The script also checks whether it is executed as the main program. If it is, it initiates the interactive process by calling the 'main'
# function, allowing the user to input the student's name and house and displaying the information.

# This modularized script provides a cleaner and more organized way to capture and display information about a student, improving code
# readability and maintainability.
