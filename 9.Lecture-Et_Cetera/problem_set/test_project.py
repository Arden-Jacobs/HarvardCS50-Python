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