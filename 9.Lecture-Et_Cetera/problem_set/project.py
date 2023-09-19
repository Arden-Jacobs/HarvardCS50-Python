from datetime import date
import csv


def main():
    write_income_header()
    write_expense_header()
    income_array = get_income()
    expense_array = get_expense()
    income_total = get_total(income_array)
    expense_total = get_total(expense_array)
    print(f"Total Income: {income_total}")
    print(f"Total Expenses: {expense_total}")

    if expense_total and income_total != None:
        net_income = income_total - expense_total
        print(f"Net Income: {net_income}")


def income_journal(**kwargs):
    return(kwargs)


def expenses_journal(**kwargs):
    return(kwargs)


def get_income():
    today_date = date.today()
    income = ["Income Statement"]
    while True:
        try:
            if input("Would you like to create a new Income entery (Y or N): ") == "Y":
                item = input("Enter child name: ")
                source = input("Enter parent name: ")
                amount = int(input("Enter amount: "))
                income.append(income_journal(date=f"{today_date}", item=item, source=source, amount=amount))
                write_income_enteries(today_date, item, source, amount)
            else:
                break
            ...
        except:
            return False
    return income

