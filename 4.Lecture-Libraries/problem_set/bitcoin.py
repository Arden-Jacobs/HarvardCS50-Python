# bitcoin.py - Converts an amount of Bitcoin to USD based on the current exchange rate

# Import the sys module for command-line arguments and the requests module for making HTTP requests
import sys
import requests

# Check if exactly one command-line argument is provided
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

# Initialize a variable to store the numeric value of the command-line argument
n = float(0)

# Loop to input a valid numeric command-line argument
while True:
    try:
        n = float(sys.argv[1])
        break
    except ValueError:
        sys.exit("Command-line argument is not a number")

# Try to fetch the current Bitcoin exchange rate and calculate the equivalent in USD
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    json_object = response.json()
    bitcoin = json_object["bpi"]["USD"]["rate_float"]
    rate = n * bitcoin
    # Print the equivalent USD amount with proper formatting
    print(f"${rate:,.4f}")

# Handle exceptions that might occur during the request
except requests.RequestException:
    sys.exit(requests.RequestException)

# Explanation:
# This script converts an amount of Bitcoin to USD based on the current exchange rate obtained from an API.

# The import statements "import sys" and "import requests" at the beginning of the script import the sys module
# for handling command-line arguments and the requests module for making HTTP requests, respectively.

# The script checks if exactly one command-line argument is provided. If not, it exits with an error message.

# A variable "n" is initialized to store the numeric value of the command-line argument.

# The loop attempts to convert the command-line argument to a float. If it succeeds, the loop breaks; otherwise,
# an error message is displayed and the script exits.

# Inside a try-except block, the script fetches the current Bitcoin exchange rate from an API and calculates
# the equivalent amount in USD using the provided numeric value.

# The final "print()" statement displays the equivalent USD amount with proper formatting.

# The except block handles any exceptions that might occur during the request and exits the script with an
# appropriate error message.
