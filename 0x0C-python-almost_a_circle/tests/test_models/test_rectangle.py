#!/usr/bin/python3
"""unittest for Rectangle class."""

import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
import io
import sys


class RectangleTest(unittest.TestCase):
    """Unit tests for Rectangle class."""

    def test_rectangle_id(self):
        self.assertIsInstance(Rectangle(3, 7), Base)

    def test_without_arg(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(5)

    def test_two_args(self):
        r1 = Rectangle(3, 7)
        r2 = Rectangle(17, 11)
        self.assertEqual(r1.id, r2.id - 1)

    def test_width(self):
        self.assertEqual(Rectangle(17, 3).width,17)

    def test_rect_float_width(self):
        self.assertEqual(Rectangle(2.3, 4.2).width, 2.3)

    def test_zero_width(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 11)

    def test_negative_width(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 5)

    def test_None_width(self):
         with self.assertRaises(TypeError):
             r1 = Rectangle(None, 5)

    """ Height::
    """

    def test_height(self):
        self.assertEqual(Rectangle(17, 3).height,3)

    def test_rect_float_height(self):
        self.assertEqual(Rectangle(2.3, 4.2).height, 4.2)

    def test_zero_height(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 0)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, -5)

    def test_None_width(self):
         with self.assertRaises(TypeError):
             r1 = Rectangle(4, None)

    """x::
    """

    def test_x(self):
        self.assertEqual(Rectangle(7, 5, 11, 3).x, 11)

    def test_zero_x(self):
        self.assertEqual(Rectangle(7, 5, 0, 3).x, 0)

    def test_float_x(self):
        self.assertEqual(Rectangle(7, 5, 11.5, 3).x, 11.5)

    def test_negative_x(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(7, 5, -11, 5)

    def test_none_x(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(7, 5, None, 5)

    """y::
    """

    def test_y(self):
        self.assertEqual(Rectangle(7, 5, 11, 3).y, 3)

    def test_zero_y(self):
        self.assertEqual(Rectangle(7, 5, 3, 0).y, 0)

    def test_float_y(self):
        self.assertEqual(Rectangle(7, 5, 11, 3.7).y, 3.7)

    def test_negative_y(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(7, 5, 11, -5)

    def test_none_y(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(7, 5, 5, None)

    """area:
    """

    def test_area(self):
        self.assertEqual(Rectangle(7, 5, 11, 3).area(), 35)

    def test_zero_x_y_area(self):
        self.assertEqual(Rectangle(7, 5, 0, 0).area(), 35)

    def test_with_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(7, 5, 11, 3).area(7)

    """display::
    """

     def test_display(self):
        r1 = Rectangle(2, 1)
        with patch('sys.stdout', new=io.StringIO()) as fakeOutput:
            r1.display()
        self.assertEqual(fakeOutput.getvalue().strip(), '#')

    def test_display2(self):
        r1 = Rectangle(3, 3)
        with patch('sys.stdout', new=io.StringIO()) as fakeOutput:
            r1.display()
        self.assertEqual(fakeOutput.getvalue().strip(), '###\n###')

    """str:
    """

    def test_str(self):
         r1 = Rectangle(7, 5, 11, 5, 7)
        with patch('sys.stdout', new=io.StringIO()) as fakeOutput:
            print(r1)
        self.assertEqual(fakeOutput.getvalue(), '[Rectangle] (7) 11/5 - 7/5\n')

    """update::
    """

    def test_update_width(self):
        r1 = Rectangle(7, 5, 11, 5, 7)
        r1.update(width=9)
        with patch('sys.stdout', new=io.StringIO()) as fakeOutput:
            print(r1)
        self.assertEqual(fakeOutput.getvalue(), '[Rectangle] (7) 11/5 - 9/5\n')

    def test_update_heigth(self):
        r1 = Rectangle(7, 5, 11, 5, 7)
        r1.update(height=6)
        with patch('sys.stdout', new=io.StringIO()) as fakeOutput:
            print(r1)
        self.assertEqual(fakeOutput.getvalue(), '[Rectangle] (7) 11/5 - 7/6\n')

    def test_update_x(self):
        r1 = Rectangle(7, 5, 11, 5, 7)
        r1.update(x=6)
        with patch('sys.stdout', new=io.StringIO()) as fakeOutput:
            print(r1)
        self.assertEqual(fakeOutput.getvalue(), '[Rectangle] (7) 6/5 - 7/5\n')

    def test_update_y(self):
        r1 = Rectangle(7, 5, 11, 5, 7)
        r1.update(y=6)
        with patch('sys.stdout', new=io.StringIO()) as fakeOutput:
            print(r1)
        self.assertEqual(fakeOutput.getvalue(), '[Rectangle] (7) 11/6 - 7/5\n')

    def test_update_id(self):
        r1 = Rectangle(7, 5, 11, 5, 7)
        r1.update(id=6)
        with patch('sys.stdout', new=io.StringIO()) as fakeOutput:
            print(r1)
        self.assertEqual(fakeOutput.getvalue(), '[Rectangle] (6) 11/5 - 7/6\n')


if __name__ == "__main__":
    unittest.main()

