
def bubble_sort(arr):
    """Sorts an array of numbers in ascending order using the bubble sort algorithm.

    Args:
        arr (list): A list of numbers to sort.

    Returns:
        list: A new list containing the sorted numbers in ascending order.

    Raises:
        TypeError: If the input list contains a string.

    Examples:
        >>> bubble_sort([3, 2, 1])
        [1, 2, 3]
    """
    try:
        start_arr = arr[:]
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
        if start_arr == arr:
            return arr
        else:
            return bubble_sort(arr)
    except TypeError as e:
        raise TypeError('Input list must only contain (real) numbers') from e
    

		


