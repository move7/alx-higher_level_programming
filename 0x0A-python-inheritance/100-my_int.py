#!/usr/bin/python3
"""MyInt class that inherits from int."""


class MyInt(int):
    """MyInt class class"""

    def __eq__(self, value):
        """invert == and != operators."""
        return self.real != value

    def __ne__(self, value):
        """invert == and != operators."""
        return self.real == value
