# test_bank.py - Test script for the value function from bank.py using pytest

# Import the value function from bank.py
from bank import value

# Function to test the value function with a greeting containing only alphabetic characters
def test_alpha():
    # Test case: Check if value("hello") returns 0 using an assertion
    assert value("hello") == 0

# Function to test the value function with a numerical input
def test_num():
    # Test case: Check if value("5") returns 100 using an assertion
    assert value("5") == 100

# Function to test the value function with a greeting starting with "hi"
def test_hi():
    # Test case: Check if value("hi") returns 20 using an assertion
    assert value("hi") == 20

# Function to test the value function with a greeting containing alphabetic characters and other characters
def test_omit_alpha():
    # Test case: Check if value("hello, world") returns 0 using an assertion
    assert value("hello, world") == 0

# Function to test the value function with a greeting in different case
def test_case():
    # Test case: Check if value("HELLO") returns 0 using an assertion
    assert value("HELLO") == 0

# Explanation:
# This script is a test script for the value function from bank.py using the pytest library.
# It tests the functionality of the value function for different input scenarios.

# The import statement "from bank import value" at the beginning of the script imports the value function
# from the bank.py module.

# The "test_alpha()" function contains a test case for a greeting with only alphabetic characters. It checks whether
# the value function correctly returns 0 when "hello" is provided.

# The "test_num()" function contains a test case for numerical input. It checks whether the value function correctly
# returns 100 when "5" is provided.

# The "test_hi()" function contains a test case for a greeting starting with "hi". It checks whether the value function
# correctly returns 20 when "hi" is provided.

# The "test_omit_alpha()" function contains a test case for a greeting containing alphabetic characters and other characters.
# It checks whether the value function correctly returns 0 when "hello, world" is provided.

# The "test_case()" function contains a test case for a greeting provided in different case (uppercase). It checks whether
# the value function correctly returns 0 when "HELLO" is provided.

# Each test case uses an assertion to verify whether the output of the value function matches the expected result.
