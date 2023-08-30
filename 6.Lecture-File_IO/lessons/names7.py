# names7.py - Reads names from a file, appends them to a list for sorting, and prints sorted greeting messages

# Initialize an empty list to store names
names = []

# Open the "names.txt" file in read mode using a context manager and loop through its lines
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())  # Append each name to the "names" list after removing trailing whitespace

# Loop through the sorted "names" list and print greeting messages for each name
for name in sorted(names):
    print(f"hello, {name}")

# Explanation:
# This script reads names from the "names.txt" file, where each name is stored on a separate line.

# The script initializes an empty list called "names" to store the names read from the file.

# It uses a context manager to open the "names.txt" file in read mode. The context manager automatically takes
# care of opening and closing the file.

# The for loop directly iterates over the lines of the file using the file object itself. For each line, the loop
# appends the name (with trailing whitespace removed using rstrip()) to the "names" list.

# After the loop, the script uses the sorted() function to sort the names in the "names" list in lexicographical order.
# The sorted list is then looped through, and for each name, a greeting message is printed using the print() function.

# The result is a series of greeting messages, each
