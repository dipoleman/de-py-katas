def get_frequencies(input_str):
    """
    Returns a dictionary containing the frequency of each character in the input string.

    Args:
        input_str (str): The input string.

    Returns:
        dict: A dictionary where the keys are the unique characters in the input string 
        and the values are the number of times each character appears in the input string.
    """
    input_str = input_str.replace(' ', '')
    unique = set(input_str)
    frequencies = {}

    for char in unique:
        frequencies[char] = input_str.count(char)

    return frequencies
