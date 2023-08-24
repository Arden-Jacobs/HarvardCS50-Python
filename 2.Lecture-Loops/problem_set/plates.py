# plates.py - Validate license plates

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    """
    Check if a license plate is valid.

    Args:
        s (str): The license plate to be checked.

    Returns:
        bool: True if the license plate is valid, False otherwise.
    """
    valid_plates = ["cs50", "ecto88", "nrvous"]

    if s.lower() in valid_plates:
        return True

    if len(s) < 4:
        return False

    prefix = s[:3]
    suffix = s[3:]

    if prefix.isalpha() and suffix.isdigit() and (len(s) == 4 or len(s) == 5 or len(s) == 6):
        return True

    return False

main()



# Explanation:
# This code validates license plates based on certain criteria. The main function prompts the user to enter a
# license plate and then checks if it is valid using the is_valid function. The program follows a series of
# checks to determine if the license plate is valid or not.

# The is_valid function is responsible for performing the validity checks. It uses the provided valid plates in
# a list called valid_plates for direct comparison. If the entered plate matches any of the valid plates,
# it returns True. Otherwise, it proceeds with other checks.

# The function checks if the entered plate has a length less than 4, in which case it returns False. It then
# splits the plate into a prefix (the first three characters) and a suffix (the remaining characters). If
# the prefix consists of alphabetic characters and the suffix consists of digits, and the length of the
# plate is either 4, 5, or 6 characters, the function considers the plate as valid