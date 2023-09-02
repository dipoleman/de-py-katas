import pytest

from src.bubble_sort.bubble_sort import bubble_sort

def test_simple_bubble_sort():
    output = bubble_sort([2,1])
    expected = [1,2]
    assert expected == output

def test_trickier_sort_input():
    output = bubble_sort([6,3,23,1,5,2,89,6,5])
    expected = [1, 2, 3, 5, 5, 6, 6, 23, 89]
    assert expected == output

def test_int_raises_type_error():
    with pytest.raises(TypeError):
        bubble_sort([6,3,-23,1,5,'r',89,6,5])