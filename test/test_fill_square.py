import pytest
from src.fill_square.fill_square import (fill_square,BadInputError)

def test_single_number():
    output = fill_square([[1]])
    expected = [[1]]
    assert output == expected

def test_single_arr_with_two_int():
    output = fill_square([[1,2]])
    expected = [[1,2],[None,None]]
    assert output == expected

def test_4by4_array():
    output = fill_square([[1,2],[3,4],[5,6],[7,8]])
    expected = [[1, 2, None, None], [3, 4, None, None], [5, 6, None, None], [7, 8, None, None]]
    assert output == expected

def test_array_with_different_lengths():
    input = [[1],[1,2,3],[1,2]]
    output = fill_square(input)
    expected = [[1,None,None],
                [1,2,3],
                [1,2,None]]
    assert output == expected

def test_array_with_different_lengths_2():
    input = [[1],[1,2,3],[1,2],[1]]
    output = fill_square(input)
    expected = [[1,None,None,None],
                [1,2,3,None],
                [1,2,None,None],
                [1,None,None,None]]
    assert output == expected

def test_array_with_different_elements():
    input =[[7],['rat','mouse']]
    output = fill_square(input)
    expected = [[7,None],['rat','mouse']]
    assert output == expected

def test_raises_error_if_not_passed_a_list():
    with pytest.raises(BadInputError, match="Invalid input: 3,4 is not a list"):
        fill_square("3,4")
