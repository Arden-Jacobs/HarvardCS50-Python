# File Name: student10.py

# Description: This script defines a class 'Student' with a constructor (__init__) to represent a student with 'name' and 'house' attributes.
# It demonstrates how to create an instance of the 'Student' class, initialize its attributes using the constructor, and access them in the 'main' function.

# Define the 'Student' class with a constructor (__init__) to represent a student.
class Student:
    def __init__(self, name, house):
        # The constructor initializes the 'name' and 'house' attributes of the 'Student' instance.
        self.name = name
        self.house = house

# Define the main function.
def main():
    # Call the 'get_student' function to collect the student's information and create an instance of the 'Student' class.
    student = get_student()
    
    # Access the 'name' and 'house' attributes of the 'student' instance and display them using a formatted string.
    print(f"{student.name} from {student.house}")

# Define the 'get_student' function to collect the student's information and create an instance of the 'Student' class.
def get_student():
    # Collect the student's name and house using the 'input' function.
    name = input("Name: ")
    house = input("House: ")
    
    # Create an instance of the 'Student' class by calling its constructor and passing the collected information as arguments.
    student = Student(name, house)
    
    # Return the 'student' instance.
    return student

# Check if the script is run as the main program.
if __name__ == "__main__":
    # If it is, call the 'main' function to create a student instance, collect input, and display the student's information.
    main()

# Explanation:

# Description: This script defines a class 'Student' with a constructor (__init__) to represent a student with 'name' and 'house' attributes.
# It demonstrates how to create an instance of the 'Student' class, initialize its attributes using the constructor, and access them in the 'main' function.

# The script consists of the following components:

# - 'Student' class: This class is defined with a constructor (__init__) that takes two parameters, 'name' and 'house'. Inside the constructor,
#   the 'name' and 'house' attributes of the 'Student' instance are initialized with the values passed as arguments.

# - 'main': This function is the entry point of the script. It calls the 'get_student' function to collect the student's information and create
#   an instance of the 'Student' class. It then accesses the 'name' and 'house' attributes of the 'student' instance and displays them using
#   a formatted string.

# - 'get_student': This function is responsible for collecting the student's name and house using the 'input' function. It then creates an instance
#   of the 'Student' class by calling its constructor and passing the collected information as arguments. The function returns the 'student' instance.

# The script also checks whether it is executed as the main program. If it is, it initiates the interactive process by calling the 'main' function,
# allowing the user to input the student's name and house and demonstrates how to create and use a class instance with a constructor.

# By adding a constructor to the 'Student' class, this script provides a cleaner and more organized way to initialize and manage the attributes of
# the class instances.
