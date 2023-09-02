import pytest
from src.crack_code.crack_code import crack_code


def test_output_is_a_boolean_with_simplest_input():
    output = crack_code("a-b-c-d(abcd)")
    assert type(output) == bool

def test_output_is_a_true_with_simplest_input():
    output = crack_code("a-b-c-d(abcd)")
    assert output == True

def test_output_is_a_false_with_simplest_input():
    output = crack_code("a-b-c-e(abcd)")
    assert output == False

def test_output_with_test_case_01():
    output = crack_code("ddd-aaa-z-y-x-123(adxy)")
    assert output == True

def test_output_with_test_case_02():
    output = crack_code("fff-gg-xx-ss-y(fgsx)")
    assert output == True

def test_output_with_test_case_03():
    output = crack_code("a-b-c-d-e-f-g-h-i-577(acdb)")
    assert output == False

def test_output_with_test_case_04():
    output = crack_code("fff-gg-xx-ss-y(fgsy)")
    assert output == False

def test_input_error_raises_typeError():
    with pytest.raises(TypeError, match='Input must be a string'):
        crack_code(["a-b-c-d(abcd)"])        

def test_input_string_is_formatted_correctly():
    with pytest.raises(ValueError, match='String is not formatted correctly'):
        crack_code("i have no parenthesis")

def test_input_string_is_formatted_correctly_body():
    with pytest.raises(ValueError, match='String is not formatted correctly'):
        crack_code("a-b-c(abcd)")

def test_input_string_is_formatted_correctly_head():
    with pytest.raises(ValueError, match='String is not formatted correctly'):
        crack_code("a-b-c-d(abc)")