from datetime import date
import inflect
import sys

p = inflect.engine()


def main():
    date = get_mintues(input("Date of Birth: "))
    print(f"{convert(date)}")


def get_mintues(s):
    try:
        dob = date.fromisoformat(s)
        current = date.today()
        day = current - dob
        return (int(day.days * 24 * 60))
    except (ValueError, TypeError):
        sys.exit("Invalid date")


def convert(d):
    words = p.number_to_words(d, andword="")
    output = words + " minutes"
    return output.capitalize()


if __name__ == "__main__":
    main()