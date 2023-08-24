# camel.py - Convert CamelCase to snake_case

def main():
    # Prompt the user for a variable name in camelCase
    name = input("Enter a variable name in camelCase: ")
    snake_case = ""

    # Convert CamelCase to snake_case
    for i in name:
        if i.isupper():
            snake_case += "_"
            snake_case += i.lower()
        else:
            snake_case += i

    print("snake_case: ", snake_case)

main()



# Explanation:
# This code snippet converts a variable name in CamelCase to snake_case.

# The main function is responsible for prompting the user for input and calling the conversion process.
# It takes the input variable name in CamelCase and initializes an empty string snake_case to store
# the converted version.

# The loop iterates through each character in the input variable name. If the character is uppercase, the code
# adds an underscore to snake_case and converts the uppercase character to lowercase. If the character
# is not uppercase, it directly adds it to snake_case.

# Finally, the converted snake_case string is printed.