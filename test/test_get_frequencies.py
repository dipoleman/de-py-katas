from src.get_frequencies.get_frequencies import get_frequencies

def test_get_frequencies_empty_string():
    assert get_frequencies("") == {}

def test_get_frequencies_one_char():
    assert get_frequencies("a") == {"a": 1}

def test_get_frequencies_two_char():
    assert get_frequencies("a b") == {"a": 1, "b": 1}

def test_get_frequencies_one_words():
    assert get_frequencies("abc") == {"a": 1, "b": 1, "c": 1}

def test_get_frequencies_two_words():
    assert get_frequencies("abccc defa") == {"a": 2, "b": 1, "c": 3, "d": 1, "e": 1, "f": 1}

def test_get_frequencies_with_numbers_in_word():
    assert get_frequencies("abc 123 def") == {"a": 1, "b": 1, "c": 1, "d": 1, "e": 1, "f": 1, "1": 1, "2": 1, "3": 1}

def test_get_frequencies_with_punctuation():
    assert get_frequencies("abc./123/def. $&&&$$$") == {"a": 1, "b": 1, "c": 1, "d": 1, "e": 1, "f": 1, "1": 1, "2": 1, "3": 1, ".": 2, "/": 2,  "&": 3, "$": 4,}

