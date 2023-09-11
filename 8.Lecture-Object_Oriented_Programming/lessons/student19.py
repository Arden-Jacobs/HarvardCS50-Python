# File Name: student19.py

# Description: This script defines a class 'Student' with a constructor (__init__) to represent a student with 'name' and 'house' attributes.
# It adds validation checks within the constructor to ensure that the 'name' is not empty and the 'house' is one of the valid options.
# The script enhances both 'name' and 'house' attributes by using the @property decorator to provide controlled access and validation.

# Define the 'Student' class with a constructor (__init__) to represent a student with 'name' and 'house' attributes.
class Student:
    def __init__(self, name, house):
        # Initialize the 'name' and 'house' attributes with the provided values.
        self.name = name
        self.house = house

    # Define the '__str__' method to provide a string representation of the 'Student' instance.
    def __str__(self):
        return f"{self.name} from {self.house}"

    # Define the 'name' property to get the 'name' attribute value.
    @property
    def name(self):
        return self._name

    # Define the 'name' property setter method to set the 'name' attribute with validation.
    @name.setter
    def name(self, name):
        # Validate the 'name' to ensure it's not empty.
        if not name:
            raise ValueError("Invalid name")
        self._name = name

    # Define the 'house' property to get the 'house' attribute value.
    @property
    def house(self):
        return self._house

    # Define the 'house' property setter method to set the 'house' attribute with validation.
    @house.setter
    def house(self, house):
        # Validate the 'house' to ensure it's one of the valid options.
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

# Define the main function.
def main():
    # Call the 'get_student' function to collect the student's information and create an instance of the 'Student' class directly.
    student = get_student()
    
    # Print the 'student' instance directly.
    print(student)

# Define the 'get_student' function to collect the student's name and house using the 'input' function.
def get_student():
    name = input("Name: ")
    house = input("House: ")
    
    # Create an instance of the 'Student' class directly and pass the collected information as arguments to its constructor.
    return Student(name, house)

# Check if the script is run as the main program.
if __name__ == "__main__":
    # If it is, it initiates the interactive process by calling the 'main' function,
    # allowing the user to input the student's name and house, demonstrating how to create a student instance with controlled access to both 'name' and 'house' attributes
    # using the property decorator.
    main()

# Explanation:

# Description: This script defines a class 'Student' with a constructor (__init__) to represent a student with 'name' and 'house' attributes.
# It adds validation checks within the constructor to ensure that the 'name' is not empty and the 'house' is one of the valid options.
# The script enhances both 'name' and 'house' attributes by using the @property decorator to provide controlled access and validation.

# The script consists of the following components:

# - 'Student' class: This class is defined with a constructor (__init__) that takes two parameters, 'name' and 'house'. Inside the constructor,
#   there are two validation checks:
#   - The 'name' is validated to ensure it's not empty. If it is empty, a 'ValueError' is raised with the message "Invalid name."
#   - The 'house' is validated to ensure it's one of the valid options: Gryffindor, Hufflepuff, Ravenclaw, or Slytherin. If it's not one of
#     these options, a 'ValueError' is raised with the message "Invalid house." Both 'name' and 'house' attributes are initialized with the provided values.

# - '__str__' method: This method is defined within the 'Student' class to provide a string representation of the 'Student' instance. It returns a string
#   containing the student's name and house.

# - 'name' and 'house' properties: These properties are defined using the @property decorator to get the 'name' and 'house' attribute values.
#   They provide controlled access to the 'name' and 'house' attributes.

# - 'name' and 'house' property setter methods: These setter methods are defined using the @name.setter and @house.setter decorators to set the 'name' and 'house' attributes
#   with validation. They check whether the provided 'name' and 'house' values meet the validation criteria before setting the corresponding attributes.

# - 'main': This function is the entry point of the script. It calls the 'get_student' function to collect the student's information and create
#   an instance of the 'Student' class directly. It then prints the 'student' instance directly.

# - 'get_student': This function is responsible for collecting the student's name and house using the 'input' function. It then creates an instance
#   of the 'Student' class directly by calling its constructor and passing the collected information as arguments. The function returns the 'Student'
#   instance directly, eliminating the need for an intermediate variable.

# The script also checks whether it is executed as the main program. If it is, it initiates the interactive process by calling the 'main' function,
# allowing the user to input the student's name and house, demonstrating how to create a student instance with controlled access to both 'name' and 'house' attributes
# using the property decorator.
