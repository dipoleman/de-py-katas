import re


def crack_code(input_str):
    """
    Determines if the input string follows a specific code pattern.

    The input string must be in the format "body(head)", where "body" is a
    string of characters that may include letters, numbers, and hyphens
    and "head" is a 4-letter string.

    The function checks if the 4 most frequent letters in the "body"
    (ignoring numbers and hyphens), sorted in descending order of frequency
    and ascending alphabetical order for letters with the same frequency,
    are the same as the 4 letters in the "head".

    Args:
        input_str (str): The input string to be checked.

    Returns:
        bool: True if the input string follows the code pattern,
        False otherwise.

    Raises:
        TypeError: If the input argument is not a string.
        ValueError: If the input string is not formatted correctly.
    """

    if not isinstance(input_str, str):
        raise TypeError('Input must be a string')

    regex = r'([a-z0-9]+-){3,}[a-z0-9]+\([a-z]{4}\)'
    if not re.search(regex, input_str):
        raise ValueError('String is not formatted correctly')

    body = input_str.split('(')[0]

    clean_body = re.sub(r"[-\d]", "", body)
    frequencies = [[clean_body.count(char), char] for char in set(clean_body)]
    sorted_freq = sorted(frequencies, key=lambda x: (-x[0], x[1]))
    body_cleaned = ''.join([x[1] for x in sorted_freq[:4]])

    head = input_str.split('(')[1][:4]

    if body_cleaned == head:
        return True
    else:
        return False
