import re


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    if re.search(r"^([0-9]{1,3}\.)[0-9]{1,3}\.[0-9]{1,3}\.([0-9]{1,3})$", ip):
        # If the conditions are met, print "Valid."
        temp = ip.split(".")
        count = 0
        for i in temp:
            if i <= "255" and i >= "0":
                count += 1
        if count == 4:
            return True
        else:
            return False
    else:
        # If the conditions are not met, print "Invalid."
        return False

if __name__ == "__main__":
    main()