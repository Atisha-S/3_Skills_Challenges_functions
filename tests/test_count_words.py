from lib.count_words import *

def test_empty_string_returns_zero():
    result = count_words("")
    assert result == 0

def test_2_words_string_returns_2():
    result = count_words("Hi Atisha")
    assert result == 2

def test_3_words_string_returns_3():
    result = count_words("Hi Atisha Singh")
    assert result == 3

def test_10_words_string_returns_10():
    result = count_words("Hi Hi Hi Hi Hi Hi Hi Hi Hi Hi")
    assert result == 10

def test_4_words_string_returns_4():
    result = count_words("Hi, Hi, Hi, Hi")
    assert result == 4