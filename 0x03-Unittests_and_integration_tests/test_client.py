"""
Test module for the client module.

This module contains unit tests for the GithubOrgClient
class in the client module.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
import client
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test cases for the GithubOrgClient class.
    """

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org, mock_get):
        """
        Test the org method of GithubOrgClient class.

        Args:
            org (str): The organization name to test.
            mock_get (MagicMock): Mock object for get_json function.
        """
        test = GithubOrgClient(org)
        result = test.org
        self.assertEqual(result, mock_get.return_value)
        mock_get.assert_called_once()
