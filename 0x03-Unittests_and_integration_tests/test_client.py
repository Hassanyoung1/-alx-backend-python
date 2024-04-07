#!/usr/bin/env python3

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
from utils import memoize


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

    def test_public_repos_url(self):
        """
        Test the _public_repos_url method of GithubOrgClient class.
        """

        @patch('client.get_json', return_value={"payload": True})
        @memoize
        def test_public_repos_url(self, _public_repos_url):
            """
            Test the _public_repos_url method of GithubOrgClient class.

            Args:
                _public_repos_url (MagicMock):
                Mock object for get_json function.
         """
            test = GithubOrgClient("_public_repos_url")
            test_public_repos_url = test._public_repos_url
            self.assertEqual(test_public_repos_url,
                             _public_repos_url.return_value)
            mock_get.assert_called_once()

            @patch('client.get_json', return_value=[{"name": "Alx"}])
            def test_public_repos(self):
                """
                Test the public_repos method of GithubOrgClient class.
                Args:
                mock_get_json (MagicMock): Mock object for get_json function.
                """
                with patch.object(GithubOrgClient, '_public_repos_url',
                                  new_callable=PropertyMock) \
                        as mock_public_repos_url:
                    mock_public_repos_url.return_value = \
                        "https://api.github.com/orgs/test_org/repos"

                    test = GithubOrgClient("test_org")
                    test_public_repos = test.public_repos
                    for repo in test_public_repos:
                        self.assertEqual(repo, {"name": "Alx"})
                    mock_public_repos_url.assert_called_once()
                    mock_get_json.assert_called_once()
