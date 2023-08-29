# test_fuel.py - Test script for the convert and gauge functions from fuel.py using pytest

# Import the convert and gauge functions from fuel.py and the pytest library
from fuel import convert, gauge
import pytest

# Test function to check for conversion errors (invalid fraction inputs)
def test_convert_error():
    # Test case: Check if ValueError is raised for invalid fraction "asd"
    with pytest.raises(ValueError):
        convert("asd")
    # Test case: Check if ValueError is raised for invalid fraction "a/b"
    with pytest.raises(ValueError):
        convert("a/b")
    # Test case: Check if ZeroDivisionError is raised for fraction "5/0"
    with pytest.raises(ZeroDivisionError):
        convert("5/0")

# Test function to test the convert function for valid fraction conversions
def test_convert():
    # Test case: Check if convert("1/100") returns 1 using an assertion
    assert convert("1/100") == 1
    # Test case: Check if convert("25/100") returns 25 using an assertion
    assert convert("25/100") == 25
    # Test case: Check if convert("50/100") returns 50 using an assertion
    assert convert("50/100") == 50
    # Test case: Check if convert("75/100") returns 75 using an assertion
    assert convert("75/100") == 75
    # Test case: Check if convert("99/100") returns 99 using an assertion
    assert convert("99/100") == 99

# Test function to test the gauge function for different percentage values
def test_gauge():
    # Test case: Check if gauge(1) returns "E" using an assertion
    assert gauge(1) == "E"
    # Test case: Check if gauge(25) returns "25%" using an assertion
    assert gauge(25) == "25%"
    # Test case: Check if gauge(50) returns "50%" using an assertion
    assert gauge(50) == "50%"
    # Test case: Check if gauge(75) returns "75%" using an assertion
    assert gauge(75) == "75%"
    # Test case: Check if gauge(99) returns "F" using an assertion
    assert gauge(99) == "F"

# Explanation:
# This script is a test script for the convert and gauge functions from fuel.py using the pytest library.
# It tests the functionality of the convert and gauge functions for different fraction and percentage scenarios.

# The import statements "from fuel import convert, gauge" and "import pytest" at the beginning of the script import
# the convert and gauge functions from fuel.py and the pytest library, respectively.

# The test_convert_error function contains test cases to check if the convert function raises the expected errors
# for invalid fraction inputs. It uses assertions and the pytest.raises context manager.

# The test_convert function contains test cases to check if the convert function correctly converts valid fractions
# to percentages and returns the expected results. It uses assertions to compare the actual and expected outputs.

# The test_gauge function contains test cases to check if the gauge function correctly determines the gauge level
# based on the percentage input and returns the expected gauge values. It uses assertions to compare the actual
# and expected outputs.
