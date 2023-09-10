# File Name: um.py

# Description: This script defines a function 'count' that counts the occurrences of the word "um" (case-insensitive)
# in a given text string. The script also includes a 'main' function to interactively input text and display the count.

# Import necessary modules: re for regular expressions.

import re

# Define the main function.
def main():
    # Get the user's input for the text and count the occurrences of "um" using the 'count' function.
    print(count(input("Text: ")))

# Define the 'count' function to count occurrences of "um" in the input text.
def count(s):
    # Define a regular expression pattern to match the word "um" as a whole word (case-insensitive).
    regex = r"\bum\b"
    
    # Use 're.findall' to find all matches of the pattern in the input text (case-insensitive).
    match = re.findall(regex, s, re.IGNORECASE)
    
    # Return the count of matches (occurrences of "um").
    return len(match)

# Check if the script is run as the main program.
if __name__ == "__main__":
    # If it is, call the 'main' function to interactively input text and display the count of "um" occurrences.
    main()

# Explanation:

# Description: This script defines a function 'count' that is used to count the occurrences of the word "um" (case-insensitive)
# in a given text string. It also includes a 'main' function for interactive use, allowing the user to input text and see the count.

# We start by importing the 're' module for regular expressions.

# The script defines a 'main' function, responsible for getting user input for the text and counting the occurrences of "um" in the text
# using the 'count' function.

# The 'count' function is designed to count occurrences of "um" as whole words (not substrings) and is case-insensitive. It achieves
# this by defining a regular expression pattern 'regex' that matches the word "um" as a whole word. The '\b' anchors ensure that "um"
# is matched as a whole word.

# Inside the 'count' function, we use 're.findall' to find all matches of the pattern in the input text. We specify the 're.IGNORECASE'
# flag to make the pattern matching case-insensitive. The matches are stored in the 'match' variable.

# Finally, the 'count' function returns the length of the 'match' list, which represents the count of occurrences of "um" in the text.

# The script also checks whether it is executed as the main program. If it is, it initiates the interactive process by calling the 'main'
# function, allowing the user to input text and see the count of "um" occurrences.
