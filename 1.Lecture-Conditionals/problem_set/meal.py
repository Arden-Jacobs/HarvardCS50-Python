# meal.py - Determine Meal Time Based on User Input

def main():
    """
    Main function to prompt the user for input and determine meal times.
    """
    # Prompt user for input.
    time = input("Enter the time of the day: ")

    # Convert the input into float.
    mod_time = convert(time)

    # Check the meal times based on the modified time.
    if 7.0 <= mod_time <= 8.0:
        print("breakfast time")
    elif 12.00 <= mod_time <= 13.00:
        print("lunch time")
    elif 18.00 <= mod_time <= 19.00:
        print("dinner time")


def convert(time):
    """
    Convert input time in HH:MM format to decimal representation of time.
    Args:
        time (str): Input time in HH:MM format.
    Returns:
        float: Decimal representation of time.
    """
    # Split the input time into hours and minutes.
    # The split() method is used on the time_str string to split it into a list of strings
    #   based on the colon (":") separator
    # Then the map() method converts the list of string representing hours and minutes into integer values
    #   using int() while looping. So, with the example "12:30", it will result in the integers 12 and 30
    hours, minutes = map(int, time.split(':'))

    # Convert hours and minutes to decimal time.
    return hours + (minutes / 60)


if __name__ == "__main__":
    main()



# In this section, the code defines a main() function that prompts the user for the time of the day and determines
# the corresponding meal time based on the input time. The code also defines a convert() function to convert the
# input time from HH:MM format to a decimal representation of time.

# The convert() function uses the split(':') method to split the input time into hours and minutes and then converts
# these values to integers using the map(int, ...) function. It then calculates the decimal representation of time
# by adding hours and dividing minutes by 60.

# The main() function uses the convert() function to convert the user input into decimal time.It then checks 
# if the modified time falls within the ranges for breakfast, lunch, or dinner, 
# and prints the corresponding meal time.

# The if __name__ == "__main__": block ensures that the main() function is executed when the script is run 
# directly and not when it's imported as a module.