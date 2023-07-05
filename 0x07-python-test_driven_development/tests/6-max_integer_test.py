#!/usr/bin/python3

"""Unittests for max_integer(list).
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """different test cases """

    def test_non_sorted_list(self):
        """list not sorted."""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_empty_list(self):
        """empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_list_single_elt(self):
        """liste with one element."""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_string_arg(self):
        """Test a string."""
        list_string = "string"
        self.assertEqual(max_integer(list_string), 't')

    def test_list_of_strings(self):
        """list of strings."""
        strings = ["Test", "a", "string", "list"]
        self.assertEqual(max_integer(strings), "string")

    def test_empty_string(self):
        """empty string."""
        self.assertEqual(max_integer(""), None)

    def test_no_arg(self):
        """no argument"""
        self.assertRaises(TypeError, max_integer())

    def test_mixt_list(self):
        """list of floats."""
        list_mixt = [14.05, -8.36, -2, '11.23', 17.89]
        self.assertRaises(TypeError, max_integer(list_mixt))


if __name__ == '__main__':
    unittest.main()
