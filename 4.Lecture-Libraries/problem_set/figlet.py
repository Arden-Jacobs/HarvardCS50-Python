from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

font_list = figlet.getFonts()
if len(sys.argv) == 3:
    if sys.argv[2] not in font_list:
        sys.exit("Invalid usage")
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        tet = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(tet))
    else:
        sys.exit("Invalid usage")
elif len(sys.argv) == 1:
    tet = input("Input: ")
    num = random.randint(0, 424)
    font = font_list[num]
    figlet.setFont(font=font)
    print(figlet.renderText(tet))
else:
    sys.exit("Invalid usage")

