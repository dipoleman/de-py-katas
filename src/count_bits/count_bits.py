def count_bits(integer):
    """
    Counts the number of bits set to 1 in the binary representation of an integer.

    Args:
        integer (int): The integer to count the bits of.

    Returns:
        int: The number of bits set to 1 in the binary representation of `integer`.
    """
    bits = sum([int(b) for b in bin(integer)[2:]])
    return bits


print(count_bits(4367385))