# File Name: wizard.py

# Description: This script demonstrates inheritance in Python by defining three classes: 'Wizard', 'Student', and 'Professor'.
# Each class inherits from the 'Wizard' class, and they represent different types of characters in a magical world.
# The script creates instances of these classes and initializes their attributes.

# Define the base class 'Wizard'.
class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

# Define the 'Student' class, inheriting from 'Wizard'.
class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)  # Call the constructor of the base class 'Wizard'.
        self.house = house

# Define the 'Professor' class, inheriting from 'Wizard'.
class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)  # Call the constructor of the base class 'Wizard'.
        self.subject = subject

# Create instances of the 'Wizard', 'Student', and 'Professor' classes.
wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")

# The instances of these classes can be further customized and used in various ways, such as defining additional methods and properties.

# Explanation:

# Description: This script demonstrates inheritance in Python by defining three classes: 'Wizard', 'Student', and 'Professor'.
# Each class inherits from the 'Wizard' class, and they represent different types of characters in a magical world.
# The script creates instances of these classes and initializes their attributes.

# The script consists of the following components:

# - 'Wizard' class: This is the base class defined with a constructor (__init__) that takes a 'name' parameter. It performs validation to ensure that
#   the 'name' is not empty and then initializes the 'name' attribute.

# - 'Student' class: This class represents a student character and inherits from the 'Wizard' class. It defines its own constructor (__init__) that takes
#   'name' and 'house' parameters. It calls the constructor of the base class using 'super().__init__(name)' to initialize the 'name' attribute.
#   It also initializes the 'house' attribute to represent the student's house.

# - 'Professor' class: This class represents a professor character and also inherits from the 'Wizard' class. It defines its own constructor (__init__)
#   that takes 'name' and 'subject' parameters. Similar to the 'Student' class, it calls the constructor of the base class to initialize the 'name' attribute.
#   It also initializes the 'subject' attribute to represent the professor's subject of expertise.

# - Creating instances: The script creates instances of the 'Wizard', 'Student', and 'Professor' classes, initializing their attributes accordingly.
#   For example, 'wizard' is an instance of the 'Wizard' class, 'student' is an instance of the 'Student' class, and 'professor' is an instance of the 'Professor' class.

# - Further customization: The instances of these classes can be further customized by defining additional methods and properties specific to each character type.
