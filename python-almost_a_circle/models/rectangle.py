#!/usr/bin/python3
"""Rectangle class"""


class Rectangle(Base):
    """Rectangle subclass"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """intializes a Rectangle instance"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter for width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width property"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height property"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for x property"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x property"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for y property"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y property"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value