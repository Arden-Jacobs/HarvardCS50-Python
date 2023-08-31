import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

arg = sys.argv[1]

if ".py" not in arg:
    sys.exit("Not a Python file")

count = 0
try:
    with open(arg) as file:
        for line in file:
            if line.strip() == "" or line.lstrip().startswith("# "):
                pass
            else:
                count += 1
    print(count)

except FileNotFoundError:
    sys.exit("File does not exist")