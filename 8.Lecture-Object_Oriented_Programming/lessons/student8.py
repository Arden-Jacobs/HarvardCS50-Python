# File Name: student8.py

# Description: This script demonstrates the mutability of dictionaries (dicts).
# It defines a 'get_student' function to collect a student's name and house as dictionary values and returns them as a dictionary.
# The 'main' function calls 'get_student' to collect the information, and it shows how the dictionary can be mutated (modified) in the 'main' function.

# Define the main function.
def main():
    # Call the 'get_student' function to collect the student's name and house as a dictionary.
    student = get_student()
    
    # Check if the student's name is "Padma." If it is, change the student's house to "Ravenclaw."
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    
    # Display the student's name and house using dictionary keys and a formatted string.
    print(f"{student['name']} from {student['house']}")

# Define the 'get_student' function to collect the student's name and house as dictionary values and return them as a dictionary.
def get_student():
    # Collect the student's name and house using the 'input' function and store them as dictionary values.
    name = input("Name: ")
    house = input("House: ")
    
    # Return the student's information as a dictionary.
    return {"name": name, "house": house}

# Check if the script is run as the main program.
if __name__ == "__main__":
    # If it is, call the 'main' function to collect input, possibly mutate the dictionary, and display the student's information.
    main()

# Explanation:

# Description: This script demonstrates the mutability of dictionaries (dicts).
# It defines a 'get_student' function that collects a student's name and house as dictionary values and returns them as a dictionary.
# The 'main' function calls 'get_student' to collect the information and shows how the dictionary can be mutated (modified) in the 'main' function.

# The script consists of the following components:

# - 'main': This function is the entry point of the script. It calls 'get_student' to collect the student's name and house as a dictionary.
#   It then checks if the student's name is "Padma." If it is, it changes the student's house to "Ravenclaw." Finally, it displays the student's
#   name and house using dictionary keys and a formatted string.

# - 'get_student': This function collects the student's name and house using the 'input' function and stores them as dictionary values.
#   It then returns the student's information as a dictionary.

# The script also checks whether it is executed as the main program. If it is, it initiates the interactive process by calling the 'main'
# function, allowing the user to input the student's name and house. If the student's name is "Padma," the script demonstrates that the
# dictionary can be mutated to change the student's house.

# This script serves as an example of working with dictionaries and how they can be modified during program execution.
