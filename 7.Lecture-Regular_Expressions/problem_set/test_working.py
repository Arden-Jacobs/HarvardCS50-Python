from working import convert
import pytest

def test_format_error():
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

def test_incorrect_time_format():
    with pytest.raises(ValueError):
        convert("09:90 AM - 17:70 PM ")
    with pytest.raises(ValueError):
        convert("13 AM to 27 PM")

def test_correct_format():
    assert(convert("9 AM to 5 PM")) == "09:00 to 17:00"
    assert(convert("9:00 AM to 5:00 PM")) == "09:00 to 17:00"
    assert(convert("10 PM to 8 AM")) == "22:00 to 08:00"
    assert(convert("10:30 PM to 8:50 AM")) == "22:30 to 08:50"

def test_noon_format():
    assert(convert("12 AM to 12 PM")) == "00:00 to 12:00"
    assert(convert("12:30 AM to 12:50 PM")) == "00:30 to 12:50"
