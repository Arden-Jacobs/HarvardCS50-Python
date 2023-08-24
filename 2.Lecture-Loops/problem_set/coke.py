# coke.py - Simulate a vending machine for buying a bottle of coke

def main():
    # Bottle cost in cents
    bottle_cost = 50
    amount_due = bottle_cost

    # Prompt user to insert coins
    while amount_due > 0:
        print("Amount Due: {}".format(amount_due))
        coin = input("Insert coin (25c, 10c, 5c): ")
        coin = int(coin)

        # Check if the coin value is valid
        if coin == 25 or coin == 10 or coin == 5:
            amount_due -= coin

        # Display change owed if the amount is fully paid
        if amount_due == 0:
            print("Change Owed: {}".format(amount_due))

        # Display change owed as negative if overpaid
        if amount_due < 0:
            print("Change Owed: {}".format(-amount_due))

main()



# Explanation:
# This code simulates a vending machine for buying a bottle of coke for 50 cents. The machine only accepts coins
# of 25 cents, 10 cents, and 5 cents.

# The main function handles the simulation. It initializes the bottle_cost variable to 50 cents and the amount_due
# variable to the same value initially. The loop keeps running as long as there is an outstanding amount due.

# Within the loop, the program prompts the user for a coin input. The input is converted to an integer, and if
# the value is 25, 10, or 5, it deducts the coin value from the amount_due. If the amount_due reaches 0, it
# indicates that the full amount has been paid and prints "Change Owed: 0". If the amount_due goes below 0,
# it indicates an overpayment and prints "Change Owed" as a negative value.
