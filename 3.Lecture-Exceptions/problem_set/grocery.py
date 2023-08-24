# grocery.py - Grocery List Tracker

# Initialize an empty dictionary to store grocery items and their quantities
grocery = {}

# Create an infinite loop to take user input for grocery items and quantities
while True:
    try:
        # Prompt the user to input a grocery item (key)
        key = input().upper()
        
        # Initialize the default quantity value
        value = 1
        
        # Check if the entered item (key) is already in the grocery dictionary
        if key in grocery.keys():
            # If yes, increment the quantity value
            grocery[key] = value + 1
        else:
            # If not, add the item to the dictionary with the initial quantity value
            grocery.update({key: value})
    except EOFError:
        # When the end of input is reached (EOFError), display the sorted grocery list with quantities
        for k in sorted(grocery):
            print("{} {}".format(grocery[k], k))
        break



# Explanation:
# This code snippet simulates a grocery list tracker. It allows the user to input grocery items and keeps track
# of the quantity of each item.

# An empty dictionary named "grocery" is initialized to store grocery items (keys) and their corresponding quantities.

# The code enters an infinite loop using a "while True" statement to repeatedly take user input until an EOFError
# (end of file) is encountered.

# Inside the loop, the user is prompted to input a grocery item using the input() function. The entered item is
# converted to uppercase using the ".upper()" method to ensure case-insensitive matching.

# A default quantity value of 1 is initialized.

# The code checks if the entered item (key) is already in the "grocery" dictionary. If it is, the code increments
# the quantity value associated with that item by 1. If not, the item is added to the dictionary with the initial
# quantity value.

# When an EOFError is encountered (end of input), the loop exits, and the code iterates through the sorted keys
# of the "grocery" dictionary. For each key (item), it displays the quantity and item using the format "{} {}"
# and the .format() method.

# The overall behavior of the program is to allow the user to input grocery items, keep track of their quantities,
# and display the sorted list of items with their quantities when the input is complete.
