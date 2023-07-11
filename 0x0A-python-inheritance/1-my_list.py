#!/usr/bin/python3
"""MyList class inherits from list"""


class MyList(list):
    """Implements sorted printing"""

    def print_sorted(self):
        """print sorted lisst"""
        print(sorted(self))
