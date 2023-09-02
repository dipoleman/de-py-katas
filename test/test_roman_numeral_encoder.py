import pytest
from src.roman_numeral_encoder.roman_numeral_encoder import roman_numeral_encoder

def test_output_is_a_string():
    output = roman_numeral_encoder(1)
    assert type(output) == str

def test_simple_number():
    output = roman_numeral_encoder(1)
    expected = 'I'
    assert output == expected

def test_number_45():
    output = roman_numeral_encoder(45)
    expected = 'XLV'
    assert output == expected

def test_number_88():
    output = roman_numeral_encoder(88)
    expected = 'LXXXVIII'
    assert output == expected

def test_number_100():
    output = roman_numeral_encoder(100)
    expected = 'C'
    assert output == expected

def test_wrong_input_type_raises_error():
    with pytest.raises(TypeError, match='Input must be an integer'):
        roman_numeral_encoder("IX")

def test_input_number_to_large_raises_error():
    with pytest.raises(ValueError, match='Input must be between 1 and 100'):
        roman_numeral_encoder(101)