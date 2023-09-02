import pytest
from src.morse_code.morse_code import morse_decoder, morse_encoder


def test_morse_decoder_with_singe_letter():
        output = morse_decoder("....")
        expected = 'H'
        assert output == expected

def test_morse_decoder_with_single_word():
        output = morse_decoder(".... ..")
        expected = "HI"
        assert output == expected

def test_morse_decoder_with_sentence():
        output = morse_decoder("--. --- --- -..    -- --- .-. -. .. -. --.    -. --- .-. - .... -.-. --- -.. . .-. ...")
        expected = "GOOD MORNING NORTHCODERS"
        assert output == expected

def test_morse_encoder_with_singe_letter():
        output = morse_encoder('H')
        expected = '....'
        assert output == expected

def test_morse_encoder_with_singe_letter():
        output = morse_encoder('H')
        expected = '....'
        assert output == expected

def test_morse_encoder_with_singe_word():
        output = morse_encoder("HI")
        expected = ".... .."
        assert output == expected

def test_morse_encoder_with_sentence():
        output = morse_encoder("GOOD MORNING NORTHCODERS")
        expected = "--. --- --- -..    -- --- .-. -. .. -. --.    -. --- .-. - .... -.-. --- -.. . .-. ..."
        assert output == expected

def test_get_same_string_when_composed():
        output = morse_decoder(morse_encoder("I HOPE THIS WORKS NUMBER 9"))
        expected = "I HOPE THIS WORKS NUMBER 9"
        assert output == expected

def test_morse_decoder_raises_type_error():
    with pytest.raises(TypeError, match="Input must be a string, not list"):
        morse_decoder([1])

def test_morse_encoder_raises_type_error():
    with pytest.raises(TypeError, match="Input must be a string, not dict"):
        morse_encoder({'a':2})

def test_morse_decoder_raises_key_error():
    with pytest.raises(KeyError, match="Invalid Morse code symbol: ...___..."):
          morse_decoder("--. --- --- -..    -- --- .-. -. .. -. --.    ...___...") 

def test_morse_decoder_raises_key_error_when_wrong_size_gaps():
    with pytest.raises(KeyError):
          morse_decoder("--. ---  --- -..    -- --- .-. -. .. -. --.")     

def test_morse_encoder_raises_key_error():
    with pytest.raises(KeyError, match="Invalid character: £"):
          morse_encoder("I LIKE MONEY £") 

