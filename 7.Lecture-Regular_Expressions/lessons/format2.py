# File Name: format2.py

# Description: Uses re.search and .group to reformat a name from "last, first" to "first last."

# Import necessary modules: re for regular expressions.

import re

# Get the user's input for their name and remove leading/trailing spaces.
name = input("What's your name? ").strip()

# Use re.search to find matches for the "last, first" format.
matches = re.search(r"^(.+), (.+)$", name)

# Check if there are matches.
if matches:
    # If matches are found, use .group to extract and rearrange the last and first names.
    name = matches.group(2) + " " + matches.group(1)

# Display a greeting message with the reformatted name.
print(f"hello, {name}")

# Explanation:

# Description: This script takes a user's input for a name and checks if it's in the "last, first" format using re.search.
# If it is, it reverts the name to the "first last" format using .group.

# The script starts by getting the user's input for their name and removes any leading or trailing spaces.

# It then uses re.search to look for matches following the pattern "^(.+), (.+)$" which corresponds to "last, first" format.

# If matches are found, it uses .group to extract and rearrange the last and first names.

# Finally, it displays a greeting message using the reformatted name.

# This script demonstrates the use of .group to manipulate matched parts of a regular expression.
