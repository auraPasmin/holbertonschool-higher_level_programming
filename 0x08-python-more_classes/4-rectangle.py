#!/usr/bin/python3
"""Write a class Rectangle that defines a rectangle by:
(based on 3-rectangle.pyi"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """pro"""
        return self.__width

    @property
    def height(self):
        """pro"""
        return self.__height

    @width.setter
    def width(self, value):
        """setter and getter"""
        if not(isinstance(value, int)):
            raise TypeError("width must be an integer")
        if(value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """setter and getter"""
        if not(isinstance(value, int)):
            raise TypeError("height must be an integer")
        elif(value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """the area"""
        area = self.__height * self.__width
        return area

    def perimeter(self):
        """the perimeter"""
        if (self.__width == 0 or self.__height == 0):
            return 0
        perimeter = (self.__height * 2) + (self.__width * 2)
        return perimeter

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
        """retangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
