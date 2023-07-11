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
