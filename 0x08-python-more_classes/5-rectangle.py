#!/usr/bin/python3
"""Write a class Rectangle that defines a rectangle by: (based on 4-rectangle.py)"""


class Rectangle:
    """Class"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height
    
    def __str__(self):
        """print"""
        rectangle = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.width):
                rectangle += "#"
            if i < self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))
    
    def __del__(self)
        print("Bye rectangle...")
