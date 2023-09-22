from datetime import date
import csv
import sys


def main():
    """
    Main function to run the financial tracking app.

    This function orchestrates the entire financial tracking process.
    It retrieves income and expense data, calculates totals, and displays results.

    Returns:
        None
    """
    try:
        # write_income_header()
        # write_expense_header()

        income_array = get_income()
        expense_array = get_expense()

        income_total = get_total(income_array)
        expense_total = get_total(expense_array)
        print(f"Total Income: {income_total}")
        print(f"Total Expenses: {expense_total}")

        if expense_total and income_total != None:
            net_income = income_total - expense_total
            print(f"Net Income: {net_income}")

        expense_category = expenses_by_category(expense_array)
        display_expenses_by_category(expense_category)
    except ValueError as e:
        sys.exit(f"ValueError: {e}")


def income_journal(**kwargs):
    """
    Record income entries.

    Args:
        **kwargs: Variable keyword arguments containing the income entry details.
            - date (str): The date of the income entry.
            - item (str): The name of the item.
            - source (str): The source of the income.
            - amount (int): The amount of income.

    Returns:
        dict: A dictionary containing the income entry details.
    """

    return kwargs


def expenses_journal(**kwargs):
    """
    Record expense entries.

    Args:
        **kwargs: Variable keyword arguments containing the expense entry details.
            - date (str): The date of the expense entry.
            - item (str): The name of the item.
            - supplier (str): The supplier of the item.
            - amount (int): The amount of the expense.
            - category (str): The category of the expense.

    Returns:
        dict: A dictionary containing the expense entry details.
    """

    return kwargs


def get_income():
    """
    Retrieve income entries.

    Returns:
        list: A list of dictionaries containing income entry details.
    """

    today_date = date.today()
    income = ["Income Statement"]
    while True:
        try:
            if input("Would you like to create a new Income entery (Y or N): ").strip().upper() == "Y":
                item = input("Enter item name: ").strip().capitalize()
                source = input("Enter source name: ").strip().capitalize()
                amount = int(input("Enter amount: ").strip())
                income.append(income_journal(date=f"{today_date}", item=item, source=source, amount=amount))
                write_income_enteries(today_date, item, source, amount)
            else:
                break
        except (ValueError,TypeError) as e:
            sys.exit(f"Error: {e}")
    return income


def get_expense():
    """
    Retrieve expense entries.

    Returns:
        list: A list of dictionaries containing expense entry details.
    """

    today_date = date.today()
    expense = ["Expense Statement"]
    while True:
        try:
            if input("Would you like to create a new Expense entry (Y or N): ").strip().upper() == "Y":
                item = input("Enter item name: ").strip().capitalize()
                supplier = input("Enter supplier name: ").strip().capitalize()
                amount = int(input("Enter amount: ").strip())
                category = input("Enter expense category: ").strip().capitalize()
                expense.append(expenses_journal(date=today_date, item=item, supplier=supplier, amount=amount, category=category))
                write_expense_enteries(today_date, item, supplier, amount, category)
            else:
                break
        except (ValueError,TypeError) as e:
            sys.exit(f"Error: {e}")
    return expense


def get_total(data):
    """
    Calculate the total amount for a given list of data.

    Args:
        data (list): A list of dictionaries containing financial data.

    Returns:
        int: The total amount.
    """

    total = 0
    try:
        for i in range(len(data)):
            if i != 0:
                for k,v in data[i].items():
                    if k == 'amount':
                        total += int(v)
        return total
    except (ValueError,TypeError) as e:
        sys.exit(f"Error: {e}")


def write_income_header():
    """
    Write the header for the income CSV file.

    Returns:
        None
    """

    with open("Income_Journal.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "item", "source", "amount"])
        writer.writeheader()


def write_expense_header():
    """
    Write the header for the expense CSV file.

    Returns:
        None
    """

    with open("Expense_Journal.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "item", "supplier", "amount", "category"])
        writer.writeheader()


def write_income_enteries(today_date, item, source, amount):
    """
    Write income entries to the CSV file.

    Args:
        today_date (str): The date of the income entry.
        item (str): The name of the item.
        source (str): The source of the income.
        amount (int): The amount of income.

    Returns:
        None
    """

    try:
        with open("Income_Journal.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["date", "item", "source", "amount"])

            writer.writerow({"date": f"{today_date}", "item": item, "source": source, "amount": amount})
    except ValueError as e:
            sys.exit(f"ValueError: {e}")


def write_expense_enteries(today_date, item, supplier, amount, category):
     """
    Write expense entries to the CSV file.

    Args:
        today_date (str): The date of the expense entry.
        item (str): The name of the item.
        supplier (str): The supplier of the item.
        amount (int): The amount of the expense.
        category (str): The category of the expense.

    Returns:
        None
    """

     try:
        with open("Expense_Journal.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["date", "item", "supplier", "amount", "category"])
            writer.writerow({"date": f"{today_date}", "item": item, "supplier": supplier, "amount": amount, "category": category})
     except ValueError as e:
            sys.exit(f"ValueError: {e}")


def expenses_by_category(data):
    """
    Calculate expenses by category.

    Args:
        data (list): A list of dictionaries containing expense entry details.

    Returns:
        dict: A dictionary mapping expense categories to their total amounts.
    """
    try:
        expense_category = {}
        category = ""
        amount = 0

        for i in range(len(data)):
            if i != 0:
                for k,v in data[i].items():
                    if "category" in k:
                        category = v
                    if "amount" in k:
                        amount = v
                if category not in expense_category:
                    expense_category[category] = 0
                expense_category[category] += amount
        return expense_category
    except (ValueError,TypeError) as e:
        sys.exit(f"Error: {e}")


def display_expenses_by_category(data):
    """
    Display expenses by category.

    Args:
        data (dict): A dictionary mapping expense categories to their total amounts.

    Returns:
        None
    """

    print("Expenses by Category:")
    for category, total_amount in data.items():
        print(f"{category}: R{total_amount:.2f}")


if __name__ == "__main__":
    main()
