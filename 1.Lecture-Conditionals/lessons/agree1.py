# agree1.py - Strips String Before Comparing

# Prompt the user for input, strip leading and trailing whitespace, and store it in the variable `answer`.
answer = input("Do you agree? ").strip()

# Compare the value of `answer` with the string "yes" to determine agreement.

# If `answer` is equal to "yes", print the corresponding message.
if answer == "yes":
    print("Agreed")

# If `answer` is not equal to "yes", print the corresponding message.
else:
    print("Not agreed")



# In this section, the program demonstrates stripping whitespace from the user's input before comparing it with
# the string "yes". The input() function is used to prompt the user for input, and the strip() method is used
# to remove any leading or trailing whitespace characters from the input. The program then uses an if
# statement to compare the cleaned answer with the string "yes", and prints the corresponding
# message based on the comparison result.