import re

# playback.py - Regular Expression Substitution

# Import the `re` module to work with regular expressions.

# Prompt the user for input and store it in the variable `prompt`.
prompt = input("Enter something you would like to echo: ")

# Use the `re.sub()` function to replace all occurrences of one or more whitespace characters with '...'
#   in the content of the `prompt` variable.
prompt = re.sub(r'\s+', '...', prompt)

# Print the modified content of the `prompt` variable.
print(prompt)



# In this section, the program imports the re module to work with regular expressions. The program then prompts
# the user for input using the input() function and stores it in the variable prompt. The re.sub() function is
# used to replace all occurrences of one or more whitespace characters with '...' in the content of the prompt
# variable. The modified content of the prompt variable is printed using the print() function.