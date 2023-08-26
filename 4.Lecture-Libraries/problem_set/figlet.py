# figlet.py - Generates stylized text using pyfiglet

# Import the Figlet class from the pyfiglet module, sys module for command-line arguments, and random module
import sys
import random
from pyfiglet import Figlet

# Create an instance of the Figlet class
figlet = Figlet()

# Get the list of available fonts from the Figlet instance
font_list = figlet.getFonts()

# Check for command-line arguments to determine font and text input
if len(sys.argv) == 3:
    if sys.argv[2] not in font_list:
        sys.exit("Invalid usage")
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        tet = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        # Render and print the stylized text using the specified font
        print(figlet.renderText(tet))
    else:
        sys.exit("Invalid usage")
elif len(sys.argv) == 1:
    tet = input("Input: ")
    # Generate a random number to select a font from the available fonts list
    num = random.randint(0, len(font_list) - 1)
    font = font_list[num]
    figlet.setFont(font=font)
    # Render and print the stylized text using the randomly selected font
    print(figlet.renderText(tet))
else:
    sys.exit("Invalid usage")

# Explanation:
# This script uses the pyfiglet module to generate stylized text using different fonts.

# The import statement "from pyfiglet import Figlet" at the beginning of the script imports the Figlet class
# from the pyfiglet module, which provides functionality for generating text art.

# An instance of the Figlet class is created using "figlet = Figlet()".

# The available font names are retrieved using "font_list = figlet.getFonts()".

# The script checks the command-line arguments to determine font and text input:
# - If there are exactly 3 arguments and the second argument is a valid font name, the specified font is used
#   to stylize the text input provided by the user.
# - If there is 1 argument (the script name), the user is prompted for text input, and a random font is selected
#   from the available fonts list to stylize the text.
# - If there are any other numbers of arguments, an error message is displayed and the script exits.

# The stylized text is rendered using the selected font and printed to the console using "print(figlet.renderText(tet))".
