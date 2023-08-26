# itunes2.py - Demonstrates iterating over JSON

# Import necessary modules for JSON manipulation, system operations, and making HTTP requests
import json
import sys
import requests

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 2:
    sys.exit()

# Make an HTTP GET request to the iTunes API to search for songs based on the provided argument
response = requests.get(
    "https://itunes.apple.com/search?entity=song&term=" + sys.argv[1]
)

# Convert the response JSON data to a Python dictionary
o = response.json()

# Iterate over the "results" section of the dictionary and print each track's name
for result in o["results"]:
    print(result["trackName"])

# Explanation:
# This code demonstrates how to retrieve and iterate over JSON data returned from the iTunes API.

# The import statements at the beginning of the script import the necessary modules:
# - json for handling JSON data
# - sys for interacting with the system (command-line arguments)
# - requests for making HTTP requests

# The if statement checks whether the correct number of command-line arguments is provided. If not,
# the script exits using sys.exit().

# The requests.get() function sends an HTTP GET request to the iTunes API. The API endpoint is
# constructed based on the provided command-line argument using sys.argv[1].

# The response JSON data is stored in the variable "o" after being converted to a Python dictionary.

# The for loop iterates over each "result" in the "results" section of the dictionary. Inside the loop,
# the script prints the name of each track using result["trackName"].
