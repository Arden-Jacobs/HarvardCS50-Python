import pytest
from project import (
    income_journal,
    expenses_journal,
    get_total,
    expenses_by_category,
)

# Test income_journal function
def test_income_journal():
    """
    Test the income_journal function.
    """
    entry = income_journal(date="2023-09-21", item="Test Item", source="Test Source", amount=100)
    assert entry == {
        "date": "2023-09-21",
        "item": "Test Item",
        "source": "Test Source",
        "amount": 100,
    }
    # check errors


# Test expenses_journal function
def test_expenses_journal():
    """
    Test the expenses_journal function.
    """
    entry = expenses_journal(
        date="2023-09-21",
        item="Test Item",
        supplier="Test Supplier",
        amount=50,
        category="Test Category",
    )
    assert entry == {
        "date": "2023-09-21",
        "item": "Test Item",
        "supplier": "Test Supplier",
        "amount": 50,
        "category": "Test Category",
    }
    # check errors



# Test get_total function
def test_get_total():
    """
    Test the get_total function.
    """
    data = [
        {"date": "2023-09-21", "item": "Item 1", "amount": 100},
        {"date": "2023-09-22", "item": "Item 2", "amount": 200},
    ]
    total = get_total(data)
    assert total == 300
    # check errors


# Test expenses_by_category function
def test_expenses_by_category():
    """
    Test the expenses_by_category function.
    """
    data = [
        {"date": "2023-09-21", "item": "Item 1", "amount": 50, "category": "Category A"},
        {"date": "2023-09-22", "item": "Item 2", "amount": 75, "category": "Category B"},
        {"date": "2023-09-23", "item": "Item 3", "amount": 100, "category": "Category A"},
    ]
    category_totals = expenses_by_category(data)
    assert category_totals == {"Category A": 150, "Category B": 75}
    # check errors
