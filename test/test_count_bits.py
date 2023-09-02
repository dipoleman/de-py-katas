from src.count_bits.count_bits import count_bits

def test_simple_input_0():
    output = count_bits(0)
    expected = 0
    assert output == expected

def test_simple_input_1():
    output = count_bits(1)
    expected = 1
    assert output == expected

def test_powers_of_two():
    output = count_bits(2**8)
    expected = 1
    assert output == expected

def test_powers_of_two_minus_one():
    output = count_bits(2**8-1)
    expected = 8
    assert output == expected

