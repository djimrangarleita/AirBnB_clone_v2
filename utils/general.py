#!/usr/bin/python3
"""
This module contains general purpose util functions
"""
import re


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


def normalize_custom_cmd(cmd):
    """Read and parse custom cmds"""
    tokens = re.split(r'[., "()]', cmd)
    my_cmd = tokens.pop(1)
    normalized_cmd = '{} {}'.format(my_cmd, ' '.join(tokens))
    return normalized_cmd
