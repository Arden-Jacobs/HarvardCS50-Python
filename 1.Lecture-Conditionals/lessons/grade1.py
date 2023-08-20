# grade1.py - Demonstrates Inequalities and Logical Operators

# Prompt the user for a score and convert it to an integer.
score = int(input("Score: "))

# Determine the grade based on the score using inequalities and logical operators.

# If the score is between 90 and 100 (inclusive), print the corresponding grade.
if 90 <= score and score <= 100:
    print("Grade: A")

# If the score is between 80 and 89, print the corresponding grade.
elif 80 <= score and score < 90:
    print("Grade: B")

# If the score is between 70 and 79, print the corresponding grade.
elif 70 <= score and score < 80:
    print("Grade: C")

# If the score is between 60 and 69, print the corresponding grade.
elif 60 <= score and score < 70:
    print("Grade: D")

# If the score is below 60, print the corresponding grade.
else:
    print("Grade: F")



# In this section, the program demonstrates determining a grade based on a numerical score using a series of
# if-elif statements. The program uses inequalities and logical operators directly within the conditions of
# the statements to determine the corresponding grade based on the score range.