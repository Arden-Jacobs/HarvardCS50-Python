# grade2.py - Demonstrates Chained Comparisons

# Prompt the user for a score and convert it to an integer.
score = int(input("Score: "))

# Determine the grade based on the score using chained comparisons.

# If the score is between 90 and 100 (inclusive), print the corresponding grade.
if 90 <= score <= 100:
    print("Grade: A")

# If the score is between 80 and 89, print the corresponding grade.
elif 80 <= score < 90:
    print("Grade: B")

# If the score is between 70 and 79, print the corresponding grade.
elif 70 <= score < 80:
    print("Grade: C")

# If the score is between 60 and 69, print the corresponding grade.
elif 60 <= score < 70:
    print("Grade: D")

# If the score is below 60, print the corresponding grade.
else:
    print("Grade: F")



# In this section, the program demonstrates determining a grade based on a numerical score using chained
# comparisons. Chained comparisons allow you to use a series of comparisons separated by logical operators
# to create a more concise and readable condition. The program directly uses chained comparisons within
# the conditions of the if and elif statements to determine the corresponding grade based on the score range.