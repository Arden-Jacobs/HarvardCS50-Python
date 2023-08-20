# deep.py - Prompts User for the Answer to the Great Question

# Prompt the user for an answer.
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

# Normalize the answer by converting to lowercase and stripping whitespace.
answer = answer.lower().strip()

# Set conditions according to the normalized answer.
if answer == "42" or answer == "forty-two" or answer == "forty two":
    print("Yes")
else:
    print("No")



# In this section, the code prompts the user for an answer to the "Great Question of Life, the Universe, and Everything"
# (a reference to Douglas Adams' "The Hitchhiker's Guide to the Galaxy"). The entered answer is normalized by
# converting it to lowercase and stripping any leading or trailing whitespace. This normalization step ensures
# that the code handles answers in a case-insensitive manner and removes any accidental whitespace.

# The program then uses an if statement with logical OR (or) operators to compare the normalized answer with
# different possible valid answers ("42", "forty-two", "forty two"). If the normalized answer matches any
# of these valid options, it prints "Yes". Otherwise, it prints "No".