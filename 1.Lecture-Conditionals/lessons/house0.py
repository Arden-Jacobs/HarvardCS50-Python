# house0.py - Compares Multiple Strings with if/elif/else

# Prompt the user for their name.
name = input("What's your name? ")

# Compare the entered name with specific names using if/elif/else statements.

# If the name is "Harry", "Hermione", or "Ron", print "Gryffindor".
if name == "Harry":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")

# If the name is "Draco", print "Slytherin".
elif name == "Draco":
    print("Slytherin")

# If the name does not match any of the specified names, print "Who?".
else:
    print("Who?")



# In this section, the code demonstrates comparing multiple strings using if, elif, and else statements.The program
# prompts the user for their name and then uses a series of if and elif statements to compare the entered name
# with specific names. Depending on the entered name, the program prints corresponding house names(e.g., "Gryffindor" or "Slytherin").
# If the entered name does not match any of the specified names, the program prints "Who?".