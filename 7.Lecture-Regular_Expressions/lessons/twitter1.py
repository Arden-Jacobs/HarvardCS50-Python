# File Name: twitter1.py

# Description: Extracts the Twitter username from a URL using the str.removeprefix method.

# Import necessary modules: None needed for this simple script.

# Get the user's input for the Twitter URL and remove leading/trailing spaces.
url = input("URL: ").strip()

# Use str.removeprefix to remove the "https://twitter.com/" part from the URL.
username = url.removeprefix("https://twitter.com/")

# Display the extracted Twitter username.
print(f"Username: {username}")

# Explanation:

# Description: This script takes a user-provided Twitter URL and extracts the username using the str.removeprefix method.

# The script starts by getting the user's input for the Twitter URL and removes any leading or trailing spaces.

# It then uses str.removeprefix to remove the "https://twitter.com/" part from the URL, leaving just the username.

# Finally, it displays the extracted Twitter username.

# This script provides a simple way to extract a username from a Twitter URL using str.removeprefix.
