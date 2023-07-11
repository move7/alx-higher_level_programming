#!/usr/bin/python3
"""This module adds attribute to an object
"""


def add_attribute(obj, attr, value):
    """Add a new attribute to an object if possible

    Args:
        obj: object
        attr: attribute name
        value: attribute value
     Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr, value)
