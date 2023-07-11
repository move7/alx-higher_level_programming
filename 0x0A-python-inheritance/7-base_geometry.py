#!/usr/bin/python3
"""this module is a BaseGeometry class."""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """raises an Exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks if a parameter is an integer.

        Args:
            name: The name of the parameter.
            value: the value to be checked.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
