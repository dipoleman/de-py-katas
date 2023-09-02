def create_counter(num):
    """
    Creates a counter object with up and down methods.

    Args:
        num (int): The initial value of the counter.

    Returns:
        dict: A dictionary containing two methods: 'up' and 'down'. 
        The 'up' method increments the counter by 1 and returns the new value. 
        The 'down' method decrements the counter by 1 and returns the new value.
    """
    counter = num

    def counter_up():
        nonlocal counter
        counter += 1
        return counter

    def counter_down():
        nonlocal counter
        counter -= 1
        return counter

    return {'up': counter_up, 'down': counter_down}

