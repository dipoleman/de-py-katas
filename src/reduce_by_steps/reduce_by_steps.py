def reduce_by_steps(bin_func, input_list, start_value):
    """Recursively applies a binary function to the elements of a list
    and an accumulator value.

    Args:
        bin_func (function): A binary function that takes two arguments.
        input_list (list): A list of elements to be reduced.
        start_value (any): The initial value of the accumulator.

    Returns:
        any: The final value of the accumulator after all elements
        in the list have been processed.

    Raises:
        TypeError: If not all elements in the input list are of the same type.
    """
    if not all(isinstance(x, type(input_list[0])) for x in input_list):
        raise TypeError(
            "All elements in the input list must be of the same type")

    if len(input_list) == 0:
        return start_value
    else:
        if start_value == '':
            start_value = bin_func(start_value, input_list[0]).lstrip()
            input_list.pop(0)
            return reduce_by_steps(bin_func, input_list, start_value)
        else:
            start_value = bin_func(start_value, input_list[0])
            input_list.pop(0)
            return reduce_by_steps(bin_func, input_list, start_value)
