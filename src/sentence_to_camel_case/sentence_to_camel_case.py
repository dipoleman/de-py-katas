def sentence_to_camel_case(arg1, arg2 = False):
    """
    Converts a sentence to camel case.

    Args:
        arg1 (str): The sentence to convert.
        arg2 (bool): If True, the first letter of the first word is capitalized. 
        If False (Default), it is not.

    Returns:
        str: The camel case version of the input sentence.
    """
    output_str = ''
    count = 0
    try:
        for word in arg1.split(' '):
            if count == 0 and arg2 is False:
                output_str += word.lower()
            else:
                output_str += word[0].upper() + word[1:].lower()

            count += 1

        return output_str
    except Exception as e:
        print(e)
        return Exception

print(sentence_to_camel_case(67))

def camel_to_english(arg1):
    """
    Converts a camel case string to an English sentence.

    Args:
        arg1 (str): The camel case string to convert.

    Returns:
        str: The English sentence version of the input string.
    """
    output_str = ''
    try:
        for index, letter in enumerate(arg1):
            if index == 0:
                output_str += letter.upper()
            elif index == len(arg1)-1:
                output_str += letter.lower()
                output_str += '.'
            else:
                if letter.isupper():
                    output_str += ' '
                    output_str += letter.lower()
                else:
                    output_str += letter

        return output_str
    except Exception:
        return Exception
