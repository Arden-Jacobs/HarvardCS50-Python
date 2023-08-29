# test_plates.py - Test script for the is_valid function from plates.py using pytest

# Import the is_valid function from plates.py
from plates import is_valid

# Function to test valid license plates
def test_valid():
    # Test case: Check if is_valid("CS50") returns True using an assertion
    assert is_valid("CS50") == True
    # Test case: Check if is_valid("CSF50") returns True using an assertion
    assert is_valid("CSF50") == True

# Function to test invalid license plates
def test_invalid():
    # Test case: Check if is_valid("CS05") returns False using an assertion
    assert is_valid("CS05") == False
    # Test case: Check if is_valid("CS50F") returns False using an assertion
    assert is_valid("CS50F") == False

# Function to test license plates with only alphabetic characters or very few characters
def test_alpha():
    # Test case: Check if is_valid("CS") returns True using an assertion
    assert is_valid("CS") == True
    # Test case: Check if is_valid("hello") returns True using an assertion
    assert is_valid("hello") == True
    # Test case: Check if is_valid("w") returns False using an assertion
    assert is_valid("w") == False

# Function to test license plates with only numerical characters
def test_number():
    # Test case: Check if is_valid("520") returns False using an assertion
    assert is_valid("520") == False
    # Test case: Check if is_valid("5014") returns False using an assertion
    assert is_valid("5014") == False

# Function to test license plates with various lengths
def test_len():
    # Test case: Check if is_valid("") returns False using an assertion
    assert is_valid("") == False
    # Test case: Check if is_valid("hello world") returns False using an assertion
    assert is_valid("hello world") == False

# Function to test license plates containing non-alphanumeric characters
def test_alnum():
    # Test case: Check if is_valid("hi,.there") returns False using an assertion
    assert is_valid("hi,.there") == False
    # Test case: Check if is_valid("hi,.50") returns False using an assertion
    assert is_valid("hi,.50") == False

# Explanation:
# This script is a test script for the is_valid function from plates.py using the pytest library.
# It tests the functionality of the is_valid function for different license plate scenarios.

# The import statement "from plates import is_valid" at the beginning of the script imports the is_valid function
# from the plates.py module.

# Each test function contains test cases that use assertions to verify whether the output of the is_valid function
# matches the expected result for various license plate scenarios.
