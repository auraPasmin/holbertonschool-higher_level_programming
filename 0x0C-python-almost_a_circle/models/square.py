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

    def update(self, *args, **kwargs):
        """ the update test"""
        for i, j in enumerate(args):
            if i == 0:
                self.id = j
            elif i == 1:
                self.size = j
            elif i == 2:
                self.x = j
            elif i == 3:
                self.y = j
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "size" in kwargs:
            self.size = kwargs["size"]
        if "x" in kwargs:
            self.x = kwargs["x"]
        if "y" in kwargs:
            self.y = kwargs["y"]

    def to_dictionary(self):
        """ dic test"""
        dic = {}
        dic["id"] = self.id
        dic["size"] = self.size
        dic["x"] = self.x
        dic["y"] = self.y
        return dic
