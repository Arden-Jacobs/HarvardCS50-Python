import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^(\d{1,2})(:[0-59]{2})? (AM|PM) to (\d{1,2})(:[0-59]{2})? (AM|PM)$",s):
        hr1, min1, noon1, hr2, min2, noon2 = matches.groups()
        if int(hr1) > 12 or int(hr2) > 12:
            raise ValueError
        time1 = time_format(hr1, min1, noon1)
        time2 = time_format(hr2, min2, noon2)
        return(time1+' to '+time2)
    else:
        raise ValueError


def time_format(hrs, mint, noon):
    hrs = int(hrs)
    if noon == "PM" and hrs != 12:
        hrs += 12
    elif noon == "AM" and hrs == 12:
        hrs = hrs - 12
    if mint == None:
        time = f"{hrs:02}:00"
    else:
        time = f"{hrs:02}{mint}"
    return time

if __name__ == "__main__":
    main()