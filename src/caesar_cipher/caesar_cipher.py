class BadInputError(Exception):
    """Raised when a function receives a bad input."""
    pass

def caesar(string, number):
    """
    Encrypts a string using the Caesar cipher.

    This function takes a string and a number as input and returns a new string 
    where each letter in the input string is shifted by the given number of 
    positions in the alphabet. The case of the letters is ignored, and non-letter 
    characters are not encrypted.

    Args:
        string (str): The string to encrypt.
        number (int): The number of positions to shift each letter.

    Returns:
        str: The encrypted string.

    Raises:
        BadInputError: If the input string is not a string or if the input number 
        is not an integer.
    """
    if not isinstance(string, str):
        raise BadInputError(f"Invalid input: {string} is not a string")
    if not isinstance(number, int):
        raise BadInputError(f"Invalid input: {number} is not an integer")

    char_key = {chr(i): i - 97 for i in range(97, 123)}
    num_key = {i - 97: chr(i) for i in range(97, 123)}
    cipher_words = []

    for word in string.split(' '):
        cipher_word = ''
        for char in word.lower():
            if ord(char) >= 97 and ord(char) <= 123:
                cipher_word += num_key[(char_key[char] + number) % 26]
            else:
                cipher_word += char
        cipher_words.append(cipher_word)

    return ' '.join(cipher_words)
