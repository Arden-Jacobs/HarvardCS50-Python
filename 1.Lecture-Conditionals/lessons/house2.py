# house2.py - Uses "match" with Case for String Comparisons

# Prompt the user for their name.
name = input("What's your name? ")

# Use the "match" statement with "case" clauses for string comparisons.

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")



# In this section, the code demonstrates using the new "match" statement with "case" clauses (introduced in Python 3.10)
# for string comparisons. The program prompts the user for their name and then uses the "match" statement to compare
# the entered name with different cases. If the entered name matches any of the specified cases ("Harry", "Hermione", "Ron", "Draco"),
# the corresponding output is printed. If the entered name does not match any of the specified cases, the _ case is used to print "Who?".