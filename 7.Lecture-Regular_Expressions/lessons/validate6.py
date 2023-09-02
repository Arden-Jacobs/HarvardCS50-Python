# File Name: validate6.py

# Description: Validates an email address by checking for the presence of "@" using regular expressions with ".+" patterns.

# Import necessary modules: re for regular expressions.

import re

# Get the user's input for the email address and remove leading/trailing spaces.
email = input("What's your email? ").strip()

# Use re.search with ".+@.+" pattern to check if "@" is present in the email address.
if re.search(".+@.+", email):
    # If "@" is found, print "Valid."
    print("Valid")
else:
    # If "@" is not found, print "Invalid."
    print("Invalid")

# Explanation:

# Description: This script validates an email address provided by the user by checking for the presence of "@" using regular expressions with ".+" patterns.

# The script starts by getting the user's input for the email address and removes any leading or trailing spaces.

# It then uses re.search with the pattern ".+@.+" to check if "@" is present in the email address.

# If "@" is found in the email address, it prints "Valid."

# If "@" is not found in the email address, it prints "Invalid."

# This script provides a basic check for the presence of "@" using regular expressions with ".+" patterns to validate an email address.
