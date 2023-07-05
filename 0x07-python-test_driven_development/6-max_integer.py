#!/usr/bin/python3
"""Module to return the max integer in a list"""


def max_integer(list=[]):
    """Function that return the max integer in a list of integers
    If the list is empty, the function returns None"""
    if len(list) == 0:
        return None
    return max(list)
