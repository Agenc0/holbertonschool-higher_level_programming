#!/usr/bin/python3
"""module defining MyList class"""


class MyList(list):
    """subclass of list"""
    def __init__(self):
        """Initializes MyList instances"""
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
