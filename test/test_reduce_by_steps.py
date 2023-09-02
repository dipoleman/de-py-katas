import pytest
from src.reduce_by_steps.reduce_by_steps import reduce_by_steps

def multiply(num1,num2):
    return num1 * num2
def make_sentence(str1,str2):
    return f"{str1} {str2}"

def test_function_returns_single_item_from_single_item_list():
    result = reduce_by_steps(multiply,[7],1)
    assert result == 7
    result = reduce_by_steps(multiply,[7],3)
    assert result == 21
    result = reduce_by_steps(make_sentence,['once...'],'')
    assert result == 'once...'

def test_function_returns_value_from_list_of_two_elements():
    result = reduce_by_steps(multiply,[7,4],1)
    assert result == 28
    result = reduce_by_steps(multiply,[7,3],3)
    assert result == 63
    result = reduce_by_steps(make_sentence,['once','upon'],'')
    assert result == 'once upon'

def test_function_returns_correct_values_complex_input():
    result = reduce_by_steps(make_sentence,['Once','upon','a','time'],'Lets start...')
    assert result == 'Lets start... Once upon a time'

def test_mixed_type_input_array_throws_TypeError():
    with pytest.raises(TypeError, match='All elements in the input list must be of the same type'):
        reduce_by_steps(multiply,[2,3,{2,3,5}],8)


