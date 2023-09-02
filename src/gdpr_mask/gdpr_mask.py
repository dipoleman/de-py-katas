def mask(*args):
    """Decorator function that masks the values of specified keys in a
    dictionary.

    Args:
        *args: A variable-length list of keys to mask in the dictionary.

    Returns:
        A decorator function that takes a function as an argument and returns
        a wrapper function. The wrapper function calls the original function
        and returns a new dictionary with the specified keys masked.
    """
    def decorator(func):

        def wrapper(*args2, **kwargs):
            result = func(*args2, **kwargs)

            def search_through_dict(input_dict):
                gdpr_output = {}
                for key, values in input_dict.items():
                    if not isinstance(values, dict):
                        if key in args:
                            secret_values = ''.join(
                                [' ' if char == ' ' else '*' for char in
                                 input_dict[key]])
                            gdpr_output[key] = secret_values
                        else:
                            gdpr_output[key] = values
                    else:
                        gdpr_output[key] = search_through_dict(values)
                return gdpr_output
            return search_through_dict(result)
        return wrapper
    return decorator
