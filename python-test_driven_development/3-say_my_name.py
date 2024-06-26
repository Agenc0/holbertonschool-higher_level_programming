#!/usr/bin/python3
"""Module that prints a name
'My name is <first name> <last name>'"""


def say_my_name(first_name, last_name=""):
    """Prints: My name is <first name> <last name>.

    Args:
        first_name (str): First name to print.
        last_name (str): Last name to print.

    Raises:
        TypeError: If first_name or last_name are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
