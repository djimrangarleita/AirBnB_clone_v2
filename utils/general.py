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
    arg = ''
    if 'update' in cmd and '{' in cmd:
        idx = cmd.find(',')
        arg, cmd = cmd[idx + 1:-1], cmd[:idx]
    tokens = re.split(r'[., \'"()]', cmd)
    my_cmd = tokens.pop(1)
    normalized_cmd = '{} {} {}'.format(my_cmd, ' '.join(tokens), arg)
    return normalized_cmd


def extract_args(cmd):
    """Parse and extract cmd args"""
    values = 0
    idx = cmd.find('{')
    if idx > 0:
        values, cmd = cmd[idx:], cmd[:idx]
        values = eval(values)
    args = cmd.split()
    if values == 0:
        values = args[2:]
    return (args, values)


def make_dict_from_str(kv_list):
    """Parse a list of string of type 'key="value"' and build a dict from it"""
    attr_dict = {}
    for raw_attr in kv_list:
        try:
            key, val = raw_attr.split('=')
            val = val.replace('_', ' ')
            val = val.replace('\\', '')
            val = val[1:-1] if '"' in val else eval(val)
            attr_dict[key.strip('"')] = val
        except Exception:
            pass
    return attr_dict
