# File Name: vault0.py

# Description: This script defines a class 'Vault' to represent a vault with 'galleons', 'sickles', and 'knuts' attributes.
# It demonstrates creating two vault instances, 'potter' and 'weasley', and calculating their total in a new vault 'total'.

# Define the 'Vault' class with a constructor (__init__) to represent a vault with 'galleons', 'sickles', and 'knuts' attributes.
class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    # Define the '__str__' method to provide a string representation of the 'Vault' instance.
    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

# Create a 'potter' vault instance with the given amounts of galleons, sickles, and knuts.
potter = Vault(100, 50, 25)

# Print the 'potter' vault instance.
print(potter)

# Create a 'weasley' vault instance with the given amounts of galleons, sickles, and knuts.
weasley = Vault(25, 50, 100)

# Print the 'weasley' vault instance.
print(weasley)

# Calculate the total amounts of galleons, sickles, and knuts by adding the corresponding values from 'potter' and 'weasley'.
galleons = potter.galleons + weasley.galleons
sickles = potter.sickles + weasley.sickles
knuts = potter.knuts + weasley.knuts

# Create a 'total' vault instance with the calculated total amounts of galleons, sickles, and knuts.
total = Vault(galleons, sickles, knuts)

# Print the 'total' vault instance, which represents the combined total of 'potter' and 'weasley'.
print(total)

# Explanation:

# Description: This script defines a class 'Vault' with a constructor (__init__) to represent a vault with 'galleons', 'sickles', and 'knuts' attributes.
# It demonstrates creating two vault instances, 'potter' and 'weasley', and calculating their total in a new vault 'total'.

# The script consists of the following components:

# - 'Vault' class: This class is defined with a constructor (__init__) that takes three parameters, 'galleons', 'sickles', and 'knuts'. Inside the constructor,
#   it initializes the 'galleons', 'sickles', and 'knuts' attributes with the provided values.

# - '__str__' method: This method is defined within the 'Vault' class to provide a string representation of the 'Vault' instance. It returns a string
#   containing the amounts of galleons, sickles, and knuts in the vault.

# - 'potter' and 'weasley' instances: Two vault instances are created, 'potter' and 'weasley', with specific amounts of galleons, sickles, and knuts.

# - Calculation of the total: The script calculates the total amounts of galleons, sickles, and knuts by adding the corresponding values from 'potter' and 'weasley'.

# - 'total' instance: A new vault instance 'total' is created with the calculated total amounts of galleons, sickles, and knuts.

# - Printing: The script prints the 'potter', 'weasley', and 'total' vault instances to display their contents and the combined total.
