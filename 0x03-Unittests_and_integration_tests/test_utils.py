#!/usr/bin/env python3

"""
Test case for the access_nested_map function in the utils module.

This module defines the TestAccessNestedMap class, which is used
to test the access_nested_map function with various input cases.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, requests, memoize
from unittest.mock import patch, Mock


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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
        ({"a": {"b": 2}}, ("a", "b", "c")),
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test the access_nested_map function with invalid inputs.

        Args:
        - nested_map (dict): The nested dictionary to access.
        - path (tuple): The path to the desired value.
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test cases for the get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')  # Patch the actual requests.get function
    def test_get_json(self, test_url, expected_payload, mock_get):
        """
        Test the get_json function with a mock response.
        """
        mock_response = Mock()
        mock_response.json.return_value = expected_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)  # Call the function directly

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, expected_payload)


class TestMemoize(unittest.TestCase):
    """
    Test cases for the memoize decorator.

    This class contains test cases to validate the behavior
    of the memoize decorator when applied to a class method.
    """
    def test_memoize(self):
        """
        Test that the memoize decorator caches the result of a method.
        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_memoized_method(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method') as mock_a_method:
            test_instance = TestClass()
            test_instance.a_memoized_method()
            mock_a_method.assert_called_once()
