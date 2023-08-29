# costumes.py - Opens and saves binary image files using the Python Imaging Library (PIL)

# Import the sys module to access command-line arguments and the PIL module for image processing
import sys
from PIL import Image

# Create an empty list to store the opened images
images = []

# Loop through the command-line arguments (image file paths) and open each image
for arg in sys.argv[1:]:
    image = Image.open(arg)  # Open the image using PIL's Image.open() method
    images.append(image)  # Append the opened image to the list

# Save the images as a GIF file with animation
images[0].save(
    "costumes.gif",                  # Save the GIF as "costumes.gif"
    save_all=True,                   # Save all frames (images)
    append_images=[images[1]],      # Append the second image as a frame
    duration=200,                    # Set the frame duration to 200 milliseconds
    loop=0                           # Set the animation loop count to 0 (infinite loop)
)

# Explanation:
# This script opens and saves binary image files using the Python Imaging Library (PIL).
# It imports the sys module to access command-line arguments and the PIL module for image processing.

# The main part of the script iterates through the command-line arguments (image file paths) using a for loop.
# It opens each image using PIL's Image.open() method and appends the opened image to the "images" list.

# After opening the images, the script saves them as a GIF animation using the save() method of the first image.
# The save_all parameter is set to True to save all frames (images), and the append_images parameter is used to
# append the second image as a frame in the animation. The duration parameter sets the time each frame is displayed,
# and the loop parameter sets the number of animation loops (0 for infinite loop).

# The result is a GIF animation saved as "costumes.gif" that combines the opened images into an animation.
