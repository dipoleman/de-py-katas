import pytest
from src.alphabet_position.alphabet_position import alphabet_position

def test_input_empty_string_returns_empty_string():
    output = alphabet_position('')
    assert output == ''

def test_input_single_letter():
    output = alphabet_position('a')
    assert output == '1'
    output = alphabet_position('z')
    assert output == '26'

def test_input_double_letters():
    output = alphabet_position('aa')
    assert output == '1 1'
    output = alphabet_position('za')
    assert output == '26 1'

def test_input_string_with_punctuation():
    output = alphabet_position('a,()a?')
    assert output == '1 1'
    output = alphabet_position('%z:,a^$')
    assert output == '26 1'

def test_using_test_case():
    output = alphabet_position("The sunset sets at twelve o' clock.")
    expected = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
    assert output == expected

def test_input_for_incorrect_input_type():
    with pytest.raises(TypeError, match='Input must be a string'):
        alphabet_position(['abc'])
    