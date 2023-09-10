# File Name: numb3rs.py

# Description: Validates an IPv4 address by checking if it consists of four groups of numbers separated by periods.
# Each group should be in the range of 0 to 255. The script uses regular expressions to validate the format and
# additional logic to check the value of each group.

# Import necessary modules: re for regular expressions.

import re

# Define the main function.
def main():
    # Get the user's input for the IPv4 address and remove leading/trailing spaces.
    print(validate(input("IPv4 Address: ").strip()))

# Define the validate function to check the validity of the IPv4 address.
def validate(ip):
    # Use re.search with the pattern to check if the IPv4 address matches the expected format.
    if re.search(r"^([0-9]{1,3}\.)[0-9]{1,3}\.[0-9]{1,3}\.([0-9]{1,3})$", ip):
        # If the conditions for the format are met, split the address into groups.
        temp = ip.split(".")
        count = 0
        for i in temp:
            # Check if each group is within the valid range (0 to 255).
            if "0" <= i <= "255":
                count += 1
        # If all groups are within the valid range and there are exactly four groups, return True (Valid).
        if count == 4:
            return True
        else:
            return False
    else:
        # If the IPv4 address does not match the expected format, return False (Invalid).
        return False

# Check if the script is run as the main program.
if __name__ == "__main__":
    main()

# Explanation:

# Description: This script validates an IPv4 address provided by the user by checking if it consists of four groups of numbers separated by periods.
# Each group should be in the range of 0 to 255. The script uses regular expressions to validate the format and additional logic to check the value of each group.

# The script starts by defining the main function, which gets the user's input for the IPv4 address and removes any leading or trailing spaces.

# It also defines the validate function to check the validity of the IPv4 address. It uses re.search with the pattern to check if the IPv4 address matches the expected format.

# If the conditions for the format are met, the address is split into groups, and each group is checked to ensure it is within the valid range (0 to 255).

# If all groups are within the valid range and there are exactly four groups, the function returns True (Valid). Otherwise, it returns False (Invalid).

# Finally, the script checks if it is run as the main program and calls the main function to start the validation process.
