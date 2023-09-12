from datetime import date
import inflect
import sys


def main():
    date = get_mintues(input("Date: "))
    print(convert(date)capitalize())
    

def get_mintues(s):
    try:
        dob = date.fromisoformat(s)
        current = date.today()
        day = current - dob
        return(day.days*24*60)
    except (ValueError, TypeError):
        sys.exit("Invalid date")

def convert(d):
    p = inflect.engine()
    words = p.number_to_words(d, andword="")
    return (words + " mintues")


if __name__ == "__main__":
    main()
