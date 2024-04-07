#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


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

    def area(self):
        """returns area value"""
        return self.__width * self.__height

    def display(self):
        """print Rectangle with #"""
        for i in range(self.__y):
            print("")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """return __str__ and print() representation of a Rectangle"""
        return '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """updates rectangle values"""
        if args and len(args) != 0:
            pos = 0
            for arg in args:
                if pos == 0:
                    self.id = arg
                elif pos == 1:
                    self.width = arg
                elif pos == 2:
                    self.height = arg
                elif pos == 3:
                    self.x = arg
                elif pos == 4:
                    self.y = arg
                pos += 1

        elif len(kwargs) != 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
