#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function."""

    def test_ordered_list(self):
        """Test with an ordered list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list of integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test with a list containing a single element."""
        self.assertEqual(max_integer([5]), 5)

    def test_identical_elements(self):
        """Test with a list of identical elements."""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_negative_numbers(self):
        """Test with a list containing negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test with a list of mixed positive and negative numbers."""
        self.assertEqual(max_integer([-10, 5, 3, -2]), 5)

    def test_max_at_beginning(self):
        """Test when the max value is at the beginning of the list."""
        self.assertEqual(max_integer([9, 2, 3, 1]), 9)

    def test_max_at_end(self):
        """Test when the max value is at the end of the list."""
        self.assertEqual(max_integer([1, 3, 2, 8]), 8)

    def test_large_numbers(self):
        """Test with a list of large numbers."""
        self.assertEqual(max_integer([1000000, 5000000, 9999999]), 9999999)

    def test_float_numbers(self):
        """Test with a list containing float numbers."""
        self.assertEqual(max_integer([1.5, 2.7, 3.8, 0.9]), 3.8)

    def test_mixed_integer_float(self):
        """Test with a mix of integers and floats."""
        self.assertEqual(max_integer([1, 2.5, 3, 4.8]), 4.8)

    def test_string_list(self):
        """Test with a string passed instead of a list."""
        self.assertEqual(max_integer("hello"), 'o')

    def test_none_argument(self):
        """Test with None as argument."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_mixed_types(self):
        """Test with a list of mixed types."""
        with self.assertRaises(TypeError):
            max_integer([1, "string", 3])

if __name__ == "__main__":
    unittest.main()
