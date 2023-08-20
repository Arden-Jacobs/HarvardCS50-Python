# bank.py - Prompt User for a Greeting and Determine Bank Fee

# Prompt the user for a greeting.
greeting = input("Enter Greeting: ")

# Normalize the greeting by converting to lowercase.
greeting = greeting.lower()

# Determine the bank fee based on the normalized greeting.
if "hello" in greeting:
    print("$0")
elif "h" == greeting[0]:
    print("$20")
else:
    print("$100")



# In this section, the code prompts the user for a greeting and then normalizes the greeting by converting it to
# lowercase. This normalization step ensures that the code handles greetings in a case-insensitive manner.

# The program then uses an if statement with multiple conditions to determine the bank fee based on the normalized
# greeting. The first condition, if "hello" in greeting:, checks if the word "hello" is present in the normalized
# greeting. If it is, the bank fee is "$0". The second condition, elif "h" == greeting[0]:, checks if the
# first character of the normalized greeting is "h". If it is, the bank fee is "$20".
# If none of the conditions match,the else statement prints a bank fee of "$100".