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

