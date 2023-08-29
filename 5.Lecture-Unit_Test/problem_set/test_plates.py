from plates import is_valid

def test_valid():
    assert is_valid("CS50") == True
    assert is_valid("CSF50") == True

def test_invalid():
    assert is_valid("CS05") == False
    assert is_valid("CS50F") == False

def test_alpha():
    assert is_valid("CS") == True
    assert is_valid("hello") == True
    assert is_valid("w") == False

def test_number():
    assert is_valid("520") == False
    assert is_valid("5014") == False

def test_len():
    assert is_valid("") == False
    assert is_valid("hello world") == False

def test_alnum():
    assert is_valid("hi,.there") == False
    assert is_valid("hi,.50") == False