# File Name: test_working.py

# Description: This script contains test cases for the 'convert' function in the 'working' module.
# The 'convert' function is designed to convert time ranges from a specific format to a standardized format.

# Import necessary modules: convert from the 'working' module and pytest for testing.

from working import convert
import pytest

# Define the 'test_format_error' function to test the handling of format errors.
def test_format_error():
    # Test case 1: An input with incorrect time range format, "09:00 AM - 17:00 PM," should raise a ValueError.
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")

    # Test case 2: An input with incorrect time range format, "9 AM - 5 PM," should raise a ValueError.
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

# Define the 'test_incorrect_time_format' function to test the handling of incorrect time formats.
def test_incorrect_time_format():
    # Test case 1: An input with invalid hours and minutes, "09:90 AM - 17:70 PM," should raise a ValueError.
    with pytest.raises(ValueError):
        convert("09:90 AM - 17:70 PM")

    # Test case 2: An input with hours exceeding 12, "13 AM to 27 PM," should raise a ValueError.
    with pytest.raises(ValueError):
        convert("13 AM to 27 PM")

# Define the 'test_correct_format' function to test the conversion of valid time ranges.
def test_correct_format():
    # Test case 1: A valid input with AM and PM, "9 AM to 5 PM," should be converted to "09:00 to 17:00."
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

    # Test case 2: A valid input with hours and minutes, "9:00 AM to 5:00 PM," should be converted to "09:00 to 17:00."
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

    # Test case 3: A valid input with PM to AM transition, "10 PM to 8 AM," should be converted to "22:00 to 08:00."
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"

    # Test case 4: A valid input with hours and minutes, "10:30 PM to 8:50 AM," should be converted to "22:30 to 08:50."
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

# Define the 'test_noon_format' function to test the conversion of time ranges with noon.
def test_noon_format():
    # Test case 1: A valid input with noon, "12 AM to 12 PM," should be converted to "00:00 to 12:00."
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

    # Test case 2: A valid input with noon and minutes, "12:30 AM to 12:50 PM," should be converted to "00:30 to 12:50."
    assert convert("12:30 AM to 12:50 PM") == "00:30 to 12:50"

# Explanation:

# Description: In this script, we have a collection of test cases for the 'convert' function, which is located in the 'working' module.
# The purpose of these tests is to verify that the 'convert' function correctly converts time ranges from various formats to a standardized format.

# We start by importing the 'convert' function from the 'working' module and the 'pytest' library for testing.

# The script defines four test functions:

# - 'test_format_error': This function tests the handling of format errors. It checks if the 'convert' function correctly raises
#   'ValueError' when given inputs with incorrect time range formats.

# - 'test_incorrect_time_format': This function tests the handling of incorrect time formats. It checks if the 'convert' function
#   correctly raises 'ValueError' when given inputs with invalid hours and minutes.

# - 'test_correct_format': This function tests the conversion of valid time ranges. It verifies that the 'convert' function correctly
#   converts valid inputs to the expected standardized format.

# - 'test_noon_format': This function tests the conversion of time ranges with noon. It checks if the 'convert' function correctly
#   handles time ranges that involve noon.

# Each test case includes assertions using 'pytest.raises' to check if the 'convert' function behaves as expected and returns the
# correct results. If the function raises a 'ValueError' or returns the correct converted format, the test cases pass.

# These test cases ensure that the 'convert' function accurately converts time ranges from various formats to a standardized format
# and handles format errors and incorrect time formats appropriately.
