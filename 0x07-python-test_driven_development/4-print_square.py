#!/usr/bin/python3

def print_square(size):
    """  prints a square with the character #.
    Parametres:
        size: length of the square.
    Returns:
        Nothing.
    Exceptions:
        Size must be an integer.
        Size must be >= 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print(size*'#')
