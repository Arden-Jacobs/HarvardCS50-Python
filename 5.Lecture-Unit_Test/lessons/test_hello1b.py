# test_hello1b.py - Test script for the hello function from hello1.py

# Import the hello function from hello1.py
from hello1 import hello

# Function to test the hello function with the default argument
def test_default():
    # Test case: Check if hello() returns "hello, world" using an assertion
    assert hello() == "hello, world"

# Function to test the hello function with different arguments
def test_argument():
    # Loop through a list of names
    for name in ["Hermione", "Harry", "Ron"]:
        # Test each name: Check if hello(name) returns the expected greeting using an assertion
        assert hello(name) == f"hello, {name}"

# Explanation:
# This script is a test script for the hello function from hello1.py. It tests the functionality of the hello function.

# The import statement "from hello1 import hello" at the beginning of the script imports the hello function from
# the hello1.py module.

# The "test_default()" function contains a test case for the hello function with the default argument. It uses an
# assertion to check whether hello() returns "hello, world".

# The "test_argument()" function contains a test case for the hello function with different arguments. It loops through
# a list of names and checks whether the hello function returns the expected greetings using assertions.

# The script concludes by calling the "test_default()" and "test_argument()" functions to run the test cases.
