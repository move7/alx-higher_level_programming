#!/usr/bin/python3
""" Module that lists all attributes and methods of an object"""

def lookup(obj):
    """returns the list of available attributes and methods of an object."""
    return (dir(obj))
