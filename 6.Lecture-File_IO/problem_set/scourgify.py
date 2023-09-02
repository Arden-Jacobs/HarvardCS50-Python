import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

arg = sys.argv[1]

if ".csv" not in arg:
        sys.exit("Not a CSV file")


try:
    with open(arg) as main:
        reader = csv.DictReader(main)
        with open(sys.argv[2],'w') as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in reader:
                #  print(row['name'].split(", "))
                lname ,f_name = row['name'].split(", ")
                house = row['house']
                writer.writerow({"first": f_name, "last":  lname, "house": house})

except FileNotFoundError:
     sys.exit(f"Could not read {sys.argv[1]}")