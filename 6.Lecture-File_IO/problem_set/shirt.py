# File: shirt.py
# Description: Combines a shirt image with a user-provided image and saves the result.

# Import necessary modules: sys for command-line arguments, PIL for image processing, and os for file extension manipulation.
import sys
from PIL import Image, ImageOps
import os

# Extract the filenames and extensions from the command-line arguments.
arg1, x1 = os.path.splitext(sys.argv[1])
arg2, x2 = os.path.splitext(sys.argv[2])

# Check the number of command-line arguments.
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

# Check if the input and output file extensions match.
if x1 != x2:
    sys.exit("Input and output have different extensions")

# Check if the extensions are valid (png, jpg, or jpeg).
elif x1 not in (".png", ".jpg", ".jpeg") or x2 not in (".png", ".jpg", ".jpeg"):
    sys.exit("Invalid input")

try:
    # Open the "shirt.png" image to be combined with the user's image.
    shirt = Image.open("shirt.png")
    # Get the size (dimensions) of the shirt image.
    size = shirt.size
    # Open the user-provided image specified in the first command-line argument.
    pic = Image.open(sys.argv[1])
    # Fit the user's image to the size of the shirt image.
    pic = ImageOps.fit(pic, size)
    # Paste the shirt image onto the user's image.
    pic.paste(shirt, shirt)
    # Save the combined image to the file specified in the second command-line argument.
    pic.save(sys.argv[2])

except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

# Explanation:

# This script combines a user-provided image with a shirt image and saves the result.
# It uses the `sys` module for command-line arguments, the `PIL` (Pillow) library for image processing, and the `os` module to extract file extensions.

# The script begins by extracting the filenames and extensions from the command-line arguments.
# It checks the number of command-line arguments and exits with an error message if there are too few or too many.

# It also checks if the extensions of the input and output files match. If they don't match, it exits with an error message.

# Next, it checks if the extensions are valid, which in this case are ".png," ".jpg," or ".jpeg."

# Inside the `try` block, the script opens the "shirt.png" image, which is intended to be combined with the user's image.
# It obtains the size (dimensions) of the shirt image.

# Then, it opens the user-provided image specified in the first command-line argument.

# The user's image is fitted to the size of the shirt image using `ImageOps.fit()` to ensure they have the same dimensions.

# The shirt image is pasted onto the user's image.

# Finally, the combined image is saved to the file specified in the second command-line argument.

# If the specified input file does not exist, the script displays an error message and exits.

# In summary, this script provides a way to create composite images by combining a shirt image with a user-provided image and saving the result.
