#!/usr/bin/python3
"""File-appending module."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file.

    Args:
        filename (str): The name of the file.
        text (str): The string that be added to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
