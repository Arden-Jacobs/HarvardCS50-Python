# File Name: student14.py

# Description: This script defines a class 'Student' with a constructor (__init__) to represent a student with 'name' and 'house' attributes.
# It adds validation checks within the constructor to ensure that the 'name' is not empty and the 'house' is one of the valid options.
# The script then implements a custom '__str__' method to provide a string representation of the 'Student' instance.

# Define the 'Student' class with a constructor (__init__) to represent a student.
class Student:
    def __init__(self, name, house):
        # Validate the 'name' to ensure it's not empty.
        if not name:
            raise ValueError("Missing name")
        
        # Validate the 'house' to ensure it's one of the valid options.
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        
        # If both 'name' and 'house' pass validation, initialize the 'name' and 'house' attributes of the 'Student' instance.
        self.name = name
        self.house = house

    # Implement a custom '__str__' method to provide a string representation of the 'Student' instance.
    def __str__(self):
        return f"{self.name} from {self.house}"

# Define the main function.
def main():
    # Call the 'get_student' function to collect the student's information and create an instance of the 'Student' class directly.
    student = get_student()
    
    # Print the 'student' instance, which now provides a custom string representation.
    print(student)

# Define the 'get_student' function to collect the student's information and create an instance of the 'Student' class directly.
def get_student():
    # Collect the student's name and house using the 'input' function.
    name = input("Name: ")
    house = input("House: ")
    
    # Create an instance of the 'Student' class directly and pass the collected information as arguments to its constructor.
    return Student(name, house)

# Check if the script is run as the main program.
if __name__ == "__main__":
    # If it is, call the 'main' function to create a student instance, collect input, and print the student instance with the custom string representation.
    main()

# Explanation:

# Description: This script defines a class 'Student' with a constructor (__init__) to represent a student with 'name' and 'house' attributes.
# It adds validation checks within the constructor to ensure that the 'name' is not empty and the 'house' is one of the valid options.
# The script then implements a custom '__str__' method to provide a string representation of the 'Student' instance.

# The script consists of the following components:

# - 'Student' class: This class is defined with a constructor (__init__) that takes two parameters, 'name' and 'house'. Inside the constructor,
#   there are two validation checks:
#   - The 'name' is validated to ensure it's not empty. If it is, a 'ValueError' is raised with the message "Missing name."
#   - The 'house' is validated to ensure it's one of the valid options: Gryffindor, Hufflepuff, Ravenclaw, or Slytherin. If it's not one of
#     these options, a 'ValueError' is raised with the message "Invalid house." If both 'name' and 'house' pass validation, the 'name' and 'house'
#     attributes of the 'Student' instance are initialized with the provided values.

# - '__str__' method: This method is implemented within the 'Student' class to provide a custom string representation of the 'Student' instance.
#   It returns a string containing the student's name and house.

# - 'main': This function is the entry point of the script. It calls the 'get_student' function to collect the student's information and create
#   an instance of the 'Student' class directly. It then prints the 'student' instance, which now provides a custom string representation.

# - 'get_student': This function is responsible for collecting the student's name and house using the 'input' function. It then creates an instance
#   of the 'Student' class directly by calling its constructor and passing the collected information as arguments. The function returns the 'Student'
#   instance directly, eliminating the need for an intermediate variable.

# The script also checks whether it is executed as the main program. If it is, it initiates the interactive process by calling the 'main' function,
# allowing the user to input the student's name and house and demonstrating how to create and print a student instance with the custom string
# representation provided by the '__str__' method.
