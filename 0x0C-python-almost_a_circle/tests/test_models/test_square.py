#!/usr/bin/python3
"""unit tests for Square class """

import unittest
from models.base import Base
from models.square import Square
import io
import sys


class Test_square(unittest.TestCase):
    """unit tests"""

    def test_square_is__base(self):
        self.assertIsInstance(Square(1), Base)

    def test_square_is_rectangle(self):
        self.assertIsInstance(Square(1), Square)

    def test_one_arg(self):
        s1 = Square(7)
        s2 = Square(5)
        self.assertEqual(s1.id, s2.id - 1)

    def test_two_args(self):
        s1 = Square(7, 3)
        s2 = Square(5, 3)
        self.assertEqual(s1.id, s2.id - 1)

    def test_zero_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_get_size(self):
        self.assertEqual(5, Square(5, 3).size)

    def test_set_size(self):
        s = Square(5, 3, 7, 11)
        s.size = 9
        self.assertEqual(9, s.size)

    def test_get_width(self):
        self.assertEqual(3, Square(5, 3).width)

    def test_get_height(self):
        s = Square(5, 3, 7, 11)
        s.size = 9
        self.assertEqual(9, s.height)

    def test_get_x(self):
        self.assertEqual(7, Square(5, 3, 7, 11).x)

    def test_get_y(self):
        self.assertEqual(11, Square(5, 3, 7, 11).y)
