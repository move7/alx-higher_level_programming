#!/usr/bin/python3
"""this module checks is an instance of a class that inherited
(directly or indirectly) from the specified class."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj: The object to check.
        a_class: The class.
    Returns:
        True :if the object is an inherited instance of a_class
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
