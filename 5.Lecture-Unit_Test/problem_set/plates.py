# plates.py - Script to validate license plate numbers

# Main function to take user input, check if the input plate is valid, and print the result
def main():
    # Prompt the user for a license plate
    plate = input("Plate: ")
    # Check if the input plate is valid using the is_valid function
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# Function to check if a given license plate is valid
def is_valid(s):
    # Extract the prefix (first 2 characters) from the input plate
    prefix = s[:2]

    # Check if the prefix is composed of alphabetic characters and the entire plate is alphanumeric
    # Also, check if the length of the plate is between 2 and 6 characters
    if (prefix.isalpha() and s.isalnum()) and (len(s) <= 6 and len(s) >= 2):
        for i in s:
            if i.isdigit():
                indice = s.index(i)
                # Check if the remaining part of the plate consists of digits and that the digit is not "0"
                if s[indice:].isdigit() and i != "0":
                    return True
                else:
                    return False
        return True
    return False

# Check if the script is run directly
if __name__ == "__main__":
    # Call the main function to start plate validation
    main()

# Explanation:
# This script prompts the user for a license plate, checks if the input plate is valid using the is_valid function,
# and then prints "Valid" or "Invalid" accordingly.

# The main function "main()" prompts the user for a license plate and calls the "is_valid()" function to check its validity.
# It then prints "Valid" or "Invalid" based on the result.

# The "is_valid()" function performs various checks to determine if the given license plate is valid:
# - It extracts the prefix (first 2 characters) from the input plate and checks if it is composed of alphabetic characters.
# - It checks if the entire plate is alphanumeric and if its length is between 2 and 6 characters.
# - It iterates through the characters of the plate to find digits. If digits are found, it checks if the remaining part of
#   the plate consists of digits and if the digit is not "0". If these conditions are met, the plate is valid.

# The "__name__ == '__main__':" check at the end of the script ensures that the main function is executed only
# when the script is run directly, not when it's imported as a module.
