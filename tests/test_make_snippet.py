from lib.make_snippet import *

def test_returns_empty_string():
    result = make_snippet("")
    assert result == ""

def test_takes_4_word_string_returns_the_4_words():
    result = make_snippet("You are very smart")
    assert result == "You are very smart"

def test_takes_5_word_string_returns_the_5_words():
    result = make_snippet("You are very very smart")
    assert result == "You are very very smart"

def test_takes_6_word_string_returns_the_6_words():
    result = make_snippet("You are very very very smart")
    assert result == "You are very very very..."

def test_takes_6_word_string_separated_by_commas_returns_the_same_string():
    result = make_snippet("You,are,very,very,very,smart")
    assert result == "You,are,very,very,very,smart"

def test_takes_6_word_string_separated_by_commas_returns_the_same_string():
    result = make_snippet("You, are, very, very, very, smart")
    assert result == "You, are, very, very, very,..."