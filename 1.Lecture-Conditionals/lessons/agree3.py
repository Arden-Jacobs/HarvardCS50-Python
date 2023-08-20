# agree3.py - Compares Multiple Strings

# Prompt the user for input, strip leading and trailing whitespace,
# convert the input to lowercase, and store it in the variable `answer`.
answer = input("Do you agree? ").strip().lower()

# Compare the lowercase value of `answer` with the lowercase strings "yes" or "y" to determine agreement.

# If `answer` is equal to "yes" or "y" (ignoring case), print the corresponding message.
if answer == "yes" or answer == "y":
    print("Agreed")

# If `answer` is not equal to "yes" or "y", print the corresponding message.
else:
    print("Not agreed")



# In this section, the program demonstrates comparing the user's input with multiple possible strings ("yes" or "y")
# to determine agreement.The process of stripping whitespace and converting to lowercase remains the same as in 
# the previous section. The program uses an if statement with the logical or operator to compare the lowercase
# answer with the lowercase strings "yes" or "y", and prints the corresponding message based on the
# comparison result (while ignoring case).