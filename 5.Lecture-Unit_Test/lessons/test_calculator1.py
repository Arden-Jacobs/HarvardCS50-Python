# test_calculator1.py - Test script for the square function from calculator1.py

# Import the square function from calculator1.py
from calculator1 import square

# Main function to run the test cases
def main():
    # Call the test_square function to run the test cases
    test_square()

# Function to test the square function
def test_square():
    # Test case 1: Check if square(2) returns 4
    if square(2) != 4:
        print("2 squared was not 4")
    # Test case 2: Check if square(3) returns 9
    if square(3) != 9:
        print("3 squared was not 9")

# Check if the script is run directly
if __name__ == "__main__":
    # Call the main function to start the test
    main()

# Explanation:
# This script is a test script for the square function from calculator1.py. It tests the functionality of the square function.

# The import statement "from calculator1 import square" at the beginning of the script imports the square function from
# the calculator1.py module.

# The main function "main()" runs the test cases. It calls the "test_square()" function to execute the test cases.

# The "test_square()" function contains the test cases for the square function. It checks whether square(2) is equal to 4
# and whether square(3) is equal to 9. If any of these checks fail, an error message is printed.

# The "__name__ == '__main__':" check at the end of the script ensures that the test cases are executed only when the
# script is run directly, not when it's imported as a module.
