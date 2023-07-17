#!/usr/bin/python3
"""This Module defines the unittests for the Base class"""

import unittest
from models.base import Base


class TestBase_instantiation(unittest.TestCase):
    """Unittests for the base class"""

    def test_idBase(self):
        """check id incrementation"""
        b1 = Base()
        b2 = Base()
        b3 = Base(None)
        self.assertEqual(b3.id, b1.id + b2.id)

    def test_id_arg(self):
        self.assertEqual(7.3, Base(7.3).id)

    def test_id_changed(self):
        """check if an id is passed and changed"""
        b1 = Base(10)
        b1.id = 13
        self.assertEqual(b1.id, 13)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_multi_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2, 3)
