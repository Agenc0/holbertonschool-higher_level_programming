#!/usr/bin/python3
"""module that writes to a file"""


def write_file(filename="", text=""):
    """writes text to filename"""

    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
