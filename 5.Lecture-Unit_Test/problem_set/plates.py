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
    # List of valid license plates
    valid_plates = ["cs50", "ecto88", "nrvous"]

    # Check if the lowercase version of the input plate is in the list of valid plates
    if s.lower() in valid_plates:
        return True

    # Check if the length of the input plate is less than 4 characters
    if len(s) < 4:
        return False

    # Separate the prefix (first 3 characters) and suffix (remaining characters)
    prefix = s[:3]
    suffix = s[3:]

    # Check if the prefix is composed of alphabetic characters, the suffix is composed of digits,
    # and the total length of the input plate is 4, 5, or 6 characters
    if prefix.isalpha() and suffix.isdigit() and (len(s) == 4 or len(s) == 5 or len(s) == 6):
        return True

    # If none of the conditions above are met, the plate is not valid
    return False

# Check if the script is run directly
if __name__ == "__main__":
    # Call the main function to start plate validation
    main()

# Explanation:
# This script takes user input for a license plate, checks if the input plate is valid using the is_valid function,
# and then prints "Valid" or "Invalid" accordingly.

# The main function "main()" prompts the user for a license plate, calls the "is_valid()" function to check its validity,
# and then prints "Valid" or "Invalid".

# The "is_valid()" function performs various checks to determine if the given license plate is valid:
# - It checks if the lowercase version of the input plate is in the list of valid plates.
# - It checks if the length of the input plate is less than 4 characters (invalid for the format).
# - It separates the prefix and suffix of the input plate and checks if they follow the alphabetic-numeric pattern.
# - It checks if the total length of the input plate is 4, 5, or 6 characters.

# The "__name__ == '__main__':" check at the end of the script ensures that the main function is executed only
# when the script is run directly, not when it's imported as a module.
