# itunes0.py - Demonstrates requests

# Import the 'sys' module to access command line arguments
import sys

# Import the 'requests' module to make HTTP requests
import requests

# Check if the number of command line arguments is not 2
if len(sys.argv) != 2:
    sys.exit()  # Exit the script if the condition is met

# Construct the URL for the iTunes API using the command line argument
search_term = sys.argv[1]
url = f"https://itunes.apple.com/search?entity=song&limit=1&term={search_term}"

# Send an HTTP GET request to the iTunes API
response = requests.get(url)

# Print the JSON response from the API
print(response.json())

# Explanation:
# This code demonstrates how to use the 'requests' module to make an HTTP GET request to the iTunes API and
# retrieve information about a song based on a search term provided as a command line argument.

# The 'import sys' and 'import requests' statements at the beginning of the script import the necessary modules.

# The 'if len(sys.argv) != 2:' statement checks if the number of command line arguments is not equal to 2.
# If this condition is met, the script exits using the 'sys.exit()' function. This ensures that the script
# is executed with the correct number of arguments.

# The command line argument provided (sys.argv[1]) is used to construct the URL for the iTunes API request.
# The 'url' variable is formatted with the search term to be used in the API request.

# The 'requests.get(url)' line sends an HTTP GET request to the constructed URL using the 'get' function
# from the 'requests' module. The response from the API is stored in the 'response' variable.

# Finally, the 'print(response.json())' statement prints the JSON response from the API, which contains
# information about the song that matches the search term.
