# outdated.py - Date Formatting Program
# Implement a program that prompts the user for a date, anno Domini, in month-day-year order,
# formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any 
# of the values in the list below:

# A list of month names
month = [
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"
]

# Main function to prompt the user for a date
def main():
    """
    Prompts the user for a date and processes it based on the format.
    """
    # Prompt the user for a date in month-day-year order
    date = input("Date: ").strip()

    # Check the format of the input date and process accordingly
    if "/" in date:
        # If date is in month/day/year format, call the check_digit function
        date = check_digit(date)
    elif " " in date:
        # If date is in month day, year format, call the check_alpha function
        date = check_alpha(date)

# Function to process date in month/day/year format
def check_digit(date):
    """
    Process date in month/day/year format and print in yyyy-mm-dd format.
    """
    while True:
        try:
            # Split the date into month, day, and year components
            mon, day, year = date.split("/")
            mon, day, year = int(mon), int(day), int(year)
            
            # Check if the month and day are within valid ranges
            if mon > 12 or day > 31:
                date = input("Date: ")
            else:
                # Print the formatted date in yyyy-mm-dd format
                print(f"{year}-{mon:02}-{day:02}")
                return (mon, day, year)
        except ValueError:
            pass

# Function to process date in month day, year format
def check_alpha(date):
    """
    Process date in month day, year format and print in yyyy-mm-dd format.
    """
    while True:
        try:
            # Split the date into month, day, and year components
            if date[0].isalpha():
                mon, day, year = date.split(" ")
                mon = mon.title()
                
                # Remove comma if present in day
                if "," in day:
                    day = day.replace(",", "")
                day, year = int(day), int(year)
                
                # Check if the month is valid and day is within range
                if mon not in month or day > 31:
                    date = input("Date: ")
                
                # Convert month to numerical value using index
                mon = month.index(mon.title()) + 1
                
                # Print the formatted date in yyyy-mm-dd format
                print(f"{year}-{mon:02}-{day:02}")
                return (mon, day, year)
            else:
                date = input("Date: ")
        except ValueError:
            return

# Call the main function to start the program
main()



# Explanation:
# This code snippet prompts the user for a date in either the "month/day/year" or "month day, year"
# format, and then processes and prints the date in the "yyyy-mm-dd" format.

# The month list contains the names of the months, and the main() function is responsible for interacting
# with the user. Depending on the format of the input date, the code calls either the check_digit()
# or check_alpha() function to handle the date processing.

# The check_digit() function handles the date format "month/day/year". It splits the input into
# components, checks the validity of the month and day, and then prints the formatted date.

# The check_alpha() function handles the date format "month day, year". It checks the validity of the
# month and day, converts the month name to a numerical value, and then prints the formatted date.
