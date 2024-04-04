#!/usr/bin/python3
"""defines class BaseGeometry"""


class BaseGeometry():
    """BaseGeometry class"""

    def area(self):
        """not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates integers

        Args:
            name (string): paramter name
            value (int): value to check

        Raises:
            TypeError: value is not an integer
            ValueError: value is lower or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
