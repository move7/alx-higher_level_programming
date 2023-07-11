#!/usr/bin/python3
"""this module checks if the object is an instance of a class ."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.

    Args:
        obj: The object to check.
        a_class: The class.
    Returns:
        True if the object is an instance of, or if the object is an instance
        of a class that inherited from,
        the specified class ; otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    return False
