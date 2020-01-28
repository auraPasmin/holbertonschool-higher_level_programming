#!/usr/bin/python3
"""Unittest base.py"""

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import json
import pep8
import unittest


class TestBase(unittest.TestCase):
    """Base.py tests"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_0(self):
        """Test number 0 for base"""
        base0 = Base()
        base1 = Base()
        base2 = Base()
        self.assertEqual(base0.id, 1)
        self.assertEqual(base1.id, 2)
        self.assertEqual(base2.id, 3)
