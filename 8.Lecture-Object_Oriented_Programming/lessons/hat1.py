# File Name: hat1.py

# Description: This script defines a class 'Hat' that represents a magical hat used to sort individuals into Hogwarts houses.
# It implements a 'sort' method as a class method to randomly sort a person into one of the Hogwarts houses.
# The script directly calls the 'sort' method of the 'Hat' class to sort a person's name into a house.

# Import the 'random' module to generate random choices.

import random

# Define the 'Hat' class to represent a magical hat.
class Hat:
    # Define a class-level variable 'houses' containing a list of Hogwarts houses.
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    # Define the 'sort' method as a class method, which takes a 'name' as input and randomly assigns it to one of the Hogwarts houses.
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

# Call the 'sort' method of the 'Hat' class to sort a person's name into one of the Hogwarts houses.
Hat.sort("Harry")

# Explanation:

# Description: This script defines a class 'Hat' that represents a magical hat used to sort individuals into Hogwarts houses.
# It implements a 'sort' method as a class method to randomly sort a person into one of the Hogwarts houses.
# The script directly calls the 'sort' method of the 'Hat' class to sort a person's name into a house.

# The script consists of the following components:

# - 'Hat' class: This class is defined to represent a magical hat. It defines a class-level variable 'houses' containing a list of Hogwarts houses.

# - 'sort' method: This method is defined as a class method using the '@classmethod' decorator. It takes two parameters: 'cls' (referring to the 'Hat' class)
#   and 'name' (the name of the person to be sorted). Inside the 'sort' method, it uses the 'random.choice' function from the 'random' module to randomly
#   select one of the Hogwarts houses from the class-level 'houses' list and prints the name of the person along with the assigned house.

# - Calling 'sort' method: The 'Hat.sort("Harry")' line of code directly calls the 'sort' method of the 'Hat' class to sort a person's name ("Harry") into one of
#   the Hogwarts houses.

# When the script is executed, it will randomly assign "Harry" to one of the Hogwarts houses and print the result.
