import pytest

from src.caesar_cipher.caesar_cipher import (caesar,BadInputError)

def test_cipher_with_single_letter_no_shift():
    output = caesar('a',0)
    expected = 'a'
    assert output == expected

def test_cipher_with_single_letter_1_shift():
    output = caesar('a',1)
    expected = 'b'
    assert output == expected

def test_cipher_with_single_letter_neg_1_shift():
    output = caesar('a',-1)
    expected = 'z'
    assert output == expected

def test_cipher_with_single_letter_and_non_char_with_shift():
    output = caesar('a%',1)
    expected = 'b%'
    assert output == expected

def test_cipher_with_single_word_with_shift():
    output = caesar('hello', 2) 
    expected = 'jgnnq'
    assert output == expected

def test_cipher_with_two_words_with_shift():
    output = caesar('HELLO world!', -3)
    expected = 'ebiil tloia!'
    assert output == expected

def test_cipher_with_number_greater_than_26():
    output = caesar('a%',27)
    expected = 'b%'
    assert output == expected

def test_cipher_raises_int_error():
    with pytest.raises(BadInputError, match="Invalid input: world is not an integer"):
        caesar('hello', 'world')

def test_cipher_raises_str_error():
    with pytest.raises(BadInputError, match="Invalid input: 7 is not a string"):
        caesar( 7, 'world')
        