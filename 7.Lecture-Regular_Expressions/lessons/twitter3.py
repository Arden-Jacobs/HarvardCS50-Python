# File Name: twitter3.py

# Description: Extracts the Twitter username from a URL allowing for variations including http, no protocol, and www.

# Import necessary modules: re for regular expressions.

import re

# Get the user's input for the Twitter URL and remove leading/trailing spaces.
url = input("URL: ").strip()

# Use re.sub with a regular expression pattern to remove variations from the URL.
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)

# Display the extracted Twitter username.
print(f"Username: {username}")

# Explanation:

# Description: This script takes a user-provided Twitter URL and extracts the username while allowing for variations including http, no protocol, and www.

# The script starts by getting the user's input for the Twitter URL and removes any leading or trailing spaces.

# It then uses re.sub with a regular expression pattern "^(https?://)?(www\.)?twitter\.com/" to remove variations from the URL,
# such as http, https, www, or no protocol before "twitter.com," leaving just the username.

# Finally, it displays the extracted Twitter username.

# This script provides flexibility in handling different URL formats for Twitter.
