def get_distinct_letters(str1, str2, capitals=False):
    """
    Returns a string containing the distinct letters from two input strings.

    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.
        capitals (bool): If True, capital and lowercase letters are treated as distinct. 
        If False, they are treated as the same.

    Returns:
        str: A string containing the distinct letters from the two input strings, 
        sorted in alphabetical order.
    """
    try:
        if capitals is False:
            str1 = str1.lower()
            str2 = str2.lower()

        str1_set = set(str1)
        str2_set = set(str2)
        result = str1_set.symmetric_difference(str2_set)
        result_str = ''.join(sorted(result))
        return result_str
    except Exception:
        return Exception

print(get_distinct_letters(56,'rt45'))