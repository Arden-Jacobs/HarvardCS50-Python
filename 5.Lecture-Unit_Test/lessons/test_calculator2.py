# test_calculator2.py - Test script for the square function from calculator2.py

# Import the square function from calculator2.py
from calculator2 import square

# Main function to run the test cases
def main():
    # Call the test_square function to run the test cases
    test_square()

# Function to test the square function using assertions
def test_square():
    # Test case 1: Check if square(2) returns 4 using an assertion
    assert square(2) == 4
    # Test case 2: Check if square(3) returns 9 using an assertion
    assert square(3) == 9

# Check if the script is run directly
if __name__ == "__main__":
    # Call the main function to start the test
    main()

# Explanation:
# This script is a test script for the square function from calculator2.py. It tests the functionality of the square function.

# The import statement "from calculator2 import square" at the beginning of the script imports the square function from
# the calculator2.py module.

# The main function "main()" runs the test cases. It calls the "test_square()" function to execute the test cases.

# The "test_square()" function contains the test cases for the square function. It uses assertions to check whether
# square(2) is equal to 4 and whether square(3) is equal to 9. If any of these assertions fail, an assertion error
# will be raised.

# The "__name__ == '__main__':" check at the end of the script ensures that the test cases are executed only when the
# script is run directly, not when it's imported as a module.
