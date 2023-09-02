"""
This module provides functions to encode and decode Morse code messages.

The `morse_map` dictionary maps Morse code symbols to their corresponding characters.
The `encode_map` dictionary is the inverse of `morse_map`, mapping characters to their corresponding Morse code symbols.

Functions:
    morse_decoder(string: str) -> str:
        Decodes a Morse code message into a string of characters.
        The input string should use spaces to separate symbols within a word, and four spaces to separate words.
        
    morse_encoder(string: str) -> str:
        Encodes a string of characters into a Morse code message.
        The output string uses spaces to separate symbols within a word, and four spaces to separate words.
"""

morse_map = {".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G", "....": "H",
             "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O", ".--.": "P", "--.-": "Q",
             ".-.": "R", "...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z",
             ".----": "1", "..---": "2", "...--": "3", "....-": "4", ".....": "5", "-....": "6", "--...": "7", "---..": "8",
             "----.": "9", "-----": "0"
             }

encode_map = {morse_map[key]:key  for key in morse_map}

def morse_decoder(string):
    if not isinstance(string, str):
        raise TypeError(f"Input must be a string, not {type(string).__name__}")
    try:
        decoded_message = ' '.join([''.join([morse_map[char] for char in word.split(' ')]) 
                                    for word in string.split('    ')])
        return decoded_message
    except KeyError as e:
        raise KeyError(f"Invalid Morse code symbol: {e.args[0]}")

def morse_encoder(string):
    if not isinstance(string, str):
        raise TypeError(f"Input must be a string, not {type(string).__name__}")
    try:
        encoded_message = '    '.join([' '.join([encode_map[char.upper()] for char in word])
                                        for word in string.split(' ')])
        return encoded_message
    except KeyError as e:
        raise KeyError(f"Invalid character: {e.args[0]}")
