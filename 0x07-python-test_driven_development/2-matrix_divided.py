#!/usr/bin/python3
def matrix_divided(matrix, div):
    """ divides all elements of a matrix by div.
    parameters:
    matrix: list of lists of integers or floats.
        div:  a number (integer or float) is divisor number.
    Returns:
        A new matrix divided by div.
    Exceptions:
        Matrix must be a matrix (list of lists) of integers/floats.
        Each row of the matrix must have the same size.
        Div must be a number.
        Division by zero.
    """
    if (not isinstance(div, int) and not isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result = []
    if (not isinstance(matrix, list) or matrix == []):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    for row in matrix:
        if (not isinstance(row, list) or row == []):
            raise TypeError("matrix must be a matrix (list of lists) of "
                            "integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size.")
        row_result = []
        for elt in row:
            if (not isinstance(elt, int) and not isinstance(elt, float)):
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
            row_result.append(round(elt / div, 2))
        result.append(row_result)
    return(result)
