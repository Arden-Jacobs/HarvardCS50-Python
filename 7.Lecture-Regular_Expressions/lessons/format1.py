# File Name: format1.py

# Description: Uses re.search to reformat a name from "last, first" to "first last."

# Import necessary modules: re for regular expressions.

import re

# Get the user's input for their name and remove leading/trailing spaces.
name = input("What's your name? ").strip()

# Use re.search to find matches for the "last, first" format.
matches = re.search(r"^(.+), (.+)$", name)

# Check if there are matches.
if matches:
    # If matches are found, extract the last and first names.
    last, first = matches.groups()
    # Reformat the name as "first last."
    name = first + " " + last

# Display a greeting message with the reformatted name.
print(f"hello, {name}")

# Explanation:

# Description: This script takes a user's input for a name and checks if it's in the "last, first" format using re.search.
# If it is, it reverts the name to the "first last" format.

# The script starts by getting the user's input for their name and removes any leading or trailing spaces.

# It then uses re.search to look for matches following the pattern "^(.+), (.+)$" which corresponds to "last, first" format.

# If matches are found, it extracts the last and first names.

# Next, it reformats the name as "first last."

# Finally, it displays a greeting message using the reformatted name.

# This script provides a more flexible way to handle name formatting using regular expressions.
