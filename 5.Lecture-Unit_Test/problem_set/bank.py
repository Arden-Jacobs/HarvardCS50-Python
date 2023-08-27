def main():
    # Prompt the user for a greeting.
    greeting = input("Enter Greeting: ")
    print(value(greeting))


def value(greeting):
    # Normalize the greeting by converting to lowercase.
    greeting = greeting.lower()

    # Determine the bank fee based on the normalized greeting.
    if "hello" in greeting:
        return("$0")
    elif "h" == greeting[0]:
        return("$20")
    else:
        return("$100")


if __name__ == "__main__":
    main()