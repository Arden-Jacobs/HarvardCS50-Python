import sys
from PIL import Image, ImageOps
import os

arg1, x1 = os.path.splitext(sys.argv[1])
arg2, x2 = os.path.splitext(sys.argv[2])

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if x1 != x2:
    sys.exit("Input and output have different extensions")
elif (".png" in ( x1 and x2)) or (".jpg" in (x1 and x2)) or ("jpeg" in (x1 and x2)):
    try:
        shirt = Image.open("shirt.png")
        size = shirt.size
        pic = Image.open(sys.argv[1])
        pic = ImageOps.fit(pic, size)
        pic.paste(shirt, shirt)
        pic.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
else:
    sys.exit("Invalid input")

