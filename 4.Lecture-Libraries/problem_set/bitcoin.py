import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

n = float(0)

while True:
    try:
        n = float(sys.argv[1])
        break
    except ValueError:
        sys.exit("Command-line argument is not a number")


try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    json_object = response.json()
    bitcoin = json_object["bpi"]["USD"]["rate_float"]
    rate = n * bitcoin
    print(f"${rate:,.4f}")

except requests.RequestException:
    sys.exit(requests.RequestException)