# File Name: test_um.py

# Description: This script contains test cases for the 'count' function in the 'um' module.
# The 'count' function is designed to count the occurrences of the word "um" (case-insensitive) in a given string.

# Import the 'count' function from the 'um' module.

from um import count

# Define the 'test_input' function to test the 'count' function.
def test_input():
    # Test case 1: The input "um?" contains one occurrence of "um" (case-insensitive).
    assert count("um?") == 1

    # Test case 2: The input "yummy" does not contain "um," so the count should be 0.
    assert count("yummy") == 0

    # Test case 3: The input "UM" contains one occurrence of "um" (case-insensitive).
    assert count("UM") == 1

# Explanation:

# Description: In this script, we have a collection of test cases for the 'count' function, which is located in the 'um' module.
# The purpose of these tests is to verify that the 'count' function correctly counts the occurrences of the word "um" (case-insensitive)
# in a given string.

# We start by importing the 'count' function from the 'um' module.

# The script defines a 'test_input' function, which contains multiple test cases.

# - Test case 1: The input "um?" contains one occurrence of "um" (case-insensitive). We use 'assert' to check if the 'count' function
#   correctly counts this occurrence as 1.

# - Test case 2: The input "yummy" does not contain the word "um," so the count should be 0. We use 'assert' to verify that the
#   'count' function correctly returns 0 in this case.

# - Test case 3: The input "UM" contains one occurrence of "um" (case-insensitive). Similar to test case 1, we use 'assert' to check
#   if the 'count' function correctly counts this occurrence as 1.

# These test cases ensure that the 'count' function functions as expected and accurately counts the occurrences of "um" in various
# input strings.
