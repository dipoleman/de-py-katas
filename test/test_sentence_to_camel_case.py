import pytest

from src.sentence_to_camel_case.sentence_to_camel_case import (
    sentence_to_camel_case, camel_to_english)


def test_returns_a_single_word_in_upper_if_true():
    expected = 'This'
    result = sentence_to_camel_case('this', True)
    print(f'Result is: {result}')
    assert result == expected


def test_returns_a_single_word_in_lower_if_false():
    expected = 'this'
    result = sentence_to_camel_case('This', False)
    print(f'Result is: {result}')
    assert result == expected


def test_returns_a_sentence_in_upper_if_true():
    expected = 'ThisIsASentence'
    result = sentence_to_camel_case('this is a sentence', True)
    print(f'Result is: {result}')
    assert result == expected


def test_returns_a_sentence_in_lower_if_false():
    expected = 'thisIsASentence'
    result = sentence_to_camel_case('This is a sentence', False)
    print(f'Result is: {result}')
    assert result == expected


def test_strange_sentence_to_upper_camel_case():
    expected = 'ThisBiggerStrangeSentence'
    result = sentence_to_camel_case('This Bigger strange Sentence', True)
    print(f'Result is: {result}')
    assert result == expected


def test_strange_sentence_to_lower_camel_case():
    expected = 'thisBiggerStrangeSentence'
    result = sentence_to_camel_case('This Bigger strange Sentence', False)
    print(f'Result is: {result}')
    assert result == expected


# def test_invalid_argument_data_type_throws_error():
#     with pytest.raises(Exception):
#         sentence_to_camel_case(67)
#         expected = "<class 'Exception'>"
#         assert result == expected
#         result = sentence_to_camel_case(67.56)
#         expected = "<class 'Exception'>"
#         assert result == expected
#         result = sentence_to_camel_case([34, 45])
#         expected = "<class 'Exception'>"
#         assert result == expected
#         result = sentence_to_camel_case({'d': 4})
#         expected = "<class 'Exception'>"
#         assert result == expected


def test_camel_to_english_sentence():
    expected = 'This is a sentence.'
    result = camel_to_english('thisIsASentence')
    print(f'Result is: {result}')
    assert result == expected

# def test_invalid_argument_sentence_to_camel_case():
#     result = sentence_to_camel_case(67)
#     assert isinstance(result, Exception)

