# File Name: vault1.py

# Description: This script defines a class 'Vault' to represent a vault containing magical currency in the form of Galleons, Sickles, and Knuts.
# It demonstrates operator overloading by implementing the '__add__' method to allow adding two vaults together to create a new vault.
# The script creates two vault instances, 'potter' and 'weasley', and then combines them to calculate the total amount of currency in a new 'total' vault.

# Define the 'Vault' class with a constructor (__init__) to represent a vault with 'galleons', 'sickles', and 'knuts' attributes.
class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    # Define the '__str__' method to provide a string representation of the 'Vault' instance.
    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    # Define the '__add__' method to allow adding two 'Vault' instances together, resulting in a new 'Vault' instance.
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)

# Create a 'Vault' instance 'potter' with specified amounts of currency.
potter = Vault(100, 50, 25)
print(potter)

# Create another 'Vault' instance 'weasley' with different amounts of currency.
weasley = Vault(25, 50, 100)
print(weasley)

# Add the 'potter' and 'weasley' vaults together using the overloaded '+' operator and store the result in a new 'total' vault.
total = potter + weasley
print(total)

# Explanation:

# Description: This script defines a class 'Vault' to represent a vault containing magical currency in the form of Galleons, Sickles, and Knuts.
# It demonstrates operator overloading by implementing the '__add__' method to allow adding two vaults together to create a new vault.
# The script creates two vault instances, 'potter' and 'weasley', and then combines them to calculate the total amount of currency in a new 'total' vault.

# The script consists of the following components:

# - 'Vault' class: This class is defined with a constructor (__init__) that takes three parameters, 'galleons', 'sickles', and 'knuts',
#   to initialize the attributes representing the amounts of each currency.

# - '__str__' method: This method is defined within the 'Vault' class to provide a string representation of the 'Vault' instance. It returns
#   a string containing the amounts of Galleons, Sickles, and Knuts in the vault.

# - '__add__' method: This special method is defined to enable operator overloading for the '+' operator. It takes two 'Vault' instances, 'self' and 'other',
#   and adds their corresponding currency amounts together to create a new 'Vault' instance representing the total amount.

# - Creating 'Vault' instances: Two 'Vault' instances, 'potter' and 'weasley', are created with different amounts of currency.

# - Combining vaults: The script demonstrates the use of the overloaded '+' operator to add the 'potter' and 'weasley' vaults together, creating a new 'total' vault
#   that contains the combined currency amounts.

# - Printing results: The script prints the 'potter' and 'weasley' vaults, as well as the 'total' vault, to display the currency amounts in each vault.

# This script showcases how to use operator overloading to create meaningful operations for custom classes, allowing the combination of 'Vault' instances in a natural way.
