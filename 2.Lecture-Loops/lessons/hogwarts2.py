# howarts2.py - Demonstrating Iterating Over and Indexing into a List

# List of students' names
students = ["Hermione", "Harry", "Ron"]

# Iterate over the list, displaying index and corresponding student's name
for i in range(len(students)):
    print(i + 1, students[i])



# Explanation:
# This code illustrates how to iterate over a list, accessing both the index and the corresponding element using
# a combination of for loop and range.

# List Definition:
# The students list is defined with three strings representing students' names: "Hermione", "Harry", and "Ron".

# Iterating Over the List and Indexing:
# The for loop iterates over the indices of the students list using the range function.
# range(len(students)) generates indices from 0 to the length of the list minus one (0 to 2 in this case).
# In each iteration, the index i is obtained from the range and is used to access the corresponding student's name using students[i].
# The print statement displays the index incremented by 1 (to make it 1-based) and the corresponding student's name.
# The loop iterates over the indices of the list and displays the index along with the corresponding student's name.
