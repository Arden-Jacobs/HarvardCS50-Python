# names2.py - Prompts for a name and writes it to a file

# Prompt the user to input their name and store it in the "name" variable
name = input("What's your name? ")

# Open the "names.txt" file in write mode and write the input name to the file
file = open("names.txt", "w")
file.write(name)  # Write the name to the file
file.close()      # Close the file after writing

# Explanation:
# This script prompts the user to input their name using the input() function and stores the input in the "name" variable.

# It then opens the "names.txt" file in write mode using the open() function with the mode "w".
# This means that if the file already exists, its contents will be replaced with the new data.

# The script uses the write() method to write the value of the "name" variable to the file.
# After writing the name to the file, the close() method is called to close the file and ensure that data is saved.

# As a result, the input name will be stored in the "names.txt" file.
