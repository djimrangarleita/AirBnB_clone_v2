"""
This module contains general purpose util functions
"""


def pascal_to_snake(name):
    """Convert a given string, e.g classname to snake case e.g module name"""
    result = ''
    if not name:
        return result
    result += name[0].lower()
    for char in name[1:]:
        if char.isupper():
            result += '_{}'.format(char.lower())
        else:
            result += char
    return result
