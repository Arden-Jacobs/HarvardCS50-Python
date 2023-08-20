# agree2.py - Lowercases String Before Comparing

# Prompt the user for input, strip leading and trailing whitespace,
# convert the input to lowercase, and store it in the variable `answer`.
answer = input("Do you agree? ").strip().lower()

# Compare the lowercase value of `answer` with the lowercase string "yes" to determine agreement.

# If `answer` is equal to "yes" (ignoring case), print the corresponding message.
if answer == "yes":
    print("Agreed")

# If `answer` is not equal to "yes", print the corresponding message.
else:
    print("Not agreed")



# In this section, the program demonstrates converting the user's input to lowercase before comparing it with
# the lowercase string "yes". The input() function is used to prompt the user for input, and the strip()
# method is used to remove leading and trailing whitespace. The lower() method is then used to convert
# the input to lowercase. The program uses an if statement to compare the lowercase answer with 
# the lowercase string "yes", and prints the corresponding message based on the comparison
# result (while ignoring case).