# generate1.py - Demonstrates 'from' import and random.choice

# Import the 'choice' function directly from the 'random' module
from random import choice

# Use the imported 'choice' function to randomly select an item from a list
coin = choice(["heads", "tails"])

# Print the randomly chosen item (coin)
print(coin)

# Explanation:
# This code demonstrates the usage of the 'from' import statement to directly import a specific
# function, 'choice', from the 'random' module. It then uses this imported function to
# randomly select an item from a list and print the result.

# The 'from random import choice' statement at the beginning of the script imports only the
# 'choice' function from the 'random' module. This allows you to use the 'choice' function directly
# without having to prefix it with 'random.' when calling it.

# The 'choice' function is used to randomly select an item from the given list ["heads", "tails"],
# which contains two possible outcomes for a coin toss.

# The selected item is stored in the variable 'coin'.

# The 'print' statement is then used to display the result of the random choice, which will either be
# "heads" or "tails" based on the random selection.
