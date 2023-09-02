# File Name: twitter2.py

# Description: Extracts the Twitter username from a URL using the re.sub method.

# Import necessary modules: re for regular expressions.

import re

# Get the user's input for the Twitter URL and remove leading/trailing spaces.
url = input("URL: ").strip()

# Use re.sub to remove the "https://twitter.com/" part from the URL.
username = re.sub(r"^https://twitter\.com/", "", url)

# Display the extracted Twitter username.
print(f"Username: {username}")

# Explanation:

# Description: This script takes a user-provided Twitter URL and extracts the username using the re.sub method.

# The script starts by getting the user's input for the Twitter URL and removes any leading or trailing spaces.

# It then uses re.sub with a regular expression pattern "^https://twitter\.com/" to remove the "https://twitter.com/" part from the URL,
# leaving just the username.

# Finally, it displays the extracted Twitter username.

# This script provides a flexible way to extract a username from a Twitter URL using regular expressions and re.sub.
