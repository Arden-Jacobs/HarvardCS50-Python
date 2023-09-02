# File Name: validate11.py

# Description: Validates an email address by checking for the presence of "@" and ".edu" using regular expressions
# and ensuring that they occur at the beginning and end of the input. It also enforces that the username and domain
# only contain word characters (alphanumeric characters and underscores). The regular expression is case-insensitive.

# Import necessary modules: re for regular expressions.

import re

# Get the user's input for the email address and remove leading/trailing spaces.
email = input("What's your email? ").strip()

# Use re.search with the pattern "^\w+@\w+\.edu$" and re.IGNORECASE to check if "@" and ".edu" are present at the beginning and end,
# and if the username and domain only contain word characters (alphanumeric characters and underscores), in a case-insensitive manner.
if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
    # If the conditions are met, print "Valid."
    print("Valid")
else:
    # If the conditions are not met, print "Invalid."
    print("Invalid")

# Explanation:

# Description: This script validates an email address provided by the user by checking for the presence of "@" and ".edu" using regular expressions.
# It ensures that "@" and ".edu" occur at the beginning and end of the input and that the username and domain only contain word characters (alphanumeric characters and underscores).
# The regular expression is case-insensitive.

# The script starts by getting the user's input for the email address and removes any leading or trailing spaces.

# It then uses re.search with the pattern "^\w+@\w+\.edu$" and re.IGNORECASE to check if "@" and ".edu" are present at the beginning and end,
# and if the username and domain only contain word characters (alphanumeric characters and underscores), in a case-insensitive manner.

# If the conditions are met, it prints "Valid."

# If the conditions are not met, it prints "Invalid."

# This script provides specific validation for email addresses containing ".edu" using a case-insensitive regular expression,
# and it enforces that the username and domain only contain word characters.
