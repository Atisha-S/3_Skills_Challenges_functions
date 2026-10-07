import pytest
from lib.improve_grammar import *

def test_yes_caspital_letter_and_yes_end_punctuation():
    result = verify_grammar("Hi my name is Atisha!")
    assert result == True 


def test_yes_caspital_letter_and_no_end_punctuation():
    result = verify_grammar("Hi my name is Atisha")
    assert result == False 


def test_no_caspital_letter_and_no_end_punctuation():
    result = verify_grammar("hi my name is Atisha")
    assert result == False 


def test_no_caspital_letter_and_yes_end_punctuation():
    result = verify_grammar("hi my name is Atisha!")
    assert result == False 


def test_2_yes_caspital_letter_and_yes_end_punctuation_with_spaces():
    result = verify_grammar(" Hi my name is Atisha! ")
    assert result == True 


def test_with_empty_text():
    with pytest.raises(Exception) as e:
        verify_grammar("")
    error_message = str(e.value)
    assert error_message == "Grammar can't be verified with an empty string"