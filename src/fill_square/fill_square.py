class BadInputError(Exception):
    """Raised when a function receives a bad input."""
    pass

def fill_square(nest):
    """
    Converts a nested list into a square matrix by filling with None values.

    Args:
        nest (List[List[Any]]): A nested list representing a matrix.

    Returns:
        List[List[Any]]: A square matrix with dimensions equal to the maximum
        of the number of rows and columns in the input matrix. The values from
        the input list are copied into the top-left corner of the output
        matrix, and the remaining cells are filled with None values.

    Raises:
        BadInputError: If the input is not a nested list or if any element of
        the input list is not a list.
    """
    if not isinstance(nest, list):
        raise BadInputError(f"Invalid input: {nest} is not a list")
    
    for child_nest in nest:
        if not isinstance(child_nest, list):
            raise BadInputError(f"Invalid input: {child_nest} is not a list")
        
    dimension_col = max([len(arr) for arr in nest])
    dimension_rows = len(nest)
    dimension = max(dimension_col, dimension_rows)
    matrix = [[None for i in range(dimension)] for i in range(dimension)]

    for row in range(dimension_rows):
        for col in range(len(nest[row])):
            matrix[row][col] = nest[row][col]
    return matrix

# print(fill_square("[1],[1,2]"))