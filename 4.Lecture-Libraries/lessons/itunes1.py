# itunes1.py - Demonstrates json

# Import necessary modules for JSON manipulation, system operations, and making HTTP requests
import json
import sys
import requests

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 2:
    sys.exit()

# Make an HTTP GET request to the iTunes API to search for a song based on the provided argument
response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]
)

# Print the JSON response with indentation for better readability
print(json.dumps(response.json(), indent=2))

# Explanation:
# This code demonstrates the use of the json, sys, and requests modules to interact with the iTunes
# API and retrieve information about a song.

# The import statements at the beginning of the script import the necessary modules:
# - json for handling JSON data
# - sys for interacting with the system (command-line arguments)
# - requests for making HTTP requests

# The if statement checks whether the correct number of command-line arguments is provided. If not,
# the script exits using sys.exit().

# The requests.get() function is used to send an HTTP GET request to the iTunes API. The API endpoint
# is constructed based on the provided command-line argument using sys.argv[1].

# The print() statement outputs the JSON response from the API in a nicely indented format using
# json.dumps() with the indent parameter set to 2 for readability.
