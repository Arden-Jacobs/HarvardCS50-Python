# File Name: validate2.py

# Description: Validates an email address by checking the username and domain separately.

# Import necessary modules: None needed for this simple script.

# Get the user's input for the email address and remove leading/trailing spaces.
email = input("What's your email? ").strip()

# Split the email address into username and domain parts using "@" as the separator.
username, domain = email.split("@")

# Check if the username is not empty and if there is a "." in the domain to determine its validity.
if username and "." in domain:
    # If the username is not empty and "." is found in the domain, print "Valid."
    print("Valid")
else:
    # If the username is empty or "." is not found in the domain, print "Invalid."
    print("Invalid")

# Explanation:

# Description: This script validates an email address provided by the user by checking the username and domain separately.

# The script starts by getting the user's input for the email address and removes any leading or trailing spaces.

# It then splits the email address into username and domain parts using "@" as the separator.

# Next, it checks if the username is not empty and if there is a "." in the domain.

# If the username is not empty and "." is found in the domain, it prints "Valid."

# If the username is empty or "." is not found in the domain, it prints "Invalid."

# This script provides a more detailed validation of email addresses by checking username and domain separately.
