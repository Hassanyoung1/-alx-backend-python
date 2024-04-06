#!/usr/bin/env python

"""
Test case for the access_nested_map function in the utils module.

This module defines the TestAccessNestedMap class, which is used
to test the access_nested_map function with various input cases.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    A test case class for the access_nested_map function.

    This class contains test cases to validate the behavior
    of the access_nested_map function with different inputs.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_output):
        """
        Test the access_nested_map function with various inputs.

        Args:
        - nested_map (dict): The nested dictionary to access.
        - path (tuple): The path to the desired value.
        - expected_output: The expected output when accessing the pathi
        in the nested_map.
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_output)
