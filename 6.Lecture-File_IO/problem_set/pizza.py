import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

arg = sys.argv[1]

if ".csv" not in arg:
    sys.exit("Not a CSV file")


try:
    table = []
    with open(arg) as file:
        reader = csv.DictReader(file)
        for row in reader:
            table.append(row)
        print(tabulate(table, headers="keys",tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File does not exist")
