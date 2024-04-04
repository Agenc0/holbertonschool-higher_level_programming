#!/usr/bin/python3
"""module to lookup object attributes"""


def lookup(obj):
    """Returns a list of attributes and methods of obj"""
    return dir(obj)
