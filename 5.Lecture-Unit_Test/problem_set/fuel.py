# fuel.py - Script to convert a fraction to a percentage and represent it with a gauge

# Main function to take user input, convert the fraction to a percentage, and represent it with a gauge
def main():
    # Prompt the user for a fraction and call the convert function to calculate the percentage
    fraction = input("Enter a Fraction: ")
    percentage = convert(fraction)
    # Call the gauge function to represent the percentage with a gauge
    gauge(percentage)

# Function to convert a fraction to a percentage
def convert(fraction):
    while True:
        try:
            # Split the user-provided fraction into two parts
            n1, n2 = fraction.split("/")
            n1, n2 = int(n1), int(n2)
            
            # Check if the fraction is valid and calculate the percentage
            if n1 > n2 or n2 == 0:
                fraction = input("Enter a Fraction: ")
            else:
                # Calculate the percentage and return the rounded value
                return round((n1 / n2) * 100)
        except (ValueError, ZeroDivisionError):
            pass

# Function to represent the percentage with a gauge
def gauge(percentage):
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")

# Check if the script is run directly
if __name__ == "__main__":
    # Call the main function to start the conversion and gauge representation
    main()

# Explanation:
# This script prompts the user for a fraction, converts it to a percentage using the convert function,
# and then represents the percentage with a gauge using the gauge function.

# The main function "main()" prompts the user for a fraction and calls the "convert()" function to calculate
# the percentage. It then calls the "gauge()" function to represent the percentage using a gauge.

# The "convert()" function takes a fraction as input, splits it into two parts, and calculates the percentage.
# It checks if the fraction is valid and returns the calculated percentage as a rounded value.

# The "gauge()" function takes a percentage as input and prints "E" if the percentage is less than or equal to 1,
# "F" if the percentage is greater than or equal to 99, or the percentage value followed by "%" otherwise.

# The "__name__ == '__main__':" check at the end of the script ensures that the main function is executed only
# when the script is run directly, not when it's imported as a module.
