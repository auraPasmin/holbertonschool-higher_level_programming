#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square"""

    def __init__(self, size, x=0, y=0, id=None):
        """builder"""
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter"""
        return self.width

    @size.setter
    def size(self, value):
        """setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """should print, and str() should return"""
        return("[Square] ({}) {}/{} - {}".format
               (self.id, self.x, self.y, self.width))
