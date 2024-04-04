#!/usr/bin/python3
"""module for inheritance checking"""


def inherits_from(obj, a_class):
    """checks for inhertied classes and not
    a_class"""

    return issubclass(type(obj), a_class) and type(obj) is not a_class
