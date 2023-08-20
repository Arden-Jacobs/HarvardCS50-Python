# faces.py - String Conversion using Replace

def main():
    """
    The main function that handles user input and calls the convert function.
    """
    # Prompt the user for input and store it in the variable `prompt`.
    prompt = input("Enter a string containing ':)' or ':(': ")
    
    # Call the `convert()` function with the input string and print the result.
    print(convert(prompt))

def convert(x):
    """
    Converts occurrences of ":)" and ":(" in the provided string to their respective emojis.
    
    :param x: The input string to be converted.
    :return: The input string with ":)" replaced by "🙂" and ":(" replaced by "🙁".
    """
    if (":)" and ":(" in x):
        x = x.replace(":)", "🙂")
        x = x.replace(":(", "🙁")
        return x
    
    if (":)" in x):
        return x.replace(":)", "🙂")
    
    if (":(" in x):
        return x.replace(":(", "🙁")

# Call the `main()` function to start the program.
main()



# In this section, we're introducing string conversion using the replace() method. The main() function handles
# user input and calls the convert() function. The convert() function takes an input string, searches for
# occurrences of ":)" and ":(" and replaces them with corresponding emojis. The docstrings provide explanations
# for both functions. The program starts by calling the main() function, which prompts the user for input,
# calls the convert() function, and displays the result.