# twttr.py - Remove vowels from input

def main():
    npt = input("Input: ")
    output = remove_vowels(npt)
    print(output)

def remove_vowels(input_str):
    """
    Remove vowels (a, e, i, o, u) from the input string.

    Args:
        input_str (str): The input string to remove vowels from.

    Returns:
        str: The input string with vowels removed.
    """
    vowels = "aeiouAEIOU"
    output = ""

    for char in input_str:
        if char not in vowels:
            output += char

    return output

main()



# Explanation:
# This code removes vowels from an input string provided by the user. The main function takes user input and then
# calls the remove_vowels function to remove vowels from the input string. The result is printed as the output.

# The remove_vowels function performs the actual task of removing vowels. It iterates through each character in
# the input string. If the current character is not a vowel (either lowercase or uppercase), it is added to the
# output string. Vowels are defined in the vowels string.
