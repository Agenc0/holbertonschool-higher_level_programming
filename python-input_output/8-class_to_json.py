#!/usr/bin/python3
"""class to JSON function"""


def class_to_json(obj):
    """returns dict desc. w/simple data structure"""
    return obj.__dict__
