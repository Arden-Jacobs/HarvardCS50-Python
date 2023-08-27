# test_calculator7.py - Test script for the square function from calculator7.py using pytest

# Import the pytest library
import pytest

# Import the square function from calculator7.py
from calculator7 import square

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

# Function to test input value as string (expecting TypeError)
def test_str():
    # Use pytest's "raises" context manager to check if TypeError is raised
    with pytest.raises(TypeError):
        square("cat")

# Explanation:
# This script is a test script for the square function from calculator7.py using the pytest library.
# It tests the functionality of the square function for different input values.

# The import statement "import pytest" at the beginning of the script imports the pytest library.

# The import statement "from calculator7 import square" imports the square function from the calculator7.py module.

# The "test_positive()" function contains test cases for positive input values. It uses assertions to check whether
# square(2) is equal to 4 and whether square(3) is equal to 9.

# The "test_negative()" function contains test cases for negative input values. It uses assertions to check whether
# square(-2) is equal to 4 and whether square(-3) is equal to 9.

# The "test_zero()" function contains a test case for the input value 0. It uses an assertion to check whether
# square(0) is equal to 0.

# The "test_str()" function contains a test case for an input value given as a string. It uses pytest's "raises"
# context manager to check if a TypeError is raised when attempting to square a string.

# The script concludes by calling the "test_positive()", "test_negative()", "test_zero()", and "test_str()" functions
# to run the test cases.
