import pytest

from src.get_distinct_letters.get_distinct_letters import (
    get_distinct_letters)

def test_get_distinct_letters_empty_string():
    expected = ''
    result = get_distinct_letters('', '')
    assert result == expected

def test_get_distinct_letters_one_letter():
    expected = 'a'
    result = get_distinct_letters('a', '')
    assert result == expected

def test_get_distinct_letters_two_letters():
    expected = 'ab'
    result = get_distinct_letters('abaabb', '')
    assert result == expected

def test_get_distinct_letters_ignoring_capitals():
    expected = 'ab'
    result = get_distinct_letters('Abaabb', '')
    assert result == expected

def test_get_distinct_letters_including_capitals():
    expected = 'ABab'
    result = get_distinct_letters('Abaabb', 'B',True)
    assert result == expected

def test_get_distinct_letters():
    expected = 'dehrw'
    result = get_distinct_letters('hello', 'world')
    assert result == expected

def test_get_distinct_letters_and_punctuation():
    expected = '?dehrw'
    result = get_distinct_letters('hello', 'world?')
    assert result == expected

def test_get_distinct_letters_and_punctuation_and_numbers():
    expected = '123?dehrw'
    result = get_distinct_letters('hello', 'world?123')
    assert result == expected

def test_get_distinct_letters_and_punctuation_and_numbers_and_capitals():
    expected = '123?Odehorw'
    result = get_distinct_letters('hello', 'wOrld?123',True)
    assert result == expected

# def test_throws_exception_when_wrong_input_arg():
#     with pytest.raises(Exception) as e:
#         result = get_distinct_letters(56,'rt45')
#         expected = "<class 'Exception'>"
#     assert result == expected