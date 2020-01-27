#!/usr/bin/python3
""" class base """

class base:
    __nb_objects = 0
    
    def __init__(self, id=None):
        """ class initializer"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id =type(self).__nb_objects
    
    

