# File Name: validate0.py

# Description: Validates an email address by checking for the presence of the "@" symbol.

# Import necessary modules: None needed for this simple script.

# Get the user's input for the email address and remove leading/trailing spaces.
email = input("What's your email? ").strip()

# Check if the email address contains the "@" symbol to determine its validity.
if "@" in email:
    # If "@" is found, print "Valid."
    print("Valid")
else:
    # If "@" is not found, print "Invalid."
    print("Invalid")

# Explanation:

# Description: This script validates an email address provided by the user by checking for the presence of the "@" symbol.

# The script starts by getting the user's input for the email address and removes any leading or trailing spaces.

# It then checks if the email address contains the "@" symbol.

# If "@" is found in the email address, it prints "Valid."

# If "@" is not found in the email address, it prints "Invalid."

# This script provides a basic check for the presence of "@" to validate an email address.
