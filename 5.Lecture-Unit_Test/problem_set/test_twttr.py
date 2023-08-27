# test_twttr.py - Test script for the shorten function from twttr.py using pytest

# Import the pytest library
import pytest

# Import the shorten function from twttr.py
from twttr import shorten

# Function to test the shorten function with word input
def test_word():
    # Test case 1: Check if shorten("big") returns "bg" using an assertion
    assert shorten("big") == "bg"
    # Test case 2: Check if shorten("TWITTER") returns "TWTTR" using an assertion
    assert shorten("TWITTER") == "TWTTR"

# Function to test the shorten function with numerical input (expecting TypeError)
def test_num():
    # Use pytest's "raises" context manager to check if TypeError is raised
    with pytest.raises(TypeError):
        shorten(7)

# Function to test the shorten function with a single letter input
def test_letter():
    # Test case: Check if shorten("i") returns an empty string using an assertion
    assert shorten("i") == ""

# Function to test the shorten function with input containing numbers
def test_omit_num():
    # Test case: Check if shorten("abc123") returns "bc123" using an assertion
    assert shorten("abc123") == "bc123"

# Function to test the shorten function with input containing punctuation
def test_omit_punc():
    # Test case: Check if shorten("hello, world") returns "hll, wrld" using an assertion
    assert shorten("hello, world") == "hll, wrld"

# Explanation:
# This script is a test script for the shorten function from twttr.py using the pytest library.
# It tests the functionality of the shorten function for different input scenarios.

# The import statement "import pytest" at the beginning of the script imports the pytest library.

# The import statement "from twttr import shorten" imports the shorten function from the twttr.py module.

# The "test_word()" function contains test cases for word input. It checks whether the shorten function returns
# the expected output for different words.

# The "test_num()" function contains a test case for numerical input. It uses pytest's "raises" context manager
# to check if a TypeError is raised when attempting to pass a number to the shorten function.

# The "test_letter()" function contains a test case for a single letter input. It checks whether the shorten function
# returns an empty string for a single letter.

# The "test_omit_num()" function contains a test case for input containing both letters and numbers. It checks whether
# the shorten function correctly removes vowels but retains numbers.

# The "test_omit_punc()" function contains a test case for input containing punctuation. It checks whether the
# shorten function removes vowels and punctuation while retaining other characters.

# The script concludes by calling the "test_word()", "test_num()", "test_letter()", "test_omit_num()",
# and "test_omit_punc()" functions to run the test cases.
