from validator_collection import checkers

def main():
    print(validator(input("What's your email address? ")))


def validator(s):
    if _ := checkers.is_email(s):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()