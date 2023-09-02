class BadInputError(Exception):
    """Raised when a function receives a bad input."""
    pass

def sum_ascii(array):
    """Finds the name with the highest ASCII score in an array of names.

    Args:
        array (list): A list of strings representing names.

    Returns:
        str: The name with the highest ASCII score. If there are multiple 
        names with the same highest score,
        the first one in the input array is returned.

    Raises:
        BadInputError: If the input array is not a list or if it contains 
        non-string elements.

    Examples:
        >>> sum_ascii(['John', 'Jane', 'Bob'])
        'John'
    """
    if not isinstance(array, list):
        raise BadInputError(f"Invalid input: {array} is not a list")
    
    for name in array:
        if not isinstance(name, str):
            raise BadInputError(f"Invalid input: {name} is not a string")

    scores = {}

    for name in array:
        scores[name] = sum([ord(char.lower()) for char in name])

    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    return sorted_scores[0][0]

