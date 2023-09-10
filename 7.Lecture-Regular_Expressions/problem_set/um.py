import re


def main():
    print(count(input("Text: ")))


def count(s):
    regex = r"\bum\b"
    match = re.findall(regex,s,re.IGNORECASE)
    return (len(match))


if __name__ == "__main__":
    main()
