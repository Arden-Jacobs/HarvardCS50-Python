# Financial Tracker App

The Financial Tracker App is a Python-based tool that allows you to conveniently track your income and expenses. It provides an easy way to record financial transactions, calculate totals, and analyze expenses by category.

# Creator Details

Name: Arden Jacobs
City: Cape Town
Country: South Africa

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Functions](#functions)
- [File Structure](#file-structure)
- [License](#license)

## Introduction

Managing your finances is essential for maintaining a healthy financial life. The Financial Tracker App simplifies this task by providing the following features:

## Features

- **Income Tracking:** Easily record your income entries, including the date, source, and amount.

- **Expense Tracking:** Record your expense entries with details such as the date, item, supplier, amount, and category.

- **Expense Analysis:** Analyze your expenses by category to gain insights into your spending habits.

- **Data Storage:** All financial data is stored in CSV files for easy access and backup.

- **Totals Calculation:** Calculate your total income, total expenses, and net income at any time.

## Getting Started

To start using the Financial Tracker App, follow these steps:

1. Clone the repository to your local machine:

   ```shell
   git clone <repository_url>

# Navigate to the project directory:

shell
Copy code
cd Financial-Tracker-App

# Run the app:

shell
Copy code
python project.py

# Usage:

When you run the app, you will be prompted to create income and expense entries.

For income entries, provide the date, source, and amount.

For expense entries, provide the date, item, supplier, amount, and category.

The app will calculate the total income, total expenses, and net income.

It will also display expenses by category.

# Functions

- main()
- Run the financial tracking app.

- income_journal(**kwargs)
- Record income entries.

- expenses_journal(**kwargs)
- Record expense entries.

- get_income()
- Retrieve income entries.

- get_expense()
- Retrieve expense entries.

- get_total(data)
- Calculate the total amount for a given list of data.

- write_income_header()
- Write the header for the income CSV file.

- write_expense_header()
- Write the header for the expense CSV file.

- write_income_entries(today_date, item, source, amount)
- Write income entries to the CSV file.

- write_expense_entries(today_date, item, supplier, amount, category)
- Write expense entries to the CSV file.

- expenses_by_category(data)
- Calculate expenses by category.

- display_expenses_by_category(data)
- Display expenses by category.

# File Structure
project.py: The main script for the Financial Tracker App.
test_project.py: The test script for the Financial Tracker App.
Income_Journal.csv: CSV file to store income entries.
Expense_Journal.csv: CSV file to store expense entries.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Happy tracking!
