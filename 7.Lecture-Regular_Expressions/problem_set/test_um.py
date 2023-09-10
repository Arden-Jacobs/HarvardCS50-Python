from um import count

def test_input():
    assert(count("um?")) == 1
    assert(count("yummy")) == 0
    assert(count("UM")) == 1
