# bank.py - Script to determine bank fees based on a greeting

# Main function to take user input, process the greeting, and print the bank fee
def main():
    # Prompt the user for a greeting.
    greeting = input("Enter Greeting: ")
    val = value(greeting)
    print(f"${val}")


def value(greeting):
    # Normalize the greeting by converting to lowercase.
    greeting = greeting.lower().strip()

    # Determine the bank fee based on the normalized greeting.
    if "hello" in greeting:
        return 0
    elif "h" == greeting[0]:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
# Check if the script is run directly
if __name__ == "__main__":
    # Call the main function to start the greeting processing and bank fee determination
    main()

# Explanation:
# This script prompts the user for a greeting, processes the greeting using the value function,
# and then prints the determined bank fee.

# The main function "main()" prompts the user for a greeting and calls the "value()" function to determine
# the corresponding bank fee. It then prints the determined bank fee.

# The "value()" function takes a greeting as input, normalizes it by converting it to lowercase, and then
# determines the bank fee based on the content of the normalized greeting:
# - If "hello" is present in the greeting, the bank fee is "$0".
# - If the first letter of the normalized greeting is "h", the bank fee is "$20".
# - For all other cases, the bank fee is "$100".

# The "__name__ == '__main__':" check at the end of the script ensures that the main function is executed only
# when the script is run directly, not when it's imported as a module.
