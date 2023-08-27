# test_hello1a.py - Test script for the hello function from hello1.py

# Import the hello function from hello1.py
from hello1 import hello

# Function to test the hello function with the default argument
def test_default():
    # Test case: Check if hello() returns "hello, world" using an assertion
    assert hello() == "hello, world"

# Function to test the hello function with an argument
def test_argument():
    # Test case: Check if hello("David") returns "hello, David" using an assertion
    assert hello("David") == "hello, David"

# Explanation:
# This script is a test script for the hello function from hello1.py. It tests the functionality of the hello function.

# The import statement "from hello1 import hello" at the beginning of the script imports the hello function from
# the hello1.py module.

# The "test_default()" function contains a test case for the hello function with the default argument. It uses an
# assertion to check whether hello() returns "hello, world".

# The "test_argument()" function contains a test case for the hello function with an argument. It uses an assertion to
# check whether hello("David") returns "hello, David".

# The script concludes by calling the "test_default()" and "test_argument()" functions to run the test cases.
