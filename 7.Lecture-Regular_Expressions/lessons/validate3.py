# File Name: validate3.py

# Description: Validates an email address by checking whether the domain ends with ".edu."

# Import necessary modules: None needed for this simple script.

# Get the user's input for the email address and remove leading/trailing spaces.
email = input("What's your email? ").strip()

# Split the email address into username and domain parts using "@" as the separator.
username, domain = email.split("@")

# Check if the username is not empty and if the domain ends with ".edu" to determine its validity.
if username and domain.endswith(".edu"):
    # If the username is not empty and the domain ends with ".edu," print "Valid."
    print("Valid")
else:
    # If the username is empty or the domain doesn't end with ".edu," print "Invalid."
    print("Invalid")

# Explanation:

# Description: This script validates an email address provided by the user by checking whether the domain part ends with ".edu."

# The script starts by getting the user's input for the email address and removes any leading or trailing spaces.

# It then splits the email address into username and domain parts using "@" as the separator.

# Next, it checks if the username is not empty and if the domain ends with ".edu."

# If the username is not empty and the domain ends with ".edu," it prints "Valid."

# If the username is empty or the domain doesn't end with ".edu," it prints "Invalid."

# This script provides a specific validation for email addresses based on the ".edu" domain.
