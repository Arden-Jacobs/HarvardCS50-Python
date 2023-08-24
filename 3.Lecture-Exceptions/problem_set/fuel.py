# fuel.py - Fuel Gauge

# Define the main function
def main():
    # Call the get_int function to get a percentage value from the user
    x = get_int("")
    
    # Check the value of x and display the appropriate message
    if x <= 1:
        print("E")
    elif x >= 99:
        print("F")
    else:
        print(f"{x}%")

# Define the get_int function to get a valid fraction from the user and calculate the percentage
def get_int(prompt):
    while True:
        try:
            # Prompt the user for a fraction and split it into two parts
            prompt = input("Enter a Fraction: ")
            n1, n2 = prompt.split("/")
            n1, n2 = int(n1), int(n2)
            
            # Check if the fraction is valid and calculate the percentage
            if n1 > n2 or n2 == 0:
                prompt = input("Enter a Fraction: ")
            else:
                return round((n1 / n2) * 100)  # Calculate and return the percentage
        except (ValueError, ZeroDivisionError):
            pass

# Call the main function to start the program
main()



# Explanation:
# This code snippet introduces a program that simulates a fuel gauge. The user is prompted to enter a fraction, which
# represents the fuel level. The program calculates and displays the fuel level percentage or indicates "E" for empty
# or "F" for full.

# The main() function and the get_int() function are defined.

# Inside the main() function, the get_int() function is called to obtain a fuel level value from the user. The result
# is stored in the variable x.

# The program checks the value of x:
# - If x is less than or equal to 1, it indicates "E" for empty.
# - If x is greater than or equal to 99, it indicates "F" for full.
# - Otherwise, it displays the calculated fuel level as a percentage.

# The get_int() function prompts the user for a fraction input, splits it into two parts (n1 and n2), and converts
# them to integers. It then checks if the fraction is valid (n1 <= n2 and n2 is not 0) and calculates the percentage
# based on the given fraction. The percentage is calculated using the formula (n1/n2) * 100.

# The result is rounded using the round() function to display a whole number percentage.

# If the user provides invalid input (ValueError or ZeroDivisionError), the program continues to prompt for input.

# The overall behavior of the program is to simulate a fuel gauge by obtaining a fraction from the user, calculating
# the percentage, and displaying the appropriate message.
