# extensions.py - Prompt User for a File Name and Determine File Type

# Prompt the user for a file name.
file_name = input("Enter file name: ")

# Normalize the file name by converting to lowercase.
file_name = file_name.lower()

# Determine the file type based on the normalized file name.
if ".gif" in file_name:
    print("image/gif")
elif ".jpg" in file_name or ".jpeg" in file_name:
    print("image/jpeg")
elif ".png" in file_name:
    print("image/png")
elif ".pdf" in file_name:
    print("application/pdf")
elif ".txt" in file_name:
    print("text/plain")
elif ".zip" in file_name:
    print("application/zip")
else:
    print("application/octet-stream")



# In this section, the code prompts the user for a file name and then normalizes the file name by converting it to
# lowercase. This normalization step ensures that the code handles file extensions in a case-insensitive manner.

# The program then uses a series of if and elif statements to determine the file type based on the normalized file
# name. If the normalized file name contains the substring ".gif", the program prints "image/gif".Similarly,
# for other common image formats (".jpg", ".jpeg", ".png"), the program prints the corresponding MIME type.
# If the file name contains ".pdf", ".txt", or ".zip", the program prints the appropriate MIME type.If none
# of the conditions match, the else statement prints "application/octet-stream", indicating an unknown file type.