import pytest
from src.sum_ascii.sum_ascii import (sum_ascii,BadInputError)

def test_sum_ascii_one_name():
    assert sum_ascii(['John']) == 'John'

def test_sum_ascii_two_names():
    assert sum_ascii(['John', 'Aa']) == 'John'

def test_sum_ascii_three_names():
    assert sum_ascii(['Aaa', 'Bbb', 'Ccc']) == 'Ccc'

def test_sum_ascii_many_names():
    assert sum_ascii(['John',"George","Hans","Hanna","Barathea"]) == 'Barathea'

def test_sum_ascii_error_if_not_passes_a_list():
    with pytest.raises(BadInputError, match="Invalid input: John, Sam, Sue is not a list"):
        sum_ascii("John, Sam, Sue")

def test_sum_ascii_error_if_list_has_a_non_string_member():
    with pytest.raises(BadInputError, match="Invalid input: 42 is not a string"):
        sum_ascii(["John", "Sam", 42, "Sue"])