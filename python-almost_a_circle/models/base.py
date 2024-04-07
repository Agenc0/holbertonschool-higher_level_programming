#!/usr/bin/python3
"""Base class"""


class Base:
    """Base class for this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initializes Base instances"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
