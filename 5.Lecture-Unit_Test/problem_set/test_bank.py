from bank import value

def test_aplha():
    assert value("hello") == 0

def test_num():
    assert value("5") == 100

def test_hi():
    assert value("hi") == 20


def test_ommit_alpha():
    assert value("hello, world") == 0

def test_case():
    assert value("HELLO") == 0