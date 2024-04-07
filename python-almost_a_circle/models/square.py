#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square subclass"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes a Square instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns __str__ and print() representation of a Square"""
        return '[Square] ({:d}) {:d}/{:d} - {:d}'.format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """getter for size property"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size property"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates Square values"""
        if len(args) != 0:
            pos = 0
            for arg in args:
                if pos == 0:
                    self.id = arg
                elif pos == 1:
                    self.size = arg
                elif pos == 2:
                    self.x = arg
                elif pos == 3:
                    self.y = arg
                pos += 1
        elif len(kwargs) != 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
