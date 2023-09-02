# File Name: validate1.py

# Description: Validates an email address by checking for the presence of "@" and "." symbols.

# Import necessary modules: None needed for this simple script.

# Get the user's input for the email address and remove leading/trailing spaces.
email = input("What's your email? ").strip()

# Check if the email address contains both "@" and "." symbols to determine its validity.
if "@" in email and "." in email:
    # If both "@" and "." are found, print "Valid."
    print("Valid")
else:
    # If either "@" or "." is not found, print "Invalid."
    print("Invalid")

# Explanation:

# Description: This script validates an email address provided by the user by checking for the presence of both "@" and "." symbols.

# The script starts by getting the user's input for the email address and removes any leading or trailing spaces.

# It then checks if the email address contains both "@" and "." symbols.

# If both "@" and "." are found in the email address, it prints "Valid."

# If either "@" or "." is not found in the email address, it prints "Invalid."

# This script provides a basic check for the presence of both "@" and "." to validate an email address.
