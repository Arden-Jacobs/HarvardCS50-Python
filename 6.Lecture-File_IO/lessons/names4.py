# names4.py - Prompts for a name and appends it to a file using a context manager

# Prompt the user to input their name and store it in the "name" variable
name = input("What's your name? ")

# Open the "names.txt" file in append mode using a context manager and append the input name to the file
with open("names.txt", "a") as file:
    file.write(f"{name}\n")  # Append the name to the file, followed by a newline character

# Explanation:
# This script prompts the user to input their name using the input() function and stores the input in the "name" variable.

# It then opens the "names.txt" file in append mode using a context manager.
# The context manager (created using the "with" statement) automatically takes care of opening and closing the file.

# Within the context, the script uses the write() method to append the value of the "name" variable to the file.
# The f-string is used to format the input name and include a newline character "\n" to separate each name.

# After the code block within the "with" context completes, the context manager automatically closes the file.

# As a result, the input name will be appended to the "names.txt" file, each name on a new line, and the file will be properly closed.
