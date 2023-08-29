from fuel import convert, gauge
import pytest

def test_convert_error():
    with pytest.raises(ValueError):
        convert("asd")
    with pytest.raises(ValueError):
        convert("a/b")
    with pytest.raises(ZeroDivisionError):
        convert("5/0")

def test_convert():
    assert convert("1/100") == 1
    assert convert("25/100") == 25
    assert convert("50/100") == 50
    assert convert("75/100") == 75
    assert convert("99/100") == 99

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(25) == "25%"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
    assert gauge(99) == "F"
