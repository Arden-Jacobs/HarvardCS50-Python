# tip.py - Calculate Tip Amount

def main():
    """
    The main function that handles user input and calculates the tip amount.
    """
    # Prompt the user for the meal cost and tip percentage, and convert them to floats.
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    
    # Calculate the tip amount.
    tip = dollars * percent
    
    # Print the calculated tip amount using an f-string.
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    """
    Convert a string with a dollar sign to a float.
    
    :param d: The string containing the dollar amount.
    :return: The corresponding float value.
    """
    if '$' in d:
        d = d.replace('$', '')
        return float(d)
    return float(d)

def percent_to_float(p):
    """
    Convert a string with a percentage sign to a float.
    
    :param p: The string containing the percentage.
    :return: The corresponding float value.
    """
    if '%' in p:
        p = p.replace('%', '')
        p = float(p)
        p = p / 100.00
        return p

# Call the `main()` function to start the program.
main()



# In this section, the program calculates the tip amount based on the meal cost and the desired tip percentage.
# The main() function handles user input and calculation. The dollars_to_float() function converts a string with
# a dollar sign to a float. The percent_to_float() function converts a string with a percentage sign to a float.
# The program starts by calling the main() function, which prompts the user for input, performs the necessary
#     calculations, and displays the calculated tip amount.