# generate.py - Demonstrates import and random.choice

import random

# Use the random.choice() function to randomly select an item from a list
coin = random.choice(["heads", "tails"])

# Print the randomly chosen item (coin)
print(coin)

# Explanation:
# This code demonstrates the usage of the random.choice() function from the random module to
# randomly select an item from a list and print the result.

# The import statement "import random" at the beginning of the script imports the random module,
# which provides various random number generation functions.

# The random.choice() function is used to randomly select an item from a given list. In this case,
# the list ["heads", "tails"] contains two possible outcomes for a coin toss, and the function will
# select one of them randomly.

# The selected item is stored in the variable 'coin'.

# The print() statement is then used to display the result of the random choice, which will either be
# "heads" or "tails" based on the random selection.
