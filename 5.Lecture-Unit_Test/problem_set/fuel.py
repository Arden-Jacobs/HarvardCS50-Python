def main():
    fraction = input("Enter a Fraction: ")
    percentage = convert(fraction)
    gauge(percentage)


def convert(fraction):
    while True:
        try:
            # Prompt the user for a fraction and split it into two parts
            n1, n2 = fraction.split("/")
            n1, n2 = int(n1), int(n2)
            
            # Check if the fraction is valid and calculate the percentage
            if n1 > n2 or n2 == 0:
                fraction = input("Enter a Fraction: ")
            else:
                return round((n1 / n2) * 100)  # Calculate and return the percentage
        except (ValueError, ZeroDivisionError):
            pass


def gauge(percentage):
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")

if __name__ == "__main__":
    main()