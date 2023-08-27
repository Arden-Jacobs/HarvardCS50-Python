# test_calculator3.py - Test script for the square function from calculator3.py

# Import the square function from calculator3.py
from calculator3 import square

# Main function to run the test cases
def main():
    # Call the test_square function to run the test cases
    test_square()

# Function to test the square function using try-except blocks
def test_square():
    # Test case 1: Check if square(2) returns 4 using a try-except block
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
    # Test case 2: Check if square(3) returns 9 using a try-except block
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")

# Check if the script is run directly
if __name__ == "__main__":
    # Call the main function to start the test
    main()

# Explanation:
# This script is a test script for the square function from calculator3.py. It tests the functionality of the square function.

# The import statement "from calculator3 import square" at the beginning of the script imports the square function from
# the calculator3.py module.

# The main function "main()" runs the test cases. It calls the "test_square()" function to execute the test cases.

# The "test_square()" function contains the test cases for the square function. It uses try-except blocks to check
# whether square(2) is equal to 4 and whether square(3) is equal to 9. If any of these assertions fail, an error
# message will be printed.

# The "__name__ == '__main__':" check at the end of the script ensures that the test cases are executed only when the
# script is run directly, not when it's imported as a module.
