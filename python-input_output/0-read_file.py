#!/usr/bin/python3
"""module that reads file"""


def read_file(filename=""):
    """init function"""

    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
