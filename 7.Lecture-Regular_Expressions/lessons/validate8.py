# File Name: validate8.py

# Description: Validates an email address by checking for the presence of "@" and ".edu" using regular expressions
# and ensuring that they occur at the beginning and end of the input.

# Import necessary modules: re for regular expressions.

import re

# Get the user's input for the email address and remove leading/trailing spaces.
email = input("What's your email? ").strip()

# Use re.search with the pattern "^.+@.+\.edu$" to check if "@" and ".edu" are present at the beginning and end of the input.
if re.search(r"^.+@.+\.edu$", email):
    # If "@" and ".edu" are found at the beginning and end, print "Valid."
    print("Valid")
else:
    # If "@" or ".edu" is not found at the beginning or end, print "Invalid."
    print("Invalid")

# Explanation:

# Description: This script validates an email address provided by the user by checking for the presence of "@" and ".edu" using regular expressions.
# It ensures that "@" and ".edu" occur at the beginning and end of the input.

# The script starts by getting the user's input for the email address and removes any leading or trailing spaces.

# It then uses re.search with the pattern "^.+@.+\.edu$" to check if "@" and ".edu" are present at the beginning and end of the input.

# If "@" and ".edu" are found at the beginning and end of the input, it prints "Valid."

# If "@" or ".edu" is not found at the beginning or end of the input, it prints "Invalid."

# This script provides specific validation for email addresses containing ".edu" using regular expressions
# and ensures that they occur at the beginning and end of the input.
