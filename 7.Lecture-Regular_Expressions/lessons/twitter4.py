# File Name: twitter.4.py

# Description: Extracts the Twitter username from a URL using a capture group and allowing for variations including http, https, www, or no protocol.

# Import necessary modules: re for regular expressions.

import re

# Get the user's input for the Twitter URL and remove leading/trailing spaces.
url = input("URL: ").strip()

# Use re.search with a regular expression pattern and a capture group to extract the username.
matches = re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)

# Check if matches are found.
if matches:
    # Display the extracted Twitter username.
    print("Username:", matches.group(1))

# Explanation:

# Description: This script takes a user-provided Twitter URL and extracts the username while allowing for variations including http, https, www, or no protocol.

# The script starts by getting the user's input for the Twitter URL and removes any leading or trailing spaces.

# It then uses re.search with a regular expression pattern "^https?://(?:www\.)?twitter\.com/(.+)$" to capture the username
# using a capture group, while ignoring the case (re.IGNORECASE).

# If matches are found, it displays the extracted Twitter username.

# This script provides flexibility in handling different URL formats for Twitter and captures the username using a capture group.
