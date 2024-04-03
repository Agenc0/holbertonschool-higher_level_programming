#!/usr/bin/python3
"""Module that adds two numbers"""


def add_integer(a, b=98):
    """Adds two integers

    Float arguments are transformed into integers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Raises:
        TypeError: If either a or b is not an integer or a float.

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return (a + b)
