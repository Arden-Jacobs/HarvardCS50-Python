# twttr.py - Script to remove vowels from a given input word

# Main function to take user input, process it using the shorten function, and print the output
def main():
    # Prompt the user for input
    npt = input("Input: ")
    # Call the shorten function to process the input and store the result
    output = shorten(npt)
    # Print the processed output
    print(output)

# Function to remove vowels from a given word
def shorten(word):
    # Define a string containing all vowels
    vowels = "aeiouAEIOU"
    # Initialize an empty string to store the output
    output = ""

    # Iterate through each character in the input word
    for char in word:
        # Check if the character is not a vowel
        if char not in vowels:
            # Add the character to the output string
            output += char

    # Return the processed output
    return output

# Check if the script is run directly
if __name__ == "__main__":
    # Call the main function to start processing
    main()

# Explanation:
# This script takes user input, processes it using the shorten function, and then prints the processed output.
# The main function handles user input and output, while the shorten function removes vowels from the input word.

# The main function "main()" prompts the user for input, calls the "shorten()" function to process the input,
# and then prints the processed output.

# The "shorten()" function iterates through each character in the input word. If the character is not a vowel,
# it's added to the output string.

# The "__name__ == '__main__':" check at the end of the script ensures that the main function is executed only
# when the script is run directly, not when it's imported as a module.
