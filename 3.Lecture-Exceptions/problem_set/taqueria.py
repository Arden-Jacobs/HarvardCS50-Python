# taqueria.py - Taqueria Menu

# Define the menu with items and their prices
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Initialize the total cost
total = 0

# Create an infinite loop to take user input and calculate the total cost
while True:
    try:
        # Prompt the user for the item
        item = input("Item: ")
        
        # Iterate through the menu to find the selected item and update the total cost
        for key in menu:
            if key.lower() == item.lower():
                total = total + menu[key]
                print(f"${total:.2f}")  # Display the updated total cost
            else:
                pass
    except EOFError:
        break  # Exit the loop when EOFError (end of file) is encountered



# Explanation:
# This code snippet simulates a taqueria menu. It allows the user to input menu items and calculates the total cost
# based on the selected items and their prices.

# The menu dictionary is defined, containing items as keys and their corresponding prices as values.

# A variable named "total" is initialized to store the accumulated total cost.

# The code enters an infinite loop using a "while True" statement, which allows the user to input menu items until
# an EOFError (end of file) is encountered.

# Inside the loop, the user is prompted to input an item using the input() function. The code then iterates through
# the menu dictionary to find a matching item. If a match is found (case-insensitive), the corresponding price is
# added to the total cost, and the updated total cost is displayed with two decimal places using an f-string.

# If the user enters an item that does not match any in the menu, the "else: pass" statement is used to continue
# searching for matches.

# If the user enters an EOF (End Of File) character, the program breaks out of the loop using the "except EOFError:"
# block, effectively ending the input loop.

# The overall behavior of the program is to allow the user to input menu items, calculate the total cost, and display
# the updated total cost with each item selection.
