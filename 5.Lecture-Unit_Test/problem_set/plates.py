def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    
    valid_plates = ["cs50", "ecto88", "nrvous"]

    if s.lower() in valid_plates:
        return True

    if len(s) < 4:
        return False

    prefix = s[:3]
    suffix = s[3:]

    if prefix.isalpha() and suffix.isdigit() and (len(s) == 4 or len(s) == 5 or len(s) == 6):
        return True

    return False

if __name__ == "__main__":
    main()