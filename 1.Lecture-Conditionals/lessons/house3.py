# house3.py - Uses "|" for Multiple Options in "match" Case

# Prompt the user for their name.
name = input("What's your name? ")

# Use the "|" operator to specify multiple options in the "case" clauses.

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")



# In this section, the code demonstrates using the | (pipe) operator to specify multiple options within a single
# "case" clause of the "match" statement.The program prompts the user for their name and then uses the "match"
# statement to compare the entered name with different cases. The case "Harry" | "Hermione" | "Ron":clause
# checks if the entered name matches any of the specified options("Harry", "Hermione", or "Ron"),and if so,
# it prints "Gryffindor".Similarly, the case "Draco": clause checks if the name is "Draco" and prints "Slytherin".
# The _ case is used to print "Who?" if the name doesn't match any of the specified options.