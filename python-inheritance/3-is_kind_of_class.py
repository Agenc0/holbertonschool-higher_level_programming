#!/usr/bin/python3
"""module to test for class or inherited class"""


def is_kind_of_class(obj, a_class):
    """checks if object is an insntance of a_class
    or a class a_class inherited from"""

    return isinstance(obj, a_class)
