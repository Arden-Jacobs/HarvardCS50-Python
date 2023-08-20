# agree4.py - Compares Multiple Strings Using startswith()

# Prompt the user for input, strip leading and trailing whitespace,
# convert the input to lowercase, and store it in the variable `answer`.
answer = input("Do you agree? ").strip().lower()

# Use the `startswith()` method to compare if the lowercase value of `answer` starts with "y".

# If `answer` starts with "y" (ignoring case), print the corresponding message.
if answer.startswith("y"):
    print("Agreed")

# If `answer` does not start with "y", print the corresponding message.
else:
    print("Not agreed")



# In this section, the program demonstrates comparing the user's input by checking if it starts with the letter
# "y" (ignoring case). The process of stripping whitespace and converting to lowercase remains the same as in
# the previous sections. The program uses the startswith() method to compare whether the lowercase answer
# starts with "y", and prints the corresponding message based on the comparison result (while ignoring case).