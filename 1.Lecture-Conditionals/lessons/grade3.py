# grade3.py - Demonstrates Fewer Comparisons

# Prompt the user for a score and convert it to an integer.
score = int(input("Score: "))

# Determine the grade based on the score using fewer comparisons.

# If the score is 90 or higher, print the corresponding grade.
if score >= 90:
    print("Grade: A")

# If the score is 80 or higher, print the corresponding grade.
elif score >= 80:
    print("Grade: B")

# If the score is 70 or higher, print the corresponding grade.
elif score >= 70:
    print("Grade: C")

# If the score is 60 or higher, print the corresponding grade.
elif score >= 60:
    print("Grade: D")

# If the score is below 60, print the corresponding grade.
else:
    print("Grade: F")



# In this section, the program demonstrates determining a grade based on a numerical score using fewer comparisons.
# By utilizing the fact that the grades are assigned in a decreasing order of score, the program can use a series
# of if and elif statements with just the lower boundary of each grade range. This approach reduces the number
# of comparisons needed to determine the grade.