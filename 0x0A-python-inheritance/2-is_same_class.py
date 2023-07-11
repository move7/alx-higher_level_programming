#!/usr/bin/python3
"""This module checks for exact same boject."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.

    Args:
        obj: the object to check.
        a_class: class.
    Returns:
        True if the object is exactly an instance of the specified class ;
        otherwise False.
    """
    if type(obj) == a_class:
        return True
    return False
