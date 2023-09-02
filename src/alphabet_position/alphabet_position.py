def alphabet_position(string):
    """
    Returns a string representing the position of each letter in the alphabet.

    Args:
        string (str): The input string.

    Returns:
        str: A string containing the positions of the letters in the alphabet,
        separated by spaces.

    Raises:
        TypeError: If the input argument is not a string.
    """
    if not isinstance(string, str):
        raise TypeError('Input must be a string')
    if string == '':
        return ''

    char_key = {chr(i): f'{i - 96}' for i in range(97, 123)}

    alphabet_numbers = ' '.join([char_key[char] for char in string.lower()
                                if ord(char) > 96 and ord(char) < 123])
    return alphabet_numbers

