# test_calculator6.py - Test script for the square function from calculator6.py

# Import the square function from calculator6.py
from calculator6 import square

# Function to test positive input values
def test_positive():
    # Test case 1: Check if square(2) returns 4 using an assertion
    assert square(2) == 4
    # Test case 2: Check if square(3) returns 9 using an assertion
    assert square(3) == 9

# Function to test negative input values
def test_negative():
    # Test case 1: Check if square(-2) returns 4 using an assertion
    assert square(-2) == 4
    # Test case 2: Check if square(-3) returns 9 using an assertion
    assert square(-3) == 9

# Function to test zero input value
def test_zero():
    # Test case: Check if square(0) returns 0 using an assertion
    assert square(0) == 0

# Call the functions to run the test cases
test_positive()
test_negative()
test_zero()

# Explanation:
# This script is a test script for the square function from calculator6.py. It tests the functionality of the square function.

# The import statement "from calculator6 import square" at the beginning of the script imports the square function from
# the calculator6.py module.

# The "test_positive()" function contains test cases for positive input values. It uses assertions to check whether
# square(2) is equal to 4 and whether square(3) is equal to 9.

# The "test_negative()" function contains test cases for negative input values. It uses assertions to check whether
# square(-2) is equal to 4 and whether square(-3) is equal to 9.

# The "test_zero()" function contains a test case for the input value 0. It uses an assertion to check whether
# square(0) is equal to 0.

# The script concludes by calling the "test_positive()", "test_negative()", and "test_zero()" functions to run the test cases.
