# names3.py - Prompts for a name and appends it to a file

# Prompt the user to input their name and store it in the "name" variable
name = input("What's your name? ")

# Open the "names.txt" file in append mode and append the input name to the file
file = open("names.txt", "a")
file.write(f"{name}\n")  # Append the name to the file, followed by a newline character
file.close()             # Close the file after appending

# Explanation:
# This script prompts the user to input their name using the input() function and stores the input in the "name" variable.

# It then opens the "names.txt" file in append mode using the open() function with the mode "a".
# This means that if the file already exists, new data will be added to the end of the file without affecting existing data.

# The script uses the write() method to append the value of the "name" variable to the file.
# The f-string is used to format the input name and include a newline character "\n" to separate each name.

# After appending the name to the file, the close() method is called to close the file and ensure that data is saved.

# As a result, the input name will be appended to the "names.txt" file, each name on a new line.
