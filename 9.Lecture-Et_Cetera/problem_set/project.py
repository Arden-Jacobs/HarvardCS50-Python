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