#!/usr/bin/python3
"""this moduleis is a Rectangle class that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle class that inherits BaseGeometry."""

    def __init__(self, width, height):
        """Intialize function.

        Args:
            width: The width of the Rectangle.
            height: The height of the Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() of the Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
