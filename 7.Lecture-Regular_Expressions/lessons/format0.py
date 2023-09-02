# File Name: format0.py

# Description: Reformats a name in "last, first" format to "first last" format.

# Get the user's input for their name and remove leading/trailing spaces.
name = input("What's your name? ").strip()

# Check if the name contains a comma (",") to determine if it's in "last, first" format.
if "," in name:
    # If it's in "last, first" format, split the name into last and first name parts.
    last, first = name.split(", ")
    # Reformat the name as "first last."
    name = f"{first} {last}"

# Display a greeting message with the reformatted name.
print(f"hello, {name}")

# Explanation:

# Description: This script takes a user's input for a name and checks if it's in the "last, first" format.
# If it is, it reverts the name to the "first last" format.

# The script starts by getting the user's input for their name and removes any leading or trailing spaces.

# It then checks if the name contains a comma (",") which indicates it's in the "last, first" format.

# If the name is in "last, first" format, it splits the name into two parts: last and first names.

# Next, it reformats the name as "first last" by rearranging the parts.

# Finally, it displays a greeting message using the reformatted name.

# This script is useful when dealing with names in different formats and ensures consistent output.
