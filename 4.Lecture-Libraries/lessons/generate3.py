# generate3.py - Demonstrates shuffle

# Import the 'random' module
import random

# A list of cards
cards = ["jack", "queen", "king"]

# Shuffle the list of cards in-place
random.shuffle(cards)

# Iterate through the shuffled cards and print each card
for card in cards:
    print(card)

# Explanation:
# This code demonstrates the usage of the 'shuffle' function from the 'random' module to shuffle
# the elements of a list.

# The 'import random' statement at the beginning of the script imports the 'random' module,
# allowing you to access its various randomization functions.

# A list named 'cards' is defined with three elements: "jack", "queen", and "king".

# The 'random.shuffle(cards)' line shuffles the elements of the 'cards' list in-place. This
# means that the order of the elements in the list is modified randomly.

# The 'for' loop is used to iterate through each card in the shuffled list 'cards'.
# Inside the loop, the 'print' statement is used to display each card on a new line.

# As a result of the shuffling, the cards will be printed in a random order.
