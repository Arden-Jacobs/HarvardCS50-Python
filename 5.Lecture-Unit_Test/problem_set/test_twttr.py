import pytest
from twttr import shorten

def test_word():
    assert shorten("big") == "bg"
    assert shorten("TWITTER") == "TWTTR"

def test_num():
    with pytest.raises(TypeError):
        shorten(7)

def test_letter():
    assert shorten("i") == ""

def test_omit_num():
    assert shorten("abc123") == "bc123"

def test_omit_punc():
    assert shorten("hello, world") == "hll, wrld"