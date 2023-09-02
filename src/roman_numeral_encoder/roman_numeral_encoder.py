def roman_numeral_encoder(num):
    """
    Converts an integer to its Roman numeral representation.

    Args:
        num (int): The integer to be converted. Must be between 1 and 100.

    Returns:
        str: The Roman numeral representation of the input integer.

    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is not between 1 and 100.
    """
    if not isinstance(num, int):
        raise TypeError('Input must be an integer')
    if num < 1 or num > 100:
        raise ValueError('Input must be between 1 and 100')

    roman = ""
    units ={0:'',1:'I',2:'II',3:'III',4:'IV',
        5:'V',6:'VI',7:'VII',8:'VIII',9:'IX'}
    tens ={0:'',1:'X',2:'XX',3:'XXX',4:'XL',5:'L',
		6:'LX',7:'LXX',8:'LXXX',9:'XC',10:'C'}
    roman = ''.join([tens[num//10],units[num%10]])
    
    return roman

