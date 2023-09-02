from src.herd_the_babies.herd_the_babies import herd_the_babies

def test_herd_the_babies_empty_input():
    assert herd_the_babies('') == ''

def test_herd_the_babies_one_parent():
    assert herd_the_babies('A') == 'A'

def test_herd_the_babies_one_parents_and_child():
    assert herd_the_babies('aA') == 'Aa'

def test_herd_the_babies_one_parent_multiple_children():
    assert herd_the_babies('aaAaaaaa') == 'Aaaaaaaa'

def test_herd_the_babies_two_parents():
    assert herd_the_babies('AB') == 'AB'

def test_herd_the_babies_complex_input():
    assert herd_the_babies('bbaBccAC') == 'AaBbbCcc'

def test_herd_the_babies_complex_input_2():
    assert herd_the_babies('bbkzzkaBcZcPACEK') == 'AaBbbCccEKkkPZzz'
