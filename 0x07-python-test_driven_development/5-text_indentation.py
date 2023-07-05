#!/usr/bin/python3
def text_indentation(text):
    """ prints a text with 2 new lines after each of these characters:
        ., ? and :.
        Parmeters:
            text:a string.
        Returns:
            Nothing.
        Exceptions:
            text must be a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    for char in text:
        result += char
        if char in ['.', '?', ':']:
            result += "  \n\n"
    print(result.strip())
