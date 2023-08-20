# house1.py - Uses "or" for Multiple String Comparisons

# Prompt the user for their name.
name = input("What's your name? ")

# Use the "or" operator to compare the entered name with specific names using if/elif/else statements.

# If the name is "Harry", "Hermione", or "Ron", print "Gryffindor".
if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")

# If the name is "Draco", print "Slytherin".
elif name == "Draco":
    print("Slytherin")

# If the name does not match any of the specified names, print "Who?".
else:
    print("Who?")



# In this section, the code demonstrates using the "or" (or) operator to simplify multiple string comparisons with
# in an if statement. The program prompts the user for their name and then uses the "or" operator to check if the
# entered name matches any of the specified names ("Harry", "Hermione", or "Ron"). If the entered name matches
# any of these names, the program prints "Gryffindor". If the entered name is "Draco", he program prints "Slytherin".
# Otherwise, if the entered name does not match any of the specified names, the program prints "Who?".