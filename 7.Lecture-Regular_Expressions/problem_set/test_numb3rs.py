from numb3rs import validate

def test_alpha():
    assert(validate("cat") == False)
    assert(validate("cat.dog.hat.mat") == False)
    assert(validate("one.two.three.four") == False)

def testinput():
    assert(validate("1.2.3.4")) == True
    assert(validate("1.2.3")) == False
    assert(validate("")) == False
    assert(validate("255.290.350.500")) == False
