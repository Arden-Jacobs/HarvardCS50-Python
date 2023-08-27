def main():
    npt = input("Input: ")
    output = shorten(npt)
    print(output)

def shorten(word):
    vowels = "aeiouAEIOU"
    output = ""

    for char in word:
        if char not in vowels:
            output += char

    return output

if __name__ == "__main__":
    main()