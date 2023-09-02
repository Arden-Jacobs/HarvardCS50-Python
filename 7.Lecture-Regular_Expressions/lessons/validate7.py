# File Name: validate7.py

# Description: Validates an email address by checking for the presence of "@" and ".edu" using regular expressions.

# Import necessary modules: re for regular expressions.

import re

# Get the user's input for the email address and remove leading/trailing spaces.
email = input("What's your email? ").strip()

# Use re.search with the pattern ".+@.+\.edu" to check if "@" and ".edu" are present in the email address.
if re.search(r".+@.+\.edu", email):
    # If both "@" and ".edu" are found, print "Valid."
    print("Valid")
else:
    # If either "@" or ".edu" is not found, print "Invalid."
    print("Invalid")

# Explanation:

# Description: This script validates an email address provided by the user by checking for the presence of "@" and ".edu" using regular expressions.

# The script starts by getting the user's input for the email address and removes any leading or trailing spaces.

# It then uses re.search with the pattern ".+@.+\.edu" to check if both "@" and ".edu" are present in the email address.

# If both "@" and ".edu" are found in the email address, it prints "Valid."

# If either "@" or ".edu" is not found in the email address, it prints "Invalid."

# This script provides specific validation for email addresses containing ".edu" using regular expressions.
