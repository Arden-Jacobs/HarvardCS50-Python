# emojize.py - Converts text input to emoji using the emoji module

# Import the emoji module for working with emojis
import emoji

# Prompt the user for input
emo = input("Input: ")

# Convert the input text to an emoji and print the output
print(emoji.emojize("Output: {}".format(emo), language='alias'))

# Explanation:
# This script uses the emoji module to convert text input into corresponding emojis.

# The import statement "import emoji" at the beginning of the script imports the emoji module, which provides
# functionality for working with emojis.

# The script prompts the user for input using the "input()" function and stores the input in the variable "emo".

# The "emoji.emojize()" function is used to convert the input text to an emoji. The converted emoji string is
# then printed along with the prefix "Output:" using the "print()" function. The "language='alias'" parameter is
# specified to use alias language for emojis (e.g., ":smile:" instead of the actual emoji character).
