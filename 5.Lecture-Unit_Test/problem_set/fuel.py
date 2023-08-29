# fuel.py - Fraction to Percentage Converter with Gauge Levels

# Main function to take user input, convert a fraction to a percentage, and print the gauge result
def main():
    # Prompt the user for a fraction
    fraction = input("Enter a Fraction: ")
    # Convert the fraction to a percentage using the convert function
    percentage = convert(fraction)
    # Print the gauge result using the gauge function
    print(gauge(percentage))

# Function to convert a given fraction to a percentage
def convert(fraction):
    while True:
        # Find the position of the "/" character in the input fraction
        div = fraction.find("/")
        try:
            # Extract the numerator and denominator from the input fraction
            n1, n2 = int(fraction[0:div]), int(fraction[div + 1:])

            # Check if the denominator is non-positive and raise a ZeroDivisionError if needed
            if n2 <= 0:
                raise ZeroDivisionError
            # Check if the fraction is valid by comparing the numerator and denominator
            if n1 > n2:
                # If the fraction is invalid, prompt the user for another fraction
                fraction = input("Enter a Fraction: ")
                continue
            else:
                # Calculate and return the percentage based on the valid fraction
                return int((n1 / n2) * 100)
        except (ValueError, ZeroDivisionError):
            # Raise errors for invalid input formats or zero denominator
            raise

# Function to determine the gauge level based on the percentage
def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

# Check if the script is run directly
if __name__ == "__main__":
    # Call the main function to start the fraction to percentage conversion and gauge printing
    main()

# Explanation:
# This script prompts the user for a fraction, converts the fraction to a percentage using the convert function,
# and then determines the gauge level using the gauge function. The gauge result is then printed.

# The main function "main()" prompts the user for a fraction, calls the "convert()" function to convert it to a percentage,
# and calls the "gauge()" function to determine the gauge level based on the percentage. It then prints the gauge result.

# The "convert()" function takes the input fraction, extracts the numerator and denominator, and performs various checks to
# ensure the fraction is valid. It calculates the percentage and returns it.

# The "gauge()" function takes the percentage as input and determines the gauge level ("E" for low, "F" for high, or the
# percentage value) based on the input percentage.

# The "__name__ == '__main__':" check at the end of the script ensures that the main function is executed only when the
# script is run directly, not when it's imported as a module.
