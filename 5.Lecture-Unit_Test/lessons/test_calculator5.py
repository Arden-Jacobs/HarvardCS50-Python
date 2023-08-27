# test_calculator5.py - Test script for the square function from calculator5.py

# Import the square function from calculator5.py
from calculator5 import square

# Function to test the square function using assertions
def test_square():
    # Test case 1: Check if square(2) returns 4 using an assertion
    assert square(2) == 4
    # Test case 2: Check if square(3) returns 9 using an assertion
    assert square(3) == 9
    # Test case 3: Check if square(-2) returns 4 using an assertion
    assert square(-2) == 4
    # Test case 4: Check if square(-3) returns 9 using an assertion
    assert square(-3) == 9
    # Test case 5: Check if square(0) returns 0 using an assertion
    assert square(0) == 0

# Call the function to run the test cases
test_square()

# Explanation:
# This script is a test script for the square function from calculator5.py. It tests the functionality of the square function.

# The import statement "from calculator5 import square" at the beginning of the script imports the square function from
# the calculator5.py module.

# The "test_square()" function contains multiple test cases for the square function. It uses assertions to check whether
# square(2) is equal to 4, whether square(3) is equal to 9, whether square(-2) is equal to 4,
# whether square(-3) is equal to 9, and whether square(0) is equal to 0. If any of these assertions fail, an assertion
# error will be raised.

# The script concludes by calling the "test_square()" function to run the test cases.
